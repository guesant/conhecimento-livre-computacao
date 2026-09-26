# MQTT

MQTT é um protocolo leve de publish/subscribe definido pela OASIS para comunicação entre clientes e um servidor broker. Ele foi desenhado para dispositivos, redes com largura de banda limitada e conexões intermitentes, mas também pode ser usado em integrações maiores quando o modelo de tópicos e sessões é adequado.

## Modelo

O cliente publica uma mensagem em um topic ou assina um topic filter. O broker faz a correspondência e encaminha a mensagem para as sessões inscritas. Um cliente pode publicar e assinar, e não precisa conhecer diretamente todos os outros clientes.

O topic organiza o espaço de nomes. Curingas em subscriptions ajudam a consumir famílias de tópicos, mas uma hierarquia permissiva demais pode expor dados entre dispositivos. Autorização deve ser definida por cliente e por topic, não somente por conexão.

## QoS

QoS 0 prioriza menor overhead e pode perder a mensagem. QoS 1 busca entrega pelo menos uma vez e pode duplicar. QoS 2 usa uma troca mais longa para reduzir duplicação dentro das garantias do protocolo. Nenhum nível transforma automaticamente efeitos de negócio em operações idempotentes.

## Sessões e mensagens retidas

Sessões persistentes permitem que o broker mantenha estado de subscriptions e mensagens conforme as opções negociadas. Mensagem retida representa o último valor conhecido de um topic e pode ser entregue quando uma nova assinatura é criada. Retain não é histórico nem event log; ele é apropriado para estado atual, como configuração ou leitura mais recente.

## Quando usar

MQTT é adequado para telemetria, sensores, dispositivos móveis, comandos de baixo overhead e redes com conectividade irregular. Para jobs com processamento complexo, workflows, resposta correlacionada ou replay de longo prazo, uma fila ou plataforma de streaming costuma oferecer um modelo mais apropriado.

## Segurança e operação

Use TLS, autenticação forte, autorização por topic, limites de tamanho, expiração de sessão e política de retenção. Monitore conexões, subscriptions, mensagens rejeitadas, backlog, taxa por cliente e comportamento de reconnect. Evite colocar credenciais ou dados sensíveis em topics, porque nomes podem aparecer em logs e ferramentas de administração.

## Relações

- [Event bus](../../comunicacao/event-bus.md) explica publish/subscribe e eventos.
- [ActiveMQ](activemq.md) documenta um broker que pode oferecer MQTT junto com outros protocolos.
- [Filas](filas.md) diferencia distribuição de trabalho de publicação para vários assinantes.

## Fonte primária

- [MQTT Version 5.0, OASIS Standard](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
