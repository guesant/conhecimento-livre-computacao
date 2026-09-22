# System calls

System calls são a interface pela qual um processo solicita operações ao kernel. Elas formam uma fronteira de privilégio: a aplicação prepara argumentos, executa a transição definida pela arquitetura e o kernel valida e executa a operação.

## Casos de uso

Abrir arquivos, criar processos, mapear memória, comunicar por sockets e consultar informações do sistema dependem de serviços do kernel expostos por system calls.

## Exemplo

Uma função de biblioteca como `open()` pode fornecer uma API conveniente em user space e, em algum ponto, solicitar ao kernel a operação correspondente. API de biblioteca e system call não são necessariamente a mesma camada.

## Boas práticas

Use ferramentas como `strace` para observar a fronteira quando o objetivo é entender por que um processo falha ao acessar arquivo, rede ou outro recurso. Interprete o trace junto com errno e contexto do processo.

## Más práticas

Não conclua que toda função de libc corresponde um-para-um a uma syscall. Também não trate uma syscall permitida como autorização suficiente: capabilities, LSMs, namespaces e permissões de filesystem podem impor controles adicionais.

## Segurança

[seccomp](../linux/seccomp.md) permite restringir quais syscalls um processo pode invocar. Esse filtro é complementar a controles que decidem se uma operação permitida pode acessar um recurso específico.

## Continue por aqui

[seccomp](../linux/seccomp.md) restringe a superfície de chamadas. [Capabilities](../linux/capabilities.md) decompõem poderes privilegiados.