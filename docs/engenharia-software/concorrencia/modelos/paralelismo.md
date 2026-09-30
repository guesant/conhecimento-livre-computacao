# Paralelismo

Paralelismo é a execução física simultânea de partes de um trabalho. Ele
depende de recursos capazes de executar mais de uma operação ao mesmo tempo,
como múltiplos cores, unidades vetoriais, GPUs, máquinas ou dispositivos de
I/O independentes.

O objetivo costuma ser reduzir o tempo de uma tarefa, aumentar throughput ou
processar conjuntos grandes de dados. Criar mais atividades não garante
paralelismo: elas precisam encontrar recursos de execução disponíveis e o
trabalho precisa poder ser dividido sem que a coordenação consuma o ganho.

## Formas de paralelismo

### Paralelismo de dados

Uma mesma operação é aplicada a partes independentes de uma coleção. Somar
blocos de um vetor, aplicar um filtro a imagens ou transformar linhas de uma
tabela são exemplos. A redução final ainda precisa combinar os resultados e
definir como tratar ordem, precisão e erros.

### Paralelismo de tarefas

Operações diferentes são executadas ao mesmo tempo quando suas dependências
permitem. Um pipeline pode baixar dados, decodificar um lote e gravar outro em
recursos distintos. Se todas as tarefas dependem do mesmo lock, conexão ou
estrutura mutável, a aparência de paralelismo não produz ganho real.

### Paralelismo de instruções e vetorial

O processador pode executar instruções independentes em diferentes unidades
internas ou aplicar uma instrução a vários valores por SIMD. Compiladores e
bibliotecas podem explorar isso, mas dependências, branches e acesso irregular
à memória reduzem o ganho.

### Paralelismo em GPU

GPUs executam muitos elementos semelhantes com um modelo de throughput alto.
Elas são adequadas para operações com grande paralelismo de dados e acesso
previsível à memória. Transferir dados entre CPU e GPU, divergir entre threads
e sincronizar blocos pode tornar uma solução mais lenta que uma implementação
na CPU.

### Paralelismo distribuído

Processos em máquinas diferentes executam partes do trabalho e trocam dados
pela rede. A latência, a falha parcial, a serialização e a necessidade de
repetição passam a fazer parte do custo. Paralelismo distribuído não deve ser
confundido com simplesmente rodar réplicas independentes de um serviço.

## Dependências e caminho crítico

Um grafo de tarefas representa dependências entre etapas. Tarefas sem
dependência podem executar em paralelo, mas o caminho crítico continua
limitando o menor tempo possível da execução. Uma etapa sequencial longa pode
dominar a latência mesmo quando há muitos cores ociosos.

A lei de Amdahl expressa esse limite para uma carga com uma fração sequencial:

```text
speedup(N) = 1 / (s + (1 - s) / N)
```

`s` é a fração que não pode ser paralelizada e `N` é o número de unidades de
execução. Se 20% do trabalho for necessariamente sequencial, o speedup
teórico nunca ultrapassará 5, mesmo com infinitos cores, antes de considerar
overhead e outras limitações.

## Custos e problemas

Paralelismo pode reduzir tempo de CPU, mas também pode aumentar:

- sincronização e contenção;
- tráfego de memória e perda de localidade;
- false sharing entre cores;
- uso de cache e largura de banda;
- custo de criar, distribuir e combinar tarefas;
- consumo de energia;
- dificuldade de reproduzir erros;
- complexidade de cancelamento e tratamento de falhas.

Uma aplicação limitada por memória, disco ou rede não melhora apenas porque
recebe mais cores. Aumentar workers pode saturar a dependência mais cedo e
elevar a latência. O número de tarefas deve ser escolhido a partir do gargalo,
da capacidade e do objetivo de latência ou throughput.

## Paralelismo em VMs e containers

Uma VM recebe vCPUs que o hypervisor agenda sobre processadores do host. Um
container recebe uma cota ou peso de CPU por cgroups. Em ambos os casos, o
paralelismo visível pode ser maior que a capacidade física efetiva por causa de
overcommit.

No Kubernetes, um Pod com vários cores em seu request pode ser colocado em um
nó que anuncia essa capacidade lógica, mas o desempenho real ainda depende da
VM, do hypervisor e da contenção do host. Em Proxmox, vCPUs adicionais não
criam cores físicos e podem aumentar espera quando as VMs competem.

## Quando usar

Paralelize quando o trabalho possui partes independentes, o custo de dividir e
combinar é menor que o ganho e a dependência de execução tem capacidade para
atender as tarefas. Meça throughput, latência, uso de CPU, espera, memória e
I/O. Para uma aplicação interativa, um throughput maior pode não compensar uma
latência de cauda pior.

## Relações

- [Concorrência](concorrencia.md) trata o progresso intercalado de atividades.
- [Comparação entre concorrência e paralelismo](../../../comparacoes/engenharia-software/concorrencia-paralelismo.md) contrasta os dois conceitos.
- [Cores](../../../sistemas/cpu/cores.md) explica a topologia de execução da CPU.
- [CPU no Kubernetes](../../../kubernetes/recursos/cpu.md) explica requests, limits e throttling.
- [CPU virtual no Proxmox](../../../sistemas/virtualizacao/proxmox-cpu.md) explica vCPUs e sobrealocação.

## Fontes primárias

- [OpenMP specifications](https://www.openmp.org/specifications/)
- [NVIDIA CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [Linux kernel, scheduler](https://docs.kernel.org/scheduler/index.html)
