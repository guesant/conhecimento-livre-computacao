# django-rules

django-rules é uma biblioteca de autorização baseada em predicados para Django.
Regras são funções reutilizáveis que podem ser combinadas para responder se um
usuário pode executar uma ação.

## Cuidados

Predicados devem permanecer pequenos, determinísticos e testáveis. Dados usados
na decisão precisam vir do servidor e não de campos enviados sem validação pelo
cliente.

## Fonte

- [django-rules](https://github.com/dfunckt/django-rules)
