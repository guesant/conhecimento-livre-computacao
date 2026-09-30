# Gerenciamento de segredos

Gerenciamento de segredos cobre armazenamento, acesso, entrega, rotação,
revogação e auditoria de valores sensíveis. O problema não termina quando o
valor é cifrado: ele reaparece no bootstrap, no runtime, em logs, backups,
caches e ferramentas de observabilidade.

## Famílias

Cifrar no Git mantém um valor versionado em forma protegida. Um secret store
externo mantém o valor fora do repositório e entrega sob demanda. Sealed
Secrets cifra para um controller específico do cluster. CSI pode montar o
valor sem materializar um Secret nativo.

Cada família muda o domínio de falha, a portabilidade, o bootstrap e o
procedimento de recuperação.

## Ciclo de vida

O ciclo inclui gerar, armazenar, autorizar, entregar, usar, rotacionar e
revogar. O consumidor deve conseguir trocar o valor sem expor o antigo e sem
interrupção desnecessária.

## Relações

- [Secret](secret.md) define o objeto sensível.
- [Bootstrap](bootstrap.md) trata a primeira credencial.
- [Rotação](rotation.md) troca valor em uso.
- [SOPS](sops.md) cifra valores estruturados no Git.
- [age](age.md) protege arquivos com recipients e identities.
- [SOPS keyservice](sops-keyservice.md) delega operações de chave a um serviço local ou remoto.
- [Custódia de chaves fora do host](custodia-de-chaves-fora-do-host.md) compara
  YubiKey, agentes, TPM e Secure Enclave contra ataques à estação do operador.
- [Secret store externo](../../secret-store-externo.md) compara backends.

## Fonte primária

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
