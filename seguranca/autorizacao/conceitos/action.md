# Action

Action é a operação que o subject tenta executar sobre um resource. Exemplos
são read, update, delete, publish, approve e download.

## Granularidade

Actions devem refletir risco e semântica de negócio. Usar apenas write pode
misturar editar, publicar e excluir, dificultando menor privilégio.

## Contrato

O nome da action precisa ser estável entre PEP, PDP, policy e auditoria. Uma
mudança de nome exige migração ou compatibilidade explícita.
