# NACL

Network Access Control List, NACL, é uma lista de regras associada a uma subnet
da Amazon VPC. Ela controla tráfego de entrada e saída no limite da subnet,
antes de o pacote alcançar recursos como interfaces de instâncias, tasks ou
nodes. NACL é uma camada diferente de security group, route table e firewall
do workload.

## Stateless

NACL é stateless. Uma regra que permite uma conexão de entrada não permite
automaticamente o tráfego de resposta; o caminho de volta precisa de regra
explícita, incluindo portas efêmeras quando aplicável. Essa característica é
fonte comum de timeouts que parecem falha de aplicação.

As regras são numeradas e avaliadas em ordem. A primeira correspondência vence
e o tráfego que não encontra uma permissão é negado pela regra final implícita.
Alterar um número menor pode mudar o resultado de várias regras sem alterar a
regra que parecia relevante.

## NACL e load balancers

Um fluxo ALB ou NLB atravessa subnets de entrada e subnets de targets. O cliente
pode ser visto como um endereço público, privado ou um proxy anterior; o target
pode receber um endereço do load balancer, do node ou do cliente conforme o
produto e os atributos. NACL deve liberar o caminho real de ida e volta, mas não
deve ser usado para interpretar `X-Forwarded-For` ou PROXY protocol.

Security groups são stateful e associados a interfaces ou recursos; NACLs são
stateless e associados a subnets. Usar NACL como única autorização de uma API
torna a regra ampla e dificulta o diagnóstico. Combine NACL, security groups,
NetworkPolicy e autenticação da aplicação.

## Diagnóstico

Compare rota, subnet, NACL de origem e destino, security groups, portas efêmeras,
IPv4 e IPv6. Logs de VPC Flow Logs podem mostrar `REJECT`, mas não provam que o
processo recebeu o pacote. Teste cada direção e documente qual interface de cada
load balancer está em cada subnet.

## Relações

- [VPC AWS](index.md) apresenta redes e subnets.
- [Balanceadores AWS](load-balancing.md) mostra listeners e target groups.
- [Firewall](../../../rede/firewall/index.md) compara camadas de filtragem.

## Fontes primárias

- [Network ACLs da VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
