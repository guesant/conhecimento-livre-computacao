# Velero

Velero protege e restaura recursos Kubernetes e pode integrar proteção de volumes.

BackupStorageLocation guarda dados de backup em object storage. Mecanismos de volume podem usar snapshots do provedor ou filesystem backup conforme configuração.

Velero é útil quando restauração seletiva, migração ou proteção integrada de recursos Kubernetes é necessária. Ele não elimina a necessidade de compreender consistência específica de bancos e aplicações.

Veja [backup](backup.md) e [teste de restauração](teste-de-restauracao.md).