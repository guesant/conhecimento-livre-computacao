# Symfony Security Voters

Symfony Security Voters é o mecanismo de autorização do Symfony baseado em
voters. Um voter decide se um sujeito pode executar um atributo sobre um
objeto.

## Modelo

O sistema consulta voters aplicáveis e combina suas respostas conforme a
estratégia configurada. A regra de negócio fica no voter, enquanto o
controller usa uma verificação explícita.

## Limites

Voters não substituem filtragem de consultas. Uma aplicação precisa proteger a
listagem, o detalhe e a mutação, e não apenas esconder controles da interface.

## Fonte

- [Symfony Voters](https://symfony.com/doc/current/security/voters.html)
