# Coreutils, alternativas e onde encontrar ajuda

Comandos como ls, cp, mv, cat, rm e mkdir parecem parte do próprio shell, mas não são: cada um é um binário separado, agrupado sob o nome coreutils, e qual implementação real responde por esses nomes varia mais do que a maioria dos scripts assume.

[Shells e scripts](shells-e-scripts.md) já cobriu como sed, awk e ps divergem entre GNU e BSD; esta página foca no conjunto ainda mais básico de utilitários, em duas alternativas reais ao GNU Coreutils, e em como encontrar ajuda sobre qualquer um desses comandos sem precisar de uma busca externa.

## GNU Coreutils: o padrão de fato em distribuições Linux de servidor

O GNU Coreutils é o pacote que fornece a implementação de ls, cp, mv, rm, cat, mkdir, chmod, chown e dezenas de outros utilitários básicos na maioria das distribuições Linux voltadas a servidor.

Cada um desses comandos tem uma base definida pelo padrão [POSIX](unix-familias-e-padroes.md), o conjunto mínimo de flags e comportamento que qualquer sistema compatível precisa oferecer, mas o GNU Coreutils vai além, com extensões próprias que se tornaram tão comuns que muitos scripts as usam sem perceber que não são universais.

Quatro exemplos de extensão GNU, ausentes ou com sintaxe diferente em implementações BSD dos mesmos comandos, estão na tabela abaixo.

| Comando | Extensão GNU |
| --- | --- |
| `ls` | `--color=auto` para saída colorida |
| `cp` | `--reflink=auto` para cópia copy-on-write |
| `date` | `-d "yesterday"` para aritmética de data em linguagem natural |
| `stat` | `--format` para formatação customizada de saída |

## BusyBox: um binário só, dezenas de comandos

BusyBox resolve um problema diferente do GNU Coreutils: em vez de dezenas de binários separados, cada um relativamente pequeno mas ainda assim somando megabytes de espaço em disco, ele compila um único executável que implementa versões simplificadas de centenas de comandos unix comuns, não só coreutils mas também utilitários de rede, init e um shell ash compatível com POSIX.

Links simbólicos com o nome de cada comando apontam para esse binário único, que detecta por qual nome foi chamado e se comporta de acordo, produzindo uma pegada de disco drasticamente menor.

É o motivo pelo qual BusyBox é a base de imagens de container minimalistas: o Alpine Linux, uma das distribuições de imagem base mais usadas justamente pelo tamanho reduzido, usa BusyBox para boa parte de seu userland, com musl libc no lugar da glibc tradicional.

Essa escolha tem um custo direto. O ash do BusyBox é um shell compatível com POSIX sh, sem as extensões do Bash, então uma imagem Alpine sem Bash instalado explicitamente quebra qualquer script que dependa de bashisms, mesmo que o script declare `#!/bin/bash` como shebang, porque o binário bash simplesmente não existe nessa imagem por padrão; [shells e scripts](shells-e-scripts.md) cobre esses bashisms em detalhe.

Da mesma forma, os comandos coreutils do BusyBox implementam um subconjunto das flags do GNU Coreutils equivalente, suficiente para a maioria dos usos comuns mas não a superfície completa, e um script que usa uma flag GNU específica pode falhar silenciosamente ou com erro de flag desconhecida ao rodar sobre ele.

## uutils/coreutils: a reimplementação em Rust

O projeto uutils/coreutils reimplementa o conjunto completo do GNU Coreutils em Rust, com o objetivo declarado de ser um substituto multiplataforma para Linux, macOS, Windows e outros sistemas unix-like, compatível linha de comando por linha de comando com o original, aproveitando as garantias de segurança de memória da linguagem.

O projeto já implementa a maior parte dos utilitários do GNU Coreutils com compatibilidade considerada madura para uso geral, e passou a ser adotado experimentalmente em algumas distribuições como alternativa avaliável ao pacote GNU tradicional. Vale conferir o repositório oficial do projeto para o estado atual de compatibilidade antes de depender dele em produção, porque a cobertura de flags específicas ainda pode variar por utilitário.

## Diferenças práticas de flags que quebram scripts

Além de sed, awk e ps, já cobertos em [shells e scripts](shells-e-scripts.md), alguns coreutils comuns também divergem de forma que quebra scripts supostamente portáveis.

| Comando/flag | GNU (Linux) | BSD (incluindo macOS) |
| --- | --- | --- |
| `date -d "1 day ago"` | Suportado, aritmética de data em linguagem natural | Não existe; usa `-v-1d` para o mesmo efeito |
| `readlink -f arquivo` | Resolve o caminho absoluto, seguindo links recursivamente | Não suportado em todas as variantes; `realpath` é mais portável |
| `cp -r` vs. `cp -R` | Ambas aceitas como equivalentes | Historicamente só `-R` era garantida em implementações mais antigas |
| `stat --format='%s'` | Sintaxe `--format` ou `-c` | Usa `-f` com uma string de formato diferente, como `%z` para tamanho |

O padrão que se repete nessa tabela, e na de sed, awk e ps de [shells e scripts](shells-e-scripts.md), é sempre o mesmo: uma flag GNU que parece universal porque sempre funcionou na máquina de quem escreveu o script, e que só se revela não portável quando o script roda pela primeira vez fora de um ambiente Linux com GNU Coreutils.

Testar um script dentro de uma imagem Alpine, baseada em BusyBox, é uma forma rápida de descobrir esse tipo de dependência oculta antes de descobrir em produção, mesmo quando o alvo final de execução não é, de fato, um sistema BSD.

## Man pages e suas oito seções

As páginas de manual, acessadas com `man comando`, são organizadas em seções numeradas, e o mesmo nome pode existir em mais de uma seção com significados completamente diferentes. Pedir por "printf" normalmente mostra a página do utilitário de shell, na seção 1, não a função da linguagem C de mesmo nome, na seção 3, a menos que a seção seja pedida explicitamente com o número antes do nome.

| Seção | Conteúdo |
| --- | --- |
| 1 | Comandos executáveis (programas de usuário) |
| 2 | Chamadas de sistema (system calls do kernel) |
| 3 | Funções de biblioteca (ex.: funções da libc) |
| 4 | Arquivos especiais (normalmente em `/dev`) |
| 5 | Formatos de arquivo e convenções (ex.: `/etc/passwd`) |
| 6 | Jogos |
| 7 | Miscelânea (convenções, protocolos, pacotes) |
| 8 | Comandos de administração do sistema (tipicamente root) |

O comando `man -k palavra-chave`, equivalente a `apropos palavra-chave`, busca por uma palavra-chave nas descrições curtas de todas as páginas de manual instaladas, útil quando o nome exato do comando não é conhecido, só o que ele deveria fazer.

## `info` e `help`: as outras duas fontes de documentação

`info comando` abre a documentação no formato Info do projeto GNU, um sistema de hipertexto navegável por teclado, com nós ligados por referências cruzadas, historicamente usado pelo GNU como alternativa mais estruturada às man pages para documentação extensa, como a do próprio Bash ou do GCC. Nem todo comando tem uma página Info; quando existe, ela costuma ser mais completa que a página man equivalente, especialmente para utilitários GNU com muitas opções.

`help comando`, um builtin do próprio Bash e não um programa externo, mostra a documentação de um builtin do shell, algo que o man normalmente não cobre em detalhe porque builtins não são binários separados no sistema de arquivos.

Comandos como cd, export, alias e type são exemplos de builtins: existem dentro do processo do shell, não como um arquivo executável independente, e por isso pedir a página de manual de um deles costuma devolver a página genérica do Bash ou nada relevante, enquanto pedir a ajuda do builtin mostra exatamente a documentação dele.

## `type`, `command -v` e `which`: descobrindo o que um nome realmente é

Os três comandos parecem responder à mesma pergunta, o que é um nome de comando de fato, mas têm confiabilidade diferente. `type nome` é a resposta mais completa: um builtin do shell que informa se o nome é um builtin, uma função definida no shell atual, um alias, ou um binário externo, e nesse último caso qual caminho exato a variável `PATH` resolveria.

É a ferramenta certa quando a dúvida é por que um comando está se comportando diferente do esperado, resposta comum sendo a existência de um alias ou uma função com o mesmo nome, sombreando o binário.

`command -v nome` é a versão POSIX-padrão da mesma pergunta, com saída mais enxuta, só o caminho ou o nome sem explicação, e por isso é a escolha certa dentro de um script: sendo builtin, funciona de forma consistente entre shells POSIX, e seu código de saída, zero se encontrado e diferente de zero se não, é o que um script realmente precisa checar.

`which nome` é um binário externo separado, não um builtin, e por isso o menos confiável dos três: consulta a variável PATH de um jeito que pode não refletir exatamente o que o shell atual resolveria, não sabe nada sobre aliases ou funções definidas na sessão corrente, a fonte mais comum de which dizer uma coisa enquanto rodar o comando faz outra, e seu comportamento varia entre implementações de sistema para sistema, incluindo se ele existe por padrão.

## Builtins vs. binários: por que a distinção importa

Um builtin roda dentro do próprio processo do shell, sem o custo de criar um novo processo via fork e exec; um binário é um arquivo executável separado no sistema de arquivos, localizado via `PATH`.

A diferença não é só de performance: um builtin pode alterar o estado do próprio shell que o chamou, como cd mudando o diretório de trabalho do shell atual, algo que um programa externo chamado cd não conseguiria fazer, porque um processo filho não pode alterar o estado do processo pai que o criou.

É por isso que cd precisa ser builtin por necessidade técnica, não por escolha de design, e por que consultar seu tipo sempre reporta builtin, nunca um caminho de arquivo.

## Continue por aqui

[Shells e scripts](shells-e-scripts.md) cobre a base de POSIX sh, os bashisms mais comuns e as diferenças GNU versus BSD de sed, awk e ps que complementam as flags de coreutils desta página. [Famílias unix-like e o padrão POSIX](unix-familias-e-padroes.md) explica por que essas divergências entre GNU e BSD existem em primeiro lugar, e onde o padrão POSIX traça a linha entre o que é garantido e o que é extensão de cada sistema. Para o índice geral desta seção, veja [Aprender](index.md).
