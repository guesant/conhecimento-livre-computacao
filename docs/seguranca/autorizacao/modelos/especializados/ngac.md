# Next Generation Access Control

Next Generation Access Control, NGAC, é uma arquitetura de controle de acesso orientada a políticas e grafos. Ela representa usuários, atributos, recursos e relações de privilégio em uma estrutura formal, permitindo administrar associações e políticas de maneira separada da aplicação.

## Modelo de grafo

O modelo usa nós e relações para representar categorias, usuários, recursos e privilégios. Uma política pode associar um atributo a um recurso e definir quais operações aquele atributo habilita. Atributos podem formar hierarquias e permitir que uma associação seja reutilizada.

O grafo facilita expressar delegação e administração, mas exige limites claros para quem pode alterar a própria política. A pessoa que administra vínculos não deve automaticamente poder conceder privilégios além do seu escopo.

## Administração

NGAC é interessante quando a pergunta não é apenas "o usuário pode ler?", mas também "quem pode criar esta associação, em qual escopo e sob quais condições?" Essa administração de privilégios é relevante em ambientes federados e com delegação entre unidades.

## Comparação

ReBAC concentra relações entre entidades. NGAC enfatiza uma arquitetura mais geral de atributos, privilégios e administração de políticas. PBAC pode expressar as regras que governam o grafo. A escolha depende de se o problema principal é colaboração entre recursos ou governança formal de concessões.

## Riscos

Grafos muito genéricos podem ser difíceis de explicar e auditar. Valide ciclos, alcance de relações, heranças inesperadas, revogação e alterações administrativas. Teste tanto uma decisão de acesso quanto a decisão de quem pode mudar a política.

## Fontes

- [NIST IR 8112, Policy Machine](https://csrc.nist.gov/pubs/ir/8112/final)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
