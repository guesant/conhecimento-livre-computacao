# Zanzibar-style authorization

Zanzibar-style authorization é uma família arquitetural de autorização
baseada em relações e tuples. O recurso não recebe apenas uma lista de papéis;
seu acesso é derivado de relações entre sujeitos, grupos, organizações e
outros recursos.

## Quando faz sentido

O modelo é útil para colaboração, hierarquias, compartilhamento e delegação
em que permissões por objeto mudam com frequência. Ele também permite que
vários serviços consultem uma fonte comum de relações.

## Custos

É necessário definir consistência, cardinalidade, ciclos de relações,
revogação, cache e proteção contra consultas excessivamente amplas. Para uma
aplicação com poucos papéis estáticos, RBAC local pode ser mais simples.

## Relações

- [ReBAC](../modelos/rebac.md) apresenta o modelo de autorização.
- [OpenFGA](../openfga.md) documenta uma implementação da família.
- [SpiceDB](spicedb.md) documenta outra implementação.
