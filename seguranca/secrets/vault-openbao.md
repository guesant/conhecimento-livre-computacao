# Comparação: Vault e OpenBao

Vault e OpenBao compartilham o modelo de secret store centralizado, com
políticas, auditoria, autenticação de workloads, armazenamento cifrado e
unseal. As implementações possuem páginas próprias.

- [Vault](vault.md) detalha a implementação HashiCorp.
- [OpenBao](openbao.md) detalha a implementação comunitária compatível.
- [Auto-unseal e KMS](auto-unseal.md) explica a dependência externa comum às
  duas alternativas.

## Critérios de escolha

A escolha deve considerar licença, governança, compatibilidade de APIs,
integrações, suporte, operação e migração. A semelhança de conceitos não
significa que todos os plugins, recursos ou contratos operacionais sejam
intercambiáveis.

Em ambientes pequenos, [SOPS e age](sops-age.md) podem cumprir o requisito
com menos componentes. [External Secrets Operator](external-secrets.md) é a
camada de integração declarativa quando os consumidores são workloads
Kubernetes.
