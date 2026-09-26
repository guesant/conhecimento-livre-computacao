# CloudNativePG

CloudNativePG é um operator Kubernetes para operar clusters PostgreSQL por meio de recursos declarativos. Ele combina CRDs e controllers para cuidar de ciclo de vida, configuração, replicação, promoção e operações de manutenção que não cabem em um StatefulSet genérico.

As regras sobre ownership do diretório de dados, promoção de uma réplica, fencing da antiga primary e compatibilidade entre versões pertencem ao PostgreSQL e ao modelo primary/standby. Elas também se aplicam a uma instalação gerenciada por systemd, VM, container, serviço gerenciado ou outro operator. O CNPG é usado aqui como a implementação Kubernetes dessas regras, não como a origem delas.

## Modelo operacional

O recurso `Cluster` representa a intenção do banco. O operator observa esse recurso e coordena pods, serviços, volumes, usuários, roles e configurações associadas. A reconciliação continua depois da criação inicial, portanto alterações manuais que desviem do estado declarado podem ser corrigidas ou substituídas pelo controller.

## O que ele resolve

O CNPG fornece uma fronteira Kubernetes para tarefas específicas de PostgreSQL, como topologia de instâncias, failover, replicação e integração com mecanismos de backup suportados. A aplicação continua responsável por schema, migrações, índices e desenho das consultas. Operator de banco não substitui o planejamento de recuperação nem o teste de restauração.

## Regra geral de ownership do PGDATA

Um processo PostgreSQL precisa ser o único dono do diretório de dados que está usando. O `PGDATA` contém o catálogo, os arquivos das relações, o controle do cluster, os arquivos de configuração e o estado necessário para interpretar o WAL. Dois processos PostgreSQL não devem trabalhar simultaneamente sobre a mesma árvore de dados, mesmo que tenham sido iniciados a partir de imagens diferentes.

Essa regra não é uma limitação específica do Kubernetes. O PostgreSQL usa locks, arquivos de controle, memória compartilhada e um formato de armazenamento associado à versão major. Iniciar uma segunda instância sobre o mesmo `PGDATA` não cria uma réplica e não é uma estratégia de upgrade. Pode falhar imediatamente ou produzir corrupção e perda de consistência se alguma camada permitir a execução concorrente.

Por isso, uma atualização segura sempre define quem tem autoridade sobre cada diretório e cada endpoint. A instância antiga precisa ser parada ou perder a autoridade antes que outra instância passe a usar aquele diretório. Em um ambiente blue/green, os diretórios são diferentes desde o início. Em uma atualização in-place, a janela em que o PostgreSQL está parado faz parte do procedimento.

## Rollout de uma versão minor

Versões minor dentro da mesma major preservam o formato interno de armazenamento e normalmente podem ser atualizadas com rolling update. Em qualquer implementação primary/standby, as réplicas devem ser atualizadas e validadas antes da instância que recebe escritas. No CNPG, quando o `imageName` muda, o operator atualiza as réplicas uma por vez, começando pela réplica de maior serial. A primary fica por último.

A primary não deve ser simplesmente reiniciada enquanto continua sendo a autoridade de escrita sem uma estratégia de transição. Depois que uma réplica foi atualizada, está saudável e está suficientemente alinhada, o CNPG pode fazer o switchover para ela. A réplica é promovida a primary, o serviço de escrita passa a apontar para ela e a antiga primary é desligada ou retirada da função de primary. Só depois desse corte ela pode ser recriada com a nova imagem e voltar como réplica.

Esse é o motivo de a estratégia correta, independentemente do orquestrador, ser promover uma réplica candidata antes de atualizar a antiga primary. O objetivo não é manter duas primaries na mesma pasta, nem atualizar o processo que ainda atende escritas. O objetivo é preservar uma única autoridade de escrita e uma única instância PostgreSQL por `PGDATA` em cada momento. O CNPG automatiza essa sequência e atualiza os endpoints dos Services conforme o estado do cluster.

No CNPG, duas formas controlam essa última etapa:

- `primaryUpdateStrategy: unsupervised` permite que o operator conclua o rollout automaticamente. É o padrão.
- `primaryUpdateStrategy: supervised` pausa depois de atualizar as réplicas e exige uma decisão operacional explícita.

Quando o rollout é supervisionado, o operador pode promover a réplica candidata:

```bash
kubectl cnpg promote <cluster> <new-primary>
```

Também existe, no CNPG, a escolha entre `primaryUpdateMethod: switchover` e `primaryUpdateMethod: restart`. O switchover favorece a promoção de uma réplica que já está rodando a imagem nova. O restart tenta reiniciar a primary no mesmo local quando possível, mas pode precisar baixar a nova imagem depois que a primary antiga for parada. Essa diferença altera a janela de indisponibilidade e deve ser decidida de acordo com o tempo de download da imagem, o RTO e o comportamento da aplicação.

Durante o rollout, os Services do CNPG acompanham o estado observado do cluster. Em outras implementações, o mecanismo equivalente pode ser um proxy, um endpoint virtual, um registro de serviço ou uma configuração de conexão. Em todos os casos, a aplicação deve usar o endpoint que representa a primary atual, e não fixar o nome de um processo ou Pod. A antiga primary também precisa ser impedida de receber novas escritas antes de qualquer reaproveitamento ou descarte do seu volume.

## Upgrade de uma versão major

Uma mudança como PostgreSQL 16 para PostgreSQL 17 não deve ser tratada como uma simples atualização rolling. Versões major podem alterar o formato de armazenamento interno, a compatibilidade das extensões e os requisitos do catálogo. O CNPG documenta três estratégias:

1. dump e restore lógico em um ambiente blue/green offline;
2. replicação lógica nativa em um ambiente blue/green online;
3. `pg_upgrade` in-place offline.

No blue/green, o cluster novo possui volumes e `PGDATA` próprios. Ele recebe uma cópia lógica ou dados replicados, é validado e só então assume o endpoint de escrita. Depois do cutover, o cluster antigo deve ser cercado, ou seja, impedido de aceitar escritas, para não haver divergência entre os dois lados. O volume antigo continua sendo uma opção de rollback apenas enquanto o plano de reconciliação e a janela de rollback forem válidos. Depois que o novo cluster aceitar escritas que não foram replicadas de volta, não é seguro simplesmente apontar o serviço novamente para o antigo.

No upgrade in-place, o CNPG encerra os Pods do cluster, cria diretórios novos para o `PGDATA` e, quando aplicável, para WAL e tablespaces, executa `pg_upgrade` com `--link` e substitui os diretórios depois do sucesso. O cluster inteiro fica indisponível durante o procedimento. Isso continua sendo diferente de dois processos PostgreSQL rodando sobre a mesma pasta: o processo antigo está parado antes da conversão, e os diretórios novos são preparados pelo job de upgrade.

Antes de um upgrade major, é necessário verificar pelo menos a compatibilidade das extensões, a distribuição base das imagens, os backups, o espaço livre, o comportamento das aplicações e o plano de recuperação. O CNPG não garante a compatibilidade das extensões instaladas. Depois do upgrade, as réplicas precisam ser recriadas a partir da primary atualizada e as estatísticas devem ser recalculadas com `ANALYZE`. Backups e WAL anteriores não atravessam automaticamente a fronteira de uma versão major para PITR.

## Sequência segura de promoção e atualização

Uma sequência operacional genérica é:

1. criar ou identificar uma réplica candidata com armazenamento próprio;
2. confirmar que ela está saudável, alinhada e executando a versão desejada;
3. verificar backups, extensões, capacidade, probes e compatibilidade da aplicação;
4. interromper ou controlar escritas quando o método de upgrade exigir isso;
5. promover a candidata ou executar o switchover controlado;
6. confirmar que o Service de escrita aponta somente para a nova primary;
7. fazer fencing da antiga primary e garantir que ela não pode aceitar escritas;
8. atualizar ou recriar a antiga primary como réplica;
9. observar replicação, erros, latência, WAL e endpoints antes de encerrar o rollback;
10. remover volumes antigos somente depois de backup verificado e de uma decisão explícita de descarte.

O passo de fencing é indispensável em qualquer topologia que possa deixar os dois lados vivos. Uma aplicação que continua usando um endpoint antigo pode produzir split-brain mesmo quando o operator já considera a nova instância como primary.

## Probes do PostgreSQL no CNPG

O CNPG inicia o instance manager como processo principal do container. Esse componente acompanha o ciclo de vida do PostgreSQL e atende às probes do Kubernetes. As probes não são equivalentes e devem responder a perguntas diferentes.

### Startup probe

A startup probe responde se o PostgreSQL conseguiu iniciar o suficiente para ser acompanhado. Por padrão, o CNPG usa `pg_isready`. Com a estratégia `pg_isready`, o processo pode ser considerado iniciado enquanto ainda rejeita conexões durante recuperação ou replay de WAL. Isso evita que o kubelet reinicie uma instância que está realizando uma recuperação válida.

Enquanto a startup probe não passa, liveness e readiness ficam desabilitadas. Se a startup probe falhar até o limite configurado, o kubelet reinicia o container. O `startDelay` define o tempo máximo para essa etapa. O valor padrão documentado pelo CNPG 1.30 é 3600 segundos, mas deve ser ajustado ao tempo real de inicialização do cluster. Um valor baixo pode causar reinícios em cascata.

O CNPG também permite estratégias mais profundas para startup, como `query` e `streaming`. `streaming` pode exigir que uma réplica comece a receber WAL e respeite um `maximumLag` antes de ser considerada iniciada. Essa verificação é útil quando uma réplica que ainda está muito atrasada não pode participar do failover, mas aumenta o tempo necessário para a startup probe passar.

### Liveness probe

A liveness probe começa depois que a startup probe passa. Ela verifica se o instance manager e a instância PostgreSQL continuam operando de forma válida. Falhas repetidas fazem o kubelet reiniciar o container.

Liveness não deve testar a disponibilidade de uma dependência externa, a saúde da aplicação ou a existência de uma conexão de usuário específica. Se o banco estiver saudável, mas a rede até um serviço externo estiver indisponível, reiniciar o PostgreSQL apenas amplia o incidente. A configuração deve tolerar recuperação, replay de WAL e pausas transitórias sem mascarar um processo realmente travado.

No CNPG 1.30, o timeout padrão usado para calcular a tolerância da liveness é 30 segundos, com verificações a cada 10 segundos. A configuração pode ser ajustada em `.spec.probes.liveness`. Se `failureThreshold` for definido explicitamente, ele deixa de ser calculado a partir de `livenessProbeTimeout`.

### Readiness probe

A readiness probe responde se a instância pode receber tráfego naquele momento. Quando falha, o Pod fica fora dos endpoints prontos dos Services, mas não é reiniciado. Essa é a probe que deve retirar uma réplica que está recuperando, atrasada ou temporariamente incapaz de atender conexões.

Por padrão, o CNPG usa `pg_isready` e só considera a instância pronta quando ela aceita conexões. Para réplicas em streaming, a prontidão também considera a conexão com a origem. A estratégia pode ser aprofundada com `type: streaming` e `maximumLag`, mantendo a réplica fora dos endpoints enquanto o atraso ultrapassar o limite configurado. Uma réplica não pronta também não é candidata adequada para promoção automática.

Uma configuração pode combinar uma atualização supervisionada com um critério de prontidão de réplica, por exemplo:

```yaml
spec:
  primaryUpdateStrategy: supervised
  primaryUpdateMethod: switchover
  probes:
    startup:
      type: pg_isready
    readiness:
      type: streaming
      maximumLag: 16Mi
```

O exemplo é ilustrativo. Os valores de tempo, atraso aceitável e estratégia devem ser definidos a partir do RTO, do tamanho do banco, da taxa de WAL e do tempo observado de recuperação. Uma probe mais profunda não substitui monitoramento de replicação, backup e capacidade.

As explicações gerais estão em [liveness probe](../recursos/liveness-probe.md), [readiness probe](../recursos/readiness-probe.md) e [startup probe](../recursos/startup-probe.md). No CNPG, a configuração específica e os efeitos sobre failover devem ser conferidos na documentação da versão do operator instalada.

## Limitações

O operator não transforma armazenamento local em alta disponibilidade. A durabilidade depende dos volumes, do domínio de falha, da estratégia de backup e da capacidade de restaurar o cluster. Uma réplica no mesmo node protege contra falha do processo, mas não contra perda do node. Credenciais, permissões e políticas de rede também continuam sendo responsabilidades da plataforma.

## Relações

- [Operators](../../kubernetes-operators.md) explica o padrão CRD mais controller.
- [StatefulSet](../core/statefulset.md) é um recurso Kubernetes, não uma implementação de operação PostgreSQL.
- [PersistentVolume](../storage/persistent-volume.md) e [PersistentVolumeClaim](../storage/persistent-volume-claim.md) definem a base de armazenamento.
- [Backup](../../confiabilidade/backup/backup.md) e [RPO](../../confiabilidade/backup/rpo.md) definem a proteção que o operator precisa participar.

## Fontes primárias

- [Rolling updates do CloudNativePG](https://cloudnative-pg.io/docs/current/rolling_update/)
- [Upgrades de PostgreSQL no CloudNativePG](https://cloudnative-pg.io/docs/current/postgres_upgrades/)
- [Postgres Instance Manager e probes](https://cloudnative-pg.io/docs/current/instance_manager/)
- [Documentação do PostgreSQL sobre continuous archiving e recovery](https://www.postgresql.org/docs/current/continuous-archiving.html)

- [Documentação geral do CloudNativePG](https://cloudnative-pg.io/documentation/current/)
