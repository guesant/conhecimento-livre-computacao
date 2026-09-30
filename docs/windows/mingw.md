# MinGW

MinGW, especialmente a família MinGW-w64, é um conjunto de ferramentas GNU para produzir executáveis Windows nativos. Diferentemente de Cygwin, o resultado usa a API Windows e o runtime C escolhido pelo toolchain, sem exigir a runtime POSIX Cygwin para executar.

## Toolchain

Um toolchain MinGW combina compilador, assembler, linker, headers e bibliotecas para um target Windows. O prefixo do compilador distingue o target, por exemplo `x86_64-w64-mingw32`. O programa compilado pode ser executado diretamente no Windows, desde que suas DLLs e dependências estejam disponíveis.

MinGW não é um shell Unix. O shell, `make`, `bash` e utilitários podem vir de MSYS2, Cygwin ou outra distribuição, mas isso é separado do runtime do programa gerado.

## Variantes

MinGW-w64 oferece targets de 32 e 64 bits e diferentes runtimes C, como MSVCRT e UCRT. MSYS2 organiza esses targets em ambientes como UCRT64 e CLANG64. A escolha afeta ABI, bibliotecas, compatibilidade e distribuição do executável.

## Quando usar

Use MinGW quando o produto final precisa ser um binário Windows nativo e o projeto usa uma toolchain GNU. Use Cygwin quando a compatibilidade POSIX no runtime for um requisito. Use WSL quando a build depende de comportamento Linux real, filesystem Linux ou ferramentas que esperam o kernel Linux.

## Fontes primárias

- [MinGW-w64](https://www.mingw-w64.org/)
- [MSYS2 environments](https://www.msys2.org/docs/environments/)
