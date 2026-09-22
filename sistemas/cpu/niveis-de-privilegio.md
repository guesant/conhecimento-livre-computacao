# Níveis de privilégio

Processadores oferecem mecanismos para distinguir execução privilegiada de execução não privilegiada. O sistema operacional usa essa separação para impedir que uma aplicação comum controle diretamente memória, dispositivos ou estruturas críticas do kernel.

## Caso de uso

Quando um processo precisa abrir um arquivo, criar um socket ou configurar memória, ele não deve simplesmente executar arbitrariamente a implementação privilegiada do kernel. Ele solicita a operação por uma interface controlada, normalmente uma system call.

## Boa prática

Ao explicar privilégio, diferencie privilégio de CPU, identidade de usuário e permissões do sistema operacional. Root é uma identidade privilegiada no modelo Unix; não é sinônimo de "ring 0".

## Má prática

Dizer que uma aplicação "entra em kernel mode porque é root" confunde mecanismos. Um processo root continua executando código de aplicação em modo de usuário e atravessa a fronteira do kernel por mecanismos controlados.

## Segurança

A separação reduz o impacto de código defeituoso ou malicioso. Vulnerabilidades no kernel são especialmente relevantes porque podem permitir atravessar essa fronteira de forma não prevista.

## Continue por aqui

[System calls](../kernel/system-calls.md) explica a interface usada para solicitar serviços privilegiados.