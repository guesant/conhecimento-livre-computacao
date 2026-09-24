# Imagem de container

Uma imagem de container é um artefato imutável que combina um sistema de arquivos em camadas com parâmetros para iniciar um processo. Ela é distribuída como conteúdo endereçado por digest e pode ser consumida por engines diferentes quando o formato e a plataforma são compatíveis.

## O que a imagem representa

A imagem descreve um ponto de partida para criar um container. Ela contém o material necessário para montar o root filesystem e uma configuração que pode definir entrada, argumentos, ambiente, diretório de trabalho, usuário e outros parâmetros de execução. O container é a instância criada a partir desse artefato, com estado próprio e ciclo de vida diferente.

Uma imagem não é uma máquina virtual. Ela não carrega um kernel independente nem fornece isolamento equivalente ao de um hypervisor. O processo executado usa as interfaces do kernel do host por meio das primitivas de isolamento e controle disponibilizadas pelo runtime.

## Modelo interno

Uma imagem para uma plataforma específica é descrita por um [manifesto](manifest.md). O manifesto aponta para um objeto de configuração e para uma sequência ordenada de [camadas](layer.md), usando [descriptors](oci/descriptor.md) que registram media type, tamanho e digest.

Um [image index](image-index.md) pode apontar para vários manifestos, por exemplo, uma variante para `linux/amd64` e outra para `linux/arm64`. O cliente escolhe a variante compatível com a plataforma solicitada e depois resolve o manifesto correspondente.

Essa composição separa identidade, conteúdo e execução. O manifesto relaciona os blobs, a configuração descreve propriedades da imagem e as camadas formam o filesystem final. Alterar qualquer um desses elementos produz uma nova identidade de conteúdo.

## Do build à execução

O builder lê um [build context](build-context.md) e produz camadas e configuração. O resultado é publicado em um [registry](distribuicao/registry.md) ou em outro [repositório de artefatos](distribuicao/artifact-repository.md). Um cliente resolve uma tag ou digest, baixa o manifesto, busca os blobs referenciados e entrega o resultado a um runtime.

O registry não executa a imagem, e o runtime não precisa conhecer como ela foi construída. Essa separação permite que BuildKit, Buildah ou outro builder produzam o artefato e que Docker Engine, Podman ou um runtime de cluster o consumam em momentos diferentes.

## Segurança e desempenho

O digest identifica o conteúdo recuperado, mas não prova a origem nem a segurança do processo de build. Autenticidade de produtor exige uma política adicional, como assinatura, atestação e verificação de identidade do publisher. O tamanho e a quantidade de camadas influenciam o tempo de pull e o aproveitamento de cache, mas reduzir camadas sem entender o cache do builder pode aumentar o custo total do pipeline.

Dados mutáveis de uma aplicação não devem ser tratados como parte da imagem. Imagens devem ser substituíveis e reproduzíveis; estado persistente pertence ao volume, banco ou serviço que possui o ciclo de vida dos dados.

## Relações

- [OCI Image Specification](oci/image-spec.md) define o formato do artefato.
- [OCI Distribution Specification](oci/distribution-spec.md) define a distribuição.
- [Dockerfile](build/dockerfile.md) define uma forma de descrever o build, não o formato OCI.
- [Compose Specification](compose/specification.md) combina imagens em uma aplicação local.

## Fontes primárias

- [OCI Image Format Specification](https://github.com/opencontainers/image-spec)
- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
