# Linux capabilities

Linux capabilities dividem parte dos poderes tradicionalmente concentrados no usuário root em unidades independentes. Um processo pode receber uma capability específica sem receber todo o conjunto de privilégios.

## Casos de uso

Uma aplicação que precisa realizar uma operação privilegiada específica pode receber somente a capability correspondente. Em containers, runtimes normalmente começam com um conjunto limitado e permitem remover ou adicionar capabilities explicitamente.

## Exemplo

`CAP_NET_ADMIN` permite várias operações administrativas de rede. `CAP_CHOWN` permite alterar ownership em situações que um usuário comum não poderia. `CAP_SYS_ADMIN` cobre uma superfície muito ampla e merece tratamento especialmente restritivo.

## Boas práticas

Comece pelo menor conjunto possível. Em containers, `cap-drop=ALL` seguido da adição explícita do necessário é um modelo fácil de auditar quando a aplicação suporta essa postura. Teste a carga real antes de promover a política.

## Más práticas

Adicionar `CAP_SYS_ADMIN` para corrigir genericamente um erro de permissão frequentemente equivale a remover uma grande parte do isolamento pretendido. Também é inadequado confundir capability com permissão de arquivo ou filtro de syscall.

## Complementos

[seccomp](seccomp.md) decide quais chamadas podem ser feitas; LSMs como AppArmor e SELinux podem restringir acesso a objetos; `no_new_privs` impede determinadas formas de aquisição de privilégios durante exec.

## Fontes

- capabilities(7): <https://man7.org/linux/man-pages/man7/capabilities.7.html>

## Continue por aqui

[seccomp](seccomp.md) complementa capabilities restringindo a superfície de syscalls.
