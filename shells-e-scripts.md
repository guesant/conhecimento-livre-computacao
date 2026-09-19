# Shells e portabilidade de scripts

Um shell é, ao mesmo tempo, duas coisas que a maioria de quem usa um terminal trata como uma só: um interpretador de linha de comando, que lê o que uma pessoa digita e executa, e uma linguagem de programação completa, usada para escrever scripts que rodam sem ninguém digitando nada.

Bash, Zsh e Fish são todos shells nesse sentido duplo, e a confusão mais comum é assumir que um shell bom para o primeiro uso, o interativo, é automaticamente uma boa escolha para o segundo, o scripting, quando as duas necessidades puxam para direções diferentes.

Esta página cobre primeiro o que um shell realmente é e onde POSIX entra nessa história, [famílias unix-like e o padrão POSIX](unix-familias-e-padroes.md) explica a especificação em si, e depois os problemas concretos de escrever um script que precisa rodar fora da máquina onde foi escrito.

## Três modos de invocação, não um

Um mesmo binário de shell se comporta de forma diferente dependendo de como foi invocado, e essa diferença decide quais arquivos de configuração ele lê antes de executar qualquer coisa. Um shell de login é o que inicia uma sessão nova, tipicamente ao conectar via SSH ou abrir um console; ele lê arquivos de perfil, listados na tabela abaixo, desenhados para configurar o ambiente uma vez por sessão, incluindo variáveis de ambiente e a variável `PATH`.

Um shell interativo é qualquer shell que espera entrada de uma pessoa e mostra um prompt, seja ele também um shell de login ou não; ele lê arquivos voltados a conforto de uso, como aliases, cores e autocomplete, tipicamente `~/.bashrc`.

| Tipo de shell | Arquivos de perfil lidos |
| --- | --- |
| Login | `/etc/profile`, `~/.profile`, `~/.bash_profile` |

Um shell não interativo é o que executa um script sem esperar entrada nenhuma. Por padrão, ele não lê nem o arquivo de perfil nem o de configuração interativa, exatamente para evitar que a saída de um alias ou de uma mensagem de boas-vindas interativa contamine a saída de um script que outro programa está processando.

Essa distinção explica um sintoma comum e confuso: uma variável de ambiente ou um alias que funciona perfeitamente quando digitado no terminal desaparece quando o mesmo comando roda dentro de um script ou de uma tarefa agendada, porque o terminal interativo carregou um arquivo de configuração que o script, rodando como shell não interativo, nunca leu.

## POSIX sh como denominador comum

`sh`, nesse contexto, não é necessariamente um shell independente; na maioria dos sistemas Linux modernos, `/bin/sh` é um link simbólico para outro shell rodando em modo de compatibilidade POSIX, o Dash no caso do Debian e do Ubuntu, que desliga deliberadamente as extensões não padronizadas desse shell.

Um script que roda em sh roda, por definição, em qualquer sistema que implemente o padrão POSIX, incluindo sistemas BSD, o que faz do shebang `#!/bin/sh` a escolha certa sempre que portabilidade máxima importa mais do que conveniência de sintaxe.

Bash é um superconjunto de POSIX sh: entende tudo que o padrão exige, mais um conjunto grande de extensões próprias, como arrays, `[[ ]]` para testes condicionais e expansão de parâmetro avançada, e é o shell padrão de login na maioria das distribuições Linux voltadas a servidor.

Zsh também é um superconjunto de POSIX sh, com seu próprio conjunto de extensões, em parte sobrepostas com as do Bash e em parte distintas, como globbing mais poderoso e um sistema de completions mais sofisticado; como o Bash, um script com shebang para Zsh não é portável para um sistema que só tem Bash ou Dash instalados, porque depende de sintaxe própria do Zsh.

Fish rompe deliberadamente com a compatibilidade POSIX: sua sintaxe de scripting é diferente o suficiente que a maioria dos scripts escritos para Bash, Zsh ou sh simplesmente não roda em Fish sem reescrita, sem `if [ ]` tradicional e sem o operador de encadeamento condicional do jeito POSIX.

Essa ruptura é uma escolha deliberada do projeto, priorizando ergonomia interativa, como autocomplete e mensagens de erro claras por padrão sem plugin nenhum, sobre compatibilidade com décadas de scripts POSIX existentes.

A tabela resume os quatro nos três eixos que a seção seguinte reaproveita:

| Shell | Bom para uso interativo | Compatível com scripts sh/Bash | Portável entre sistemas POSIX |
| --- | --- | --- | --- |
| POSIX sh (ex.: Dash) | Limitado, poucos recursos de conforto | É a própria base | Máxima, por definição |
| Bash | Bom, recursos maduros | Sim, superconjunto de sh | Alta, mas não é POSIX puro |
| Zsh | Muito bom, altamente configurável | Sim, superconjunto de sh | Alta para o eixo interativo; scripts com sintaxe própria não são portáveis |
| Fish | Muito bom, ergonomia por padrão | Não, sintaxe própria e incompatível | Nenhuma para scripts |

Escolher um shell interativo, Zsh, Fish ou qualquer outro, é uma decisão pessoal de conforto que não deveria vazar para dentro de um script. Escolher a linguagem de um script é uma decisão de portabilidade, guiada por onde esse script vai rodar, independente de qual shell interativo a pessoa que o escreveu usa no dia a dia.

Misturar as duas decisões, escrevendo um script que depende do shell interativo de quem o escreveu, é o erro mais comum que essa distinção deveria prevenir.

## O shebang decide o intérprete, não é uma formalidade

A primeira linha de um script, chamada shebang, diz ao kernel exatamente qual programa deve interpretar o resto do arquivo; não é decoração, é a diferença entre o script rodar com os recursos de POSIX sh puro ou com todas as extensões do Bash disponíveis.

`#!/bin/sh` compromete o script a rodar sob qualquer shell que o sistema tenha registrado como `/bin/sh`, o que significa que nenhuma extensão do Bash pode ser usada, mesmo que o sistema onde o script foi escrito tenha Bash instalado nesse caminho.

`#!/bin/bash`, ou de forma mais portável entre distribuições `#!/usr/bin/env bash`, que procura o Bash na variável de ambiente de caminhos em vez de assumir um caminho fixo, declara a dependência real e faz o script falhar, na melhor das hipóteses com um erro de sintaxe, onde só existe um sh mínimo.

Declarar `#!/bin/sh` e depois usar sintaxe de Bash dentro do script é o erro mais comum e mais silencioso desse par de decisões: o script roda sem problema em qualquer sistema onde esse caminho aponta para Bash, um comportamento comum mas não garantido, e só quebra quando alguém tenta rodá-lo num sistema onde ele é de fato um interpretador POSIX estrito, como o Dash.

Nesse ponto o script já costuma estar em produção há tempo suficiente para que ninguém lembre que ele nunca foi testado fora do ambiente original.

## Bashisms: sintaxe que parece POSIX mas não é

Bashisms são construções de sintaxe que funcionam em Bash, e frequentemente também em Zsh, mas não existem no padrão POSIX sh, e por isso quebram silenciosamente ou com erro obscuro quando um script declarado `#!/bin/sh` roda sob o Dash ou outro sh estrito.

| Construção (bashism) | Equivalente POSIX |
| --- | --- |
| `[[ "$a" == "$b" ]]` | `[ "$a" = "$b" ]` |
| `local var=valor` dentro de função | Não existe em POSIX sh puro |
| Arrays: `arr=(a b c)`, `"${arr[@]}"` | Não existem em POSIX sh |
| `$(( a ** b ))`, `((...))` para aritmética | `$((a * a))` repetido, ou `expr` |
| `source arquivo` | `. arquivo` |
| `${VAR^^}` / `${VAR,,}` | `tr '[:lower:]' '[:upper:]'` |
| `echo -e` para interpretar `\n` | `printf` |

A diferença mais traiçoeira dessa tabela é `[[ ]]` contra `[ ]`: os dois se parecem tanto visualmente que é fácil escrever o teste duplo num script com shebang POSIX sem perceber, porque a maioria dos editores não avisa, e porque ele funciona perfeitamente enquanto alguém testa o script no próprio terminal Bash.

O shellcheck, um analisador estático de scripts shell, identifica exatamente esse tipo de bashism usado sob um shebang POSIX, além de variáveis não citadas e pipelines onde a flag `pipefail` provavelmente deveria estar; rodá-lo sobre um script é a forma prática de verificar a promessa que o shebang faz, antes que a divergência vire um bug descoberto em produção.

## `set -euo pipefail`: o que cada flag garante

`set -euo pipefail` é citado com tanta frequência como "modo seguro" que é fácil assumir que ele torna um script à prova de falha silenciosa. Cada flag cobre um caso específico, e todas juntas ainda deixam brechas reais.

A flag `-e` encerra o script no primeiro comando que retornar código de saída diferente de zero, mas não se aplica a um comando já testado por uma condição, como num if ou num comando encadeado com verificação, porque nesses contextos o código de saída é explicitamente examinado, e não se aplica sozinha ao último comando de um pipeline, o motivo pelo qual a flag de pipefail existe separadamente.

A flag `-u` trata o uso de uma variável não definida como erro fatal, em vez de expandir para uma string vazia silenciosamente.

A pegadinha é que parâmetros posicionais como `$1` e `$2` contam como não definidos quando o script recebe menos argumentos do que o esperado, então essa flag também torna acesso a um argumento ausente um erro fatal.

A flag de pipefail faz o código de saída de um pipeline inteiro refletir o primeiro comando que falhar, não só o último; sem ela, um pipeline sempre retorna o código de saída do último comando, mascarando a falha real do primeiro, e por ser uma extensão de Bash e Zsh, essa flag não existe em POSIX sh puro.

Nenhuma das três flags protege contra um comando dentro de uma substituição de comando usada como valor, sem checar depois o código de saída, nem contra funções que capturam erros internamente com seu próprio tratamento condicional.

## Diferenças GNU vs. BSD que quebram scripts supostamente portáveis

Os nomes sed, awk e ps existem tanto em sistemas Linux, normalmente nas versões GNU, quanto em sistemas [BSD](unix-familias-e-padroes.md), incluindo o macOS, que usa uma base BSD para seus utilitários, mas o mesmo nome de comando não significa as mesmas flags aceitas.

O exemplo mais citado é o `sed -i`, para edição no próprio arquivo: no GNU sed, `sed -i 's/a/b/' arquivo.txt` funciona diretamente, enquanto no BSD sed a mesma flag exige um argumento explícito para o sufixo de backup, mesmo que esse argumento seja uma string vazia.

Rodar a versão GNU num sistema BSD trata o próprio script sed como o argumento do sufixo de backup e a lista de arquivos como o script de verdade, produzindo um erro confuso em vez de um aviso claro sobre a flag incompatível.

O awk tem uma superfície de compatibilidade maior entre implementações, porque a maior parte do que scripts comuns usam é coberta pelo padrão POSIX; a divergência aparece nas extensões específicas do GNU awk, como a função `gensub()`, que simplesmente não existem no awk padrão de um sistema BSD.

O ps diverge na própria gramática de flags: o ps do GNU, no Linux, aceita tanto a sintaxe estilo BSD sem hífen (`ps aux`) quanto a sintaxe estilo UNIX System V com hífen (`ps -ef`), porque foi desenhado para aceitar as duas por compatibilidade, enquanto um ps BSD nativo só entende a sintaxe BSD original.

Um script que mistura as duas convenções assumindo que todo ps aceita a sintaxe com hífen quebra num BSD real, e a mesma lógica de superfície reduzida se estende aos comandos coreutils mais básicos, que [coreutils e documentação](coreutils-e-documentacao.md) cobre em detalhe.

## Continue por aqui

[Famílias unix-like e o padrão POSIX](unix-familias-e-padroes.md) explica o que a especificação POSIX garante e por que ela é o que torna um script portável entre Linux e BSD possível em primeiro lugar. [Coreutils e documentação](coreutils-e-documentacao.md) continua o assunto de portabilidade nos comandos básicos do dia a dia e mostra como encontrar ajuda sobre qualquer um deles. Para o índice geral desta seção, veja [Aprender](index.md).
