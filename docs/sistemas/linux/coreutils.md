# GNU Coreutils

GNU Coreutils é o conjunto de utilitários de linha de comando que forma o
padrão de fato em muitas distribuições Linux. Ferramentas como `cp`, `mv`,
`rm`, `cat`, `ls`, `sort`, `cut` e `wc` implementam operações básicas de
arquivos, texto e processos.

BusyBox reúne implementações menores de muitos comandos em um único binário,
uma escolha comum em initramfs e sistemas embarcados. `uutils/coreutils` é uma
reimplementação em Rust que busca compatibilidade com o comportamento esperado
dos utilitários GNU.

Scripts portáveis não devem presumir que uma opção específica de GNU existe em
BusyBox ou em outro Unix. A implementação real deve ser descoberta com `type`
ou `command -v` antes de atribuir semântica a um nome.

## Relações

- [Documentação de comandos](documentacao.md) explica como consultar man pages,
  `info` e `help`.
- [Shells e scripts](../../shells-e-scripts.md) trata da portabilidade do
  interpretador.

## Fontes primárias

- [GNU Coreutils](https://www.gnu.org/software/coreutils/)
- [BusyBox](https://busybox.net/)
- [uutils/coreutils](https://uutils.github.io/coreutils/)
