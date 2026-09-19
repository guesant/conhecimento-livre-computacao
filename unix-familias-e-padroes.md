# Famílias unix-like e o padrão POSIX

"Linux" nomeia só o kernel; a distribuição em volta dele, com userland, gerenciador de pacotes e sistema de inicialização, vem de um projeto separado, e é fácil nunca notar essa costura porque ela é familiar demais. Um sistema BSD inverte essa relação por design: kernel e userland são desenvolvidos, versionados e lançados juntos, pelo mesmo projeto, como uma unidade coesa chamada base system.

Essa diferença estrutural é o que separa "um BSD" de "uma distribuição Linux" antes mesmo de falar de qualquer projeto individual, e o que amarra os dois mundos apesar dessa diferença é o padrão POSIX, coberto primeiro nesta página porque as duas famílias só interoperam por causa dele.

## O que o POSIX garante

POSIX não é um produto, uma distribuição ou um shell específico. É uma especificação escrita, formalmente ISO/IEC/IEEE 9945, mantida pelo Open Group como parte da Single UNIX Specification, que define um conjunto mínimo de comportamento que qualquer sistema "compatível" precisa implementar.

O objetivo declarado da especificação é que software escrito contra ela rode sem modificação em qualquer sistema que a implemente, o que é exatamente o problema que aparece na prática toda vez que um script escrito num servidor Linux precisa rodar também num sistema BSD.

A especificação cobre três áreas centrais: a linguagem de comandos do shell, um conjunto de utilitários de linha de comando e as APIs de sistema em C, resumidas na tabela abaixo.

| Área POSIX | Exemplos |
| --- | --- |
| Shell Command Language | `sh` |
| Utilitários de linha de comando | `grep`, `sed`, `awk`, `ls`, `cp` |
| APIs de sistema em C | `open()`, `read()`, `write()`, `fork()`, `exec()` |

A primeira área é o Shell Command Language, a sintaxe mínima que um interpretador de comandos garante, sem as extensões de shells como o Bash ou o Zsh; [shells e scripts](shells-e-scripts.md) aprofunda essa base e o que cada shell adiciona por cima dela.

A segunda área é o conjunto de utilitários de linha de comando listado acima, com comportamento e flags mínimas garantidas; [coreutils e documentação](coreutils-e-documentacao.md) detalha onde essas implementações divergem além desse mínimo.

A terceira área são as APIs de sistema em C listadas acima, que permitem que um programa nativo compile e rode sobre qualquer sistema compatível sem alterar a lógica de acesso ao sistema operacional.

Em nenhuma dessas três áreas o POSIX escolhe um lado das divergências reais entre implementações. Ele define o subconjunto de comportamento que todas são obrigadas a implementar igual, e deixa extensões, como a flag `--color` do GNU ou `date -v` do BSD, como decisão própria de cada implementação, fora do escopo do padrão.

É por isso que dois sistemas POSIX-compliant, como um Debian e um FreeBSD, ainda podem divergir enormemente em como se instala software ou como o sistema inicia, mesmo compartilhando o mesmo comportamento mínimo de shell e utilitários: gerenciamento de pacotes, formato de inicialização de sistema, interface gráfica e virtualização nunca estiveram no escopo da especificação.

A frase "compatível com POSIX", encontrada na documentação de ferramentas reais, quase nunca significa uma certificação formal; essa certificação existe, mas é rara e cara, usada sobretudo por fornecedores de sistemas operacionais comerciais como garantia contratual. Na prática, a afirmação costuma significar uma de duas coisas.

Ou a ferramenta implementa fielmente o subconjunto que o POSIX exige, o caso de um `sh` estrito como o Dash, ou a ferramenta é um superconjunto que aceita entrada POSIX válida além de suas próprias extensões, o caso do Bash e do Zsh, que rodam a maioria dos scripts POSIX sem modificação mas também aceitam sintaxe que o padrão não exige.

Um script escrito contra essa segunda categoria de ferramenta pode usar uma extensão não POSIX sem perceber e ainda assim rodar sem erro ali, o que cria uma falsa sensação de portabilidade que só quebra quando o mesmo script roda contra uma implementação da primeira categoria.

## A família BSD: base system integrado

Num sistema BSD, o kernel, o compilador, os utilitários equivalentes aos coreutils e boa parte da documentação são desenvolvidos dentro do mesmo repositório de código-fonte e lançados sob o mesmo número de versão.

Isso significa que atualizar um sistema BSD para uma nova versão principal atualiza kernel e userland em lockstep, testados juntos pelo mesmo projeto, uma garantia de coesão que uma distribuição Linux não tem da mesma forma, porque o kernel Linux e o userland GNU, ou musl e BusyBox nas variantes mais minimalistas, são versionados por projetos completamente separados. A distribuição é quem assume a responsabilidade de integrar essas peças de forma coerente, o que a seção seguinte desta página detalha.

FreeBSD é o BSD com a base de usuários mais ampla e o foco mais generalista da família, priorizando desempenho de rede e I/O e mantendo um sistema de ports e pacotes maduro. OpenBSD trata segurança e correção de código como o critério central de qualquer decisão de design, não como uma camada adicionada depois, com uma prática contínua de auditoria de código-fonte que prioriza simplicidade e clareza de implementação mesmo ao custo de performance.

Esse foco produziu dois projetos hoje usados muito além do próprio OpenBSD, o OpenSSH, cliente e servidor SSH de fato universal em sistemas unix-like incluindo a maioria das distribuições Linux, e o PF, o firewall stateful do OpenBSD adotado também por outros BSDs.

NetBSD prioriza rodar em tantas arquiteturas de hardware quanto possível, da plataforma de servidor comum a hardware embarcado e a máquinas obsoletas que nenhum outro sistema operacional moderno ainda suporta, uma amplitude de suporte que molda decisões de arquitetura interna do próprio projeto.

DragonFly BSD nasceu em 2003 como um fork do FreeBSD 4.x, criado por Matthew Dillon depois de uma divergência técnica sobre a direção da arquitetura de multiprocessamento simétrico que o FreeBSD estava adotando na época; o projeto é hoje mais conhecido pelo HAMMER, e seu sucessor HAMMER2, um sistema de arquivos com suporte nativo a snapshots projetado para armazenamento multi-terabyte.

Um sistema BSD costuma instalar software por dois caminhos complementares. O ports tree, encontrado com variações próprias em FreeBSD, OpenBSD e NetBSD, é uma coleção de Makefiles e metadados que descrevem como baixar o código-fonte de um programa, aplicar patches específicos do sistema, compilar e instalar, um modelo historicamente mais próximo de compilar a partir do código-fonte do que de baixar um binário pronto.

O pkg, o gerenciador de pacotes binários do FreeBSD, com equivalentes próprios em outros BSDs, resolve o caso comum de instalar software sem precisar compilar localmente, distribuindo pacotes binários pré-compilados a partir da mesma árvore de ports, de forma conceitualmente parecida a `apt` ou `dnf` no mundo Linux.

A licença de um projeto BSD, geralmente uma variante da licença BSD de duas ou três cláusulas, também separa essa família do mundo Linux de um jeito com consequências práticas, não só filosóficas. A licença BSD é permissiva, permite que qualquer pessoa ou empresa pegue o código, modifique e distribua uma versão derivada, incluindo uma versão proprietária de código fechado, sem obrigação de publicar as modificações.

A GPL, sob a qual a maior parte do userland GNU e o próprio kernel Linux são licenciados, é copyleft: qualquer trabalho derivado distribuído precisa ser disponibilizado sob a mesma licença, com o código-fonte correspondente acessível.

É por isso que o núcleo Darwin do macOS, derivado de código BSD, e o sistema operacional dos consoles PlayStation da Sony, também derivado de FreeBSD, puderam virar produtos proprietários fechados por cima de uma base aberta, um uso que a licença BSD permite e que a GPL não permitiria da mesma forma.

## As famílias de distribuições Linux

Uma distribuição Linux é o oposto do modelo BSD: o kernel Linux é um projeto, o userland, GNU na maioria dos casos ou musl e BusyBox nas variantes minimalistas, é outro, e uma distro é o trabalho de integrar essas peças de origens distintas, junto com um sistema de empacotamento próprio, numa combinação coerente o suficiente para ser instalada e usada como um sistema único.

Nenhuma dessas três peças, sozinha, é "Linux" no sentido popular do termo: o kernel sem userland não tem nem um shell para o usuário interagir, o userland sem um kernel não tem onde rodar, e o empacotamento é a peça que decide como o sistema recebe atualizações, resolve dependências entre pacotes e se mantém consistente ao longo do tempo.

É essa terceira peça, mais do que a escolha de kernel ou userland, praticamente idênticos entre a maioria das distros mainstream, que mais diferencia uma família de distribuições de outra no dia a dia de quem opera o sistema.

Debian e Ubuntu priorizam estabilidade e um ciclo de lançamento previsível sobre pacotes com a versão mais recente possível. O Debian estável, em particular, mantém versões de pacotes congeladas, com backport de correções de segurança mas não de features novas, durante todo o ciclo de suporte, uma escolha deliberada que prioriza previsibilidade em produção sobre acesso imediato à última versão de qualquer software.

Ubuntu é construído sobre a base do Debian, com um ciclo de lançamento próprio e suporte comercial da Canonical; `apt` é o gerenciador de pacotes de ambos, operando sobre pacotes `.deb`.

Fedora e RHEL seguem uma relação parecida, com prioridades diferentes: Fedora é o ponto de desenvolvimento mais próximo do estado da arte, com ciclos de lançamento mais curtos e adoção mais rápida de versões novas de kernel e software, enquanto o RHEL, Red Hat Enterprise Linux, é a distribuição comercial construída a partir do trabalho consolidado no Fedora, com suporte de longo prazo, certificações e um modelo de negócio voltado a contratos empresariais.

`dnf`, sucessor do yum, é o gerenciador de pacotes de ambos, operando sobre pacotes `.rpm`.

Arch Linux prioriza um modelo rolling release, atualizações contínuas sem versões numeradas discretas, e minimalismo deliberado: uma instalação Arch começa praticamente vazia, e quem a instala configura exatamente o que precisa, em vez de partir de um conjunto de pacotes pré-selecionados pela distro.

Essa filosofia atrai um público que quer controle granular sobre cada componente do sistema, ao custo de exigir mais conhecimento prévio do que uma instalação Debian ou Ubuntu guiada; `pacman` é o gerenciador de pacotes, com a AUR, Arch User Repository, como repositório adicional mantido pela comunidade.

Alpine Linux prioriza tamanho reduzido acima de tudo, usando musl libc no lugar da glibc tradicional, BusyBox no lugar do GNU Coreutils completo, e `apk` como gerenciador de pacotes, também minimalista; [coreutils e documentação](coreutils-e-documentacao.md) detalha o que essa troca custa em compatibilidade de flags.

Essa combinação produz uma imagem base ordens de grandeza menor que uma distro Debian ou Ubuntu completa, o motivo de sua adoção generalizada em imagens de container voltadas a produção, ao custo de scripts que assumem Bash ou flags GNU específicas poderem quebrar sobre ela sem aviso claro.

## O fio que conecta as duas famílias

POSIX é, na prática, o contrato que torna um script portável entre Linux e BSD possível em primeiro lugar: sem uma especificação comum, não haveria garantia nenhuma de que `grep`, `sed` ou o próprio shell se comportariam de forma parecida o suficiente entre os dois mundos.

Mas o padrão garante o denominador comum, não a experiência completa de nenhum dos dois lados; tanto Linux, via GNU, quanto os BSDs adicionam extensões próprias por cima da base POSIX, e é justamente nessas extensões, fora do que o padrão exige, que scripts supostamente portáveis mais frequentemente quebram. Escrever um script verdadeiramente portável entre Linux e BSD significa, na prática, restringir deliberadamente o uso a exatamente o que POSIX garante, o assunto que [shells e scripts](shells-e-scripts.md) cobre em detalhe.

## Continue por aqui

[Shells e scripts](shells-e-scripts.md) aprofunda a base POSIX sh que esta página apresentou, o que Bash, Zsh e Fish adicionam por cima dela, e as pegadinhas reais de escrever um script portável entre Linux e BSD. [Coreutils e documentação](coreutils-e-documentacao.md) detalha onde GNU Coreutils, BusyBox e a reimplementação em Rust uutils divergem além do mínimo que o POSIX exige, e como encontrar ajuda sobre qualquer um desses comandos. Para o índice geral desta seção, veja [Aprender](index.md).
