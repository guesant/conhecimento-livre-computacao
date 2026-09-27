# Pundit

Pundit é uma biblioteca de autorização para Ruby e Rails baseada em classes de
policy. Cada policy concentra decisões para um recurso ou contexto.

## Uso

O controller chama métodos como authorize e policy_scope. O primeiro protege
uma ação sobre um objeto; o segundo evita que a listagem retorne objetos fora
do escopo permitido.

## Limites

A convenção não impede erro de integração. Teste tanto decisões individuais
quanto escopos de consulta, especialmente em cenários multi-tenant.

## Fonte

- [Pundit](https://github.com/varvet/pundit)
