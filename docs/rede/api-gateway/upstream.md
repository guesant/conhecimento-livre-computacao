# API gateway upstream

Upstream é um grupo lógico de targets que pode receber tráfego de um service.
Ele organiza balanceamento, health checks, pesos e failover.

## Target

Um target é um endereço e porta concretos. O upstream pode ter vários targets
para distribuir carga ou sobreviver à falha de um deles. A saúde do target não
prova saúde funcional da aplicação, apenas o resultado do check configurado.

Pesos e retries alteram a distribuição e podem multiplicar carga quando um
destino está lento. Timeouts devem refletir o contrato de cada upstream, não
um valor global arbitrário.

## Relações

- [Service](service.md) referencia o upstream.
- [Route](route.md) seleciona o service.
- [Plugin](plugin.md) pode aplicar policy antes do encaminhamento.

## Fonte primária

- [Kong upstreams](https://docs.konghq.com/gateway/latest/entities/upstream/)
