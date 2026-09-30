# Registry OCI

Um registry OCI é um serviço que armazena e distribui manifestos, blobs e
referências de conteúdo conforme a [OCI Distribution
Specification](../oci/distribution-spec.md). Ele pode servir imagens de
container e também outros artefatos que usem manifestos, descriptors e media
types compatíveis.

## Repositório, tag e blob

Um repositório organiza manifestos e blobs sob um nome. Uma tag é um ponteiro
mutável para um manifesto ou image index. Um blob é recuperado por digest e
pode ser compartilhado por várias imagens. Essa separação permite deduplicação,
cache e cópia seletiva, mas exige que a policy de retenção preserve todo o
grafo referenciado por uma imagem ainda publicada.

## Capacidades

Todo registry compatível precisa suportar o pull conforme a categoria declarada.
Push, descoberta, gerenciamento de conteúdo, referrers, replicação, retenção,
scanning e interface de usuário são capacidades adicionais do produto. Um
registry pode implementar a API básica e ainda não oferecer o conjunto de
governança necessário para um ambiente de produção.

Autenticação e autorização protegem operações, mas não substituem verificação
de digest ou assinatura. O registry pode controlar quem publica uma tag, porém
o consumidor ainda precisa decidir se confia no publisher e se aceita o
artefato para aquela plataforma e ambiente.

## Registry dedicado e repositório universal

Um registry dedicado reduz escopo e peças operacionais quando o problema é
distribuir OCI. Um gerenciador universal reúne imagens, charts, pacotes e
arquivos sob políticas comuns, ao custo de mais formatos, integrações e
superfície de manutenção. A escolha deve considerar o número de ecossistemas,
replicação, retenção, identidade, auditoria e custo operacional.

## Relações

- [Repositório de artefatos](artifact-repository.md) compara as duas categorias
  de produto.
- [Tag](../tag.md) e [digest](../digest.md) são referências diferentes.
- [Skopeo](skopeo.md) copia ou inspeciona conteúdo sem executar containers.
- [Manifesto](../manifest.md) define o grafo que o registry armazena.

## Fonte primária

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
