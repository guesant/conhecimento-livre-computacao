# Compatibilidade Unix no Windows

Compatibilidade Unix no Windows não é uma propriedade única. Algumas soluções
implementam uma camada de APIs, outras fornecem compiladores para binários
nativos e outras executam um kernel Linux ou uma distribuição integrada.

## Modelos

- [Cygwin](../cygwin.md) fornece uma camada de compatibilidade POSIX e um
  ambiente de ferramentas Unix.
- [MinGW](../mingw.md) produz binários Windows nativos usando toolchains GNU.
- [MSYS2](../msys2.md) combina um ambiente shell com toolchains e pacotes para
  desenvolvimento no Windows.
- [WSL](../wsl.md) integra fluxos Linux ao Windows.
- [WSL 1 e WSL 2](../wsl1-e-wsl2.md) compara a camada de tradução e a
  virtualização leve usadas pelas duas gerações.

## Critério de escolha

Use uma camada POSIX quando o objetivo principal for portar ferramentas e
scripts. Use MinGW ou MSYS2 quando o resultado precisar ser um executável
nativo do Windows. Use WSL quando o ambiente de execução precisar se comportar
como Linux e a integração com o host for aceitável.
