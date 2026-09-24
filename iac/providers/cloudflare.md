# Provider Cloudflare

O provider Cloudflare permite declarar recursos e consultar dados da conta Cloudflare, incluindo zonas, DNS, regras e túneis conforme a cobertura da versão usada. Ele é útil quando a borda pública precisa seguir o mesmo ciclo de revisão da infraestrutura.

## Cuidados

Use uma API token com escopo mínimo por zona e serviço. Separe recursos gerenciados pelo OpenTofu de mudanças manuais e confirme dependências entre DNS, certificados, túneis e regras antes de aplicar.

## State

O state pode conter identificadores e valores sensíveis retornados pela API. Use backend remoto cifrado, lock e controle de acesso, e não exponha o plano em logs públicos.

## Fonte primária

- [Cloudflare provider](https://registry.opentofu.org/providers/cloudflare/cloudflare/latest)
