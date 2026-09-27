# Policy Store

Policy Store é o armazenamento de policies, modelos, roles, relações ou
atributos usados por um sistema de autorização.

## Requisitos

O store deve oferecer versionamento, controle de acesso, backup, auditoria e
propagação previsível. A disponibilidade do store pode afetar a capacidade de
tomar decisões novas.

## Separação

O store de policies não precisa ser o mesmo banco do domínio. Separar os dois
reduz acoplamento, mas exige sincronização e uma estratégia de consistência.
