# Akamai

Akamai opera uma plataforma distribuída de entrega de conteúdo, segurança, conectividade e computação. Sua identidade histórica está na CDN e na borda da internet, mas a oferta também inclui cloud compute, armazenamento, rede, containers e serviços adquiridos ou integrados à plataforma Akamai Cloud.

## Duas camadas que não devem ser confundidas

A camada de edge aproxima DNS, cache, proxy, entrega de conteúdo, proteção de aplicações e mitigação de ataques dos usuários. A camada de cloud compute fornece máquinas, rede, storage e execução mais próxima de uma IaaS tradicional. Elas podem ser combinadas, mas têm failure domains, métricas e responsabilidades diferentes.

## Quando faz sentido

Akamai é especialmente relevante quando latência global, distribuição de conteúdo, proteção de aplicações, absorção de tráfego e presença na borda são requisitos centrais. A camada de compute também pode atender APIs, containers e workloads que precisam de uma alternativa à concentração em uma única região hyperscale.

## Limitações e avaliação

Uma CDN não resolve automaticamente consistência de banco, processamento assíncrono ou armazenamento stateful. Cache incorreto pode servir dados antigos ou expor conteúdo privado. A equipe deve separar cache público, autenticação, invalidação, observabilidade e origem.

Compare também o modelo comercial, a cobertura de regiões, a integração com a origem, os custos de transferência e a maneira de automatizar o serviço. Para uma aplicação pequena sem necessidade de distribuição global, a plataforma pode introduzir mais componentes do que o necessário.

## Fontes primárias

- [Akamai Cloud Computing](https://techdocs.akamai.com/cloud-computing/docs/welcome)
- [Akamai Cloud Compute](https://techdocs.akamai.com/platform-basics/docs/cloud-compute)
- [Akamai developer documentation](https://techdocs.akamai.com/)
