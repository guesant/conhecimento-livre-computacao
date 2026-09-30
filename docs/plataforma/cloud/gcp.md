# Google Cloud

Google Cloud Platform, GCP, é a nuvem pública da Google. Ela oferece computação, armazenamento, rede, bancos de dados, análise de dados, inteligência artificial, Kubernetes gerenciado e plataformas para execução de aplicações. A organização do ambiente envolve projetos, identidades, redes, regiões, zonas, quotas e serviços com responsabilidades diferentes.

## Modelo de plataforma

Compute Engine oferece máquinas virtuais. Google Kubernetes Engine, GKE, oferece Kubernetes gerenciado. Cloud Run executa containers em uma plataforma orientada a requisições, Cloud SQL fornece bancos relacionais gerenciados e Cloud Storage fornece objetos. BigQuery é um serviço analítico, não um banco transacional genérico. A diferença entre essas abstrações precisa orientar o desenho da aplicação.

Regiões e zonas possuem propriedades de latência, disponibilidade e catálogo diferentes. Alguns serviços são regionais, zonais ou globais. Uma arquitetura que usa um recurso global pode ainda depender de dados regionais, quotas ou serviços sem a mesma cobertura geográfica. A documentação de cada serviço deve ser consultada antes de assumir portabilidade.

## Pontos fortes

GCP costuma ser uma opção forte para analytics, machine learning, workloads Kubernetes, redes globais e equipes que valorizam automação por APIs. A integração entre projetos, IAM, observabilidade e serviços de dados pode reduzir trabalho de plataforma quando as fronteiras entre os serviços são bem definidas.

## Limitações e custos

O catálogo continua sendo complexo e o preço efetivo depende de região, uso, transferência, armazenamento, commitments e serviços auxiliares. Um desenho baseado em APIs específicas pode aumentar o custo de migração. Kubernetes gerenciado reduz a operação do control plane, mas não elimina problemas de workloads, rede, storage, segurança e observabilidade.

## Critérios de avaliação

Avalie a região, o tipo de dado, a integração com identidade, o modelo de rede, as quotas, os limites de cada runtime e a forma de exportar dados. Para aplicações pequenas, compare o custo e a carga operacional de GCP com uma VPS ou plataforma mais simples. Para analytics, Kubernetes ou serviços globais, compare capacidades concretas e não apenas o nome do provedor.

## Fontes primárias

- [Google Cloud products](https://cloud.google.com/products)
- [Google Cloud regions and zones](https://cloud.google.com/compute/docs/regions-zones)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
- [Cloud Run](https://cloud.google.com/run)
