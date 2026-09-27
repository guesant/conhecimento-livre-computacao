# Builds reproduzíveis

Um build reproduzível é uma construção que produz o mesmo resultado verificável
quando é executada novamente com as mesmas entradas relevantes. Em muitos
projetos, isso significa obter bytes idênticos para um pacote, uma imagem, um
binário ou um arquivo gerado.

O objetivo não é apenas acelerar o pipeline. A reprodução permite que uma
segunda parte compare o artefato publicado com uma construção independente e
detecte alterações introduzidas no ambiente de build, no worker ou na etapa de
publicação.

## O que precisa ser igual

"Mesmo source" não é uma definição suficiente. O resultado também pode
depender de:

- commit, submódulos e arquivos do contexto de build;
- lockfiles e índices de dependências;
- compilador, linker, SDK e geradores de código;
- imagem base e pacotes do sistema;
- opções do build e variáveis de ambiente;
- locale, timezone, ordem de arquivos e ordem de iteração;
- timestamps, identificadores aleatórios e caminhos absolutos;
- arquitetura, sistema operacional e instruções habilitadas;
- conteúdo baixado durante a execução;
- versão e configuração do próprio sistema de build.

Um projeto precisa decidir quais dessas entradas são fixadas, quais são
registradas e quais são deliberadamente permitidas a variar. Se a arquitetura
do alvo faz parte do produto, o resultado deve ser reproduzível por arquitetura
ou a arquitetura deve aparecer explicitamente na identidade do artefato.

## Fontes comuns de não determinismo

### Tempo

Arquivos gerados, archives, metadados de pacotes e imagens podem incorporar a
hora atual. Duas execuções feitas em segundos diferentes produzem hashes
diferentes mesmo sem alteração no source.

O padrão [SOURCE_DATE_EPOCH](https://reproducible-builds.org/specs/source-date-epoch/)
fornece um timestamp determinístico, normalmente derivado da revisão ou do
pacote. As ferramentas devem consumir esse valor em vez de consultar o relógio
para dados que precisam ser estáveis. O valor não deve ser usado para fingir
que o runtime está em outra data; ele controla somente metadados do build.

### Ordem e nomes

Listagens de diretórios, iteração sobre mapas e arquivos de archives podem
variar. Ordene entradas quando o formato permitir e normalize separadores,
permissões, owner, group e caminhos. Uma ordem estável também torna diffs de
artefatos úteis para investigação.

### Ambiente

Locale, timezone, versão de libc, caminho absoluto do workspace, hostname e
variáveis herdadas podem vazar para o output. O build deve executar em um
ambiente declarado, com locale e timezone conhecidos, e evitar incorporar
hostname, diretórios temporários ou detalhes do worker.

### Dependências flutuantes

Uma dependência referenciada por uma faixa de versão, uma tag mutável ou um
índice que mudou entre execuções quebra a reprodução. Use lockfiles, checksums,
digests e repositórios versionados. Os downloads devem ser feitos a partir de
fontes confiáveis e, quando possível, sem acesso à rede depois que as entradas
foram resolvidas.

### Aleatoriedade e paralelismo

Geradores de código, IDs temporários e algoritmos que percorrem estruturas em
ordem não definida podem produzir resultados diferentes. Use seeds explícitos
quando a aleatoriedade fizer parte do processo e não use uma seed fixa como
substituto de uma fonte de entropia quando o artefato precisar de segurança.

Paralelismo também pode revelar race conditions em geradores e linkers. A
reprodução precisa ser testada com a mesma configuração de concorrência e,
quando necessário, com execuções em workers diferentes.

## Reprodutibilidade não é o mesmo que hermeticidade

Um build hermético não acessa entradas implícitas fora do conjunto declarado.
Ele restringe rede, filesystem, ambiente e ferramentas disponíveis. Isso ajuda
a garantir que todas as entradas sejam conhecidas.

Um build reproduzível exige, além disso, que essas entradas produzam o mesmo
resultado. Um processo pode ser hermético e ainda não reproduzível se incorporar
o horário atual ou uma ordem instável. Também é possível obter um artefato
reproduzível por acidente em um build que depende de estado global e, portanto,
não é seguro para verificação independente.

## Estratégia de implementação

Uma adoção gradual costuma seguir esta ordem:

1. identificar o artefato e sua identidade, incluindo plataforma e formato;
2. capturar o comando, a revisão, o lockfile e as versões das ferramentas;
3. executar duas construções em diretórios, workers e horários diferentes;
4. comparar hashes e localizar o primeiro arquivo divergente;
5. remover uma fonte de variação por vez;
6. bloquear dependências e entradas de rede não declaradas;
7. repetir em outro ambiente independente;
8. registrar o resultado na proveniência e no relatório de verificação.

Compare arquivos descompactados quando o container ou archive possuir
metadados variáveis. O hash final continua sendo a verificação de publicação,
mas o diff interno ajuda a encontrar timestamps, ordem de entradas, caminhos e
arquivos que não deveriam ter sido incluídos.

## Imagens e pacotes

Para imagens OCI, fixe a imagem base por digest, controle o contexto, normalize
os timestamps quando o exporter suportar essa opção e não use tags como prova de
identidade. A configuração de build precisa declarar argumentos que alteram a
imagem. Segredos devem ser montados apenas durante a etapa necessária e nunca
gravados em camadas ou no output.

Para pacotes, fixe a toolchain, os arquivos de origem e os metadados do formato.
Archives devem ter ordem de entradas, timestamps, owner, group e permissões
normalizados. Pacotes que compilam código nativo também precisam considerar
flags, CPU alvo, linker e recursos que podem variar entre workers.

## Verificação independente

Uma verificação forte não recompila usando exatamente o mesmo worker que
publicou o artefato. O verificador deve receber a revisão e os parâmetros
esperados, construir em um ambiente separado e comparar o resultado com o
digest publicado.

Essa comparação não prova que o source é benigno. Ela mostra que o artefato
corresponde ao processo e às entradas que outra parte conseguiu reproduzir. A
análise de vulnerabilidades, o SBOM, os testes e a revisão de código continuam
sendo controles distintos.

## Limites e decisões

Nem todo artefato é igualmente fácil de reproduzir. Toolchains bootstrap,
otimizações específicas de CPU, código que incorpora entropia, dados externos e
geradores não determinísticos podem exigir uma estratégia específica. Quando a
igualdade byte a byte for inviável, registre o motivo, defina uma comparação
mais fraca e preserve a proveniência completa.

Não esconda divergências com um novo timestamp ou removendo metadados sem
entender sua função. Metadados úteis podem ser movidos para uma declaração
externa, e arquivos gerados podem ser normalizados de modo documentado. O
critério é manter a informação necessária para operação e verificação sem fazer
o resultado depender do ambiente acidental.

## No pipeline

Um pipeline que busca builds reproduzíveis deve:

- versionar a configuração e os scripts de build;
- manter lockfiles e checksums junto do source;
- fixar imagens base, actions e ferramentas por versão ou digest;
- declarar a plataforma e a toolchain;
- controlar locale, timezone e `SOURCE_DATE_EPOCH`;
- evitar downloads não registrados durante o build;
- produzir logs e proveniência suficientes para repetir a execução;
- comparar pelo menos duas execuções em ambientes separados;
- bloquear a promoção quando o resultado divergir sem uma exceção registrada.

O [SBOM](sbom.md) deve ser gerado para o artefato efetivamente publicado. A
[proveniência](provenance.md) deve apontar para o mesmo digest e registrar os
materiais usados para obtê-lo.

## Relações

- [Proveniência](provenance.md) registra a execução e suas entradas.
- [SLSA](slsa.md) organiza requisitos de confiança para builds.
- [SBOM](sbom.md) descreve a composição do artefato.
- [Pinagem por digest e hash](../../pinagem-por-digest-e-hash.md) trata de referências imutáveis.
- [Nix](../../build/nix.md) apresenta um modelo de ambientes e derivações reproduzíveis.
- [Bazel](../../build/bazel.md) explica um sistema de build com grafo e regras explícitas.

## Fontes primárias

- [Reproducible Builds](https://reproducible-builds.org/docs/definition/)
- [Deterministic build systems](https://reproducible-builds.org/docs/deterministic-build-systems/)
- [SOURCE_DATE_EPOCH](https://reproducible-builds.org/specs/source-date-epoch/)
- [Timestamps](https://reproducible-builds.org/docs/timestamps/)
- [Debian reproducible builds](https://wiki.debian.org/ReproducibleBuilds)
- [Docker build attestations](https://docs.docker.com/build/metadata/attestations/)
