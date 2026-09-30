# Organization-Based Access Control

Organization-Based Access Control, OrBAC, descreve autorização a partir de conceitos organizacionais. Em vez de ligar diretamente um usuário a uma permissão, a política relaciona organizações, papéis, atividades, visões e contextos.

## Conceitos

Uma política OrBAC pode dizer que um papel de auditor pode executar uma atividade de leitura sobre uma visão financeira dentro de um contexto de auditoria. Subjects concretos são associados a papéis, objetos a visões e operações a atividades.

Essa camada de abstração permite reutilizar a mesma regra em muitas organizações e separar a política organizacional dos nomes específicos de usuários e tabelas.

## Vantagens

OrBAC é expressivo para ambientes com várias organizações, políticas setoriais e contextos operacionais. Ele torna explícito que uma permissão depende tanto da função quanto do ambiente em que a atividade ocorre.

## Limitações

A nomenclatura e a administração são mais complexas que RBAC. A aplicação precisa definir quem administra cada organização e como conflitos entre políticas são resolvidos. Sem um catálogo de atividades e visões estável, a abstração vira apenas uma camada de nomes diferentes.

## Relação com ABAC e RBAC

OrBAC usa conceitos que podem ser implementados por atributos e papéis. ABAC pode representar organização e contexto como atributos. RBAC pode representar papéis organizacionais, mas não captura sozinho a relação entre atividade, visão e contexto.

## Casos adequados

Considere OrBAC para federações, instituições com políticas próprias, ambientes de saúde e educação e plataformas multi-organização com governança delegada. Para uma aplicação de tenant único, um modelo menor tende a ser mais fácil de revisar.

## Fontes

- [OrBAC, site do projeto](https://orbac.org/)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
