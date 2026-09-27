# Mapa de mutações e recuperação

Exclusão, edição, revisões e WAL têm responsabilidades diferentes. O histórico editorial responde qual conteúdo pode ser publicado. Auditoria responde quem executou uma ação. WAL protege recuperação física e replicação.

- [Exclusão](exclusao.md) trata de soft delete, hard delete, retenção e purga.
- [Revisões](revisoes.md) trata de hard edit, versionamento editorial e ponteiros de publicação.
- [WAL](wal.md) trata de Write-Ahead Logging, replay, replicação e PITR.

Esses mecanismos podem coexistir, mas não devem ser usados como substitutos uns dos outros.
