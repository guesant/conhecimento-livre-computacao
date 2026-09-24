# Longhorn

Longhorn é um sistema de armazenamento em blocos distribuído para Kubernetes.
Ele integra o modelo por meio de CSI, cria réplicas de volume e oferece
backupstore externo conforme sua configuração.

## Modelo

Um volume possui engine e réplicas. A escrita pode ser enviada de forma
síncrona às réplicas ativas; quando uma réplica falha, o sistema reconstrói
conforme capacidade, regras de scheduling e dados disponíveis.

Réplicas protegem contra falhas de componente, mas não contra corrupção
lógica, remoção acidental ou ransomware. Backupstore em S3, NFS ou backend
compatível precisa estar fora do mesmo failure domain para cobrir perda total
do cluster.

## Escolha

Longhorn é atraente em clusters pequenos porque oferece armazenamento
distribuído sem exigir SAN dedicado. O custo inclui componentes adicionais,
latência de rede, consumo de disco para réplicas, rebuild e operação de
backup.

Um cluster de nó único não obtém alta disponibilidade de host com Longhorn.
Meça latência de escrita do banco antes de escolher réplica síncrona para
workload sensível.

## Relações

- [CSI](csi.md) conecta o backend ao Kubernetes.
- [Armazenamento local e distribuído](local-distributed.md) compara failure
  domains.
- [Backup](../../confiabilidade/backup/backup.md) é independente da réplica.

## Fonte primária

- [Longhorn documentation](https://longhorn.io/docs/)
