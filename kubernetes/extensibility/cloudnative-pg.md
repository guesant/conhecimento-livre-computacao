# CloudNativePG

CloudNativePG é um operator Kubernetes para operar clusters PostgreSQL por meio de recursos declarativos. Ele combina CRDs e controllers para cuidar de ciclo de vida, configuração, replicação, promoção e operações de manutenção que não cabem em um StatefulSet genérico.

## Modelo operacional

O recurso `Cluster` representa a intenção do banco. O operator observa esse recurso e coordena pods, serviços, volumes, usuários, roles e configurações associadas. A reconciliação continua depois da criação inicial, portanto alterações manuais que desviem do estado declarado podem ser corrigidas ou substituídas pelo controller.

## O que ele resolve

O CNPG fornece uma fronteira Kubernetes para tarefas específicas de PostgreSQL, como topologia de instâncias, failover, replicação e integração com mecanismos de backup suportados. A aplicação continua responsável por schema, migrações, índices e desenho das consultas. Operator de banco não substitui o planejamento de recuperação nem o teste de restauração.

## Limitações

O operator não transforma armazenamento local em alta disponibilidade. A durabilidade depende dos volumes, do domínio de falha, da estratégia de backup e da capacidade de restaurar o cluster. Uma réplica no mesmo node protege contra falha do processo, mas não contra perda do node. Credenciais, permissões e políticas de rede também continuam sendo responsabilidades da plataforma.

## Relações

- [Operators](../../kubernetes-operators.md) explica o padrão CRD mais controller.
- [StatefulSet](../core/statefulset.md) é um recurso Kubernetes, não uma implementação de operação PostgreSQL.
- [PersistentVolume](../storage/persistent-volume.md) e [PersistentVolumeClaim](../storage/persistent-volume-claim.md) definem a base de armazenamento.
- [Backup](../../confiabilidade/backup/backup.md) e [RPO](../../confiabilidade/backup/rpo.md) definem a proteção que o operator precisa participar.

## Fonte primária

- [CloudNativePG documentation](https://cloudnative-pg.io/documentation/current/)
