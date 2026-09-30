# Nuvens de escala global

Nuvens de escala global operam uma infraestrutura de computação, rede,
armazenamento e serviços gerenciados em escala muito maior que um provedor de VPS
ou uma nuvem regional. O termo descreve a escala e o modelo operacional, não uma
garantia de que qualquer workload terá alta disponibilidade automaticamente.

A unidade de decisão é composta por conta ou organização, região, zona de
disponibilidade, identidade, rede virtual, quotas, serviços de dados e plano de
recuperação. A abstração reduz o trabalho de comprar e operar hardware, mas aumenta
a necessidade de governar permissões, custos, dependências e transferência de dados.

## O que comparar

AWS, Google Cloud e Microsoft Azure oferecem capacidades sobrepostas, mas não são
intercambiáveis em todos os detalhes. Compare:

- regiões, zonas e requisitos de residência dos dados;
- computação virtual, containers, Kubernetes e funções;
- redes virtuais, balanceadores, NAT, DNS e conectividade privada;
- bancos gerenciados, armazenamento de objetos, filas e caches;
- identidade, gestão de chaves, logs, métricas e resposta a incidentes;
- quotas, preços de transferência, suporte, SLA e exportação de dados;
- qualidade dos providers de IaC e dificuldade de migrar o workload.

Uma arquitetura distribuída entre regiões ou provedores não surge apenas de criar
duas máquinas. Ela exige replicação de dados, estratégia de DNS, observabilidade,
teste de recuperação, controle de consistência e uma decisão sobre o que acontece
quando a comunicação entre os ambientes falha.

## Páginas das plataformas

- [Amazon Web Services](../aws/index.md) explica a organização da conta, regiões,
  serviços e limitações da AWS.
- [Google Cloud](../gcp.md) explica a organização de projetos, regiões e serviços
  principais do Google Cloud.
- [Microsoft Azure](../azure.md) explica assinaturas, regiões, recursos e serviços
  principais do Azure.

## Modelos de composição

Um workload pequeno pode usar uma única região, uma rede privada, um banco gerenciado
e backup externo. Um sistema mais crítico pode separar contas ou projetos por
ambiente, distribuir réplicas por zonas e manter uma cópia de recuperação em outra
região. O ganho de disponibilidade precisa ser comparado ao custo de replicação,
saída de dados, operação e testes.

Também é possível manter a aplicação em uma nuvem de escala global e usar serviços especializados
de outra plataforma ou de um provedor de edge. Essa composição reduz acoplamento em
algumas camadas, mas aumenta o número de fronteiras de autenticação, contratos,
monitoramento e caminhos de falha.

## Relação com IaC

Providers de OpenTofu e Terraform permitem declarar recursos, mas não escondem as
diferenças entre as plataformas. A automação precisa tratar estado, locking, drift,
permissões, quotas e importação de recursos existentes. Leia as páginas de cada
plataforma antes de transformar uma composição em módulos reutilizáveis.

## Portabilidade em camadas

Portabilidade não é uma propriedade única. Um workload pode ser portável no
formato da imagem e dependente do serviço de banco, portável no código e preso ao
modelo de identidade, ou recuperável em outra região sem ser executável em outro
provedor.

Analise a portabilidade separando:

- artefato, como imagem OCI, pacote ou binário;
- configuração, como variáveis, secrets e políticas;
- estado, como banco, objetos, filas e certificados;
- rede, como DNS, endereços, balanceadores e conectividade;
- operação, como observabilidade, backup, quotas e escala;
- identidade, como usuários, roles, chaves e federação.

Uma migração só é real quando esses elementos podem ser reconstruídos e
validados. Exportar uma imagem Docker não exporta automaticamente permissões,
dados, rotas ou o contrato de recuperação.

## Falhas que atravessam provedores

Usar dois provedores não elimina automaticamente o domínio de falha. DNS,
autoridade de certificados, repositório de imagens, CI, identidade, CDN e
operador humano podem continuar sendo únicos. Também existe o risco de uma
falha de configuração ser replicada pelos módulos de IaC em todas as regiões.

Um desenho multi-cloud precisa definir qual camada realmente será independente,
qual consistência é aceitável e como o tráfego muda de destino. Sem essa
decisão, a segunda nuvem pode ser apenas uma cópia cara que compartilha os
mesmos secrets e o mesmo caminho de controle.

## Fontes primárias

- [AWS global infrastructure](https://docs.aws.amazon.com/global-infrastructure/latest/regions/)
- [Google Cloud regions and zones](https://cloud.google.com/compute/docs/regions-zones)
- [Azure regions](https://learn.microsoft.com/en-us/azure/reliability/regions-overview)
