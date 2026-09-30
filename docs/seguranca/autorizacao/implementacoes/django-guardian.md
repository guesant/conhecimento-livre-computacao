# django-guardian

django-guardian adiciona permissões por objeto ao sistema de autorização do
Django. Ele complementa permissões globais com grants associados a usuários,
grupos e instâncias de modelo.

## Uso

É adequado quando Django auth já fornece identidade e papéis, mas o domínio
precisa decidir acesso a objetos individuais. Consultas devem usar filtros de
permissão para não carregar dados indevidos.

## Fonte

- [django-guardian](https://django-guardian.readthedocs.io/)
