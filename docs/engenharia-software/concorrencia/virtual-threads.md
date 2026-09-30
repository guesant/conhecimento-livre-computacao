# Virtual threads

Virtual threads são threads leves gerenciadas pelo runtime, e não uma relação
um para um com threads do sistema operacional. O nome é usado principalmente
para o modelo introduzido na plataforma Java e finalizado no JDK 21 pelo JEP
444.

O objetivo é permitir o estilo thread-per-request em aplicações com muita
concorrência de I/O sem criar uma thread de sistema operacional para cada
requisição. Uma virtual thread pode ficar suspensa enquanto espera rede, disco
ou outra operação bloqueante. O runtime libera a thread de plataforma que a
estava executando para carregar outra virtual thread.

## Modelo M:N

O scheduler da JVM associa muitas virtual threads a um conjunto menor de
platform threads. A platform thread atua como carrier enquanto a virtual thread
executa. A mesma virtual thread pode usar carriers diferentes ao longo da sua
vida, portanto não existe afinidade permanente entre ela e uma thread do
kernel.

O sistema operacional continua escalonando as platform threads sobre os
processadores lógicos disponíveis. Virtual threads não criam cores adicionais,
não aumentam a capacidade de execução de trabalho de CPU e não substituem o
dimensionamento de uma aplicação.

## Quando ajudam

Elas são adequadas quando uma tarefa passa boa parte do tempo esperando I/O e
é útil manter o código sequencial. É possível criar uma virtual thread por
tarefa sem usar um pool para limitar sua quantidade, enquanto os recursos
externos, como conexões de banco, sockets e filas, recebem limites próprios.

Elas não são uma solução para saturação de CPU. Milhões de tarefas que fazem
cálculo continuamente ainda competem por um número finito de processadores e
precisam de controle de paralelismo, filas ou um executor limitado.

## Pinning

Alguns caminhos impedem a virtual thread de se desmontar do carrier enquanto
estão bloqueados. O JEP 444 identifica como casos importantes código dentro de
`synchronized` e chamadas nativas. Um bloqueio de I/O durante esse pinning
ocupa a platform thread inteira e pode reduzir a escalabilidade.

Isso não significa que todo `synchronized` seja incorreto. Se a seção crítica
é curta e puramente em memória, o custo é diferente de manter I/O bloqueante
dentro dela. O diagnóstico deve observar eventos de pinning e revisar somente
os caminhos que realmente capturam carriers por períodos longos.

## Estado e limites

Thread locals continuam existindo, mas uma aplicação que cria muitas virtual
threads precisa avaliar o custo de cada estado associado. O número de tarefas
concorrentes também precisa respeitar limites de banco, APIs externas, memória,
descritores de arquivo e tempo de resposta.

O modelo não transforma operações bloqueantes de bibliotecas não cooperativas
em operações eficientes automaticamente. Verifique a implementação do driver,
o comportamento de chamadas nativas e o uso de locks antes de migrar uma carga
real.

## Kubernetes e Proxmox

Dentro de um container ou de uma VM, virtual threads continuam consumindo CPU
real quando executam código. O Kubernetes controla a quantidade de tempo de CPU
por cgroups e o Proxmox apresenta vCPUs ao sistema convidado. Nenhuma dessas
camadas conhece a intenção de uma virtual thread.

Se o container receber `100m`, a JVM poderá criar muitas virtual threads, mas o
tempo total de computação continuará limitado à cota de 0,1 CPU. O benefício
aparece quando as tarefas bloqueiam e liberam carriers, não quando todas fazem
cálculo ao mesmo tempo.

## Fontes primárias

- [JEP 444, Virtual Threads](https://openjdk.org/jeps/444)
- [Oracle Java 21, Virtual Threads](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html)
- [Kubernetes, resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
