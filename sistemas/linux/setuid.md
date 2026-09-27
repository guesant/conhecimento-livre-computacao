# setuid

Set-user-ID, setuid, é um bit de modo de arquivo que pode fazer um executável
iniciar com o effective user ID do proprietário do arquivo. Ele permite que um
programa realize uma operação privilegiada sem conceder ao processo chamador
todos os privilégios do usuário dono, mas transforma o programa em uma fronteira
de segurança crítica.

## Identidades do processo

Um processo possui IDs real, efetivo, salvo e de filesystem. O real indica quem
iniciou a operação; o efetivo participa de verificações de permissão; o salvo
permite algumas transições controladas. A diferença explica por que um binário
setuid pode começar com identidade de um usuário privilegiado e depois reduzir
seu privilégio.

`setgid` é o equivalente relacionado ao grupo. Capabilities oferecem uma
granularidade diferente, dividindo poderes do superusuário. Um programa setuid
mal projetado ainda pode herdar ambiente, descritores, caminhos e argumentos
perigosos, mesmo quando usa capabilities em parte do fluxo.

## Riscos

PATH, `LD_PRELOAD`, variáveis de ambiente, arquivos temporários, symlinks,
locale, parsing e chamadas a programas externos são riscos clássicos. O kernel
ativa secure execution em certas condições, mas o programa precisa limpar
entrada, usar caminhos absolutos, reduzir IDs, fechar descritores e evitar
dependências controladas pelo chamador.

Filesystems podem montar `nosuid`, impedindo o efeito do bit em uma árvore.
Containers e namespaces também alteram a interpretação do privilégio. Não use
o fato de um arquivo possuir setuid como prova de que o processo terá root
efetivo em qualquer ambiente.

## Auditoria

Inventarie arquivos setuid e setgid, justifique cada um e monitore alterações.
Remova o bit quando a função não precisar dele, mantenha pacotes atualizados e
teste o caminho de execução com um usuário sem privilégios. `find` pode localizar
arquivos, mas a decisão de remover exige conhecer o pacote e a função do sistema.

## Relações

- [Capabilities Linux](../../kubernetes/seguranca/linux-capabilities.md) compara privilégio granular.
- [Syscalls](../kernel/system-calls.md) trata a interface usada pelo binário.
- [auditd](auditd.md) pode registrar execução e mudança de arquivos sensíveis.

## Fontes primárias

- [execve(2)](https://man7.org/linux/man-pages/man2/execve.2.html)
- [credentials(7)](https://man7.org/linux/man-pages/man7/credentials.7.html)
- [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html)
