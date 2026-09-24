# Pulumi

Pulumi descreve infraestrutura usando linguagens de programação como TypeScript,
Python, Go e C#. O programa constrói um grafo de recursos que o engine
compara com o state e aplica por meio de providers.

## Trade-offs

Usar uma linguagem geral oferece abstrações, testes, loops e bibliotecas
existentes. Também introduz estado implícito no programa, dependências de
runtime, diferenças entre versões da linguagem e maior possibilidade de
lógica arbitrária no caminho de provisionamento.

A escolha é boa quando a infraestrutura realmente precisa de abstrações de
programação que HCL não expressa bem. Para configurações simples, o custo
cognitivo de uma linguagem geral pode superar o benefício.

## Segurança e state

State pode conter valores sensíveis e precisa de backend protegido e lock.
Credenciais devem entrar pelo ambiente ou secret manager. O programa não deve
imprimir segredos como efeito de debug ou preview.

## Relações

- [HCL](hcl.md) contrasta linguagem declarativa com linguagem geral.
- [State](state.md) é necessário independentemente do idioma.
- [Terraform](terraform.md) e [OpenTofu](opentofu.md) são alternativas.

## Fonte primária

- [Pulumi concepts](https://www.pulumi.com/docs/concepts/)
