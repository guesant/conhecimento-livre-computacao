# Software Bill of Materials

SBOM é um documento estruturado que descreve componentes que compõem um software e relações relevantes entre eles.

Ele melhora inventário e resposta a vulnerabilidades porque permite perguntar quais produtos incluem determinado componente.

Um SBOM não prova que os componentes são seguros nem que o build foi confiável. [Proveniência](provenance.md) e [assinatura](artifact-signing.md) respondem outras propriedades.

[SPDX](spdx.md) e [CycloneDX](cyclonedx.md) são formatos capazes de representar SBOMs.

## Ferramentas que geram SBOM

As ferramentas abaixo produzem inventários a partir de fontes diferentes. O resultado não é equivalente entre elas: uma imagem de container, um filesystem, um lockfile e um build podem conter componentes diferentes. A escolha deve acompanhar o artefato que será publicado e a pergunta que o inventário precisa responder.

| Ferramenta | Entrada principal | Saídas ou uso comum | Limite importante |
| --- | --- | --- | --- |
| Syft | Imagens, diretórios, arquivos e imagens OCI | CycloneDX, SPDX e formatos nativos | Descobre o que está presente no artefato analisado, não a intenção do manifesto de build |
| Trivy | Imagens, filesystem e repositórios | CycloneDX, SPDX e integração com análise de vulnerabilidades | O SBOM e o resultado de vulnerabilidades são artefatos diferentes, mesmo quando gerados na mesma execução; em imagens, os componentes podem trazer a camada de origem |
| cdxgen | Source trees, manifests e lockfiles | CycloneDX para múltiplos ecossistemas | A qualidade depende de o manifesto e o lockfile representarem todas as dependências transitivas |
| CycloneDX CLI | BOMs e dados de componentes existentes | Validação, conversão e agregação de CycloneDX | É principalmente uma ferramenta de manipulação do BOM, não um detector completo de componentes de qualquer imagem |
| SPDX SBOM Generator | Repositórios e ecossistemas suportados | SPDX | A cobertura varia conforme a linguagem e o gerenciador de dependências |
| Tern | Imagens de container e camadas | Relatórios de componentes e licenças | A análise é orientada a camadas e precisa ser interpretada junto com o manifesto final |

As páginas oficiais das ferramentas são as melhores referências para formatos, ecossistemas e limitações de cada versão: [Syft](https://github.com/anchore/syft), [Trivy](https://aquasecurity.github.io/trivy/latest/docs/supply-chain/sbom/), [cdxgen](https://github.com/CycloneDX/cdxgen), [CycloneDX CLI](https://github.com/CycloneDX/cyclonedx-cli), [SPDX SBOM Generator](https://github.com/opensbom-generator/spdx-sbom-generator) e [Tern](https://github.com/tern-tools/tern).

No repositório, o Trivy gera um SBOM CycloneDX por imagem implantada. O inventário é produzido depois que os charts são renderizados, portanto descreve imagens que o cluster realmente referencia, e não somente imagens mencionadas em arquivos de exemplo.

## Trivy e detecção de camadas

Ao analisar uma imagem, o Trivy inspeciona o filesystem resultante e detecta pacotes do sistema operacional e dependências de linguagens. O resultado não é uma leitura do Dockerfile: ele responde quais componentes estão presentes na imagem que será executada. Isso evita confundir uma instrução de build com o conteúdo efetivamente distribuído.

O SBOM gerado para uma imagem identifica o artefato por propriedades como `ImageID` e `RepoDigest`. Os componentes detectados também podem carregar `LayerDigest` e `LayerDiffID`, permitindo relacionar um pacote à camada na qual ele foi introduzido. O `LayerDigest` identifica o blob distribuído, enquanto o `LayerDiffID` identifica o conteúdo descomprimido usado na cadeia do filesystem. Essa distinção é a mesma documentada em [camada de filesystem](../../containers/layer.md).

Essa informação de camada é útil para investigar a origem de uma dependência, comparar imagens e localizar a etapa que introduziu um pacote. Ela não transforma o SBOM em um histórico completo do build. Um arquivo removido por uma camada posterior pode continuar existindo em blobs antigos da imagem, mas não necessariamente aparecerá como componente do filesystem final. Para investigar segredos ou dados que tenham passado por camadas anteriores, é necessário analisar o histórico e os blobs da imagem com uma ferramenta apropriada.

Para gerar os formatos mais usados, o alvo deve ser a imagem identificada pelo digest que será promovido:

```shell
trivy image --format cyclonedx --output sbom.cdx.json registry.example/app@sha256:...
trivy image --format spdx-json --output sbom.spdx.json registry.example/app@sha256:...
```

O formato CycloneDX, sem um scanner adicional, representa o SBOM. A análise de vulnerabilidades, segredos e licenças é uma responsabilidade separada do inventário de componentes, ainda que o Trivy possa executar esses scanners na mesma ferramenta. Se o pipeline precisar incluir vulnerabilidades no relatório CycloneDX, isso deve ser uma decisão explícita, porque mistura composição com resultados de segurança que mudam conforme a base consultada.

Para um filesystem extraído, o comando equivalente é `trivy fs --format cyclonedx --output sbom.cdx.json caminho/`. A diferença é importante: `image` preserva a identidade e metadata da imagem, enquanto `fs` responde sobre os arquivos que foram entregues ao scanner, sem representar necessariamente o manifesto e a cadeia de camadas da imagem original.

## Ferramentas relacionadas que não geram SBOM

[Renovate](../../renovate-atualizacao-automatica-de-dependencia.md) deve aparecer no fluxo de supply chain, mas não é um gerador de SBOM. Ele atualiza versões, tags, digests e lockfiles. Isso mantém a entrada de dependências atualizada para que um gerador como Syft, Trivy ou cdxgen produza um inventário atual, mas não substitui a geração do inventário.

[Grype](https://github.com/anchore/grype) e [OSV-Scanner](https://google.github.io/osv-scanner/) consomem ou descobrem componentes para procurar vulnerabilidades. Um scanner pode receber um SBOM pronto e correlacioná-lo com uma base de vulnerabilidades; isso não significa que ele seja a ferramenta responsável por gerar o SBOM.

## Quando gerar

Gere o SBOM no ponto em que o artefato já tem identidade estável, normalmente depois do build e antes da publicação ou promoção. Para imagens, prefira analisar o digest que será implantado. Para código-fonte, preserve o commit e o lockfile usados na execução. Armazene o SBOM junto da evidência do build, com o formato e a ferramenta identificados, e não trate um inventário antigo como descrição do artefato atual.

## Relação com outras garantias

Um SBOM descreve composição. [Proveniência](provenance.md) descreve como o artefato foi produzido, [atestação](attestation.md) vincula afirmações a uma identidade e [assinatura](artifact-signing.md) protege a integridade e a autoria da afirmação ou do artefato. Atualizar dependências com Renovate e gerar SBOM com Trivy são controles complementares, não etapas que provam a mesma propriedade.
