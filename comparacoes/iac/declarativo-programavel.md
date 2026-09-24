# Terraform/OpenTofu e Pulumi

Essas ferramentas provisionam infraestrutura por APIs e mantêm estado, mas usam modelos de autoria diferentes.

## Terraform e OpenTofu

HCL fornece uma linguagem declarativa específica para infraestrutura. Providers expõem recursos e data sources. O modelo favorece planos legíveis e uma linguagem limitada ao domínio.

OpenTofu preserva compatibilidade com grande parte do ecossistema Terraform e possui governança própria.

## Pulumi

Pulumi permite descrever infraestrutura em linguagens como TypeScript, Python, Go e C#. Isso oferece abstrações e ferramentas das linguagens gerais, mas também permite introduzir complexidade de software convencional na definição de infraestrutura.

## Quando HCL favorece o cenário

Equipes querem uma DSL comum independente da linguagem de aplicação, valorizam um ecossistema amplo de módulos/providers e a lógica de composição não exige abstrações sofisticadas.

## Quando linguagem geral favorece o cenário

A infraestrutura possui geração e abstrações complexas que se beneficiam de funções, tipos, testes e bibliotecas da linguagem, e a equipe consegue governar essa liberdade.

## Anti-patterns

HCL excessivamente metaprogramado fica difícil de ler. Pulumi usado como aplicação arbitrária pode esconder o grafo de infraestrutura atrás de abstrações profundas. Nos dois casos, abstração deve reduzir repetição sem apagar o recurso que será criado.

## Continue por aqui

[Infraestrutura como código](../../iac-provisionamento.md) explica a família antes da escolha de implementação.
