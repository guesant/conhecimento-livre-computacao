# Linux Security Modules

Linux Security Modules, LSM, é uma infraestrutura de hooks do kernel que permite
que mecanismos de segurança participem das decisões de acesso. Ela não é uma
política pronta nem um produto único. SELinux, AppArmor, Smack, TOMOYO e outros
mecanismos usam partes desse framework com modelos diferentes.

## Onde o LSM atua

Hooks podem ser consultados em operações sobre arquivos, processos, sockets,
credenciais, mounts e outros objetos do kernel. Uma decisão LSM complementa
permissões DAC, capabilities, namespaces e seccomp. Permitir uma operação numa
camada não garante que ela será permitida por todas as demais.

O mecanismo de segurança precisa definir como a política é carregada, qual
estado é efetivo, como ocorre a composição e onde as negações são registradas.
O nome do módulo ou a presença do pacote não prova que uma política está ativa.

## Relações

- [Mandatory Access Control](../../seguranca/autorizacao/modelos/mac.md) explica
  a ideia de política mandatória.
- [SELinux](../../seguranca/mac-selinux.md) usa contextos, domínios e tipos.
- [AppArmor](../../seguranca/mac-apparmor.md) usa perfis centrados em programas.
- [Capabilities](capabilities.md) e [seccomp](seccomp.md) restringem outras
  dimensões da execução.

## Fonte primária

- [Linux Security Modules documentation](https://www.kernel.org/doc/html/latest/security/lsm.html)
