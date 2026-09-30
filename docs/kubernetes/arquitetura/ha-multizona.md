# Alta disponibilidade multizona no Kubernetes

Alta disponibilidade multizona tenta manter o control plane funcional quando
uma zona ou um datacenter inteiro falha. Ela não é apenas adicionar Nodes ao
cluster: exige distribuir os membros do consenso, oferecer um endpoint estável
para a API e manter storage, rede e backups fora do mesmo domínio de falha.

## Componentes

Servidores distribuídos entre zonas reduzem a chance de a falha física de uma
zona remover a maioria do control plane. O custo é a latência entre membros do
consenso, que aparece em cada escrita que precisa de confirmação da maioria.

Um load balancer multi-zona fornece um endereço estável para kubeconfigs e
agentes e remove endpoints sem saúde da rotação. Ele não substitui o quorum do
datastore, porque apenas distribui conexões.

Um datastore externo pode separar o ciclo de vida do K3s do ciclo de vida do
consenso, mas cria outro serviço crítico com seu próprio backup, replicação e
procedimento de recuperação.

## Limites

Alta disponibilidade reduz indisponibilidade por falha de infraestrutura. Ela
não substitui backup, não recupera exclusões lógicas e não corrige um manifesto
inválido. Para clusters pequenos, três servidores com quorum local e backup
testado podem ser uma solução melhor que uma topologia multizona mais cara e
complexa.

## Relações

- [Quorum](../control-plane/quorum.md) explica a maioria necessária.
- [Datastore do K3s](../control-plane/datastore.md) explica as opções de
  backend.
- [Topologias K3s multinó](../../topologias-rede-e-falhas-em-k3s-multino.md)
  detalha servidores, agentes e manutenção.
