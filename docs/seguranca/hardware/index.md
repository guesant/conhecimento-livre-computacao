# Hardware de confiança

Hardware de confiança protege operações criptográficas ou medições de
integridade fora do processo geral que usa o sistema. O objetivo pode ser
impedir exportação de chaves, liberar uma operação somente após uma condição,
medir o estado de boot ou produzir uma attestation verificável.

Isso não torna o dispositivo confiável em todos os sentidos. O sistema ainda
precisa controlar quem pode pedir uma operação, qual contexto é autorizado,
como as chaves são recuperadas e o que acontece quando o hardware falha.

- [TPM](tpm.md) descreve o módulo de confiança da plataforma.
- [Secure Enclave](secure-enclave.md) descreve o processador isolado das
  plataformas Apple.
- [YubiKey](yubikey/index.md) descreve autenticadores físicos, famílias,
  conectores, protocolos, NFC, biometria e variantes de conformidade.
- [Agentes de chave](../identidade/agentes/index.md) descreve processos que
  usam arquivos, tokens ou hardware para realizar operações.
