# Comparação entre concorrência e paralelismo

Concorrência organiza várias atividades que podem avançar na mesma janela de
tempo. Paralelismo executa partes do trabalho fisicamente ao mesmo tempo. Os
conceitos se relacionam, mas respondem a perguntas diferentes: concorrência
trata composição, coordenação e progresso; paralelismo trata capacidade de
execução simultânea e ganho de throughput ou tempo.

## Diferenças principais

| Dimensão | Concorrência | Paralelismo |
| --- | --- | --- |
| Pergunta principal | Como várias atividades progridem? | Como partes executam ao mesmo tempo? |
| Recurso mínimo | Um scheduler capaz de intercalar atividades | Mais de uma unidade de execução útil |
| Exemplo | Event loop alternando requisições em um core | Dois cores processando dois lotes simultaneamente |
| Gargalo frequente | Locks, filas, dependências e backpressure | CPU, memória, sincronização e caminho crítico |
| Risco típico | Corrida, deadlock, starvation e replay | Contenção, false sharing e custo de coordenação |
| Métrica principal | Atividades pendentes, espera e progresso | Speedup, eficiência e throughput |

## Combinações possíveis

### Concorrente sem paralelo

Um event loop em um único core pode manter muitas requisições concorrentes.
Enquanto uma espera I/O, outra é executada. Há interleaving, mas não há duas
instruções da aplicação executando ao mesmo tempo.

### Concorrente e paralelo

Um pool pode manter várias tarefas ativas e distribuí-las em cores diferentes.
As tarefas são concorrentes porque precisam coordenar seu estado e são
paralelas quando partes delas executam simultaneamente.

### Paralelo com coordenação mínima

Um programa pode dividir um vetor em blocos independentes, processá-los em
cores distintos e combinar os resultados no final. A execução é paralela, mas
as fases de distribuição e redução ainda precisam de coordenação.

### Concorrência distribuída

Serviços em máquinas diferentes podem progredir independentemente mesmo sem
executar no mesmo instante. A comunicação tem atrasos e falhas parciais, então
o problema exige idempotência, timeouts, ordenação ou consenso conforme a
invariante.

## Escolha por tipo de trabalho

Para I/O, concorrência assíncrona ou threads leves podem manter muitas
operações em espera sem reservar uma thread de sistema para cada uma. O ganho
vem de não bloquear o recurso de execução, não de executar mais cálculo.

Para cálculo, paralelismo pode reduzir o tempo quando existem unidades de
execução disponíveis e o trabalho pode ser dividido. Mais threads do que a
capacidade útil podem aumentar overhead e piorar o resultado.

Para serviços, é comum combinar as duas abordagens: várias requisições
concorrentes, um limite de workers para controlar paralelismo, filas para
absorver picos e limites de conexão para não sobrecarregar dependências.

## Exemplo de configuração

Considere um serviço que recebe requisições e consulta um banco:

```text
concorrência: até 1.000 requisições aguardando ou executando
paralelismo: até 8 operações de CPU simultâneas
conexões do banco: até 32 conexões
```

Esses números não precisam ser iguais. A aplicação pode manter muitas tarefas
concorrentes, limitar o cálculo a oito workers e limitar o banco a 32
conexões. Se a fila crescer continuamente, o serviço precisa aplicar
backpressure, rejeitar ou atrasar novas tarefas, em vez de criar trabalho sem
limite.

## Como medir

Não conclua que uma aplicação precisa de paralelismo apenas porque há muitas
atividades concorrentes. Observe:

- tempo de CPU e tempo de espera;
- run queue e CPU steal em ambientes virtualizados;
- largura de banda e latência de memória;
- tamanho das filas e número de tarefas pendentes;
- throttling de cgroups;
- latência média e de cauda;
- speedup ao aumentar workers;
- erros, retries e saturação de dependências.

Se aumentar workers não reduz o tempo de uma carga de CPU, o gargalo pode ser
o caminho crítico, a memória ou a sincronização. Se aumenta throughput mas
piora p95 e p99, o limite de paralelismo está provavelmente acima da capacidade
do sistema ou da dependência.

## Relações

- [Concorrência](../../engenharia-software/concorrencia/modelos/concorrencia.md)
  explica coordenação e progresso intercalado.
- [Paralelismo](../../engenharia-software/concorrencia/modelos/paralelismo.md)
  explica execução simultânea e speedup.
- [Threads](../../engenharia-software/concorrencia/threads.md) explica uma forma de executar atividades.
- [Virtual threads](../../engenharia-software/concorrencia/virtual-threads.md)
  explica concorrência de I/O no runtime Java.
