# OpenTelemetry

OpenTelemetry é um ecossistema de APIs, SDKs, bibliotecas de instrumentação,
protocolos, convenções semânticas e componentes para produzir, transportar e processar
telemetria. Ele cobre principalmente traces, métricas e logs, sem ser um backend de
armazenamento, uma ferramenta de consulta ou um produto de dashboards.

O projeto surgiu da convergência entre OpenTracing e OpenCensus. A consequência prática
é separar a instrumentação da aplicação do backend escolhido. Uma aplicação pode exportar
telemetria para um Collector e depois trocar o destino sem reescrever todos os pontos de
instrumentação.

## Sinais

Os sinais são formas diferentes de descrever a atividade do sistema:

| Sinal | Pergunta principal | Exemplo |
| --- | --- | --- |
| Trace | Por quais etapas passou uma operação? | Requisição HTTP até o banco |
| Span | Qual unidade de trabalho consumiu tempo? | Consulta SQL ou chamada RPC |
| Métrica | Qual comportamento agregado ocorreu? | Latência, erros ou saturação |
| Log | Qual evento detalhado foi registrado? | Exceção e contexto de execução |
| Baggage | Que contexto deve acompanhar a operação? | Identificador de tenant |
| Profile | Quais funções consumiram recursos? | CPU ou alocação de memória |

Traces, métricas e logs são sinais centrais. Baggage é contexto transportado, não uma
substituição para autorização. Profiles e eventos possuem suporte e maturidade diferentes
conforme o sinal e a linguagem, portanto devem ser avaliados antes de serem tratados como
parte homogênea da plataforma.

Um mesmo evento pode aparecer em mais de um sinal. Uma exceção pode gerar um span com
status de erro, um log estruturado e uma métrica de contagem. A correlação deve ser útil,
sem transformar cada ocorrência em uma label de alta cardinalidade.

## API, SDK e instrumentação

A API oferece interfaces que bibliotecas e código de aplicação podem usar sem depender da
implementação completa do SDK. O SDK configura processors locais, exporters, sampling,
recursos e ciclo de vida. Bibliotecas de instrumentação conectam frameworks, clientes HTTP,
drivers de banco, bibliotecas de mensageria e runtimes aos sinais.

Essa separação permite que uma biblioteca produza spans sem assumir qual backend será
usado. O código da aplicação normalmente configura o SDK e o exporter no processo de
execução. A biblioteca instrumentada deve depender da API e de convenções apropriadas, e
não de um exporter específico.

## Recursos e escopo

Um recurso identifica a entidade que produz telemetria. `service.name`, ambiente,
versão, host, container, namespace e pod ajudam a distinguir instâncias e releases.
Defina `service.name` explicitamente; deixar o SDK usar um nome genérico como
`unknown_service` dificulta consultas e alertas.

O recurso é associado ao provider de traces ou métricas no momento da criação. Ele não é
o mesmo que um atributo de um span individual. Instrumentation scope identifica a
biblioteca ou componente que gerou o dado, incluindo nome e versão quando disponíveis.

## Contexto e correlação

O contexto acompanha uma execução entre funções, threads, filas e serviços. Propagators
serializam esse contexto em headers HTTP, metadata RPC ou envelopes de mensagem. O
propagator W3C Trace Context é comum em aplicações web, mas o transporte precisa ser
validado na fronteira entre cada sistema.

O trace context ajuda a correlacionar spans. Baggage carrega pares nome-valor entre
serviços, mas pode aumentar exposição de dados e custo de processamento. Não propague
segredos, tokens ou atributos que permitam alterar autorização sem validação local.

[Contexto e propagação](context.md) detalha carriers, propagators, baggage e falhas de
correlação.

## Convenções semânticas

Convenções semânticas definem nomes, tipos e valores para atributos de HTTP, RPC, banco,
mensageria, exceções, recursos e outros domínios. Sem convenções, duas equipes podem
registrar a mesma operação com nomes incompatíveis, dificultando dashboards e consultas.

Convenção não significa capturar todos os campos. A aplicação ainda precisa controlar
cardinalidade, sensibilidade, retenção e custo. A versão das convenções também faz parte
da compatibilidade da telemetria.

## Sampling

Sampling decide quais traces serão mantidos ou exportados. Head sampling decide cedo, com
baixo custo, mas pode descartar um trace antes que sua importância seja conhecida. Tail
sampling aguarda mais contexto e pode preservar erros ou traces lentos, mas exige memória,
coordenação e uma topologia capaz de reunir os spans.

Sampling não deve eliminar completamente evidências raras sem uma estratégia para erros,
latência alta e operações críticas. A taxa escolhida deve considerar volume, custo de
armazenamento, necessidade de auditoria e política de privacidade.

[Sampling](sampling.md) detalha os modelos e seus trade-offs.

## OTLP e Collector

OTLP é o protocolo nativo de transporte do OpenTelemetry. A aplicação pode exportar
diretamente para um backend compatível ou enviar para o [Collector](collector.md), que
recebe, processa e encaminha os sinais.

O Collector pode centralizar batching, retry, filtragem, transformação, enriquecimento,
roteamento e exportação para mais de um destino. Ele não substitui necessariamente o
backend: normalmente encaminha telemetria para Prometheus, Loki, Jaeger, Tempo, Sentry,
um serviço gerenciado ou outro sistema compatível.

## O que OpenTelemetry não resolve

OpenTelemetry não define sozinho a retenção, o modelo de consulta, o dashboard, o SLO,
a política de alerta ou a autorização de acesso aos dados. Também não transforma uma
instrumentação ruim em diagnóstico útil.

A plataforma precisa definir quem pode ler atributos, quanto tempo cada sinal permanece,
como dados pessoais são removidos e o que acontece quando o Collector ou o backend está
indisponível. Telemetria é um fluxo de produção que possui custo e failure domains.

## Relações

- [OpenTelemetry Collector](collector.md) recebe, processa e encaminha sinais.
- [Instrumentação](instrumentation.md) cria dados na aplicação.
- [Contexto e propagação](context.md) explica correlação e baggage.
- [Sampling](sampling.md) explica seleção de traces.
- [Tracing](../tracing.md) explica o sinal distribuído.
- [Exemplars](../metric-types/exemplars.md) ligam métricas a traces.

## Fontes primárias

- [OpenTelemetry, conceitos](https://opentelemetry.io/docs/concepts/)
- [OpenTelemetry, sinais](https://opentelemetry.io/docs/concepts/signals/)
- [OpenTelemetry, visão geral da especificação](https://opentelemetry.io/docs/specs/otel/overview/)
- [OpenTelemetry, convenções semânticas](https://opentelemetry.io/docs/specs/semconv/)
