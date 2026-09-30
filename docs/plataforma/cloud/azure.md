# Microsoft Azure

Microsoft Azure é uma nuvem pública hyperscale com serviços de computação, rede, armazenamento, bancos, identidade, integração, dados e desenvolvimento. Sua força histórica está na integração com o ecossistema Microsoft e em cenários empresariais híbridos, mas a plataforma também atende aplicações Linux, containers, Kubernetes e workloads multiplataforma.

## Modelo de plataforma

Virtual Machines oferecem infraestrutura virtual. Azure Kubernetes Service, AKS, gerencia o control plane do Kubernetes. App Service oferece uma plataforma para aplicações web, Azure Functions oferece execução orientada a eventos, Azure SQL fornece bancos gerenciados e Blob Storage armazena objetos. Entra ID, anteriormente Azure Active Directory, participa da identidade de usuários, workloads e recursos.

Regiões, pares de regiões, zonas de disponibilidade e regiões especializadas influenciam disponibilidade e recuperação. Uma região pode oferecer somente parte do catálogo. O desenho precisa distinguir replicação dentro da região, replicação entre regiões e backup independente.

## Pontos fortes

Azure é uma escolha natural quando identidade Microsoft, Active Directory, contratos empresariais, ferramentas de desenvolvimento, Windows Server, SQL Server ou integração híbrida fazem parte do ambiente. Também oferece um catálogo amplo para Linux e cloud native.

## Limitações e custos

A terminologia, a quantidade de serviços e as diferenças de SKU podem dificultar comparação e governança. Custos de transferência, licenças, armazenamento, logs e serviços gerenciados precisam ser medidos. Uma dependência profunda de identidade ou de produtos específicos pode aumentar o custo de saída.

## Critérios de avaliação

Avalie a integração com Entra ID, a região, a necessidade de licenciamento, a compatibilidade dos runtimes, a rede híbrida, as quotas e a política de exportação. Não trate Azure como sinônimo de Windows: a decisão deve partir do workload e das responsabilidades que a equipe realmente quer assumir.

## Fontes primárias

- [Azure regions overview](https://learn.microsoft.com/en-us/azure/reliability/regions-overview)
- [Azure products](https://azure.microsoft.com/en-us/products)
- [Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/)
- [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/)
