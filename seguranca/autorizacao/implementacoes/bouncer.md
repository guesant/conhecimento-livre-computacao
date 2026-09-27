# Bouncer

Bouncer é uma biblioteca Laravel para administrar abilities, roles e relações
de autorização. Ela permite declarar capacidades e associá-las a usuários ou
papéis.

## Cuidados

Permissões armazenadas no banco precisam de migração, auditoria e uma política
de cache. Uma mudança de role deve invalidar decisões antigas e não pode ser
aceita apenas porque veio de uma tela administrativa.

## Fonte

- [Bouncer](https://github.com/JosephSilber/bouncer)
