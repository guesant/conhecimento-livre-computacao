# API gateway service

Um service de gateway representa o upstream lógico para o qual uma ou mais
rotas encaminham requisições. Ele pode apontar para host, porta, protocolo ou
uma abstração de descoberta.

## Responsabilidade

Separar service e route permite alterar destino sem reescrever todas as regras
de entrada. Health checks, timeouts, retries e TLS até o upstream pertencem a
essa relação, mas seus valores precisam considerar idempotência e capacidade
da aplicação.

Retries automáticos podem duplicar operações quando a requisição alcançou o
upstream e a resposta se perdeu. Não habilite retry amplo para escrita sem um
contrato de idempotência.

## Relações

- [Route](route.md) seleciona o service.
- [Upstream](upstream.md) agrupa targets e balanceamento.
- [API gateway](index.md) fornece o ponto de entrada.

## Fonte primária

- [Kong services](https://docs.konghq.com/gateway/latest/entities/service/)
