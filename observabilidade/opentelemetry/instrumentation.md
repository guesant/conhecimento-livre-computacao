# Instrumentação OpenTelemetry

Instrumentação adiciona APIs e SDKs para produzir telemetria com contexto,
atributos e exportação configurados. Ela pode ser manual, automática ou uma
combinação das duas.

O primeiro objetivo não é gerar o maior número possível de spans. É registrar as
fronteiras que explicam o comportamento do sistema: entrada HTTP, saída HTTP ou RPC,
consulta de banco, consumo de mensagem, job, chamada para serviço externo e operações de
negócio que tenham valor diagnóstico.

## Automática e manual

Instrumentação automática usa agentes, middleware ou bibliotecas que já conhecem o
framework. Ela reduz o tempo para obter cobertura inicial e pode capturar operações
comuns, mas depende da qualidade da integração, dos defaults e da política de atributos.

Instrumentação manual permite nomear uma operação de negócio, adicionar eventos e medir
uma etapa que a instrumentação do framework não conhece. Deve ser aplicada nos limites
sem duplicar spans automáticos ou criar um span para cada função trivial.

## Decisões

Instrumente bordas de entrada e saída, operações de banco, filas e jobs com
nomes estáveis. Não inclua segredos, tokens, dados pessoais ou identificadores
de cardinalidade ilimitada como atributos.

Instrumentação automática reduz esforço inicial, mas pode capturar mais
detalhes do que a política permite ou produzir spans de baixo valor. Manual
permite semântica melhor nos limites de negócio.

## Atributos e eventos

Use convenções semânticas para nomes de HTTP, RPC, banco, mensageria, exceções, recursos
e runtime. Atributos de recurso identificam o serviço e sua instância; atributos de span
descrevem a operação; eventos registram ocorrências dentro do span, como uma exceção.

Não coloque request IDs, URLs arbitrárias, emails ou IDs de usuário como labels de
métricas sem avaliar cardinalidade. Um identificador pode ser útil em logs e traces, mas
ser destrutivo quando transformado em uma dimensão de série temporal.

## Ciclo de vida

Inicialize providers, recursos, propagators e exporters durante o startup. Finalize-os
graciosamente para permitir que batches pendentes sejam exportados, sem atrasar o
encerramento indefinidamente. Em workers e jobs, o ciclo de vida precisa considerar
processamento contínuo e shutdown coordenado.

Propague o `CancellationToken` ou mecanismo equivalente para chamadas de rede e banco.
Não deixe uma exportação de telemetria impedir o encerramento de um processo que precisa
ser substituído.

## Privacidade e custo

Telemetria pode conter dados de negócio e dados pessoais. Defina classificação, retenção,
controle de acesso, mascaramento e redaction no ponto de produção ou no Collector. Uma
regra de filtragem posterior não deve ser usada como justificativa para capturar segredos
em todos os processos.

Sampling, batching e seleção de atributos controlam custo, mas podem remover evidências.
Preserve erros, traces lentos e fluxos críticos quando o objetivo for diagnóstico.

## Relações

- [OpenTelemetry](index.md) define APIs e SDKs.
- [Collector](collector.md) processa e exporta.
- [Contexto e propagação](context.md) correlaciona operações entre fronteiras.
- [Sampling](sampling.md) seleciona traces conforme custo e valor diagnóstico.
- [Tracing](../tracing.md) usa contexto propagado.

## Fonte primária

- [OpenTelemetry instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/)
- [OpenTelemetry resources](https://opentelemetry.io/docs/concepts/resources/)
- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
