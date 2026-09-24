# Reverse proxy

Reverse proxy recebe conexões destinadas a serviços e seleciona ou protege backends.

Pode realizar load balancing, TLS termination, autenticação, rate limiting e roteamento, dependendo do produto e configuração. Nenhuma dessas funções é obrigatória à definição.

## Modos de roteamento

[Host routing](host-routing.md) usa nome do host. [Path routing](path-routing.md) usa caminho da requisição. TLS pode envolver [termination](../../seguranca/tls/termination.md) ou [passthrough](../../seguranca/tls/passthrough.md).

## Cenários

Em single-node, um reverse proxy pode fornecer um único ponto de entrada para vários serviços. Em Kubernetes, Ingress/Gateway controllers podem ocupar responsabilidade equivalente integrada ao estado do cluster.
