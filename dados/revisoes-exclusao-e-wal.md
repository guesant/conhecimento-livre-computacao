# Exclusão, edição, revisões e WAL

Exclusão e edição não são apenas operações de interface. Elas definem o que pode ser recuperado, auditado, publicado, replicado, indexado e apagado de verdade. Antes de escolher uma estratégia, é necessário distinguir histórico editorial, auditoria, recuperação de desastre, replicação e retenção legal. Eles podem compartilhar mecanismos, mas não têm o mesmo objetivo.

Os termos `soft edit` e `hard edit` não são uma nomenclatura universal. Neste documento, `hard edit` significa atualização destrutiva no mesmo registro lógico e `soft edit` significa uma atualização por nova revisão, mantendo versões anteriores e movendo um ponteiro para a versão corrente. O segundo modelo também é chamado de versionamento, histórico de revisões, append-only editorial ou temporalidade aplicada ao domínio.

## Exclusão lógica

Soft delete marca um registro como excluído sem removê-lo fisicamente. O modelo mais simples possui `deleted_at`, podendo também registrar `deleted_by`, motivo, estado e a revisão que estava publicada.

Uma consulta pública normalmente filtra `deleted_at IS NULL`. A área administrativa pode consultar registros excluídos com uma intenção explícita. Isso permite recuperação acidental, investigação, restauração rápida e preservação de referências internas.

Soft delete não é anonimização, erasure nem cumprimento automático de retenção. O conteúdo continua presente em tabelas, índices, réplicas, backups, snapshots, caches, logs e possivelmente WAL. Se a obrigação exige remover dados pessoais, uma marca de exclusão pode ser insuficiente.

Também há custos operacionais:

- toda leitura precisa aplicar o filtro correto;
- índices devem considerar a população ativa;
- relações precisam definir se registros excluídos continuam válidos;
- contagens, unicidade e buscas podem incluir dados que o usuário não vê;
- o espaço físico cresce até uma purga controlada;
- restauração e exportação precisam declarar se incluem excluídos;
- caches e índices de busca precisam ser invalidados quando o registro deixa de ser visível.

Um padrão seguro é encapsular a consulta de ativos, testar explicitamente o caminho administrativo e criar uma rotina de retenção separada. Não esconda o filtro somente em uma camada que possa ser ignorada por uma query direta ou por um relatório.

## Exclusão física

Hard delete remove fisicamente o registro lógico da tabela e as relações que devem ser removidas com ele. A operação pode ser necessária quando o dado não possui valor de negócio, quando a retenção terminou ou quando a legislação exige eliminação real.

Excluir a linha não significa que todos os vestígios desapareceram imediatamente. O banco pode manter páginas reutilizáveis, backups e registros de recuperação; réplicas podem ainda estar aplicando a operação; caches podem continuar servindo uma resposta; exportações antigas podem existir em outros sistemas. A política precisa definir escopo de eliminação, retenção residual, propagação e verificação.

Hard delete também aumenta o risco operacional. Uma falha de seleção pode remover muitos registros, uma relação mal definida pode produzir cascata e uma purga pode competir com consultas ou gerar muito WAL. Use transação, predicado identificável, limite operacional, contagem esperada, revisão e backup ou ponto de recuperação compatível com o risco.

Não trate `ON DELETE CASCADE` como uma política de negócio. Ele expressa uma regra de integridade referencial, mas não decide se o usuário tem autorização para apagar, se o dado precisa ser retido ou se uma versão publicada deve continuar disponível.

## Edição destrutiva no mesmo registro

No hard edit, o registro lógico mantém a mesma identidade e seus campos são substituídos por uma nova representação. O banco pode usar MVCC para garantir consistência entre transações. No PostgreSQL, por exemplo, uma atualização cria uma nova versão física da linha e o vacuum recupera versões antigas quando elas não são mais necessárias. Isso é um mecanismo interno de concorrência, não um histórico editorial acessível à aplicação.

O modelo é simples e adequado quando o estado anterior não possui valor próprio. Ele reduz tabelas e joins, facilita consultas correntes e combina com dados derivados ou configurações cujo histórico pode ser obtido por outro sistema.

O custo é perder o histórico de negócio se não houver uma trilha separada. Depois de alterar um título, uma permissão, um preço ou uma configuração, a aplicação pode não saber quem alterou, qual era o valor anterior, qual revisão foi publicada ou como reconstruir o estado em uma data passada.

Auditoria criada por triggers ou por uma tabela de alterações pode preservar esse histórico, mas isso já é uma segunda representação. Ela deve definir formato, identidade do ator, transação, origem, campos alterados, retenção e proteção contra alteração pelo próprio usuário auditado.

## Atualização por nova revisão

No versionamento editorial, o registro de identidade permanece estável e cada mudança cria uma nova revisão. Uma representação conceitual é:

| Tabela | Responsabilidade |
| --- | --- |
| Entidade ou registro | Identidade estável, slug atual, estado corrente e ponteiros de publicação. |
| Revisão | Uma versão imutável dos atributos editoriais, autor, data, ordem e metadados da mudança. |
| Relações da revisão | Arrays e objetos normalizados em tabelas relacionadas, ligados à revisão quando o relacionamento também precisa ser histórico. |
| Auditoria | Quem executou uma ação, qual operação ocorreu, contexto e resultado, sem substituir a revisão editorial. |

Uma atualização acontece em uma transação:

1. valide a revisão esperada pelo editor;
2. crie uma nova revisão com um identificador monotônico ou ordenável;
3. grave relações e atributos dependentes dessa revisão;
4. valide invariantes e unicidade;
5. mova o ponteiro corrente ou publicado;
6. invalide caches e índices derivados depois do commit;
7. retorne a revisão criada e seu estado.

O ponteiro pode ser `current_revision_id`, `draft_revision_id` ou `published_revision_id`. Separar corrente de publicada é útil quando o editor trabalha em rascunho e o site público só pode ler uma revisão aprovada. Uma alteração de slug pode manter a identidade do registro e acrescentar aliases para que rotas antigas continuem funcionando.

Esse modelo permite comparar revisões, restaurar uma versão anterior criando outra revisão, publicar sem editar o passado e consultar o estado de uma data. Restaurar não deve apagar o histórico atual; deve criar uma nova revisão cujo conteúdo deriva da versão escolhida.

## Revisão não é auditoria

Uma revisão responde "qual conteúdo ou estado foi produzido e pode ser publicado?". Auditoria responde "quem executou qual ação, quando, por qual interface ou processo e com qual resultado?".

Uma revisão pode conter o autor editorial e a mensagem da alteração, mas isso não substitui uma trilha de segurança. A auditoria pode registrar login, ator efetivo, IP ou request id conforme a política, permissão avaliada, entidade afetada, resultado e motivo. Ela deve ser append-only ou protegida por controles que impeçam o auditado de reescrever sua própria evidência.

Da mesma forma, WAL não é auditoria. WAL permite recuperação física do banco e pode alimentar replicação ou decodificação lógica. Ele não é uma API editorial estável, não deve ser usado como histórico de interface e não oferece necessariamente o contexto humano de uma alteração.

## Exclusão em um modelo versionado

Há mais de uma forma válida de apagar uma entidade versionada.

### Tombstone ou revisão de exclusão

Cria uma nova revisão que declara a entidade como removida, ou move o ponteiro para um estado excluído. A identidade e o histórico permanecem consultáveis. Esse modelo é útil quando a aplicação precisa preservar referências, sincronizar a remoção ou restaurar posteriormente.

### Exclusão lógica da identidade

Marca a entidade como excluída e deixa as revisões intactas. É simples, mas o filtro precisa impedir que uma revisão antiga volte a aparecer por uma consulta que ignore o estado da identidade.

### Purga física

Remove identidade, revisões, relações e dados derivados conforme a política de retenção. A operação deve considerar referências externas, backups, réplicas, caches, índices, WAL e exportações. A purga precisa ter uma prova de escopo e um mecanismo para verificar o resultado.

Não use o mesmo botão para "retirar da publicação" e "apagar definitivamente". São intenções, autorizações e consequências diferentes.

## WAL, ou Write-Ahead Logging

WAL é o log de escrita antecipada usado por bancos como PostgreSQL para proteger a integridade. A regra é que a descrição da alteração seja persistida no log antes que as páginas de tabela e índice sejam consideradas persistidas. Em uma falha, o banco pode refazer alterações confirmadas que ainda não chegaram às páginas de dados.

O [WAL do PostgreSQL](https://www.postgresql.org/docs/current/wal-intro.html) é principalmente um mecanismo de recuperação de crash. O [PostgreSQL MVCC](https://www.postgresql.org/docs/current/mvcc-intro.html) é o mecanismo de visibilidade e isolamento entre versões de linhas durante transações. Eles se relacionam, mas não significam que a aplicação possui revisões editoriais disponíveis.

WAL também participa de:

- replicação física, enviando alterações para uma réplica;
- arquivamento contínuo e recuperação para um ponto no tempo;
- backup físico online;
- decodificação lógica e integrações que consomem mudanças;
- medição de lag, retenção e capacidade de armazenamento.

Na recuperação para um ponto no tempo, o PostgreSQL restaura uma base física e reproduz WAL até o instante desejado. A documentação de [continuous archiving e PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) destaca que a sequência de WAL precisa estar disponível desde o backup base e que o custo de armazenamento e replay precisa ser administrado.

WAL não deve ser tratado como:

- backup completo isolado;
- substituto de backup base;
- log de auditoria legível por usuários;
- histórico sem prazo de expiração;
- mecanismo para recuperar uma única linha com a mesma facilidade de uma revisão;
- garantia contra exclusão lógica ou corrupção já confirmada.

Uma exclusão ou corrupção confirmada é uma alteração legítima do ponto de vista transacional. Réplicas físicas e WAL normalmente propagam essa alteração. Para recuperar o estado anterior, é necessário PITR, uma revisão de domínio, backup lógico ou outro mecanismo de cópia adequado.

## Decisão por tipo de dado

| Tipo de dado | Estratégia frequentemente adequada |
| --- | --- |
| Cache | Hard edit ou substituição completa; não use revisão editorial. |
| Métrica e telemetria | Append-only com retenção e agregação; não use soft delete para sempre. |
| Configuração corrente | Hard edit com auditoria e controle de versão externo, ou revisões se rollback for requisito. |
| Conteúdo editorial | Entidade estável, revisões imutáveis e ponteiro de publicação. |
| Permissão e identidade | Histórico de atribuições, expiração e auditoria; purga conforme requisito legal. |
| Evento de integração | Append-only, idempotência e retenção; não reescreva evento já publicado. |
| Dados pessoais | Minimização, retenção explícita e mecanismo de eliminação que alcance cópias e derivados. |
| Estado operacional derivado | Recalcular ou substituir quando possível; preserve a fonte de verdade em outro lugar. |

Não existe uma estratégia universal. O critério é o valor do passado, a necessidade de restauração, a obrigação de apagamento, o custo de consulta e o impacto da propagação da mudança.

## Concorrência e integridade

Versionamento não resolve concorrência sozinho. Duas pessoas podem criar revisões ao mesmo tempo e uma pode mover o ponteiro depois da outra. Use uma revisão esperada, `updated_at` controlado, número de versão ou comparação e troca atômica do ponteiro.

Se a regra exige que uma única revisão esteja publicada, imponha isso por constraint e transação. Se relações precisam corresponder à mesma revisão, grave-as no mesmo limite transacional. Se o update puder ser repetido por timeout, use uma chave idempotente ou detecte a revisão já criada.

O `SELECT FOR UPDATE` pode proteger uma operação curta que realmente depende de exclusão mútua, mas não deve transformar uma edição inteira em uma fila de locks. Em muitos casos, controle otimista e uma constraint são suficientes.

## Índices, consultas e caches

Soft delete exige índice para o caminho ativo e filtros consistentes. Revisões exigem índices por entidade, estado, publicação, autor e ordenação temporal conforme as consultas reais. Um ponteiro corrente evita procurar a última revisão em toda leitura pública.

Consultas administrativas podem pedir histórico completo, mas a API pública deve selecionar apenas a revisão publicada e os campos necessários. Não devolva todas as revisões para resolver uma tela que precisa de um estado.

Caches devem ser invalidados quando o ponteiro publicado mudar, não somente quando uma linha de revisão for criada. Índices de busca, feeds, previews e exportações precisam ter uma política própria de atualização. O banco pode confirmar uma revisão enquanto uma cópia derivada ainda serve a versão anterior; isso é aceitável apenas se o contrato de consistência estiver definido.

## Retenção e segurança

Soft delete, revisões, auditoria, backups e WAL ampliam a superfície de dados. Classifique o que cada cópia contém, quem pode ler, por quanto tempo fica disponível e como é destruída. Criptografia em repouso protege contra certos acessos, mas não substitui autorização, retenção e purga.

Uma política deve responder se a exclusão vale para:

- tabela corrente;
- revisões antigas;
- auditoria;
- réplicas;
- cache e índice de busca;
- backups lógicos e físicos;
- WAL arquivado;
- exportações e sistemas consumidores.

Quando a obrigação exige apagamento de dados pessoais, documente o limite técnico e jurídico da operação. Não declare "apagado" apenas porque a linha deixou de aparecer na consulta principal.

## Relações com este repositório

- [Transações e ACID](transacoes-acid.md) explica atomicidade, isolamento, confirmação e recuperação.
- [Replicação](replicacao.md) explica cópias, atraso, replay e o fato de que alterações destrutivas também são replicadas.
- [Backup](../confiabilidade/backup/backup.md), [RPO](../confiabilidade/backup/rpo.md), [RTO](../confiabilidade/backup/rto.md) e [teste de restauração](../confiabilidade/backup/teste-de-restauracao.md) tratam recuperação e prova de que ela funciona.
- [Auditoria e abordagens de auditoria](../auditoria-e-abordagens.md) trata evidências e independência, que não devem ser confundidas com revisões ou WAL.
- [Idempotência](../confiabilidade/idempotencia.md) trata repetição segura de comandos de edição e exclusão.

## Fontes primárias

- [PostgreSQL, Write-Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html)
- [PostgreSQL, MVCC introduction](https://www.postgresql.org/docs/current/mvcc-intro.html)
- [PostgreSQL, continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [PostgreSQL, logical decoding](https://www.postgresql.org/docs/current/logicaldecoding.html)
