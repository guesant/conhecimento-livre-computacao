# Sockets

Um CPU socket é o encaixe e o pacote físico que conecta um processador à placa
principal. Em uma máquina com dois sockets, cada pacote pode conter vários
cores e processadores lógicos. O número de sockets não é o número de cores e
não é o número de threads de uma aplicação.

## Topologia

Uma forma útil de ler a máquina é:

```text
host
  sockets
    cores
      processadores lógicos por SMT
```

O socket pode possuir controlador de memória próprio, links para outros sockets
e dispositivos PCIe. Quando a memória é distribuída dessa forma, o host opera
como NUMA. A latência e a largura de banda dependem de onde a thread executa e
de onde a página de memória está alocada.

## Multi-socket

Mais de um socket aumenta a capacidade total, mas também introduz custos de
coerência de cache, acesso remoto à memória e coordenação entre schedulers.
Uma aplicação paralela pode escalar bem até saturar memória ou interconexão,
mesmo que ainda existam cores livres.

Afinidade de CPU e política de memória podem manter uma carga dentro do mesmo
domínio NUMA. Isso é útil para workloads sensíveis à latência, mas reduz a
flexibilidade do scheduler. O ganho precisa ser medido com a carga real.

## Virtualização

Uma VM não precisa enxergar a mesma quantidade de sockets que o host. O
hypervisor apresenta uma topologia virtual formada por sockets e cores virtuais,
e agenda os vCPUs sobre os processadores lógicos disponíveis no host.

Expor sockets virtuais demais pode afetar o comportamento de licenciamento,
NUMA e do scheduler do convidado. Para uma VM comum, uma topologia simples com
o número necessário de vCPUs costuma ser preferível. Use uma topologia NUMA
virtual quando a memória e o tamanho da VM justificarem a complexidade.

## Não confundir com socket de rede

Em redes, socket é uma abstração de comunicação associada a endereço, porta,
protocolo e estado de conexão. Este documento trata de CPU socket. O significado
precisa ser inferido pelo contexto, porque a palavra é usada nos dois domínios.

## Relações

- [Cores](cores.md) explica a unidade física dentro de um socket.
- [CPU virtual no Proxmox](../virtualizacao/proxmox-cpu.md) explica a topologia
  apresentada a uma VM.
- [CPU no Kubernetes](../../kubernetes/recursos/cpu.md) explica por que a API do
  Kubernetes usa unidades abstratas, não sockets físicos.

## Fontes primárias

- [Linux CPU topology](https://docs.kernel.org/admin-guide/cputopology.html)
- [NUMA memory policy](https://docs.kernel.org/admin-guide/mm/numa_memory_policy.html)
