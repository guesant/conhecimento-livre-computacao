# CPU virtual no Proxmox

O Proxmox VE usa QEMU e KVM para apresentar uma CPU virtual à VM. A VM não
recebe um core físico reservado apenas porque sua configuração mostra um certo
número de vCPUs. Ela recebe processadores virtuais que o host agenda sobre os
processadores lógicos disponíveis.

## Topologia da VM

Na configuração de uma VM, `sockets` e `cores` descrevem a topologia apresentada
ao sistema convidado. O número total de vCPUs é calculado pela combinação desses
campos. Essa topologia pode influenciar o scheduler convidado, NUMA virtual,
licenciamento e compatibilidade de aplicações.

O valor deve representar a necessidade da VM, e não a topologia física inteira
do host. Aumentar vCPUs sem paralelismo suficiente na aplicação pode elevar
overhead de scheduling, sincronização e contenção.

Uma configuração com `sockets: 2` e `cores: 4` apresenta oito vCPUs ao
convidado. Isso não significa que o host tenha dois sockets livres ou que cada
socket virtual esteja ligado a um socket físico específico. O hypervisor pode
agendar os threads das vCPUs em qualquer processador permitido pelo nó.

Em geral, uma VM pequena pode usar um socket virtual com o número necessário de
cores. Mais sockets virtuais podem ser necessários por compatibilidade do
sistema convidado, por licenciamento ou por uma topologia NUMA planejada, mas
não melhoram o desempenho por si só. Alguns softwares cobram por socket
visível, então a escolha da topologia também pode ter impacto financeiro.

## É possível configurar mais vCPUs que a máquina física?

Há duas perguntas diferentes.

É possível que a soma das vCPUs configuradas em várias VMs seja maior que a
capacidade física do host. Isso é sobrealocação de CPU, também chamada de
overcommit. Por exemplo, quatro VMs com quatro vCPUs cada podem coexistir em um
host com oito processadores lógicos. Quando todas trabalham ao mesmo tempo,
os threads das VMs competem pelo scheduler do host e cada uma recebe apenas a
parcela possível naquele instante.

Para uma VM individual, não se deve presumir que qualquer quantidade de vCPUs
acima da capacidade física será aceita. O guia do Proxmox documenta uma
proteção que impede iniciar uma VM com mais cores virtuais do que os
processadores fisicamente disponíveis no servidor. Portanto, a sobrealocação
normal deve ser feita entre VMs, não assumida como uma forma de criar uma VM
isolada com capacidade inexistente.

Mesmo quando uma configuração é aceita, vCPU não cria capacidade. Cada vCPU
normalmente corresponde a um thread de execução do QEMU no host. Se o host
estiver contendido, aumentam o tempo de espera, as trocas de contexto, o CPU
steal time observado pelo convidado e a latência de cauda.

## Sockets físicos, cores e threads

A topologia física pode ser resumida assim:

```text
processadores lógicos = sockets físicos x cores por socket x threads por core
```

Por exemplo, um host com um socket, oito cores e SMT de dois threads apresenta
até 16 processadores lógicos ao sistema operacional. Isso não significa que
16 workloads independentes sempre terão o desempenho de 16 cores físicos. Os
threads SMT compartilham unidades de execução e recursos de cache.

O Proxmox agenda vCPUs sobre os processadores lógicos disponíveis. `sockets` e
`cores` da VM descrevem a topologia exposta ao convidado, enquanto o host
continua tendo sua própria topologia física. Não é necessário que os números de
sockets coincidam.

## Limites relevantes

Não existe um único limite útil chamado "número máximo de vCPUs". Há limites
independentes:

1. o hardware e os processadores lógicos do host;
2. a capacidade do scheduler para manter os threads executando;
3. os limites aceitos por QEMU, Proxmox e pelo arquivo de configuração da VM;
4. o número de CPUs que o firmware e o sistema convidado conseguem inicializar;
5. limites de licença baseados em sockets ou cores;
6. a topologia NUMA e a capacidade de memória associada a cada domínio;
7. a política de live migration e o modelo de CPU escolhido.

O limite sintático de uma ferramenta não é uma recomendação de arquitetura.
Uma VM pode conseguir inicializar com muitos vCPUs e ainda apresentar pior
desempenho por custo de sincronização, interrupções, NUMA remoto e scheduler
do convidado.

## Limite e peso

O Proxmox oferece mecanismos distintos para limitar e priorizar CPU:

| Mecanismo | Papel |
| --- | --- |
| `cpulimit` | teto de tempo de CPU que a VM pode consumir |
| `cpuunits` | peso relativo quando VMs competem pelo host |
| afinidade | restringe os processadores em que o processo da VM pode executar |
| NUMA | apresenta ou organiza domínios de memória e CPU para VMs maiores |

Um peso maior não cria capacidade. Ele só aumenta a parcela relativa quando há
contenção. Um limite menor pode impedir a VM de usar toda a capacidade de seus
vCPUs, mesmo que eles estejam livres.

`cpulimit` restringe o tempo de CPU que a VM pode consumir no host. `cpuunits`
é um peso relativo entre workloads concorrentes. Uma VM com quatro vCPUs e
`cpulimit` equivalente a meio processador pode enxergar quatro CPUs, mas não
conseguir consumir quatro unidades de tempo simultaneamente. São controles
diferentes da quantidade de vCPUs apresentada ao convidado.

Sobrealocação é adequada para workloads com picos desencontrados, ambientes de
desenvolvimento e serviços que passam a maior parte do tempo ociosos. Deve ser
tratada com cuidado para bancos sensíveis a latência, sistemas de tempo real,
workers saturados continuamente e nós Kubernetes que já fazem sua própria
alocação lógica.

## Tipo de CPU

O tipo de CPU define quais recursos e flags o QEMU expõe ao convidado. O tipo
`host` pode oferecer mais recursos do processador físico, mas reduz a
portabilidade de live migration entre nós diferentes. Modelos compatíveis com
uma família comum de CPUs favorecem migração, ao custo de ocultar extensões
disponíveis apenas no host mais novo.

Escolha a política junto com o domínio de migração. Uma VM que nunca será
migrada pode priorizar recursos do host; uma VM que precisa circular entre nós
heterogêneos deve usar um modelo comum e validado.

## Pinning e NUMA

CPU pinning pode reduzir interferência e melhorar previsibilidade, mas transforma
capacidade dinâmica em capacidade rígida. Um pinning incorreto deixa vCPUs
concentrados em um único core, ignora SMT ou separa a CPU da memória que ela
acessa com menor latência.

NUMA virtual faz sentido quando a VM é grande o suficiente para atravessar
domínios de memória e o sistema convidado está preparado para tomar decisões
NUMA. Para VMs pequenas, a topologia virtual simples costuma produzir menos
surpresas.

## Containers LXC

Um container LXC no Proxmox compartilha o kernel do host e não recebe uma
topologia de hardware virtual igual a uma VM. A configuração de `cores`,
`cpulimit` e `cpuunits` controla o cgroup do container. O sistema dentro do
container pode observar um conjunto de CPUs conforme a configuração e a versão,
mas isso não transforma o container em uma máquina com sockets próprios.

## Relação com Kubernetes

Quando Kubernetes roda dentro de uma VM Proxmox, há duas camadas de decisão:

1. Proxmox agenda vCPUs sobre processadores do host.
2. Kubernetes agenda Pods sobre os recursos que o nó convidado anuncia.

Um Pod com `500m` recebe uma abstração de tempo de CPU dentro do nó convidado,
que já depende da capacidade e do limite da VM. Sobrevender vCPUs no Proxmox e
CPU no Kubernetes pode acumular contenção em ambas as camadas.

Um exemplo ajuda a separar os números. Um host com oito processadores lógicos
pode executar uma VM com quatro vCPUs e outra com quatro. Se o Kubernetes
receber essa VM como um nó de quatro CPUs, um request de `500m` representa meia
unidade do nó convidado, não meia CPU física garantida. O caminho completo é
host físico, thread do QEMU, vCPU da VM, CPU alocável do nó e request do Pod.

Não some requests como se eles fossem uma medição direta do consumo físico. O
scheduler do Kubernetes garante o modelo lógico do nó, enquanto o Proxmox
precisa garantir que a sobrealocação global ainda tenha latência e capacidade
aceitáveis. Monitore CPU steal, throttling, run queue, latência e saturação do
host antes de aumentar vCPUs.

## Fontes primárias

- [Proxmox VE Administration Guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.html)
- [QEMU/KVM virtual CPU models](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#qm_cpu)
- [Proxmox `pct` CPU limits](https://pve.proxmox.com/pve-docs/pct.1.html)
