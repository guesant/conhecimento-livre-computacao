# Self-stabilization

Self-stabilization, ou autoestabilização, é uma propriedade de tolerância a falhas em que um sistema distribuído consegue alcançar um estado legítimo depois de começar em qualquer estado permitido ou sofrer uma falha transitória. O sistema não precisa estar correto imediatamente, mas deve convergir em tempo finito e permanecer correto enquanto as hipóteses do algoritmo forem mantidas.

O modelo é especialmente útil quando não é possível conhecer ou limpar todo o estado corrompido. Em vez de depender de uma recuperação perfeita, cada processo executa regras locais que eliminam combinações inválidas até que o conjunto alcance uma configuração legítima.

## Legitimidade e convergência

Uma especificação define quais estados são legítimos e quais transições são permitidas. A propriedade de convergência exige que, a partir de qualquer estado inicial, a execução alcance um estado legítimo em número finito de passos. A propriedade de fechamento exige que, depois de legítimo, o sistema permaneça no conjunto de estados legítimos enquanto as falhas e o ambiente respeitarem as hipóteses.

Essas propriedades não significam que todo processo individual conheça o estado global nem que a convergência seja rápida em qualquer topologia. O tempo de estabilização depende do algoritmo, do número de processos, da conectividade, do escalonador, da perda de mensagens e do modelo de falhas.

## Falhas transitórias e permanentes

Uma falha transitória corrompe estado ou comunicação e depois deixa de ocorrer. É o cenário clássico: memória alterada, mensagem duplicada, reinício parcial ou uma combinação impossível de variáveis. O algoritmo precisa recuperar sem uma intervenção externa que reescreva todo o estado.

Uma falha permanente continua violando as hipóteses, como um processo que nunca volta, um enlace permanentemente partido ou um adversário que modifica o estado sem parar. Autoestabilização sozinha não garante recuperação nesse cenário. É preciso modelar falhas, detecção, reconfiguração, redundância ou um mecanismo de consenso compatível.

## Exemplo conceitual

Em um anel de processos que precisa manter um token único, uma corrupção pode produzir zero tokens ou vários tokens. Um protocolo autoestabilizante permite que processos comparem estados locais e criem, removam ou encaminhem tokens conforme regras determinísticas até que reste exatamente uma circulação legítima.

O exemplo mostra a diferença entre reiniciar todo o sistema e recuperar a partir de um estado arbitrário. Também mostra por que uma prova precisa declarar o tamanho da topologia, o modo de comunicação, a justiça do escalonador e a quantidade de estados disponíveis.

## Relação com outros mecanismos

Autoestabilização não é o mesmo que alta disponibilidade. Alta disponibilidade busca manter o serviço acessível; autoestabilização busca alcançar e permanecer em um conjunto legítimo de estados. Um sistema pode estar disponível e incorreto, ou correto e temporariamente indisponível durante a recuperação.

Também não é o mesmo que consenso. Consenso escolhe um valor ou decisão comum sob um modelo de falhas. Um protocolo pode usar consenso como parte da recuperação, mas uma regra autoestabilizante pode ter um objetivo diferente, como estabelecer uma árvore, um líder, um relógio ou uma coloração válida.

Reconciliação periódica, controllers declarativos e sistemas de desired state possuem uma intuição semelhante: comparar o estado observado com uma condição desejada e aplicar correções repetidamente. Isso não torna todo controller formalmente autoestabilizante. Para usar o termo com precisão, é necessário especificar o conjunto legítimo, as transições, as hipóteses e a prova de convergência.

## Variantes

Um sistema silenciosamente autoestabilizante chega a um estado em que os processos deixam de produzir movimentos, embora o estado continue legítimo. Em sistemas com mudanças contínuas, a execução pode permanecer legítima sem ficar silenciosa.

Self-stabilization pode ser combinada com reconfiguração, mobilidade, segurança e recuperação de topologia. Em cada extensão, a especificação precisa dizer quais propriedades continuam preservadas durante uma mudança. A noção de superstabilization, por exemplo, acrescenta condições sobre o caminho de recuperação durante uma mudança no ambiente.

## Aplicações e limites operacionais

As ideias aparecem em protocolos de sincronização, eleição, manutenção de árvores, roteamento, sensores, redes móveis, sistemas de cluster e componentes que reconciliam estado. Em produção, a inspiração costuma aparecer como reconciliação, resync, repair, anti-entropy e reeleição.

Não basta adicionar um loop que "tenta corrigir". Um mecanismo real precisa de limites, backoff, observabilidade, proteção contra flapping, autoridade para mudanças e uma forma de distinguir estado atrasado de estado inválido. Caso contrário, a própria recuperação pode gerar carga, conflitos ou oscilações.

## Relações

- [Sistemas distribuídos](sistemas-distribuidos.md)
- [Reconciliação e GitOps](../entrega/gitops.md)
- [Resiliência](../confiabilidade/resiliencia.md)
- [Idempotência](../confiabilidade/idempotencia.md)
- [Colaboração distribuída e local-first](../dados/colaboracao/index.md)

## Fontes

- [Dijkstra, Self-stabilizing systems in spite of distributed control](https://doi.org/10.1145/361179.361202)
- [Edsger Dijkstra, versão reproduzida do artigo](https://www.cs.uni.edu/~adberns/papers/Dijkstra.pdf)
- [CRDTs, estabilização e segurança em sistemas distribuídos](https://pages.lip6.fr/Marc.Shapiro/papers/CRDTs-beatcs-2011-06.pdf)
- [Self-stabilization, Wikipedia](https://en.wikipedia.org/wiki/Self-stabilization)
