# Conceitos de autorização

Autorização decide se um subject pode executar uma action sobre um resource em
um contexto. A decisão pode ser feita por uma biblioteca local, por um PDP
externo, pelo banco, por um gateway ou por uma combinação desses pontos.

## Mapa

Modelos como RBAC, ABAC e ReBAC descrevem como a decisão é representada.
PDP, PEP, PAP e PIP descrevem responsabilidades da arquitetura. Subject,
resource, action, relation e permission descrevem os dados da decisão.

Fine-grained authorization, object-level authorization, RLS e field-level
authorization delimitam o nível de detalhe. Default deny, least privilege,
deny-overrides e allow-overrides definem propriedades de segurança e
combinação de regras.

As páginas de implementação mostram como ferramentas concretas realizam essas
ideias. Elas não devem ser tratadas como equivalentes apenas porque usam a
palavra policy.
