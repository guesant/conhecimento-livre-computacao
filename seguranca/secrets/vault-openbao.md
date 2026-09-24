# Vault e OpenBao

Vault e OpenBao são secret stores que centralizam valores, políticas, auditoria
e emissão ou integração com identidades. OpenBao é uma alternativa comunitária
compatível com conceitos do Vault.

## Unseal e domínio de falha

O store cifra dados em repouso e precisa ser destravado para servir valores.
Auto-unseal usa um KMS ou outra autoridade externa. Guardar a única chave de
unseal dentro do cluster que o store deveria proteger cria dependência
circular.

## Escolha

Um store dedicado é justificável quando rotação, auditoria, múltiplos
consumidores e políticas centralizadas compensam a operação adicional. Em um
ambiente pequeno, SOPS e age podem reduzir componentes e ainda oferecer
separação adequada.

## Relações

- [External Secrets Operator](external-secrets.md) integra o backend.
- [Bootstrap](bootstrap.md) trata a credencial inicial.
- [Rotação](rotation.md) descreve a substituição segura.

## Fontes primárias

- [Vault](https://developer.hashicorp.com/vault/docs)
- [OpenBao](https://openbao.org/docs/)
