# Proveniência de artefatos

Proveniência é o registro verificável da origem e do processo que produziu um
artefato. Ela relaciona uma saída, como um pacote, uma imagem OCI ou um binário,
às entradas, ao código de build, aos parâmetros, ao ambiente e à identidade do
builder.

A pergunta central é "de onde veio este artefato e como ele foi produzido?".
Essa pergunta é diferente de "qual é o conteúdo?", respondida por um digest, e
de "quais componentes estão dentro dele?", respondida por um
[SBOM](sbom.md).

## O problema que a proveniência resolve

Um pipeline pode produzir a imagem correta a partir da revisão correta e ainda
deixar pouca evidência para quem precisa auditar o resultado. Um digest mostra
que o conteúdo observado corresponde ao conteúdo publicado, mas não revela:

- qual revisão do código foi usada;
- qual definição do workflow iniciou o build;
- quais dependências foram resolvidas;
- quais parâmetros externos foram fornecidos;
- qual builder executou os passos;
- se o artefato foi produzido por um ambiente autorizado.

Proveniência transforma essas informações em uma declaração que pode ser
armazenada junto do artefato, assinada e validada por uma política. Ela reduz o
espaço de investigação em incidentes e permite rejeitar um artefato que tenha
um conteúdo aparentemente válido, mas uma origem ou um processo incompatível
com o esperado.

## O que uma declaração costuma conter

O formato depende do ecossistema. Um modelo de proveniência de build precisa,
no mínimo, representar a relação entre os seguintes elementos:

| Elemento | Pergunta respondida |
| --- | --- |
| Artefato sujeito | Qual digest ou identificador foi produzido? |
| Fonte | Qual repositório, revisão ou conjunto de fontes entrou no build? |
| Definição do build | Qual workflow, recipe, Dockerfile ou configuração definiu a execução? |
| Dependências resolvidas | Quais materiais externos foram usados e com quais identificadores? |
| Parâmetros externos | Quais valores foram fornecidos por quem iniciou a execução? |
| Builder | Qual serviço, workflow ou identidade executou a construção? |
| Parâmetros do sistema | Em qual plataforma, ambiente ou worker o build ocorreu? |
| Execução | Qual foi a invocação e quando ela começou e terminou? |

Os campos devem ser verificáveis. Uma string dizendo "built by CI" é uma
descrição, não uma identidade forte. Uma referência a uma branch sem o commit
correspondente também é insuficiente, porque a branch pode avançar depois da
execução.

## Proveniência e reprodutibilidade

Proveniência registra uma execução. Um build reproduzível permite executar
novamente o processo com as mesmas entradas e obter o mesmo resultado. As duas
propriedades se complementam, mas não são equivalentes.

Uma proveniência pode registrar corretamente que um builder executou um
workflow, mesmo que duas execuções produzam bytes diferentes por causa de
timestamps, ordem de arquivos ou dependências flutuantes. Da mesma forma, um
artefato pode ser reproduzível sem carregar uma declaração assinada que informe
quem o produziu.

[Builds reproduzíveis](reproducible-builds.md) explica as fontes de
nondeterminismo e as técnicas para eliminá-las. O processo de verificação mais
forte combina:

1. digest do artefato;
2. proveniência assinada;
3. política que verifica fonte, builder, parâmetros e materiais;
4. reconstrução independente quando a reprodução for exigida;
5. comparação dos resultados reconstruídos.

## SLSA e in-toto

[SLSA](slsa.md) define requisitos e um modelo de confiança para builds. A
proveniência recomendada por SLSA descreve uma definição de build, as
dependências resolvidas e os detalhes da execução. A versão adotada precisa
ser identificada no campo de tipo do predicate, porque o significado dos
campos é parte do contrato que o verificador interpreta.

[in-toto](https://in-toto.io/) fornece um modelo geral para afirmar etapas e
materiais de uma cadeia de software. Proveniência de build é um caso de uso
importante, mas a cadeia pode também registrar revisão, teste, assinatura,
publicação e promoção. Uma atestação in-toto transporta a declaração; ela não
define sozinha quais valores devem ser aceitos pela organização.

Formatos como [DSSE](https://github.com/secure-systems-lab/dsse) protegem uma
mensagem estruturada com uma assinatura e um tipo de payload. A assinatura
ajuda a detectar alteração e vincular a declaração a uma identidade, mas a
política ainda precisa verificar se aquela identidade é autorizada para aquele
repositório, builder ou ambiente.

## Verificação

Verificar proveniência não significa apenas decodificar um JSON. Uma verificação
útil valida a cadeia completa:

1. localizar o artefato pelo digest, não por uma tag mutável;
2. localizar a atestação correspondente;
3. validar a assinatura e a cadeia de confiança da identidade emissora;
4. verificar o tipo e a versão do predicate;
5. comparar o repositório, a revisão, o workflow e o builder com a política;
6. validar os materiais e parâmetros esperados;
7. decidir se o artefato pode ser publicado, promovido ou executado.

Uma regra de promoção pode aceitar somente um digest cuja proveniência venha
de um workflow específico, em uma branch protegida, usando um builder
gerenciado e sem parâmetros proibidos. O Kargo, o Argo CD ou o runtime não
devem inferir essa confiança apenas do nome da imagem.

## Imagens OCI

Para uma imagem, a declaração deve se referir ao digest do manifesto ou do
índice que será promovido. A tag é um alias conveniente, mas pode ser movida
para outro digest. O digest da imagem deve ser ligado à proveniência por uma
referência explícita e não apenas por uma convenção de nomenclatura.

O build de uma imagem também tem entradas que não aparecem necessariamente no
Dockerfile: contexto de build, arquivos copiados, imagem base, argumentos,
segredos usados em etapas, dependências baixadas e opções do BuildKit. Se uma
entrada pode alterar a saída, ela deve ser fixada ou representada na
proveniência.

Proveniência não substitui o [SBOM](sbom.md). O SBOM descreve os componentes
observados na imagem final; a proveniência descreve como aquela imagem foi
produzida. Para investigar uma vulnerabilidade, as duas evidências devem ser
consultadas juntas.

## Limitações

Proveniência não prova que o código é seguro, que o builder não foi
comprometido ou que uma dependência não contém vulnerabilidades. Ela também
não transforma automaticamente um build em reproduzível. A confiança depende
de uma cadeia de identidade, de um builder protegido, de entradas completas e
de uma política que não aceite declarações vagas.

Uma proveniência incompleta pode ser pior do que parece: ela pode dar a
impressão de rastreabilidade enquanto omite justamente o parâmetro que mudou o
resultado. Por isso, o projeto deve documentar quais campos são obrigatórios,
quais são opcionais e como uma ausência é tratada.

## Aplicação prática

Para cada artefato publicado, mantenha pelo menos:

- digest imutável do artefato;
- revisão exata do source;
- definição versionada do build;
- lista ou referência aos materiais resolvidos;
- identidade do builder;
- atestação assinada e verificável;
- política de promoção;
- vínculo com SBOM, testes e scans executados.

No caso de uma falha, essa coleção deve permitir responder qual revisão produziu
o artefato, quais imagens base e dependências foram usadas, quais verificações
passaram e quais implantações receberam o mesmo digest.

## Relações

- [Software supply chain](index.md) organiza as garantias da cadeia.
- [Builds reproduzíveis](reproducible-builds.md) trata da repetição determinística.
- [Atestação](attestation.md) trata do envelope de afirmações verificáveis.
- [SLSA](slsa.md) define requisitos e vocabulário para a proveniência de builds.
- [Assinatura de artefatos](artifact-signing.md) trata da integridade e da identidade.
- [SBOM](sbom.md) descreve a composição do artefato.

## Fontes primárias

- [SLSA provenance](https://slsa.dev/spec/v1.0/provenance)
- [SLSA build track](https://slsa.dev/spec/v1.2/build-track-basics)
- [in-toto](https://in-toto.io/)
- [in-toto attestation](https://github.com/in-toto/attestation)
- [DSSE](https://github.com/secure-systems-lab/dsse)
- [OCI image annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md)
