# Relationship Tuple

Relationship tuple é uma afirmação estruturada de relação entre um subject,
uma relação e um resource. Um exemplo conceitual é `user:gabriel member
document:manual`.

## Papel

Tuples são dados de autorização. O schema interpreta esses dados e deriva
permissões. Separar fatos de permissões facilita explicar por que uma decisão
foi permitida.

## Cuidados

Identificadores precisam ser estáveis, relações devem ter escopo de tenant e
operações de escrita precisam ser idempotentes. Um tuple incorreto pode ampliar
acesso sem que o código da aplicação tenha mudado.
