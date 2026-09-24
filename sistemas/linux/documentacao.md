# Documentação de comandos Linux

Man pages são a referência local mais direta para um comando e são divididas
em seções. A seção 1 cobre comandos de usuário, a 2 chamadas de sistema, a 3
bibliotecas, a 5 formatos de arquivo, a 8 administração do sistema. O número
é importante quando existem páginas homônimas, como `printf(1)` e `printf(3)`.

`info` apresenta documentação estruturada de alguns projetos GNU, enquanto
`help` mostra a ajuda dos builtins do shell. `type` e `command -v` distinguem
um builtin, alias, função ou binário antes de consultar sua documentação.

Essa distinção evita um diagnóstico enganoso: `which` pode não conhecer
aliases e funções, e uma opção documentada para o binário GNU pode não existir
quando o nome resolve para um builtin ou para uma implementação BusyBox.

## Relações

- [GNU Coreutils](coreutils.md) apresenta os utilitários básicos.
- [Shells e scripts](../../shells-e-scripts.md) explica a camada que resolve
  builtins, funções e executáveis.

## Fontes primárias

- [Man-pages project](https://www.kernel.org/doc/man-pages/)
- [GNU Info](https://www.gnu.org/software/texinfo/)
