# Resource limits

Resource limit define um teto de uso para um container conforme o recurso e os mecanismos do runtime/kernel.

CPU e memória não se comportam de forma simétrica. CPU pode ser throttled; ultrapassar limite efetivo de memória pode resultar em OOM e encerramento.

Um limit não informa ao scheduler quanto reservar; essa responsabilidade pertence a [requests](requests.md).
