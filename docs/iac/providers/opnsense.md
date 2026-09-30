# Provider OPNsense

O provider OPNsense administra recursos do firewall OPNsense por API, como interfaces, aliases, regras, NAT e serviços suportados pelo provider. A cobertura depende da versão e não deve ser confundida com a configuração completa disponível na interface do produto.

## Cuidados

Proteja a API, use uma conta ou chave com permissões mínimas e valide o plano fora do caminho de administração antes de aplicar. Uma regra incorreta pode interromper o acesso ao próprio firewall, por isso mantenha uma forma independente de recuperação.

## Relações

- [OPNsense](../../rede/roteamento/opnsense.md) explica o produto e seus limites.
- [pfSense](../../rede/roteamento/pfsense.md) é uma alternativa com ecossistema e provider diferentes.

## Fonte primária

- [OPNsense provider](https://registry.opentofu.org/providers/stevenaldinger/opnsense/latest)
