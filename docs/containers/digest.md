# Digest de imagem

Um digest é um identificador criptográfico do conteúdo de um manifesto, índice ou blob. A referência `repository@sha256:...` aponta para bytes específicos no registry e não depende de um nome de release continuar apontando para o mesmo lugar.

## Integridade e identidade

O cliente calcula ou valida o digest do conteúdo baixado contra o valor da referência. Se os bytes mudarem, o digest não será o mesmo. Essa propriedade permite cache, deduplicação e rollback para uma identidade conhecida sem depender de timestamps ou nomes humanos.

O digest não é uma assinatura. Ele prova que o conteúdo corresponde à referência content-addressable, mas qualquer pessoa que consiga publicar no repositório pode produzir um conteúdo novo e obter um digest novo. Autenticidade exige controle de acesso, assinatura, attestation ou outra policy de confiança.

## Tag com digest

Uma referência pode combinar tag e digest, como `image:main@sha256:...`. A tag comunica a origem ou o canal em que o artefato foi observado. O digest determina qual conteúdo será usado. Se a tag se mover depois, a referência combinada continua resolvendo o digest indicado.

## Índice e plataforma

Quando o digest aponta para um image index, o cliente ainda seleciona um manifesto compatível com a plataforma. Quando aponta para o manifesto de uma plataforma, a seleção já está determinada. Essa diferença importa em ambientes heterogêneos e em auditorias que precisam demonstrar exatamente qual variante foi executada.

## Relações

- [Tag](tag.md) é um nome mutável para descoberta e canais.
- [Image index](image-index.md) compõe variantes de plataforma.
- [Descriptor OCI](oci/descriptor.md) carrega o digest, tamanho e media type.
- [Pinagem por digest e hash](../pinagem-por-digest-e-hash.md) relaciona a prática à cadeia de suprimentos.

## Fonte primária

- [OCI Descriptor](https://github.com/opencontainers/image-spec/blob/main/descriptor.md)
- [Docker image digests](https://docs.docker.com/dhi/core-concepts/digests/)
