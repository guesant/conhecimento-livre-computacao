# Linters de qualidade de artefato

shellcheck e ansible-lint, já cobertos em [Shells e scripts](shells-e-scripts.md) e em [Ansible](ansible.md), verificam a promessa de um script ou de um playbook contra o que ele de fato faz.

O mesmo princípio, verificar um artefato estaticamente contra um conjunto de regras conhecidas, sem executar nada, se estende a outros tipos de arquivo que um repositório de infraestrutura acumula: um `Dockerfile`, um documento YAML, uma página Markdown, o texto em si, e até o código duplicado entre arquivos diferentes. Cada um desses linters cobre um artefato diferente, e nenhum cobre o que os outros cobrem.

## hadolint: más práticas conhecidas de Dockerfile

Um `Dockerfile` sintaticamente válido ainda pode conter más práticas bem documentadas:

rodar `apt-get upgrade` sem fixar versão (o que torna o build não reprodutível, uma imagem construída hoje pode ser diferente de uma construída amanhã com o mesmo Dockerfile), não limpar o cache do gerenciador de pacotes na mesma camada em que ele foi usado (o que infla o tamanho final da imagem, porque uma camada já commitada não encolhe removendo um arquivo numa camada posterior), ou copiar um diretório inteiro sem `.dockerignore` correspondente.

`hadolint` verifica um Dockerfile contra uma lista extensa dessas más práticas conhecidas, cada regra com um código próprio (no estilo `DL3008`) documentado o suficiente para explicar por que aquele padrão é considerado um problema, não apenas que é um problema.

## yamllint e markdownlint: sintaxe e estilo, não conteúdo

YAML aceita mais de uma forma de representar a mesma estrutura (aspas opcionais em certas strings, indentação com quantidades diferentes de espaço, listas em bloco ou em linha), e um arquivo tecnicamente válido ainda pode ter inconsistências que dificultam revisão num diff, como indentação alternando entre dois e quatro espaços no mesmo arquivo.

`yamllint` verifica esse tipo de consistência de estilo, além de alguns erros sintáticos genuínos (uma chave duplicada no mesmo nível, por exemplo, que o parser YAML de muitas linguagens aceita silenciosamente usando só o último valor, sem avisar da duplicata).

`markdownlint` cumpre o mesmo papel para Markdown: cabeçalhos que pulam um nível, listas com marcador inconsistente, linha em branco ausente ao redor de um bloco de código, problemas que não impedem a renderização mas tornam o arquivo-fonte mais difícil de manter ao longo do tempo.

## cspell: ortografia como gate de qualidade

Um erro de ortografia num texto técnico não quebra nada tecnicamente, mas corrói a confiança de quem lê: um documento com erros de digitação recorrentes sugere que ninguém o revisou com cuidado, o que faz o leitor questionar também a precisão técnica do conteúdo, mesmo sem relação real entre as duas coisas.

`cspell` verifica ortografia contra um dicionário, mas o desafio real de aplicar isso a texto técnico não é a ortografia comum, é a quantidade de termos técnicos, nomes próprios e siglas que um dicionário genérico não conhece; por isso uma configuração de `cspell` sobre um repositório técnico depende de um dicionário customizado próprio, expandido continuamente conforme termos novos e legítimos aparecem, sob risco de o gate travar em falsos positivos constantes sem esse ajuste contínuo.

## jscpd: duplicação de código entre arquivos

Código duplicado (o mesmo bloco lógico copiado e colado em mais de um lugar, em vez de extraído para uma função ou módulo compartilhado) não é um erro sintático nem uma vulnerabilidade, mas é uma fonte silenciosa de inconsistência: corrigir um bug numa das cópias e esquecer a outra deixa o sistema com dois comportamentos divergentes para o que deveria ser a mesma lógica.

`jscpd` detecta esse tipo de duplicação comparando blocos de código entre arquivos, mesmo quando não são idênticos byte a byte (variação de nome de variável, por exemplo), reportando trechos que ultrapassam um limiar configurável de similaridade e tamanho, pequeno demais para gerar ruído em coincidências triviais, grande o suficiente para não deixar passar duplicação real.

## ast-grep: busca e lint por estrutura, não por texto

Uma busca de texto comum (`grep`) encontra uma string ou um padrão de caracteres, sem entender nada sobre a estrutura do código onde ela aparece; procurar por uma chamada de função específica com grep também encontra a mesma sequência de caracteres dentro de um comentário ou de uma string literal, sem diferenciar os dois casos.

`ast-grep` busca contra a árvore sintática abstrata (AST) do código, a mesma representação estrutural que um compilador ou interpretador constrói antes de processar o programa, o que permite expressar um padrão como "uma chamada desta função com este primeiro argumento", entendendo que aquilo é uma chamada de função de verdade, não apenas texto parecido.

Isso o torna adequado tanto para busca precisa (encontrar todos os usos reais de um padrão, sem falso positivo de comentário ou string) quanto para lint customizado (proibir um padrão específico de uso que as ferramentas de lint genéricas de uma linguagem não cobrem, por ser uma regra própria do projeto).

## Continue por aqui

[Shells e scripts](shells-e-scripts.md) e [Ansible](ansible.md) cobrem `shellcheck` e `ansible-lint`, os dois linters de artefato mais específicos deste repositório. [Segurança de aplicações](seguranca/appsec/index.md) cobre a categoria de análise voltada a segurança, um objetivo diferente do de qualidade e consistência que os linters desta página perseguem.
