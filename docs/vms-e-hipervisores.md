# Máquinas virtuais

Uma máquina virtual (VM) roda seu próprio kernel completo, sobre hardware virtualizado ou paravirtualizado por um hipervisor. KVM, integrado ao kernel Linux, é o hipervisor tipo 1 mais comum em infraestrutura self-hosted.

O hipervisor apresenta a cada VM uma visão de hardware, como CPU, memória, disco e rede, independente das demais VMs no mesmo host físico, e o kernel convidado dentro da VM não sabe, a não ser que seja informado explicitamente por paravirtualização, que está rodando sobre hardware virtualizado em vez de físico.

Um container é um modelo diferente: não tem kernel próprio nem hipervisor, e todos os containers de um host, junto com o próprio host, compartilham o mesmo kernel. Namespaces e cgroups do kernel Linux produzem a visão isolada e os limites de recursos de um container, sem nenhuma camada de virtualização de hardware entre o processo confinado e o kernel real.

Essa distinção de fundo, hipervisor com kernel próprio de um lado, kernel único compartilhado do outro, explica praticamente todas as diferenças práticas entre os dois modelos.

## O que cada modelo isola de fato

| Aspecto | Máquina virtual | Container |
| --- | --- | --- |
| Kernel | Próprio, por VM | Compartilhado com o host e com os demais containers |
| Isolamento de hardware | Virtualizado ou paravirtualizado pelo hipervisor | Nenhum, acesso direto ao kernel real do host |
| Superfície de ataque entre instâncias | Limitada ao hipervisor, se o kernel convidado for comprometido | O kernel do host inteiro, se um mecanismo de isolamento falhar |
| Diversidade de sistema operacional convidado | Qualquer SO suportado pelo hipervisor, como Windows sobre host Linux | Só binários compatíveis com o kernel do host |

Uma VM precisa inicializar um kernel completo e, tipicamente, um processo de init próprio antes de qualquer aplicação começar a rodar, o que custa de segundos a dezenas de segundos de boot e um piso de memória alocada medido em centenas de megabytes, independentemente de quão pequena seja a aplicação real dentro dela.

Um container não tem esse boot, porque iniciar um container é criar um processo e aplicar isolamento a ele, não inicializar um sistema operacional inteiro; o custo por instância se aproxima do custo real da própria aplicação. Essa diferença de custo é o que permite rodar dezenas ou centenas de containers em um host onde caberiam poucas VMs equivalentes, a chamada densidade de instâncias por host.

Comprometer uma aplicação dentro de uma VM e, a partir daí, alcançar o host físico exige em geral duas etapas: primeiro comprometer o kernel convidado daquela VM, depois encontrar uma falha de escape do próprio hipervisor, uma superfície de ataque historicamente pequena e intensamente escrutinada.

Comprometer uma aplicação dentro de um container e alcançar o host exige em geral só uma etapa, uma falha no próprio kernel do host, o mesmo kernel que o container já usa diretamente para toda chamada de sistema.

Essa diferença de uma camada a menos é o motivo pelo qual mecanismos que adicionam uma segunda camada de contenção a um container, como sandboxes de namespace ou tecnologias que interceptam chamadas de sistema ou executam o container dentro de uma VM leve, existem: eles tentam recuperar parte da separação que uma VM tem por padrão, sem pagar o custo total de boot e memória de uma VM completa.

Uma VM se justifica quando o requisito é isolamento forte entre cargas de trabalho de diferentes origens de confiança rodando no mesmo hardware físico, quando a carga de trabalho precisa de um sistema operacional diferente do host, ou quando a customização de kernel por carga de trabalho é um requisito real.

Um container se justifica quando as cargas de trabalho já compartilham compatibilidade de kernel, o caso comum de qualquer cluster Kubernetes, quando densidade e velocidade de inicialização importam mais que isolamento máximo por instância, e quando o modelo de confiança já assume que tudo rodando no mesmo host pertence ao mesmo nível de confiança.

Nenhum dos dois modelos substitui o outro de forma universal; a maioria dos ambientes de produção reais usa os dois juntos, VMs como unidade de isolamento entre clientes ou ambientes, containers como unidade de empacotamento e densidade dentro de cada VM.

## QEMU e KVM: emulação completa vs. virtualização acelerada

QEMU pode rodar uma máquina virtual de duas formas fundamentalmente diferentes, e essa diferença explica boa parte de como um hipervisor real se organiza na prática. Em modo de emulação pura, QEMU usa o TCG, um tradutor dinâmico de instruções: ele lê as instruções da arquitetura de CPU convidada, uma a uma, e as traduz em tempo real para instruções equivalentes da arquitetura do host.

Esse mecanismo é o que permite rodar uma VM com uma arquitetura de CPU completamente diferente da do host, por exemplo emular um sistema ARM inteiro sobre um host x86_64, ao custo de desempenho: cada instrução convidada passa por tradução antes de executar, o que torna essa via uma ou duas ordens de magnitude mais lenta que executar a mesma carga diretamente no hardware.

KVM é um módulo do kernel Linux que expõe diretamente as extensões de virtualização de hardware da CPU, como Intel VT-x ou AMD-V, para um processo em espaço de usuário.

Quando o host e o convidado compartilham a mesma arquitetura de CPU, o KVM permite que a maior parte das instruções do convidado execute diretamente no processador físico, sem tradução, com a CPU alternando entre modo host e modo convidado por meio de instruções de hardware dedicadas para isso. O resultado é desempenho próximo do nativo, tipicamente dentro de uma margem de alguns pontos percentuais da execução direta no host, muito diferente da penalidade pesada da tradução via TCG.

QEMU e KVM não competem entre si. QEMU sozinho, usando TCG, é um emulador completo mas lento; KVM sozinho é só um módulo de kernel que expõe extensões de virtualização, sem interface de usuário nem dispositivos virtuais próprios.

A combinação comum, e a que a maioria das instalações de virtualização em Linux usa por padrão, é QEMU como processo de espaço de usuário que emula os dispositivos periféricos da VM, como disco, rede, vídeo e USB, enquanto delega a execução da CPU e da memória ao KVM sempre que a arquitetura do convidado permite.

Nessa combinação, QEMU continua presente mesmo quando o KVM está ativo: ele fornece o modelo de dispositivos, o firmware de boot e a interface de gerência, mesmo não sendo mais ele quem executa cada instrução do convidado.

QEMU e KVM, por si só, expõem uma interface de linha de comando extensa e nenhuma abstração de mais alto nível para tarefas comuns, como definir uma VM de forma persistente ou gerenciar redes e armazenamento compartilhados entre várias VMs.

`libvirt` é a camada que resolve isso: um daemon e uma API que abstraem QEMU e KVM, e também outros hipervisores, definindo VMs como XML declarativo e gerenciando pools de armazenamento, redes virtuais e snapshots de forma consistente independentemente do hipervisor por trás.

| Ferramenta | Papel |
| --- | --- |
| libvirt | Daemon e API que abstraem QEMU, KVM e outros hipervisores |
| virt-manager | Interface gráfica mais comum sobre libvirt |
| virsh | Interface de linha de comando equivalente ao virt-manager |

Na prática, a maioria dos usuários que rodam QEMU e KVM em um desktop ou em um homelab nunca invoca o binário do QEMU diretamente: é libvirt quem monta e executa o comando completo por trás, a partir da definição declarativa da VM.

QEMU suporta várias formas de armazenamento para o disco virtual de uma VM, da mais simples, uma imagem bruta byte a byte idêntica ao conteúdo do disco, a formatos próprios com recursos adicionais.

O formato `qcow2` é o mais usado na prática, por reunir alocação fina, que faz o arquivo crescer conforme dados reais são escritos em vez de reservar o tamanho total declarado desde a criação; snapshots internos, armazenados dentro do próprio arquivo; encadeamento de camadas, em que uma imagem declara outra como base somente leitura e armazena só as diferenças; e compressão opcional por cluster.

O custo dessas vantagens é uma camada adicional de indireção em cada acesso a disco comparada a uma imagem bruta, o que pode se traduzir em alguma perda de desempenho de entrada e saída dependendo da carga.

## IOMMU e passthrough de dispositivos

Um dispositivo com capacidade de acesso direto à memória, ou DMA, escreve e lê memória do sistema diretamente, sem passar pela CPU a cada byte.

Sem nenhum mecanismo de controle entre o dispositivo e o barramento de memória, esse acesso é irrestrito: o dispositivo pode, por erro de programação, falha de hardware ou firmware malicioso, direcionar uma transferência DMA para qualquer endereço físico do sistema, incluindo memória do kernel ou de outros processos que nada têm a ver com aquele dispositivo.

É exatamente o mesmo problema que a unidade de gerenciamento de memória, ou MMU, resolve para processos em espaço de usuário, impedindo que um processo acesse memória fora do que lhe foi alocado, só que aplicado a dispositivos de hardware em vez de processos.

O IOMMU (Input-Output Memory Management Unit) é, na prática, o equivalente da MMU aplicado a dispositivos: uma unidade de hardware que intercepta os endereços que um periférico usa em uma transferência DMA e os traduz para endereços físicos permitidos, segundo uma tabela de tradução que o sistema operacional configura.

Um dispositivo sob controle do IOMMU não enxerga memória física diretamente, ele opera sobre um espaço de endereços que o IOMMU traduz e restringe, do mesmo jeito que um processo em modo usuário opera sobre endereços virtuais que a MMU traduz e restringe.

Intel VT-d e AMD-Vi são as duas implementações de hardware equivalentes desse mecanismo, uma por fabricante de CPU; o conceito e o propósito são os mesmos, mudando apenas o nome comercial e detalhes de habilitação na BIOS ou UEFI e no kernel.

Na prática, o IOMMU não isola dispositivos individualmente, ele isola grupos de dispositivos, conjuntos que precisam ser tratados como uma unidade porque compartilham o mesmo caminho de acesso ao barramento PCIe, por exemplo todos os dispositivos atrás da mesma ponte PCIe ou de um mesmo controlador.

Dois dispositivos no mesmo grupo de IOMMU não podem ser isolados um do outro pelo hardware disponível; se um deles for passado para uma VM, o outro precisa ir junto, mesmo que só um dos dois seja realmente necessário no convidado. Esse comportamento é o motivo prático mais comum pelo qual o passthrough de um dispositivo específico, uma GPU por exemplo, às vezes obriga a mover outros dispositivos aparentemente não relacionados do mesmo grupo junto para a VM.

VFIO (Virtual Function I/O) é o framework do kernel Linux que expõe um dispositivo PCI, já isolado por um grupo de IOMMU, como um driver de espaço de usuário seguro, o mecanismo que QEMU e KVM usam para passar esse dispositivo diretamente para dentro de uma VM.

Em vez de ser controlado pelo driver normal do kernel do host, o dispositivo é vinculado ao driver genérico `vfio-pci`, que o mantém disponível para ser atribuído a um processo QEMU específico; a partir desse ponto, o convidado dentro da VM enxerga e controla o dispositivo físico quase como se estivesse rodando diretamente sobre o hardware, com o IOMMU garantindo que o DMA da VM não escape para fora da memória alocada a ela.

O caso de uso mais comum que leva alguém a precisar entender IOMMU na prática, fora de um contexto de infraestrutura corporativa, é justamente esse: passar uma GPU dedicada para uma VM Windows ou Linux rodando sobre QEMU e KVM em um homelab ou desktop, para jogos ou uma aplicação que exige acesso quase nativo ao hardware gráfico.

## Continue por aqui

[Zones e jails](sistemas/virtualizacao/zones-jails.md) e [microVMs e sandboxes](sistemas/virtualizacao/microvms-e-sandboxes.md) cobrem o espectro de tecnologias que ficam entre um container comum e a VM completa descrita aqui. [Wine e compatibilidade](wine-e-compatibilidade.md) trata de um problema vizinho, rodar software Windows em Linux, mas sem nenhuma das formas de isolamento desta página. Para o índice geral desta seção, veja [aprender](index.md).
