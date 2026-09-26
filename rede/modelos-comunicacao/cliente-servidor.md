# Cliente-servidor

Cliente-servidor é um modelo em que um cliente inicia ou mantém uma interação
com um serviço que responde a pedidos e aplica regras de acesso. Os papéis são
lógicos e podem mudar por fluxo. Um processo pode ser cliente de um banco de
dados e servidor de uma API ao mesmo tempo.

## Fluxo

O cliente descobre o serviço, estabelece uma conexão ou sessão, envia uma
operação e interpreta a resposta. O servidor autentica, autoriza, valida,
processa e registra a operação. Em protocolos modernos, uma requisição pode
ser assíncrona, streaming ou desconectada, portanto o modelo não exige que o
cliente fique bloqueado aguardando uma resposta única.

HTTP, DNS, SMTP, SSH, bancos de dados e muitos serviços de infraestrutura usam
variações desse modelo. O servidor pode ser replicado atrás de um balanceador,
e o cliente pode usar cache, retry, circuit breaker ou conexão persistente.

## Vantagens e limites

Centralizar dados e autorização facilita governança, backup, auditoria e
revogação. Também concentra custo, capacidade e falhas. O servidor precisa de
limites de conexão, filas, timeouts, rate limiting, observabilidade e
planejamento de recuperação.

Retries mal definidos podem multiplicar carga e repetir operações. Operações
de escrita precisam de idempotência ou de uma forma explícita de deduplicação.
Cache e réplicas melhoram latência, mas introduzem consistência e invalidação.

## Quando usar

Cliente-servidor é uma escolha natural quando existe uma fonte de verdade,
política central de acesso, dado compartilhado ou necessidade de auditoria.
Ele também é apropriado quando os clientes não devem aceitar conexões de
entrada ou não possuem armazenamento e capacidade suficientes para cooperar.

Quando a comunicação precisa continuar entre dispositivos sem um serviço
central, ou quando o conteúdo deve ser distribuído entre participantes, avalie
[P2P](p2p.md).

## Fontes primárias

- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 9293, TCP](https://www.rfc-editor.org/rfc/rfc9293)
