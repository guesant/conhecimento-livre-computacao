# POSIX

POSIX é uma família de especificações que define interfaces e comportamentos
comuns para sistemas operacionais Unix-like. O padrão não é uma distribuição,
um kernel, um shell específico ou um gerenciador de pacotes. Ele delimita um
contrato de portabilidade para programas e scripts que precisam atravessar
implementações diferentes.

## O que o padrão cobre

A especificação cobre três grupos que aparecem juntos no uso cotidiano:

| Área | Exemplos |
| --- | --- |
| Linguagem de comandos | `sh`, expansão de parâmetros, pipelines e redirecionamentos |
| Utilitários | `grep`, `sed`, `awk`, `ls`, `cp` e `test` |
| Interfaces de sistema | `open()`, `read()`, `write()`, `fork()` e `exec()` |

O shell POSIX define o comportamento mínimo de uma linguagem de comandos. Bash,
Zsh e outros shells podem implementar esse contrato e adicionar extensões. Um
script que usa apenas a sintaxe padronizada tende a ser mais portátil que um que
depende de arrays Bash, substituições específicas ou opções não padronizadas.

Os utilitários também possuem um conjunto mínimo de opções e resultados. Uma
implementação GNU pode oferecer flags adicionais que não existem no BSD ou em
uma implementação minimalista. A diferença entre `date`, `sed` ou `grep` em
Linux, macOS e BSD costuma aparecer justamente fora desse subconjunto comum.

As APIs POSIX em C fornecem uma base para processos, arquivos, sinais, threads,
rede e sincronização. Isso não significa que um programa POSIX terá exatamente
o mesmo desempenho, os mesmos limites ou a mesma extensão de sistema em todos
os sistemas. Significa que existe uma interface comum que pode ser usada como
ponto de partida.

## O que POSIX não define

POSIX não determina o sistema de inicialização, o gerenciador de pacotes, a
estrutura completa do filesystem, a interface gráfica, o modelo de containers,
o mecanismo de segurança MAC ou a forma de distribuir imagens. Dois sistemas
podem compartilhar interfaces POSIX e ainda ter operações, defaults e ciclos de
atualização muito diferentes.

A compatibilidade também pode ter níveis diferentes. Uma ferramenta pode
implementar o subconjunto de forma estrita, oferecer um superconjunto compatível
ou declarar compatibilidade sem ter certificação formal. Para uma portabilidade
real, escreva contra o menor contrato necessário e teste em cada ambiente-alvo.

## Portabilidade de scripts

Um script portátil deve escolher o interpretador explicitamente, evitar
extensões de shell não necessárias e tratar diferenças de opções dos utilitários.
O uso de `#!/bin/sh` não torna um script automaticamente portátil: o conteúdo
também precisa seguir a linguagem POSIX e não assumir que `/bin/sh` é Bash.

Quando uma extensão é necessária, separe a parte específica do ambiente ou
declare o requisito. Isso torna a falha previsível e evita que uma execução
funcione em uma distribuição apenas porque o shell padrão oferece uma extensão
que não existe no destino.

## Relações

- [Famílias Unix](../../unix-familias-e-padroes.md) compara POSIX, BSD e as
  distribuições Linux.
- [Shells e scripts](../../shells-e-scripts.md) explica o contrato do shell e
  as extensões de Bash, Zsh e Fish.
- [GNU Coreutils](../linux/coreutils.md) mostra onde as implementações GNU
  ultrapassam o comportamento mínimo.
- [Documentação de comandos](../linux/documentacao.md) apresenta como verificar
  a implementação disponível no sistema.

## Fontes primárias

- [The Open Group, POSIX Base Specifications](https://pubs.opengroup.org/onlinepubs/9699919799/)
- [IEEE, Portable Operating System Interface](https://standards.ieee.org/standard/1003_1-2017.html)
