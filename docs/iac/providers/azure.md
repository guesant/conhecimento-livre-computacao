# Provider Azure

O provider AzureRM administra recursos do Microsoft Azure, incluindo grupos de recursos, identidade, rede, computação e serviços gerenciados. O provider AzureAD trata objetos do diretório quando essa separação for necessária.

## Cuidados

Separe subscriptions e estados conforme os limites de segurança e cobrança. Use identidades federadas ou managed identities quando possível, limite o escopo das roles e preserve o lockfile para evitar mudanças de schema inesperadas.

## Operação

Planeje dependências entre rede, identidade e workloads. Uma alteração no grupo de recursos pode ter impacto muito maior do que o recurso individual que aparece no arquivo HCL.

## Fonte primária

- [AzureRM provider](https://registry.opentofu.org/providers/hashicorp/azurerm/latest)
