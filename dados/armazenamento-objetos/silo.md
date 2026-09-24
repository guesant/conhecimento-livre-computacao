# Silo

Silo é um storage de objetos compatível com a API S3, mantido como fork do
MinIO pelo projeto PGSTY. A compatibilidade inclui a organização de objetos e
as APIs necessárias para muitos clientes S3, mas cada versão do fork deve ser
avaliada pelas próprias notas de compatibilidade e release notes.

Silo é adequado para dados descartáveis ou de integração que precisam de uma
interface de objeto, como o cache distribuído do GitLab Runner. O cache não é
backup: perder ou expirar um objeto deve apenas causar um cache miss e uma nova
execução do job.

## Limites relevantes

O limite de tamanho do objeto, de partes de multipart upload, de versões e de
objetos listados por operação deve ser considerado ao escolher a chave e o
formato do cache. A capacidade real continua limitada pelo hardware, filesystem,
rede e número de operações concorrentes. Silo documenta limites de API, mas o
operador ainda precisa reservar folga de disco e memória.

Credenciais devem ser específicas para o bucket do runner e ter somente as
permissões necessárias. Use TLS, pin de versão, monitoramento e backup
independente para qualquer bucket que contenha dados não descartáveis.

## Garbage collection e lifecycle

Um bucket de cache deve ter regras de lifecycle desde a criação. Expire objetos
atuais por idade, remova versões não correntes quando versionamento estiver
habilitado e limpe delete markers. O período deve cobrir o intervalo em que o
cache gera economia real, não o tempo de retenção de um artefato de auditoria.

Como cache do GitLab Runner é recriável, uma política inicial conservadora pode
combinar TTL curto, prefixos por projeto e retenção limitada de versões. O
operador deve observar bytes usados, crescimento, objetos expirados e falhas do
processamento de lifecycle. Se o limite de armazenamento for atingido, o
comportamento esperado é reduzir acertos de cache, não interromper o GitLab.

## Relações

- [Cache de GitLab Runner](../../ci/gitlab-runner/cache.md) configura Silo como
  backend S3 distribuído.
- [Supply chain e SBOM](../../supply-chain-e-sbom.md) orienta pinagem, SBOM e
  verificação da imagem do serviço.
- [Backup](../../confiabilidade/backup/backup.md) diferencia durabilidade de
  dados de cache descartável.

## Fontes primárias

- [Silo](https://github.com/pgsty/silo)
- [Silo server limits](https://github.com/pgsty/silo/blob/main/docs/minio-limits.md)
- [Silo bucket lifecycle](https://github.com/pgsty/silo/blob/main/docs/bucket/lifecycle/README.md)
