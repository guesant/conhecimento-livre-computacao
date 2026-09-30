# OpenTelemetry Collector

O OpenTelemetry Collector recebe, processa e exporta telemetria entre
instrumentação e backends. Ele permite centralizar batching, filtros,
enriquecimento, retry e roteamento sem embutir toda a lógica em cada serviço.

Ele é uma implementação vendor-neutral de um pipeline de telemetria. Pode receber dados
produzidos por OpenTelemetry e por formatos ou agentes compatíveis, aplicar decisões
operacionais e exportar para um ou mais backends. O Collector não é um banco de dados e
não deve ser tratado como armazenamento durável por padrão.

## Pipeline

Uma pipeline define receivers, processors e exporters para um tipo de sinal. Receivers
aceitam dados; processors transformam ou filtram; exporters enviam. Connectors podem
ligar duas pipelines, atuando como exporter de uma e receiver de outra. Extensions
adicionam capacidades como health check e diagnóstico sem processar diretamente cada
registro de telemetria.

Configurar um componente não o habilita. O componente precisa aparecer na seção `service`
e em uma pipeline compatível.

O Collector normalmente possui pipelines separadas para `traces`, `metrics` e `logs`.
Um receiver ou processor pode ser reutilizado na configuração, mas cada pipeline possui
seu próprio fluxo e seus próprios custos. A ordem dos processors altera o resultado.

A configuração precisa separar pipelines de traces, métricas e logs quando
suas garantias e destinos diferem.

## Agent e gateway

No modo agent, um Collector próximo da aplicação recebe telemetria localmente. Esse
desenho reduz a dependência direta da aplicação em uma rede distante e permite batching,
retry e filtragem no nó. O agent precisa de limites de memória e de uma política para
quando o backend ficar indisponível.

No modo gateway, um serviço centralizado recebe sinais de vários agents ou aplicações.
Ele pode fazer roteamento, tail sampling, enriquecimento comum e exportação para vários
destinos. O gateway se torna um componente compartilhado e precisa de escala, segurança,
alta disponibilidade e controle de cardinalidade.

Os dois modos podem ser combinados. A escolha depende de latência, volume, isolamento de
falhas, custo de rede, necessidade de sampling centralizado e capacidade operacional.

## Resiliência

Batching reduz chamadas pequenas ao backend. Retry pode recuperar falhas transitórias,
mas também pode aumentar a pressão quando o destino está indisponível. Filas em memória
absorvem picos curtos, mas perdem dados quando o Collector termina e não substituem uma
fila durável.

Use memory limiter, filas, backpressure e limites de concorrência com base em testes.
Observe o próprio Collector, incluindo memória, rejeições, filas, exportações falhas,
tempo de processamento e dados descartados. Um Collector sem telemetria própria cria um
ponto cego no pipeline.

## Failure modes

Fila, retry e backpressure podem proteger um backend lento, mas consomem
memória e podem descartar dados quando o limite é atingido. Um Collector
indisponível pode bloquear uma aplicação se a exportação for síncrona ou perder
telemetria se a política for best effort.

O Collector também pode descartar dados por filtro, erro de configuração, atributos
inválidos, excesso de cardinalidade ou incompatibilidade de protocolo. Todo descarte
intencional deve possuir uma razão, métrica e documentação de retenção.

## Segurança

Proteja endpoints de ingestão com rede restrita, TLS e autenticação quando a topologia
permitir acesso fora do host confiável. Não exponha portas de diagnóstico ou receivers
em endereços públicos sem necessidade. Filtre segredos, tokens e dados pessoais antes de
exportar para um backend compartilhado.

O endpoint de health check não deve revelar credenciais ou dados da pipeline. A segurança
do Collector inclui também os exporters: um erro de destino ou configuração pode enviar
telemetria para o ambiente errado.

## Relações

- [OpenTelemetry](index.md) define o ecossistema.
- [Instrumentação](instrumentation.md) produz sinais.
- [Grafana Alloy](../alloy.md) é uma distribuição que pode executar funções
  semelhantes.

## Fonte primária

- [Collector](https://opentelemetry.io/docs/collector/)
- [Componentes do Collector](https://opentelemetry.io/docs/collector/components/)
- [Configuração do Collector](https://opentelemetry.io/docs/collector/configuration/)
