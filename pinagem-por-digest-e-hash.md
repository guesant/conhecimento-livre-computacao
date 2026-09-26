# Pinagem por digest e hash em cada ecossistema

[Tags e digests de imagens](containers/tag.md) e [digest de imagem](containers/digest.md) estabelecem o conceito central: uma tag é um ponteiro que pode ser reapontado para um conteúdo diferente sem aviso, um digest é o hash do conteúdo em si, então fixá-lo garante que o que chega hoje é byte a byte igual ao que foi avaliado e aprovado, não uma versão futura republicada sob o mesmo nome.

Esse mesmo problema, e a mesma solução de fundo, se repete em praticamente todo ecossistema que distribui pacote ou dependência, cada um com sua própria sintaxe e seu próprio nome para o mecanismo, mas resolvendo exatamente a mesma pergunta: o que exatamente estou baixando, e como sei que da próxima vez será a mesma coisa?

## Imagens de container: tag e digest juntos

Como já descrito em [digest de imagem](containers/digest.md), uma imagem referenciada como `imagem:tag@sha256:...` combina os dois: a tag continua legível para um humano relacionar a imagem às notas de release, mas o runtime resolve o digest para decidir de fato o conteúdo puxado, tornando irrelevante se a tag foi ou não reapontada depois.

Fixar só a tag, sem o digest, deixa o manifesto vulnerável a exatamente o cenário que motiva essa prática inteira: um registry que permite republicar uma tag (a maioria permite, por padrão) pode servir um conteúdo diferente do que existia quando alguém revisou e aprovou aquela referência, sem que o texto do manifesto precise mudar em nada.

## GitHub Actions: uma Action de terceiro é código de terceiro rodando com suas credenciais

Uma Action de terceiro referenciada por tag (`uses: alguem/acao@v3`, por exemplo) é código de terceiro que roda dentro do próprio workflow, com acesso a segredos do repositório e ao token de CI, exatamente o mesmo risco de supply chain de uma imagem de container, mas com uma superfície ainda mais sensível, porque o que está rodando não é só o conteúdo de uma imagem isolada, é código com acesso direto ao contexto de execução do workflow.

Uma tag de versão num repositório git, ao contrário de um digest de imagem, pode ser movida a qualquer momento por quem controla o repositório, que consegue apontar a tag `v3` para um commit diferente sem aviso, o que faz fixar por tag oferecer garantia zero contra esse cenário específico.

A prática recomendada, e a que [zizmor](seguranca/supply-chain/index.md) cobre como um dos padrões que uma ferramenta de lint de workflow sinaliza quando ausente, é fixar pelo hash do commit (`uses: alguem/acao@a1b2c3...`, um valor imutável por construção, já que o hash de um commit muda se qualquer coisa nele mudar), mantendo a versão legível como comentário ao lado (`@a1b2c3... # v3.2.1`) só para referência humana, sem que essa parte legível tenha efeito nenhum na resolução real.

Um bot de atualização de dependência que entende esse padrão, como o Renovate já descrito em [Renovate: atualização automática de dependência](renovate-atualizacao-automatica-de-dependencia.md), mantém tanto o comentário de versão quanto o hash do commit em sincronia a cada atualização, sem exigir que alguém calcule o hash manualmente a cada bump.

## Pacotes Python: `--require-hashes` muda o modo de falha padrão

Um arquivo de dependências Python fixado por número de versão (`requests==2.31.0`, por exemplo) ainda deixa uma lacuna: nada garante que o pacote baixado do índice é byte a byte o mesmo que foi originalmente publicado sob aquele número de versão, seja por um índice espelho comprometido, seja por uma falha de integridade na distribuição.

O modo de hash-checking do `pip` (ativado com `--require-hashes`, geralmente aplicado sobre um arquivo de requisitos gerado por uma ferramenta como pip-compile, que já lista hash junto de cada pacote) muda o comportamento padrão de instalação.

Em vez de confiar em qualquer artefato com o nome e a versão certos, o `pip` recusa instalar qualquer coisa cujo hash não bata exatamente com o declarado, e recusa até mesmo instalar uma dependência transitiva sem hash declarado, fechando por completo a lacuna de "baixei algo com o nome certo, mas não necessariamente o conteúdo certo".

## npm: o lockfile já carrega o hash de integridade

O `package-lock.json` de um projeto Node não guarda só a versão exata resolvida de cada dependência (incluindo as transitivas, fixadas numa árvore completa e determinística), guarda também um campo de integridade com o hash criptográfico esperado de cada pacote; `npm install` verifica esse hash contra o que de fato baixa, e recusa a instalação se não bater, o mesmo princípio do --require-hashes do pip, aqui embutido por padrão no fluxo normal em vez de exigir uma flag adicional.

Isso é o motivo pelo qual versionar o lockfile junto com o manifesto de dependência (em vez de tratá-lo como um artefato descartável gerado a cada instalação) importa para reprodutibilidade e integridade, não só para performance de instalação: sem o lockfile, cada instalação nova resolve a árvore de dependências de novo, potencialmente pegando versões mais novas das transitivas e perdendo a garantia de hash calculada da última vez que alguém resolveu essa árvore deliberadamente.

## O padrão que se repete

Em todo ecossistema citado aqui, a mesma tensão se repete sob nomes diferentes: uma referência legível por humano (uma tag, um número de versão) é conveniente mas mutável por natureza ou por política de quem a distribui; uma referência por hash criptográfico do conteúdo é verbosa e ilegível para um humano, mas imutável por construção matemática, não por promessa de boa conduta de quem publica.

A prática madura em cada ecossistema converge para o mesmo desenho, manter os dois juntos: a referência legível para contexto humano e para uma ferramenta de atualização automática saber o que propor a seguir, o hash para a garantia real de que o conteúdo resolvido é exatamente o esperado, não apenas algo com o nome certo.

## Continue por aqui

[Imagem de container](containers/image.md) cobre o modelo do artefato. [Proveniência](seguranca/supply-chain/provenance.md) cobre a diferença entre um hash de integridade como os desta página e uma assinatura ou atestação, uma garantia mais forte sobre quem produziu o artefato, não só sobre se o conteúdo foi alterado.
