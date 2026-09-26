# Amazon Web Services

Amazon Web Services, AWS, é uma nuvem pública hyperscale. Ela oferece infraestrutura sob demanda e um catálogo amplo de serviços de computação, rede, armazenamento, bancos de dados, identidade, observabilidade, análise e inteligência artificial. A unidade operacional não é apenas uma máquina virtual: conta, região, zona de disponibilidade, identidade, rede virtual, políticas e serviços gerenciados formam o ambiente.

## Modelo de plataforma

EC2 representa computação virtual controlada pelo cliente. S3 representa armazenamento de objetos. RDS representa bancos relacionais gerenciados. EKS oferece Kubernetes gerenciado, e Lambda oferece execução orientada a eventos. Esses nomes são exemplos de famílias de serviço, não uma arquitetura obrigatória. Uma aplicação também pode combinar VPC, IAM, load balancer, filas, cache, observabilidade e serviços de dados.

Regiões são áreas geográficas independentes e zonas de disponibilidade são domínios separados dentro de uma região. A escolha precisa considerar latência, residência dos dados, preço, serviços disponíveis e estratégia de recuperação. Distribuir instâncias em zonas diferentes ajuda contra falhas locais, mas não substitui backup, teste de restauração ou planejamento para falha regional.

## Pontos fortes

AWS é especialmente forte quando a equipe precisa de um catálogo grande, integrações prontas, múltiplas regiões, serviços gerenciados maduros e um ecossistema amplo de parceiros e profissionais. Também é adequada quando a organização precisa separar contas, políticas, ambientes e responsabilidades em escala empresarial.

## Limitações e custos

A amplitude aumenta a carga cognitiva. IAM, redes, políticas, quotas, logs e cobrança exigem governança desde o começo. Custos podem surgir de transferência de saída, endereços, armazenamento, requisições, logs e serviços auxiliares, não apenas de instâncias. A adoção de muitos serviços específicos também pode elevar o custo de migração.

AWS não é automaticamente a melhor escolha para um site simples, um pequeno VPS ou uma equipe que não precisa de serviços gerenciados. Nesses casos, a complexidade operacional pode superar o benefício do catálogo.

## Critérios de avaliação

Antes de adotar AWS, valide a região necessária, o modelo de identidade, o orçamento de transferência, o plano de backup, as quotas, o suporte, a exportação de dados e a automação por IaC. Para ambientes críticos, separe contas e ambientes, use credenciais temporárias, aplique least privilege e trate o billing como parte da arquitetura.

## Fontes primárias

- [AWS overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
- [AWS global infrastructure](https://docs.aws.amazon.com/global-infrastructure/latest/regions/)
- [AWS products](https://aws.amazon.com/products/)
