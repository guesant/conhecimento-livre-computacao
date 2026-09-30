# StatefulSet

StatefulSet administra Pods que precisam de identidade estável, ordem ou
armazenamento associado a cada réplica. Ao contrário de um Deployment, ele
trata o ordinal, o nome previsível e a associação entre Pod e volume como
partes do contrato do workload.

## Identidade

As réplicas recebem nomes como `app-0` e `app-1`. A identidade ordinal pode
ser usada por protocolos de cluster, mas o nome previsível não transforma a
aplicação em um sistema distribuído correto. O software ainda precisa lidar
com eleição, quorum, replicação, split brain e recuperação.

Um Service headless pode publicar DNS por Pod para clientes que precisam
encontrar membros individualmente. Um Service comum pode continuar fornecendo
um endpoint lógico para operações que não precisam de um membro específico.

## Storage e ordem

VolumeClaimTemplates cria uma solicitação de armazenamento por réplica. O
volume continua existindo quando o Pod é recriado, mas exclusão de StatefulSet
não implica apagar automaticamente os volumes. A política de retenção precisa
ser deliberada para evitar perda ou acumulação de dados.

O update pode ser ordenado e pode parar ao primeiro Pod que não fica pronto.
Isso protege protocolos que exigem ordem, mas aumenta o tempo de rollout e faz
uma réplica mal configurada bloquear as seguintes.

## Relações

- [PersistentVolumeClaim](../storage/persistent-volume-claim.md) representa a
  solicitação de armazenamento.
- [Service](service.md) pode publicar identidade de rede.
- [Deployment](deployment.md) é preferível quando réplicas são intercambiáveis.

## Fonte primária

- [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
