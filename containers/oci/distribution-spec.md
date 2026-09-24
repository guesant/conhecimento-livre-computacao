# OCI Distribution Specification

A OCI Distribution Specification define um protocolo para distribuir conteúdo
entre clientes e registries. Imagens são o caso mais comum, mas a API pode
transportar outros artefatos quando seus manifestos e blobs obedecem às regras
de descriptors e media types.

## Responsabilidades

O protocolo organiza operações de pull, push, descoberta de conteúdo e
gerenciamento do ciclo de vida. Um registry recebe requisições para manifestos
e blobs, controla autorização e retorna respostas que clientes podem validar
por digest.

O protocolo não define o processo de build, o formato de um Dockerfile nem a
forma como um runtime inicia um processo. Essas responsabilidades pertencem ao
[formato de imagem OCI](image-spec.md), ao builder e à [OCI Runtime
Specification](runtime-spec.md).

## Modelo de distribuição

Um repositório é um escopo para manifestos, blobs e tags. Um blob é conteúdo
endereçado por digest. Um manifesto pode apontar para outros manifestos e
blobs, enquanto um image index aponta para manifestos de plataformas diferentes.
O cliente pode reutilizar conteúdo já presente localmente porque a identidade
do blob não depende da tag que levou até ele.

O endpoint `/v2/` permite verificar se um serviço implementa a API de registry
esperada. A existência desse endpoint não prova que o registry suporta todas as
categorias opcionais de push, descoberta e gerenciamento; a compatibilidade
precisa ser avaliada segundo as capacidades declaradas pelo produto.

## Failure modes

Falhas de autenticação, autorização, inexistência de repositório, digest
incorreto e media type incompatível têm causas diferentes. Um cliente que
trata todos os erros como falha transitória pode repetir uma operação inválida
ou esconder uma alteração de policy. Pulls devem distinguir credenciais,
referência, integridade e indisponibilidade de rede.

## Relações

- [Registry OCI](../distribuicao/registry.md) descreve o produto que expõe a
  API.
- [Manifesto](../manifest.md) e [descriptor](descriptor.md) definem os
  conteúdos transportados.
- [Skopeo](../distribuicao/skopeo.md) opera sobre imagens sem executar um
  container.

## Fonte primária

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
