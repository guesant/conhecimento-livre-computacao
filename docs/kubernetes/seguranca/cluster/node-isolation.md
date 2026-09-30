# Isolamento de nós

O isolamento de um workload depende de duas perguntas diferentes: em qual nó
ele pode ser executado e com quais outros componentes ele pode se comunicar.
Scheduling e rede devem ser projetados juntos, porque colocar um Pod em um nó
dedicado não bloqueia tráfego e uma NetworkPolicy não impede que um workload
privilegiado use recursos do próprio host.

## Posicionamento de workloads

Node selectors e node affinity selecionam nós por labels. Taints marcam um nó
como não elegível para Pods que não tenham a toleration correspondente.
Topology spread constraints distribuem réplicas entre domínios como nós,
zonas ou regiões. O objetivo pode ser disponibilidade, isolamento de dados,
separação de workloads sensíveis ou uso de hardware específico.

Labels usadas para segurança precisam ser protegidas. Se uma identidade puder
alterar livremente a label que identifica um nó isolado, ela pode influenciar o
scheduler e escapar da intenção da separação. Node authorizer e
NodeRestriction ajudam a impedir que o Kubelet se atribua propriedades que não
deveria controlar.

Um padrão de isolamento deve definir:

- quem pode aplicar ou remover labels e taints;
- quais Pods toleram o taint;
- o que acontece quando o nó dedicado fica indisponível;
- se a afinidade é obrigatória ou apenas uma preferência;
- como réplicas são distribuídas quando há poucos nós;
- qual volume, CNI e runtime existem naquele grupo.

## NetworkPolicy

NetworkPolicy expressa tráfego permitido por direção. Uma policy de ingress
restringe quem pode conectar ao Pod. Uma policy de egress restringe os destinos
que o Pod pode alcançar. Policies aplicáveis são combinadas de forma aditiva,
portanto uma regra ampla em outro objeto pode desfazer a expectativa de
isolamento de uma regra estreita.

Uma estratégia usual é começar com default deny por direção e liberar DNS,
tráfego entre serviços necessários, acesso a dependências e egress explícito.
O CNI precisa implementar a API e as exceções para `hostNetwork`, tráfego de
host, NodePort, load balancer e interfaces externas devem ser testadas no
ambiente real.

NetworkPolicy não autentica a aplicação, não substitui TLS, não define
permissões do API server e não é um firewall universal do nó. Um atacante com
acesso privilegiado ao host pode estar fora do domínio que a policy controla.

## Módulos do kernel

Um processo sem privilégio pode provocar a carga de alguns módulos do kernel
ao tentar usar determinadas famílias de sockets. Em um nó Kubernetes isso
pode introduzir uma superfície que não era necessária ao workload. A orientação
oficial usa como exemplo o bloqueio de DCCP e SCTP pelo mecanismo de módulos,
com uma regra em `/etc/modprobe.d/kubernetes-blacklist.conf`:

```text
blacklist sctp
blacklist dccp
```

O arquivo precisa ser aplicado pela imagem e pelo processo de provisionamento
do nó, não criado manualmente em um único nó sem controle de configuração.
Depois, verifique quais módulos já estão carregados e como o runtime trata
capacidades e containers privilegiados.

Um LSM como SELinux pode negar requisições de carregamento de módulo por meio
de uma policy adequada. Isso não remove módulos já carregados nem impede um
componente que recebeu privilégio suficiente de alterar a própria proteção.
Blacklists, LSM, capabilities e ausência de `privileged` são controles
complementares.

## Host access e recursos privilegiados

`hostPath`, `hostNetwork`, `hostPID`, `hostIPC`, dispositivos, mounts de
`/proc` e `/sys`, capabilities de administração e acesso ao socket do runtime
podem transformar um Pod em uma extensão do nó. O controle deve considerar
também init containers, ephemeral containers, Jobs de manutenção e operadores.

Se um agente de monitoramento precisa ler o host, restrinja a ServiceAccount,
o Namespace, as imagens, os volumes, os nós e o processo de atualização. Não
permita que a necessidade de observabilidade se torne uma ClusterRole ampla
ou um Pod privilegiado reutilizável por aplicações.

## Relações

- [NetworkPolicy](../../networking/network-policy.md) descreve o objeto de
  política de rede.
- [CNI](../../networking/cni.md) descreve a camada que implementa a rede.
- [Taints e tolerations](../../scheduling/taints-tolerations.md) controlam
  elegibilidade de scheduling.
- [Affinity](../../scheduling/affinity.md) e [topology spread](../../scheduling/topology-spread.md)
  tratam distribuição e afinidade.
- [Capabilities](../linux-capabilities.md) e [seccomp](../seccomp.md)
  reduzem operações disponíveis ao processo.

## Fontes primárias

- [Assign Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Configure a SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Seccomp](https://kubernetes.io/docs/reference/node/seccomp/)
