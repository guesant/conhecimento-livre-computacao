# Metadados de cloud

Provedores de cloud costumam disponibilizar uma API de metadados a partir da
instância. Ela pode fornecer identidade da máquina, configuração de rede,
dados de provisionamento e, quando a role da instância permite, credenciais
temporárias para serviços do provedor. Dentro de um cluster, isso significa
que um Pod comprometido pode tentar alcançar uma fonte de credenciais que não
foi criada para aquela aplicação.

O problema não é específico de um endpoint ou de um provedor. A propriedade
importante é que o nó possui uma identidade de infraestrutura e o tráfego até
ela pode atravessar interfaces, bridges, NAT ou o caminho de rede do host.
`hostNetwork` e componentes privilegiados podem escapar de parte do isolamento
oferecido pela rede de Pods.

## Princípio de menor privilégio

A role atribuída ao nó deve permitir somente as operações que os componentes
do cluster realmente precisam. Não coloque credenciais de aplicação na role
da instância apenas porque todos os Pods conseguem alcançar o nó. Aplicações
que precisam acessar cloud devem usar uma identidade vinculada ao workload,
quando o provedor e o CNI oferecerem essa integração, com audience, escopo e
expiração adequados.

Uma role de nó ampla torna a NetworkPolicy uma segunda barreira de alto valor,
mas não uma autorização de aplicação. Se uma policy for removida, se o CNI
for contornado por `hostNetwork` ou se um Pod ganhar acesso ao host, todas as
permissões da role do nó podem se tornar disponíveis.

## Proteções de rede

Controle o caminho até o endpoint de metadados no nível em que o provedor
oferece suporte. Dependendo do ambiente, isso pode envolver firewall do host,
regras do CNI, NetworkPolicy de egress, configuração do agente de metadata e
restrições de interface. Bloquear somente o endereço em uma policy de Pod não
é suficiente se o tráfego passar por um proxy ou por uma interface que a
policy não cobre.

Uma policy de egress deve permitir apenas dependências explícitas. DNS deve
continuar funcionando por meio do serviço de DNS do cluster, e o caminho até
o endpoint de metadados deve ser testado com um Pod normal e com um Pod que
possua `hostNetwork`, porque os dois caminhos podem ser diferentes.

## Dados de provisionamento

User data, cloud-init e dados de bootstrap são frequentemente tratados como
configuração, mas podem conter tokens, senhas, chaves ou URLs de onboarding.
Não use esse mecanismo para persistir segredos de aplicação. Caso o provedor
precise de um bootstrap secret, defina validade curta, rotação, proteção de
logs e remoção depois do primeiro uso.

Também é preciso considerar snapshots, imagens, discos e logs do agente de
provisionamento. Um segredo removido do arquivo atual pode continuar em uma
imagem ou em um backup. O ciclo de vida da credencial deve incluir a origem,
as cópias temporárias e a revogação.

## Verificação

Uma revisão deve responder:

- quais Pods podem alcançar o endpoint de metadados;
- quais roles estão atribuídas aos nós;
- quais workloads usam `hostNetwork` ou privilégios de host;
- se o CNI aplica egress de forma real;
- se o provedor exige headers, tokens de sessão ou versões específicas;
- como uma credencial temporária é revogada ou substituída;
- se os testes de segurança diferenciam nó, Pod e container.

Não faça um teste destrutivo contra a API de metadados. Use uma identidade de
teste com permissões vazias ou mínimas, registre a rota e confirme que uma
aplicação sem necessidade de cloud não consegue alcançar o serviço.

## Relações

- [Isolamento de nós e rede](node-isolation.md) trata NetworkPolicy,
  `hostNetwork` e fronteiras do host.
- [ServiceAccount](../../core/serviceaccount.md) trata identidade dentro do
  cluster.
- [Secrets](../../core/secret.md) trata o objeto de dados sensíveis do
  Kubernetes, que não deve ser confundido com a API de metadados.

## Fonte primária

- [Securing a Cluster, cloud provider security](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
