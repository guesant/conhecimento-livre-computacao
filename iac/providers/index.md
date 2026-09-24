# Providers do OpenTofu

Providers são plugins que traduzem recursos e data sources do OpenTofu para APIs externas. O OpenTofu usa o Registry para descobrir providers, resolver versões e verificar checksums no lockfile; a existência de um provider no Registry não significa que ele seja mantido pelo projeto OpenTofu.

## Critérios de escolha

Avalie o mantenedor, a frequência de releases, a cobertura da API, a compatibilidade com a versão do OpenTofu, o tratamento de segredos e a qualidade do import e do refresh. Fixe a versão no bloco `required_providers`, preserve `.terraform.lock.hcl` e revise mudanças de schema antes de aplicar.

## Providers documentados

- [Cloudflare](cloudflare.md) gerencia DNS, zonas, regras e outros serviços da Cloudflare.
- [Proxmox](proxmox.md) gerencia recursos do Proxmox VE.
- [OPNsense](opnsense.md) integra configurações de firewall e rede pela API.
- [Keycloak](keycloak.md) declara realms, clientes e identidades.
- [AWS](aws.md), [GKE](gke.md) e [Azure](azure.md) expõem recursos de provedores de nuvem.

Eles têm modelos de estado, escopos de credenciais e riscos operacionais diferentes. Não permita que dois owners reconciliem o mesmo recurso e não coloque tokens em arquivos de state sem backend e controles adequados.

## Relações

- [OpenTofu](../opentofu.md) explica o ciclo de plano, aplicação e state.
- [Provider](../provider.md) define o conceito de provider, resource e data source.
- [Estado](../state.md) explica por que o backend e o lock são parte da segurança operacional.

## Fontes primárias

- [OpenTofu Registry](https://registry.opentofu.org/)
- [OpenTofu provider requirements](https://opentofu.org/docs/language/providers/requirements/)
