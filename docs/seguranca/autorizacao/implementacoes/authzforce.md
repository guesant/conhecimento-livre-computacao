# AuthzForce

AuthzForce é uma implementação de autorização baseada em XACML. Ela avalia
políticas com atributos de sujeito, recurso, ação e ambiente, produzindo uma
decisão conforme o algoritmo de combinação configurado.

## Modelo

O fluxo clássico envolve um PEP, um PDP, um Policy Administration Point e um
Policy Information Point. A decisão pode depender de atributos consultados em
fontes externas, o que torna timeout e disponibilidade parte do desenho.

## Quando usar

AuthzForce é relevante quando compatibilidade com XACML e ABAC formal é um
requisito. Para uma aplicação pequena, a complexidade do modelo pode superar o
benefício de uma biblioteca local.

## Fonte

- [AuthzForce](https://authzforce.github.io/)
