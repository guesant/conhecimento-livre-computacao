# Ingress

Ingress é uma API para publicar rotas HTTP e HTTPS de fora do cluster para
Services. Um recurso Ingress descreve regras, hosts e TLS, enquanto um
Ingress controller observa essas regras e configura um proxy ou load balancer.

## API e implementação

Criar um objeto Ingress não publica tráfego sozinho. É necessário um
controller que suporte a classe indicada e que tenha acesso aos Services,
Secrets e endpoints. Diferentes controllers implementam annotations e recursos
adicionais de formas diferentes, por isso uma configuração baseada em
annotations não é automaticamente portável.

TLS no Ingress associa um certificado a hosts e termina a conexão no ponto
definido pelo controller. O tráfego até o Service pode continuar sem TLS ou
usar TLS novamente, conforme o modelo de confiança e a necessidade do backend.

## Limites e evolução

Ingress cobre o caso comum de roteamento HTTP, mas sua API evolui lentamente e
depende de extensões. Gateway API separa papéis de infraestrutura, operação e
desenvolvimento com recursos mais expressivos. Escolher Gateway API não é
apenas trocar o kind: o controller, o modelo de ownership e o suporte de
recursos precisam ser avaliados.

## Relações

- [Service](../core/service.md) é o backend lógico.
- [Gateway API](../../gateway-api.md) é a evolução para roteamento expressivo.
- [TLS termination](../../seguranca/tls/termination.md) trata fronteiras de
  confiança.

## Fonte primária

- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
