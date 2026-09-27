# Cores

Um core é uma unidade de execução dentro de um pacote de CPU. Ele possui
recursos próprios para buscar, decodificar e executar instruções, embora possa
compartilhar cache, controlador de memória ou outros componentes com os demais
cores do mesmo processador.

O número de cores físicos informa quanta execução paralela o chip pode sustentar
em condições ideais, mas não determina sozinho o desempenho. Frequência,
microarquitetura, tamanho de cache, largura de memória, vetorização, consumo e
o tipo de carga também importam.

## Cores físicos e processadores lógicos

Um sistema operacional normalmente enxerga cada contexto de execução como um
processador lógico. Um core físico pode expor um ou mais processadores lógicos
por SMT, chamado Hyper-Threading em algumas gerações da Intel.

SMT permite que o core aproveite unidades que estariam ociosas quando uma
thread espera por memória ou possui dependências. Dois processadores lógicos no
mesmo core não equivalem a dois cores físicos: compartilham recursos internos e
podem disputar largura de execução, cache e energia.

Por isso, uma topologia pode ser descrita como:

| Nível | Significado |
| --- | --- |
| Socket | pacote físico instalado na placa |
| Core | unidade física de execução dentro do pacote |
| Thread lógico | contexto de execução exposto pelo core ao sistema |

Essa hierarquia é diferente de uma thread de aplicação. A aplicação cria
threads de software; o sistema operacional as agenda em processadores lógicos.

## Afinidade e NUMA

Em uma máquina com vários sockets, cada grupo de cores pode estar mais próximo
de uma parte da memória. Esse modelo é chamado NUMA. Acesso à memória local
costuma ter menor latência que acesso à memória ligada a outro socket.

Afinidade de CPU pode reduzir migrações e melhorar localidade de cache, mas
fixar tarefas demais pode deixar cores ociosos enquanto outros ficam saturados.
Use a topologia observada pelo sistema e meça antes de impor pinning.

## Cores heterogêneos

Processadores modernos podem combinar cores de desempenho e cores de eficiência.
Eles não têm necessariamente a mesma frequência, largura de execução ou custo
energético. O scheduler e o sistema operacional podem preferir um tipo conforme
a carga, a política de energia e a prioridade.

Uma contagem de cores sem a distinção entre tipos pode esconder diferenças
importantes entre máquinas. Em virtualização, o convidado pode receber uma
topologia simplificada e não enxergar a topologia física completa.

## Relações

- [Sockets](sockets.md) explica os pacotes físicos e os domínios NUMA.
- [CPU](cpu.md) descreve o componente que contém os cores.
- [Threads](../../engenharia-software/concorrencia/threads.md) explica como o
  software usa processadores lógicos.
- [CPU virtual no Proxmox](../virtualizacao/proxmox-cpu.md) explica como essa
  topologia é apresentada a uma VM.

## Fontes primárias

- [Linux CPU topology](https://docs.kernel.org/admin-guide/cputopology.html)
- [lscpu(1)](https://man7.org/linux/man-pages/man1/lscpu.1.html)
