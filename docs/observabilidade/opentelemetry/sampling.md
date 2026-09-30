# Sampling no OpenTelemetry

Sampling seleciona quais traces ou spans serão mantidos e exportados. Ele controla
volume, custo e carga de processamento, mas também pode remover a evidência necessária
para investigar uma falha rara. A política precisa ser escolhida pela pergunta que a
telemetria deve responder.

## Head sampling

Head sampling decide no início da operação, antes de conhecer todos os spans e resultados.
É simples, barato e pode ser aplicado no SDK ou no primeiro Collector. A decisão é
propagada para que os serviços mantenham uma visão coerente do trace.

Uma taxa fixa é fácil de operar, mas pode descartar justamente erros raros ou requisições
lentas. Regras que preservam certos endpoints, ambientes ou tipos de operação podem
melhorar o valor, desde que a cardinalidade e o custo sejam controlados.

## Tail sampling

Tail sampling aguarda spans suficientes para decidir com base no resultado completo. Pode
preservar traces com erro, alta latência, exceções ou atributos de negócio importantes.

O Collector ou backend precisa reunir os spans do trace no mesmo componente lógico. Isso
exige memória, timeout de espera e estratégia para traces incompletos. Aumentar a janela
de espera pode melhorar a decisão, mas também aumenta memória, latência de exportação e
risco de descarte.

## Regras de seleção

Uma política pode combinar critérios:

- manter todos os erros classificados;
- manter traces acima de um limite de duração;
- manter operações críticas;
- amostrar uma fração dos sucessos;
- reduzir volume de ambientes de desenvolvimento;
- descartar atributos ou sinais que não tenham valor operacional.

A regra deve explicar o que acontece quando os dados necessários para a decisão estão
ausentes. Não dependa de um atributo arbitrário se instrumentações diferentes podem
produzir nomes incompatíveis.

## Consistência entre serviços

Se cada serviço decidir de forma independente, um trace pode ficar parcialmente visível.
Isso não é sempre errado, mas precisa ser entendido nas consultas. Sampling distribuído
deve considerar propagação da decisão, múltiplos hops e serviços que não usam OpenTelemetry.

O trace ID deve permanecer estável mesmo quando parte dos spans não for exportada. Logs e
métricas correlacionados devem indicar quando a referência aponta para um trace que foi
descartado.

## Custo e privacidade

Sampling não substitui redaction, controle de acesso ou retenção. Um trace descartado
depois de conter um segredo em memória ainda pode ter sido registrado em logs, filas ou
buffers. A filtragem de dados sensíveis precisa ocorrer antes da exportação e, quando
possível, antes da criação do atributo.

Calcule o custo considerando volume de spans, tamanho de atributos, retenção, replicação,
egress, processamento do Collector e consultas. Capturar tudo pode ser útil em um teste
curto, mas raramente é um default sustentável para produção.

## Diagnóstico

Ao investigar uma ausência, diferencie quatro casos: a aplicação não criou o span, o
contexto não foi propagado, o sampling descartou o trace ou o exporter/backend falhou.
Métricas do SDK e do Collector devem mostrar contagem criada, amostrada, exportada,
rejeitada e descartada quando a implementação oferecer esses dados.

## Fontes

- [OpenTelemetry, sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [OpenTelemetry Collector, tail sampling](https://opentelemetry.io/docs/collector/transforming-telemetry/)
- [OpenTelemetry, conceitos](https://opentelemetry.io/docs/concepts/)
