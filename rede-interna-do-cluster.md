# Rede interna do cluster

Dentro de um cluster Kubernetes, cada pod recebe seu próprio endereço IP, e pods em nós diferentes precisam conseguir se comunicar por esses endereços como se estivessem na mesma rede plana, mesmo que os nós físicos estejam em redes distintas. Resolver isso é responsabilidade de uma **CNI** (Container Network Interface): um plugin de rede, com uma especificação padronizada, que o Kubernetes invoca sempre que um pod é criado ou destruído, para conectar (ou desconectar) esse pod à rede do cluster. Kubernetes não vem com uma CNI própria; é uma peça que precisa ser escolhida e instalada separadamente, e existem várias implementações concorrentes (Calico, Flannel, Cilium, entre outras) com trade-offs diferentes de desempenho, funcionalidade e complexidade operacional.

## Rede overlay

Como os nós físicos podem estar em sub-redes diferentes, sem uma rota direta entre os endereços de pod, uma abordagem comum é criar uma rede overlay: os pacotes entre pods são encapsulados dentro de outro pacote, endereçado entre os nós físicos, e desencapsulados ao chegar no nó de destino. VXLAN é um dos protocolos de encapsulamento mais usados para isso. Esse encapsulamento tem um custo real de desempenho (cada pacote carrega um cabeçalho extra, e a CPU gasta ciclos encapsulando e desencapsulando), que implementações mais recentes tentam reduzir com técnicas como roteamento direto quando os nós estão na mesma rede física, ou aceleração via eBPF.

## Descoberta de serviço via CoreDNS

Um pod pode ser destruído e recriado a qualquer momento, e cada recriação normalmente resulta num IP novo; depender do IP de um pod específico para encontrá-lo, portanto, não funciona. Um objeto `Service` do Kubernetes resolve isso dando um nome estável e um IP virtual estável a um grupo de pods, com o próprio Kubernetes atualizando quais pods reais aquele nome aponta conforme eles nascem e morrem. CoreDNS é o servidor DNS que roda dentro do cluster e resolve esses nomes de serviço (`meu-servico.meu-namespace.svc.cluster.local`, por exemplo) para o IP virtual correspondente, permitindo que uma aplicação dentro do cluster encontre outra pelo nome, sem nunca precisar saber um IP de pod individual.

## Políticas de rede

Por padrão, o Kubernetes deixa todo pod falar com todo outro pod do cluster, sem restrição nenhuma; a CNI só resolve como um pacote chega ao destino, não se ele deveria chegar. Um objeto `NetworkPolicy` restringe isso: ele declara, por seletor de rótulo, de onde um pod pode receber tráfego e para onde pode enviar, e a CNI é quem aplica essa regra de verdade, porque é ela quem intercepta cada pacote entre pods.

Implementar `NetworkPolicy` é opcional para uma CNI, e nem toda CNI o faz sozinha; Flannel é um exemplo de quem não faz. O Cilium implementa a política nativa e ainda oferece um CRD próprio mais expressivo, a `CiliumNetworkPolicy`, que aceita regra por identidade do Kubernetes, por nome de DNS ou por camada 7, para protocolos como HTTP e Kafka.

Há uma sutileza que decide se a segmentação vale alguma coisa. A ausência de uma `NetworkPolicy` para um namespace, por si só, não bloqueia nada, apenas deixa de restringir, e um cluster pode passar a impressão de estar segmentado enquanto a maior parte do tráfego continua liberada. Uma configuração de segmentação séria inverte esse padrão, no Cilium com `policyEnforcementMode: always`, de modo que todo tráfego entre pods é negado até que uma política explícita o libere.

## Continue por aqui

A CNI usada neste cluster é o Cilium, cuja instalação está documentada na role `cilium` em [Ansible: as roles do bootstrap](../arquitetura/ansible.md), incluindo o `policyEnforcementMode: always` que nega tudo por padrão. As `CiliumNetworkPolicy` reais de cada namespace vivem em `argocd/apps/platform/network-policies`, uma allow list por serviço; [zero trust](zero-trust.md) discute o princípio geral por trás dessa segmentação, e [modelo de ameaças](../arquitetura/modelo-de-ameacas.md) explica como o tráfego de uma `Service` interage com o firewall do próprio node, um ponto onde a rede do cluster e a rede do sistema operacional se encontram.
