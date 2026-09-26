# Estratégia de backup de cluster

O estado de um cluster com Kubernetes, banco de dados e segredos cifrados vive
em domínios diferentes. Um backup não cobre automaticamente os demais: o etcd
protege o estado da API, o CloudNativePG protege o banco PostgreSQL e a chave
age permite recuperar os segredos cifrados no GitOps.

As páginas canônicas separam os mecanismos:

- [Backup do etcd](confiabilidade/backup/etcd.md) cobre snapshots do datastore
  e restauração.
- [Backup do CloudNativePG](confiabilidade/backup/cloudnative-pg.md) cobre
  backup completo, WAL e recuperação para um ponto no tempo.
- [Backup da chave age](seguranca/secrets/age-key-backup.md) cobre a
  recuperação do material que decifra o repositório.

## Composição da recuperação

Uma reconstrução completa precisa recuperar os três domínios na ordem adequada
ao cenário. Restaurar objetos Kubernetes sem recuperar volumes não restaura um
banco. Recuperar o banco sem a chave age não permite reconstruir os manifests
cifrados. Guardar todos os materiais no mesmo host também elimina a proteção
contra a perda desse host.

O procedimento precisa manter cópias fora do domínio de falha original e
testar a restauração regularmente. Uma cópia nunca validada pode estar
corrompida, incompleta ou associada a uma rotação antiga.

## Relações

- [Backup](confiabilidade/backup/backup.md), [RPO](confiabilidade/backup/rpo.md) e [RTO](confiabilidade/backup/rto.md)
  define os objetivos de recuperação.
- [Reconstrução de cluster single-node e recuperação de segredos](../operacional/reconstrucao-de-cluster-single-node-e-recuperacao-de-segredos.md)
  trata do cenário operacional deste ambiente.
- [Estado fora do Git](../operacional/estado-fora-do-git.md) lista o material
  necessário para reconstrução.
