# Software supply chain

Software supply chain abrange componentes, ferramentas, identidades e processos que transformam source code em artefatos consumidos e implantados.

A categoria inclui [SBOM](sbom.md), [proveniência](provenance.md), [atestação](attestation.md), [assinatura de artefatos](artifact-signing.md), [VEX](vex.md) e formatos como [SPDX](spdx.md) e [CycloneDX](cyclonedx.md). Ferramentas como Trivy, Syft e cdxgen geram inventários; Renovate mantém as dependências que serão inventariadas; [OpenSSF Scorecard](openssf-scorecard.md) avalia práticas do repositório e da cadeia de entrega.

Essas peças respondem perguntas diferentes. SBOM descreve composição; proveniência descreve origem/processo; assinatura vincula uma afirmação ou artefato a uma identidade; VEX comunica impacto de vulnerabilidade num produto.
