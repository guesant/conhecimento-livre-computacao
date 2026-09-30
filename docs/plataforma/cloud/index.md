# Nuvem

Computação em nuvem é a entrega sob demanda de capacidade computacional, armazenamento, rede e serviços gerenciados. Hospedagem web, VPS, plataforma de aplicações e rede de borda podem usar a mesma infraestrutura física, mas oferecem responsabilidades e graus de controle diferentes. Por isso, comparar apenas o preço mensal de um recurso não é suficiente.

## Categorias

- Nuvem e infraestrutura reúne compute, armazenamento, rede e serviços
  gerenciados.
- Hospedagem gerenciada reduz a responsabilidade operacional, mas também limita
  o controle sobre o sistema.
- Plataformas de aplicações concentram build, deploy, runtime e integrações.
- Edge e entrega aproximam DNS, CDN, proxy, segurança e funções do usuário.

## Modelos de serviço

Em uma infraestrutura como serviço, o fornecedor entrega máquinas virtuais, discos, redes e APIs. O cliente ainda administra o sistema operacional, a aplicação, a atualização e boa parte da segurança. É o modelo típico de AWS EC2, Google Compute Engine, Azure Virtual Machines, Akamai Cloud, Magalu Cloud, QNAX e VPS de provedores de hospedagem.

Uma plataforma como serviço esconde parte do sistema operacional e concentra o fluxo de deploy. Vercel e Heroku são exemplos com propostas diferentes: Vercel privilegia frontends, funções e entrega na borda; Heroku privilegia o ciclo de vida de aplicações web com buildpacks, dynos e add-ons. A redução do trabalho operacional vem acompanhada de restrições de runtime e maior dependência da plataforma.

Plataformas de deploy autohospedadas, como Coolify, Dokploy e CapRover, oferecem uma experiência
parecida com PaaS sobre servidores escolhidos pelo operador. Elas reduzem o trabalho de configurar
builds, proxy e certificados, mas não removem a responsabilidade por hosts, armazenamento,
credenciais, backups e recuperação. [PaaS autohospedado e plataformas de deploy](paas-autohospedado-e-deploy.md)
explica essa fronteira.

Hospedagem gerenciada e compartilhada abstraem ainda mais a operação. Hostinger, Hostnet e HostGator oferecem produtos para sites, CMS, e-mail, WordPress, cloud hosting e VPS. Eles podem ser adequados para uma aplicação simples, mas não devem ser avaliados como se fossem uma nuvem hyperscale com os mesmos controles de rede, identidade e automação.

Provedores de edge e rede, como Cloudflare e Akamai, ficam entre a aplicação e o usuário. DNS, CDN, proxy reverso, WAF, mitigação de DDoS, funções na borda e conectividade podem reduzir latência e exposição, mas não substituem automaticamente um banco de dados, um worker ou uma plataforma de execução stateful. Cloudflare Pages, Workers e Tunnel representam problemas diferentes dentro desse espaço: publicação, execução e conectividade.

## Dimensões de comparação

Uma escolha adequada considera, pelo menos, estas dimensões:

- controle sobre o sistema operacional, a rede e o armazenamento;
- regiões, latência, residência dos dados e requisitos regulatórios;
- serviços gerenciados de banco, Kubernetes, filas, observabilidade e identidade;
- disponibilidade, recuperação, backups, suporte e termos de SLA;
- preço de computação, armazenamento, transferência de saída e serviços acessórios;
- APIs, providers de IaC, qualidade da documentação e facilidade de exportar dados;
- maturidade do ecossistema, habilidades disponíveis e custo de operação;
- dependência de serviços proprietários e dificuldade de migração.

## Mapa dos provedores

| Provedor | Categoria predominante | Força típica | Cuidado principal |
| --- | --- | --- | --- |
| AWS | Nuvem hyperscale | Amplitude de serviços e ecossistema | Complexidade, cobrança e acoplamento |
| Google Cloud | Nuvem hyperscale | Dados, Kubernetes e rede global | Catálogo, preços e disponibilidade por região |
| Azure | Nuvem hyperscale | Integração empresarial e Microsoft | Complexidade de serviços e identidade |
| Akamai | Edge, segurança e cloud | Distribuição, rede e baixa latência | Separar edge da capacidade de compute |
| Linode | IaaS e cloud para desenvolvedores | VPS, API e operação simples | Menor amplitude que hyperscalers |
| Magalu Cloud | Cloud brasileira | Operação no Brasil e serviços de infraestrutura | Capacidade e catálogo por serviço |
| QNAX | IaaS, VPS e infraestrutura brasileira | Servidores, rede e suporte local | Confirmar termos, regiões e limites |
| Brasa Cloud | Cloud brasileira e plataformas gerenciadas | Desenvolvedores, dados no Brasil e cobrança em real | Produto em evolução e escopo do beta |
| 4B Digital | Cloud e infraestrutura para empresas | Portfólio brasileiro e serviços para parceiros | Confirmar produto, contrato e operação |
| Saphir | Hosting, cloud e serviços gerenciados | Operação assistida e infraestrutura nacional | Menor foco em cloud self-service |
| Hostinger | Hospedagem, cloud hosting e VPS | Sites e pequenos projetos | Limites de hospedagem gerenciada |
| Hostnet | Hospedagem e serviços web | Sites, e-mail e suporte local | Não é uma hyperscale cloud |
| HostGator | Hospedagem, cloud e VPS | Entrada simples e variedade de planos | Avaliar backups, suporte e controle real |
| Vercel | PaaS web e edge | Deploy, previews e frontends | Runtime e persistência dependem do desenho |
| Heroku | PaaS de aplicações | Buildpacks e experiência de deploy | Menor controle da infraestrutura |
| Coolify | PaaS autohospedado | Control plane para aplicações, bancos e serviços Docker | Operação do host, painel, volumes e credenciais |
| Dokploy | PaaS autohospedado | Deploy Docker, Compose, múltiplos servidores e bancos | Segurança do painel e recuperação do control plane |
| CapRover | PaaS autohospedado | Fluxo simples sobre Docker Swarm e Nginx | Limites do Compose e dependência do modelo Swarm |
| Railway | PaaS cloud gerenciado | Projetos, serviços, ambientes, templates e deploy rápido | Custos, limites e dependência do provedor |
| Surge.sh | Publicação estática | CLI, CDN, previews, revisões e rollback de arquivos estáticos | Não executa backend ou estado durável |
| ZEIT | Marca histórica | Empresa e identidade anterior à Vercel | Referências antigas podem misturar produto, marca e domínio |
| now.sh | Produto e domínio históricos | Deploy por CLI, previews e roteamento web | Deve ser interpretado como antecessor da Vercel |
| AbraCloud | Associação setorial brasileira | Diretório, representação e relacionamento do ecossistema cloud | Não é um provedor cloud único nem um SLA |
| Cloudflare | Edge, rede e serverless | DNS, CDN, segurança e Workers | Não substitui todo backend stateful |
| Cloudflare Pages | Publicação web e edge | Builds, previews, artefatos estáticos e Functions | Não é uma VM nem um backend stateful |
| Cloudflare Workers | Runtime edge | Lógica distribuída, APIs e integrações | Limites de runtime, estado e compatibilidade |
| Cloudflare Tunnel | Conectividade privada e ingress | Publicar origens privadas por conexão de saída | Não substitui autenticação ou segmentação |
| Netlify | PaaS web e edge | Builds, previews, funções e entrega web | Runtime e dados exigem desenho separado |
| GitHub Pages | Hospedagem estática | Publicação integrada a repositórios GitHub | Sem backend persistente ou dados privados |
| ngrok | Túneis e ingress de desenvolvimento | Endpoints públicos para serviços locais | Exposição pública, limites e dependência externa |

## Como escolher

Comece pelo workload e pelas responsabilidades que a equipe pode assumir. Um site institucional pode precisar apenas de hospedagem gerenciada e CDN. Uma API com banco e jobs pode pedir VPS ou IaaS, desde que backups, atualizações e observabilidade sejam responsabilidade explícita de alguém. Uma organização com múltiplas equipes pode justificar serviços gerenciados, identidade centralizada e políticas de rede de uma hyperscale, mesmo pagando mais por complexidade.

Residência de dados no Brasil, suporte em português e cobrança em real podem ser fatores decisivos, mas não provam disponibilidade, resiliência ou conformidade por si só. É preciso verificar contrato, localização efetiva dos dados, backup, recuperação, subcontratados, logs e processo de incidentes.

Para workloads distribuídos, combine camadas em vez de procurar um fornecedor universal. Uma aplicação pode executar em IaaS, usar um banco gerenciado, publicar arquivos em object storage e colocar DNS, CDN e WAF em uma rede de edge. Essa composição aumenta a responsabilidade de integração, mas também reduz a dependência de uma única camada.

## Relação com infraestrutura como código

As páginas em [providers do OpenTofu](../../iac/providers/index.md) descrevem a integração declarativa com APIs de provedores. Elas não substituem esta área. Um provider de OpenTofu é uma implementação de automação; AWS, Azure, Cloudflare ou Proxmox são serviços e plataformas que precisam ser compreendidos antes da automação.

## Fontes primárias

- [AWS global infrastructure](https://docs.aws.amazon.com/global-infrastructure/latest/regions/)
- [Google Cloud regions and zones](https://cloud.google.com/compute/docs/regions-zones)
- [Azure regions](https://learn.microsoft.com/en-us/azure/reliability/regions-overview)
- [Akamai Cloud Computing](https://techdocs.akamai.com/cloud-computing/docs/welcome)
- [Magalu Cloud documentation](https://docs.magalu.cloud/docs/)
- [Cloudflare developer platform](https://www.cloudflare.com/developer-platform/products/)
