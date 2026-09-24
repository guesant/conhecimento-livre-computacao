# Terraform

Terraform é uma ferramenta declarativa de infraestrutura que usa HCL, providers
e state para planejar e aplicar mudanças em APIs externas.

## Modelo

A configuração descreve resources, data sources, variáveis e módulos. O
provider traduz a declaração para a API. O state conserva a identidade que
permite comparar o desejado com o observado.

O backend remoto e o lock são importantes quando o state é compartilhado. O
plano deve ser revisado antes do apply, especialmente quando contém
substituições ou destruições.

## Escolha

Terraform possui ecossistema amplo e providers maduros. A escolha também
envolve governança, licença, compatibilidade de módulos e política de
dependências da organização. Não trate arquivos HCL como garantia de
interoperabilidade perfeita entre versões e providers.

## Relações

- [OpenTofu](opentofu.md) mantém compatibilidade de linguagem com governança
  diferente.
- [Pulumi](pulumi.md) usa linguagens gerais e outro modelo de state.
- [HCL](hcl.md) define a linguagem comum.

## Fonte primária

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
