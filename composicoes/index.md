# Composições de arquitetura

Ferramentas raramente operam isoladas. Esta área explica como responsabilidades de categorias diferentes se conectam e onde existe sobreposição.

Uma composição não documenta a configuração específica do `hl-infrastructure`. Ela descreve padrões reutilizáveis: quem produz, quem consome, qual interface conecta as peças, quais componentes são opcionais e quais combinações criam responsabilidades duplicadas.

## Plataforma Kubernetes

[Do tráfego do Pod à aplicação](kubernetes/rede-e-trafego.md) relaciona CNI, Service, Gateway/Ingress e service mesh.

## Entrega

[IaC, configuração e GitOps](entrega/iac-configuracao-gitops.md) mostra onde provisionamento, configuração de host e reconciliação de workloads começam e terminam.

## Observabilidade

[Pipelines de observabilidade](observabilidade/pipeline.md) separa instrumentação, coleta, armazenamento, consulta, visualização e alerta.

## Identidade e confiança

[Emissão e distribuição de confiança](seguranca/pki.md) relaciona CA, cert-manager/ACME, certificados e trust bundles.
