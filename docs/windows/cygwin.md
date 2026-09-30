# Cygwin

Cygwin é um ambiente Unix-like para Windows formado por uma DLL de compatibilidade POSIX, um instalador e um conjunto de pacotes. A DLL traduz operações esperadas por aplicações POSIX para APIs do Windows. O resultado é uma sessão com shell, paths, processos e utilitários semelhantes aos de um sistema Unix, sem executar um kernel Linux.

## Modelo de execução

Programas compilados para Cygwin normalmente dependem da runtime Cygwin. Eles não são automaticamente binários Win32 nativos. A visão `/`, `/home`, `/usr` e `/etc` é uma representação POSIX sobre uma árvore Windows, com mapeamentos configurados no ambiente.

Isso melhora a portabilidade de software que depende de `fork`, sinais, pseudo-terminals e convenções POSIX, mas introduz uma camada de compatibilidade. Um programa Cygwin e um programa nativo Windows podem ter expectativas diferentes sobre paths, permissões, sockets e processo pai.

## Pacotes e build

O instalador seleciona mirrors e pacotes Cygwin. O projeto constrói a runtime e os pacotes para o ambiente Cygwin, enquanto aplicações podem ser compiladas a partir de source packages e receitas do projeto. O resultado deve ser distinguido de uma build MinGW, que não depende da mesma runtime POSIX.

## Quando usar

Cygwin é útil para portar ferramentas Unix que precisam de compatibilidade POSIX real e para oferecer um ambiente shell integrado ao Windows. Não é a escolha natural quando o objetivo é produzir um executável Windows pequeno, independente da DLL Cygwin, ou executar um kernel e userland Linux reais.

## Fonte primária

- [Cygwin documentation](https://cygwin.com/docs.html)
- [Cygwin User's Guide](https://cygwin.com/cygwin-ug-net/cygwin-ug-net.html)
