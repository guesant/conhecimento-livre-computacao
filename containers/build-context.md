# Build context

Build context é o conjunto de arquivos que um builder recebe como entrada de um build. Instruções como `COPY` e `ADD` só podem referenciar caminhos que fazem parte desse conjunto, respeitando as exclusões definidas pelo arquivo de ignore aplicável.

## Fronteira do contexto

O diretório indicado ao comando de build costuma ser o contexto, mas a origem também pode ser um arquivo tar, uma URL, um repositório ou um contexto especial fornecido pelo builder. O Dockerfile pode estar em outro caminho, porém isso não amplia automaticamente o conjunto de arquivos que podem ser copiados.

Essa distinção explica por que um arquivo existente no computador pode não estar disponível no build. Também explica por que apontar o contexto para a raiz inteira de um monorepo aumenta o custo de transferência e a superfície de dados que um Dockerfile pode alcançar.

## Exclusão e segurança

`.dockerignore` e mecanismos equivalentes reduzem o contexto antes do envio ao builder. Eles devem excluir dependências locais, artefatos de build, caches, credenciais, chaves privadas, arquivos de estado e qualquer conteúdo que não seja necessário para reproduzir a imagem.

Excluir um caminho do contexto é diferente de copiar e apagar depois. Se um segredo foi incluído em uma camada, uma camada posterior que o remove não elimina o blob anterior do histórico da imagem. O desenho correto impede a entrada do segredo e usa mounts efêmeros quando o build realmente precisa de uma credencial.

## Performance e reprodutibilidade

Contextos menores reduzem tempo de envio, uso de disco e invalidações de cache causadas por arquivos irrelevantes. A seleção de arquivos precisa ser explícita o suficiente para que a imagem não dependa acidentalmente de um arquivo local que não está documentado como entrada.

Um contexto remoto pode melhorar a automação quando o código já está em uma fonte versionada, mas adiciona dependência de rede e de resolução de referência. Pipelines reprodutíveis registram a revisão ou digest do material usado, em vez de confiar em um branch móvel.

## Relações

- [Dockerfile](build/dockerfile.md) consome o contexto.
- [BuildKit](build/buildkit.md) oferece mounts e mecanismos de secret para o build.
- [Imagem de container](image.md) é o resultado distribuído.
- [OCI Image Specification](oci/image-spec.md) define o formato do resultado, não o contexto.

## Fonte primária

- [Docker build context](https://docs.docker.com/build/concepts/context/)
