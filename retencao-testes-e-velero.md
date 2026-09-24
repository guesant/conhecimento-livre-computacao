# Retenção, testes de restauração e Velero

Um backup que permanece no mesmo host, mesma conta ou mesmo storage do dado original está sujeito ao mesmo evento que poderia destruir o original, não é, na prática, um backup independente. "Fora do cluster" precisa ser avaliado por domínio de falha real, não por localização nominal: um backup em outro disco do mesmo host protege contra falha de disco, mas não contra falha do host inteiro.

Um "outro bucket" na mesma conta de object storage não isola contra uma credencial administrativa comprometida, quem acessa um bucket geralmente acessa o outro; só uma conta, projeto ou provedor separado isola de verdade contra esse cenário. Para ambientes pessoais sem orçamento para uma segunda conta, um disco externo físico, mantido desconectado entre backups, é um isolamento mínimo aceitável, desde que genuinamente guardado em outro local físico.

Reter poucos pontos economiza espaço, mas aumenta o risco de a única cópia disponível já estar corrompida ou nem existir quando o incidente for percebido; reter tudo indefinidamente custa espaço sem benefício correspondente na maioria dos casos. Uma política equilibrada combina múltiplas granularidades, vários pontos recentes de alta frequência (horários ou diários) e poucos pontos antigos de baixa frequência (semanais, mensais).

O ponto crítico é que uma política com muitos pontos recentes e nenhuma cópia anterior a uma janela de detecção de corrupção não atende a um incidente descoberto tardiamente: se um erro lógico levou duas semanas para ser percebido, toda a retenção horária e diária já expirou, só uma retenção semanal ou mensal salva a situação.

Retenção não é só quantidade, inclui também onde e como cada ponto é protegido contra exclusão acidental ou maliciosa, imutabilidade ou WORM quando o destino suportar.

Um Job de backup marcado `Completed` prova que os dados foram lidos e enviados a algum lugar; não prova que o artefato resultante é íntegro, completo ou realmente restaurável. Um teste de restauração real precisa validar três camadas: o processo completa sem erro, os dados restaurados existem com tamanho plausível, e a aplicação funciona corretamente com os dados restaurados.

Essa última camada, validação funcional, é a mais frequentemente pulada e a mais importante: um banco restaurado que inicia sem erro pode ainda ter perdido índices ou não passar numa consulta simples de verificação. Testar depois de qualquer mudança relevante na estratégia, e num cronograma regular mesmo sem mudanças, é o que sustenta a confiança no RPO e no RTO declarados; um teste sem essas métricas registradas não comprova os objetivos.

## Velero: além do snapshot do etcd

Um snapshot do etcd cobre só o estado declarado da API Kubernetes. O Velero cobre uma camada adicional: lê os manifests via API, os serializa, e, quando configurado para isso, também copia ou tira snapshot dos dados dentro dos volumes referenciados.

A granularidade é a diferença prática mais relevante: um snapshot do etcd restaura o cluster inteiro de uma vez, o Velero pode restaurar um único namespace ou um subconjunto de recursos selecionado por label, sem tocar no resto do cluster, o que também o torna a base para migrar workloads entre clusters ou distribuições diferentes.

O Velero separa duas responsabilidades por plugins diferentes: um provider de **BackupStorageLocation** é para onde os manifests serializados são enviados, um object storage compatível com S3; um provider de **VolumeSnapshotLocation** sabe tirar um snapshot nativo de um volume num storage específico. Quando o storage de volumes não oferece snapshot nativo integrável, o **File System Backup**, baseado em Kopia, copia o conteúdo do volume arquivo por arquivo, funcionando com qualquer backend, ao custo de ser mais lento que um snapshot nativo.

Um `Schedule` cria um novo `Backup` a cada execução do cron informado, e o campo `--ttl` decide quando o Velero pode expirá-lo.

Combinar vários `Schedules`, cada um com seu próprio prazo de expiração, é o que aproxima o Velero de uma retenção em camadas, já que um único agendamento não expressa "manter N diários, M semanais" sozinho.

Filtros como `--include-namespaces` e `--include-resources` restringem um backup ou uma restauração a um subconjunto, o que é exatamente a granularidade seletiva que o snapshot do etcd não oferece.

Hooks de pré e pós-backup, declarados como anotações no próprio Pod, executam um comando dentro de um container antes ou depois da cópia, úteis para uma aplicação que precisa ser colocada num estado consistente antes do backup. Para um banco gerenciado por um operator como o CloudNativePG, o mecanismo de backup nativo do operator continua preferível a um hook genérico do Velero: o operator já coordena WAL, consistência e retenção especificamente para aquele banco.

Adotar o Velero soma uma dependência de storage externo e um mecanismo de volume adicional para manter testado sobre o que o snapshot do etcd já oferece. Isso só compensa quando restauração seletiva, cobertura de volumes ou portabilidade entre clusters realmente importam; caso contrário o snapshot do etcd sozinho é mais simples de operar e testar.

## Export seletivo como paliativo manual

Entre não ter nada e adotar o Velero existe um meio-termo manual: exportar os recursos de um namespace com `kubectl get all,configmap,secret,ingress,pvc --namespace <namespace> -o yaml` para um arquivo.

Esse export não é um manifesto pronto para reaplicar, porque carrega campos que o próprio cluster gerencia, como a versão interna do recurso e seu identificador único; serve como referência para reconstrução manual ou como cópia adicional do estado observado, não como algo para aplicar direto num cenário de restauração real.

Esse tipo de export só cobre recursos que o próprio comando lista explicitamente, então CRDs de operators (cert-manager, o próprio Argo CD) ficam de fora, a menos que sejam exportados à parte com o mesmo `-o yaml`. Para um cluster que já declara o estado desejado no Git via GitOps, esse export é útil sobretudo para o que foi criado fora do fluxo declarativo, já que o repositório em si já funciona como o backup dos recursos que ele gerencia.

Como qualquer outro backup, um arquivo assim só protege de verdade depois de copiado para fora do host que o gerou, e nunca deveria ser versionado num repositório Git comum, porque um export desse tipo inclui `Secret` em texto claro.

## Continue por aqui

[Fundamentos de backup, RPO e RTO](fundamentos-de-backup-rpo-e-rto.md) cobre o vocabulário básico (réplica, snapshot, backup) e as metas que este texto pressupõe.
