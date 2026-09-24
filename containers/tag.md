# Tag de imagem

Uma tag é um nome legível que um registry resolve para um manifesto ou image index. Ela funciona como um ponteiro dentro de um repositório, não como uma identidade imutável do conteúdo.

## Semântica

Uma tag como `1.4.0` pode seguir uma política de publicação que nunca a reescreve, mas o formato do nome não impede uma alteração posterior. Tags como `latest`, `stable`, `main` e `canary` normalmente são canais móveis. O cliente só descobre o conteúdo atual depois de consultar o registry.

O mesmo nome pode apontar para um manifesto simples ou para um image index. A resolução depende do estado atual do registry e da negociação do cliente. Uma tag não contém, por si só, a informação suficiente para reproduzir o pull no futuro.

## Quando usar

Tags são adequadas para descoberta humana, canais de release e automação que deliberadamente acompanha uma linha móvel. Elas também facilitam a comunicação entre build, publicação e promoção, desde que o sistema registre o digest resolvido antes de executar uma mudança.

Elas não são suficientes como referência final de produção quando a reproducibilidade e a auditoria exigem que o conteúdo não mude silenciosamente. Nesse caso, a configuração deve registrar o digest e tratar a tag apenas como metadado de origem ou conveniência.

## Política de tags

Uma política útil separa tags de release, pré-release, branch e ambiente. Ela define quem pode criar ou mover cada uma, quanto tempo tags temporárias permanecem e como imagens antigas são retidas. Sem essas regras, uma tag vira um canal de alteração implícita que dificulta rollback e investigação.

## Relações

- [Digest](digest.md) identifica o conteúdo de forma content-addressable.
- [Manifesto](manifest.md) é o conteúdo que a tag resolve.
- [Registry OCI](distribuicao/registry.md) armazena e serve essa associação.
- [Rollout de imagens](../../arquitetura/rollout-de-imagens.md) trata a promoção no repositório deste projeto.

## Fonte primária

- [Docker image tag](https://docs.docker.com/reference/cli/docker/image/tag/)
