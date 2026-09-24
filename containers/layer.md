# Camada de filesystem

Uma camada de imagem é um changeset de filesystem que registra arquivos adicionados, modificados ou removidos em relação à camada anterior. A imagem final resulta da aplicação ordenada dessas camadas sobre um diretório vazio, com regras do formato para representar alterações e whiteouts.

## O que a camada é

O conteúdo de uma camada é um arquivo de dados, normalmente um tar comprimido, identificado por digest. A compressão pertence ao transporte e ao armazenamento do blob. O `DiffID` usado na configuração da imagem representa o conteúdo não comprimido, enquanto o digest do descriptor normalmente identifica o blob distribuído na forma comprimida.

Confundir esses dois valores causa erros ao comparar imagens, reconstruir metadata ou validar uma cadeia de camadas. O digest do descriptor responde qual blob foi distribuído. O `DiffID` responde qual conteúdo descomprimido participa do root filesystem.

## Ordem e composição

As camadas são aplicadas numa ordem definida pelo manifesto. Uma camada posterior pode substituir um arquivo anterior ou registrar a remoção de um caminho. O runtime ou o snapshotter apresenta o resultado como uma árvore única por meio de um filesystem de união ou de uma implementação equivalente.

A ordem também é uma parte do comportamento do build. Uma alteração em uma camada inicial invalida o cache das camadas posteriores, enquanto uma alteração isolada no fim da sequência pode preservar trabalho anterior. Por isso, dependências estáveis costumam ser colocadas antes de arquivos que mudam frequentemente, respeitando as necessidades de segurança e reprodutibilidade.

## Whiteouts e limites

Remover um arquivo não apaga bytes de uma camada anterior. A camada posterior registra uma instrução de remoção, e a visão combinada deixa de expor o caminho. Segredos copiados para uma camada e removidos em outra continuam recuperáveis de um artefato antigo, por isso apagar um arquivo no mesmo Dockerfile não substitui impedir que ele entre no contexto ou em uma camada.

Camadas não são banco de dados, cache de aplicação nem mecanismo de backup. Elas são parte da distribuição do filesystem inicial. Estado gerado em execução deve viver fora da imagem, porque recriar um container precisa ser seguro e previsível.

## Trade-offs

Mais camadas podem melhorar o reuso de cache e a separação entre responsabilidades, mas aumentam metadata e podem tornar o pull mais fragmentado. Menos camadas podem reduzir overhead em casos específicos, mas uma mudança frequente pode invalidar um bloco grande e aumentar o tempo de build. O critério deve ser o padrão de mudança e distribuição, não uma regra universal sobre quantidade de instruções.

## Relações

- [Imagem de container](image.md) combina camadas e configuração.
- [Manifesto](manifest.md) referencia a sequência de camadas.
- [OCI Image Specification](oci/image-spec.md) define os media types e as regras do formato.
- [BuildKit](build/buildkit.md) e [Buildah](build/buildah.md) produzem camadas a partir de um contexto.

## Fonte primária

- [OCI Image Layer Specification](https://github.com/opencontainers/image-spec/blob/main/layer.md)
- [OCI Image Configuration](https://github.com/opencontainers/image-spec/blob/main/config.md)
