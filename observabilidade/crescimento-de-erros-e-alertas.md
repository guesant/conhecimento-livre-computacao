# Crescimento de erros e alertas

Uma taxa de erro alta é importante, mas o crescimento da taxa costuma ser o sinal
mais útil para detectar uma regressão recente. Um serviço pode ter muitos erros
absolutos porque recebe muito tráfego e ainda estar dentro do SLO. Também pode ter
poucos erros absolutos e estar completamente indisponível para uma operação de baixo
volume. O alerta precisa combinar volume, proporção, duração e impacto.

## O que medir

Comece contando operações e resultados com uma métrica de counter. Separe sucesso,
erro de aplicação, rejeição por autenticação, entrada inválida, limite de taxa,
timeout e erro de dependência. Um código 401 pode ser comportamento normal de uma
API pública, enquanto um 500 ou um timeout normalmente representa falha do serviço.
Somar tudo em uma única série torna o alerta difícil de interpretar.

Uma cobertura mínima para um serviço orientado a requisições inclui:

| Medição | Pergunta |
| --- | --- |
| Total de requisições | A demanda mudou? |
| Erros por classe | Qual resultado está falhando? |
| Taxa de erro | Qual proporção das operações falha? |
| Latência | A falha vem acompanhada de degradação? |
| Saturação | CPU, memória, fila, conexões ou disco estão no limite? |
| Dependência | Banco, API externa, DNS ou fila está causando a falha? |

## Absoluto, taxa e crescimento

Uma contagem absoluta ajuda a detectar volume operacional e fila de incidentes. A taxa
normaliza pelo tráfego e é melhor para comparar períodos com demanda diferente. O
crescimento compara a janela atual com uma janela anterior ou com uma baseline sazonal.

Para counters Prometheus, use rate para taxa por segundo e increase para o número
estimado de eventos no intervalo. Não aplique deriv diretamente a um counter que
reinicia; use as funções apropriadas para séries monotônicas.

Um exemplo conceitual de taxa de erro por serviço é:

    sum by (service) (rate(http_requests_total{status=~"5.."}[5m]))
    /
    sum by (service) (rate(http_requests_total[5m]))

Esse resultado é uma proporção, não uma porcentagem. Multiplique por 100 apenas na
visualização ou na regra que usa um limiar em percentual.

Para detectar crescimento, compare uma janela recente com uma baseline:

    rate(http_requests_total{status=~"5.."}[5m])
    >
    2 * rate(http_requests_total{status=~"5.."}[1h])

Essa comparação é apenas uma heurística. Ela pode disparar quando a taxa anterior era
próxima de zero, quando o tráfego é muito pequeno ou quando existe sazonalidade. Uma
regra real deve combinar um piso de erro, um mínimo de requisições e uma duração.

## Janela curta e janela longa

Uma janela curta detecta uma regressão rapidamente, mas reage a picos breves. Uma
janela longa é mais estável, mas atrasa a percepção. Usar duas janelas ajuda a separar
incidente intenso de oscilação:

- a janela curta identifica uma mudança abrupta;
- a janela longa confirma que o impacto não é apenas um instante;
- o volume mínimo impede que uma única requisição falha gere paging;
- o campo for evita notificar por uma amostra isolada.

Uma regra pode ter severidade diferente conforme a combinação. Um aumento de erros
curto pode gerar evento para investigação. Erro sustentado acima do orçamento de erro
pode gerar page. O cálculo deve usar o SLO e o impacto real, não apenas o nome do
status HTTP.

## Crescimento sem cardinalidade perigosa

Não coloque user ID, e-mail, token, IP bruto ou correlation ID como label de uma métrica
de erro. Cada valor cria uma série nova e pode consumir memória e armazenamento sem
limite útil. A documentação do OpenTelemetry também alerta que atributos de alta
cardinalidade, como IDs de usuário e paths crus, aumentam o custo de métricas.

Para investigar um usuário, utilize logs estruturados, traces amostrados, uma ferramenta
de eventos ou uma consulta protegida em dados de auditoria. Para alertas, agregue por
serviço, rota normalizada, método, status, região ou dependência, conforme o número de
combinações seja controlável.

## Alertas acionáveis

Cada alerta deve dizer:

- qual condição foi observada;
- qual serviço, operação e dependência estão envolvidos;
- qual impacto é provável;
- qual runbook deve ser seguido;
- quem recebe a notificação;
- quando o alerta deve se resolver ou ser silenciado.

Um alerta de crescimento de erros não deve apenas dizer que uma métrica dobrou. Ele
precisa mostrar o valor atual, a baseline, a quantidade de requisições, a rota
normalizada, a severidade e um link para diagnóstico. Se a causa for conhecida, o
alerta pode apontar para saturação, banco, deploy ou dependência correspondente.

Prometheus avalia a expressão e mantém o estado do alerta. O Alertmanager agrupa,
roteia, inibe e limita notificações. Não coloque lógica de agrupamento ou notificação
dentro da expressão de negócio se ela pertence ao roteador de alertas.

## Falsos positivos e falsos negativos

Alertar apenas por crescimento produz ruído quando o baseline é pequeno. Alertar apenas
por taxa produz falsos negativos em serviços de baixo tráfego. Alertar apenas por
quantidade absoluta mascara degradações em serviços de alto volume.

Teste as regras com tráfego normal, deploy, dependência lenta, queda completa, retorno
do serviço, baixa demanda e mudança de horário. Registre por que um limiar existe e
revise-o quando o SLO, o volume ou a arquitetura mudar.

## Relações

- [Observabilidade](index.md) diferencia sinais, ferramentas e perguntas.
- [RED](red.md) organiza rate, errors e duration.
- [Golden signals](golden-signals.md) adiciona tráfego e saturação à visão operacional.
- [Alertas acionáveis](alertas-acionaveis.md) trata severidade e resposta.
- [Regras do Prometheus](prometheus/rules.md) explica recording rules e alerting rules.
- [Cardinalidade](cardinalidade.md) trata o custo de labels de alta variedade.
- [Limitação adaptativa por falhas](../rede/rate-limiting/falhas-recorrentes.md)
  aplica uma resposta operacional a falhas repetidas.

## Fontes

- [Prometheus, alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
- [Prometheus, functions](https://prometheus.io/docs/prometheus/latest/querying/functions/)
- [OpenTelemetry, signals](https://opentelemetry.io/docs/concepts/signals/)
- [OpenTelemetry, metrics cardinality](https://opentelemetry.io/docs/concepts/signals/metrics/)
