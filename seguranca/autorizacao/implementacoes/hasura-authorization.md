# Hasura Authorization

Hasura Authorization combina roles, session variables e regras de linha,
coluna e relacionamento para proteger uma API GraphQL. A policy é aplicada
próxima da consulta ao banco.

## Modelo

O role da sessão seleciona permissões para cada operação. Filtros de linha e
limites de coluna devem acompanhar o modelo de tenant e a origem dos claims.

## Limites

Uma regra GraphQL não substitui proteção de mutations fora do Hasura nem
garante segurança de funções SQL privilegiadas. Audite o schema exposto e os
permissões efetivas do banco.

## Fonte

- [Hasura Authorization](https://hasura.io/docs/3.0/auth/authorization/overview/)
