# Repositório de artefatos

Um repositório de artefatos é um serviço que armazena, indexa, autoriza e distribui pacotes produzidos por processos de build. Um registry OCI é uma especialização voltada a manifestos, blobs e referências de conteúdo OCI. Um gerenciador universal pode reunir imagens, charts Helm, pacotes npm, módulos e arquivos genéricos sob uma mesma governança.

## Registry e gerenciador universal

Um registry dedicado reduz escopo e quantidade de componentes. Ele é adequado quando a necessidade principal é publicar e puxar imagens ou outros artefatos compatíveis com a Distribution Specification. A organização ainda precisa resolver autenticação, retenção, replicação, scanning e auditoria conforme o produto escolhido.

Um gerenciador universal pode reduzir o número de serviços de distribuição e centralizar permissões. O benefício vem acompanhado de mais superfície operacional, mais tipos de armazenamento e políticas que precisam distinguir ecossistemas diferentes. Guardar todos os artefatos juntos não elimina a necessidade de políticas próprias para imagens, pacotes e arquivos.

## Funções que não devem ser confundidas

Armazenar blobs não é o mesmo que construir imagens. Servir um manifesto não é o mesmo que verificar a origem de um publisher. Scanning não é assinatura, e retenção não é backup. Uma arquitetura de supply chain precisa nomear cada responsabilidade para não tratar uma capacidade parcial como garantia completa.

As funções normalmente envolvidas são autenticação, autorização, descoberta, upload, download, retenção, replicação, metadata, assinatura, provenance, análise de vulnerabilidades e auditoria. Algumas podem estar integradas no mesmo produto, mas continuam sendo decisões diferentes.

## Seleção

Para escolher um repositório, avalie formatos necessários, modelo de identidade, compatibilidade com builders e runtimes, suporte a conteúdo imutável, retenção, replicação, disponibilidade, custo e integração com a CI. Em ambiente pequeno, um registry SaaS integrado à forge pode ter custo menor que operar Harbor ou um gerenciador universal. Em ambiente regulado ou multi-equipe, a governança adicional pode justificar o serviço maior.

## Relações

- [Registry OCI](registry.md) descreve a especialização de distribuição.
- [OCI Distribution Specification](../oci/distribution-spec.md) define a API interoperável.
- [Supply chain e SBOM](../../seguranca/supply-chain/index.md) trata provenance e metadata de segurança.
- [Skopeo](skopeo.md) move e inspeciona artefatos sem executar containers.

## Fontes primárias

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
- [Harbor documentation](https://goharbor.io/docs/)
