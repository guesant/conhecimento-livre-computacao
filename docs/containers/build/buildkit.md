# BuildKit

BuildKit é um backend de build usado pelo ecossistema Docker e disponível de forma independente.

Ele oferece execução paralela de etapas independentes, cache, mounts especializados e secrets de build que evitam persistir credenciais em layers.

## Caso de uso

É apropriado para pipelines de build OCI que precisam de cache eficiente, multi-stage builds e integração com Dockerfile.

## Má prática

Passar secrets por ARG ou ENV pode deixá-los em metadados ou histórico. Use mecanismos de secret mount quando disponíveis.
