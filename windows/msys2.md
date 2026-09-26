# MSYS2

MSYS2 é uma distribuição de ferramentas e bibliotecas para desenvolvimento no Windows. Ela combina um ambiente shell Unix-like, o subsistema MSYS2 e toolchains MinGW-w64 para criar programas nativos Windows. O gerenciador `pacman` instala os pacotes e mantém os ambientes atualizados.

## Ambientes

O ambiente `MSYS` é usado para ferramentas que dependem da camada POSIX e não precisam ser distribuídas como executáveis Windows nativos. Ambientes como `UCRT64`, `MINGW64`, `CLANG64` e outros produzem aplicações nativas com runtime e ABI específicos.

Não misture indiscriminadamente `/usr/bin` do MSYS com `/ucrt64/bin` ou outro prefixo MinGW. A escolha do shell define PATH, compilador, bibliotecas e o tipo de binário gerado.

## Pacotes e build

MSYS2 mantém repositórios oficiais e receitas de build baseadas em PKGBUILD, com `pacman`, `makepkg` e funções específicas para os targets. O projeto fornece toolchains e pacotes prontos; o usuário pode construir pacotes locais, mas deve considerar a ABI do ambiente escolhido.

## Comparação

MSYS2 é mais integrado que uma instalação manual de MinGW porque fornece shell, package manager e toolchains coordenados. Ele não é uma distribuição Linux e não substitui WSL quando a aplicação depende de syscalls, namespaces ou um kernel Linux.

## Fontes primárias

- [MSYS2 introduction](https://www.msys2.org/wiki/MSYS2-introduction/)
- [MSYS2 environments](https://www.msys2.org/docs/environments/)
- [MSYS2 repositories and mirrors](https://www.msys2.org/docs/repos-mirrors/)
