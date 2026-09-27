# Polar

Polar é a linguagem de políticas do Oso. Ela expressa regras de autorização em
termos de atores, recursos, papéis e relações.

## Uso

A aplicação fornece classes, fatos e contexto. A política consulta esses dados
para responder se uma ação é permitida. Esse modelo é útil quando a regra
precisa permanecer próxima do domínio e das abstrações da aplicação.

## Cuidados

Fatos incompletos ou objetos carregados de forma inconsistente produzem
decisões incorretas. A política deve ter testes de autorização, limites claros
para acesso a dados e uma estratégia para auditar decisões.

## Fonte

- [Documentação da linguagem Polar](https://www.osohq.com/docs/reference/polar)
