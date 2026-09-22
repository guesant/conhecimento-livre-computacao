# Aprender

Aprender explica conceitos, abordagens e ferramentas sem depender das decisões específicas do `hl-infrastructure`. A organização segue uma árvore de conhecimento: primeiro domínio e categoria, depois conceito ou abordagem e, por fim, implementações concretas.

A regra central é profundidade estreita. Uma página pode ser longa, mas deve aprofundar uma unidade de conhecimento. Quando ferramentas ou abordagens diferentes pertencem à mesma categoria, a categoria recebe uma página-mapa e cada assunto independente recebe endereço próprio.

## Sistemas e Linux

[Sistemas e Linux](sistemas/index.md) começa pela execução: CPU, níveis de privilégio, system calls, processos e mecanismos de isolamento. A partir daí entram namespaces, [cgroups](sistemas/linux/cgroups.md), [capabilities](sistemas/linux/capabilities.md), [seccomp](sistemas/linux/seccomp.md), Unix, shells, coreutils e systemd.

Essa base explica por que containers não são uma tecnologia única do kernel: eles combinam mecanismos diferentes de isolamento, controle de recursos, privilégio e filesystem.

## Virtualização e containers

Máquinas virtuais e hipervisores introduzem isolamento por virtualização de hardware. Zones, jails e microVMs ocupam outros pontos do espectro. OCI formaliza formatos e interfaces do ecossistema de containers; imagens, registries e runtimes tratam de distribuição e execução; orquestradores tratam de ciclo de vida em escala.

A página [Containers e Kubernetes](plataforma/index.md) funciona como mapa entre esses níveis.

## Redes

[Redes](rede/index.md) organiza o assunto em fundamentos, DNS, conectividade privada, firewall/gateway e rede de cluster.

DNS é desmembrado entre resolução e registros, servidores, [DNSSEC](rede/dns/dnssec.md), [mDNS](rede/dns/mdns.md) e [registro de domínio](rede/dns/registro-de-dominio.md). Conectividade separa [VPN](rede/conectividade/vpn.md), [tunneling](rede/conectividade/tunel.md) e [borda](rede/conectividade/borda.md).

A progressão evita aprender Cilium, Gateway API ou service mesh antes de compreender rotas, DNS, transporte e fronteiras de rede.

## Kubernetes

Kubernetes é organizado por distribuição e arquitetura, recursos e extensibilidade, armazenamento, empacotamento e operação. [K3s](k3s.md) é uma distribuição concreta, não a definição da plataforma. Helm é uma forma de empacotar e renderizar recursos, não o modelo de recursos do Kubernetes.

Operators, namespaces, Jobs, requests/limits, probes, PDBs, storage e manutenção de nó são tratados como conceitos independentes para evitar páginas que misturam todas as propriedades de um workload.

## Automação e infraestrutura como código

Esta área separa DevOps, IaC e GitOps como ideias relacionadas mas distintas. [Infraestrutura como código](iac-provisionamento.md) trata declaração e provisionamento; [Ansible](ansible.md) trata uma implementação de automação e configuração; SSH, just, jq/yq e ferramentas de transferência possuem responsabilidades próprias.

## Entrega e GitOps

[Entrega e GitOps](entrega/index.md) organiza reconciliação, CI/CD e estratégias de rollout.

Entrega progressiva é separada em [canary](entrega/progressiva/canary.md), [blue-green](entrega/progressiva/blue-green.md) e [Argo Rollouts](entrega/progressiva/argo-rollouts.md). Isso distingue a estratégia da ferramenta que a implementa. Feature flags aparecem ao lado porque podem complementar rollout, mas controlam ativação de comportamento em outro nível.

## Segurança

[Segurança](seguranca/index.md) é uma árvore própria.

[Segurança de aplicações](seguranca/appsec/index.md) separa [SAST](seguranca/appsec/sast/index.md), [SCA](seguranca/appsec/sca/index.md), [DAST](seguranca/appsec/dast.md) e [secret scanning](seguranca/appsec/secret-scanning/index.md). Implementações como [CodeQL](seguranca/appsec/sast/codeql.md) e [OSV-Scanner](seguranca/appsec/sca/osv-scanner.md) ficam abaixo da abordagem que implementam.

Segurança de CI/CD trata a pipeline como superfície própria, com [zizmor](seguranca/cicd/zizmor.md) como implementação especializada. [Segurança de IaC](seguranca/iac/index.md) distingue schema validation, configuration scanning, policy as code e posture/compliance scanning, com páginas próprias para [Checkov](seguranca/iac/checkov.md) e [KubeLinter](seguranca/iac/kubelinter.md).

[PKI e confiança](seguranca/pki/index.md) separa protocolo, emissão e distribuição. [step-ca](seguranca/pki/step-ca.md) é uma CA; [trust-manager](seguranca/pki/trust-manager.md) distribui bundles de confiança. Segredos, RBAC, zero trust, threat modeling, MITRE ATT&CK, OWASP, compliance e supply chain permanecem categorias independentes.

## Observabilidade

[Observabilidade](observabilidade/index.md) começa pelos sinais antes das ferramentas.

[Métricas](observabilidade/metricas.md), [logs](observabilidade/logs.md) e [distributed tracing](observabilidade/tracing.md) possuem modelos e custos próprios. [Prometheus](observabilidade/prometheus.md), [Loki](observabilidade/loki.md) e [Grafana](observabilidade/grafana.md) são implementações concretas e, por isso, não ficam mais comprimidos numa única página de "stack".

## Dados e mensageria

[Dados e mensageria](dados/index.md) evita usar "NoSQL" ou "mensageria" como categorias finais.

[Bancos chave-valor](dados/bancos/key-value.md) e [bancos de documentos](dados/bancos/documentos.md) têm modelos diferentes. [Filas](dados/mensageria/filas.md) e [event streaming](dados/mensageria/event-streaming.md) também são separados porque retenção, consumo, replay e ordenação não funcionam da mesma maneira.

## Cenários, composições e comparações

A árvore por domínio responde onde cada conceito pertence, mas decisões reais atravessam domínios. [Cenários e padrões de solução](cenarios/index.md) partem das restrições do ambiente, como single-node ou pequeno cluster. [Composições](composicoes/index.md) explicam como responsabilidades diferentes se conectam, como CNI + Gateway + mesh ou IaC + configuração + GitOps. [Comparações](comparacoes/index.md) colocam alternativas que disputam uma responsabilidade sob critérios comuns.

Essas páginas não substituem Arquitetura. Elas podem concluir "sob estas premissas, este padrão tende a reduzir complexidade" de forma reutilizável; a decisão concreta de como o `hl-infrastructure` foi montado continua documentada em Arquitetura.

## Backup e recuperação

Backup começa por RPO e RTO, segue para retenção e testes de restauração e então chega às particularidades de etcd, CloudNativePG, chaves e reconstrução de cluster. A ordem é deliberada: ferramenta de backup sem objetivo de recuperação definido produz cópias, não necessariamente recuperabilidade.

## Qualidade, governança e diagnóstico

Padrões da Internet, fundações de software livre, linters e automação de dependências formam a camada de governança e qualidade. Diagnóstico reúne técnicas que atravessam domínios, como iperf3, tcpdump e strace.

Essas páginas não substituem as páginas conceituais. Um diagnóstico com `strace`, por exemplo, fica mais útil depois que [system calls](sistemas/kernel/system-calls.md) já são compreendidas.

## Como ler uma página

Páginas profundas procuram responder, quando aplicável: o que é; o que não é; como funciona; quando usar; quando não usar; exemplos; boas práticas; más práticas; falhas comuns; trade-offs; implicações de segurança e operação; alternativas; aplicações reais e fontes primárias.

Exemplos em Aprender demonstram mecanismos. Passos destinados a alterar o cluster real pertencem a [Operacional](../operacional/index.md). Decisões específicas deste repositório pertencem a [Arquitetura](../arquitetura/index.md).

## Continue por aqui

Se o objetivo é compreender a infraestrutura de baixo para cima, uma ordem útil é Sistemas e Linux → Virtualização e containers → Redes → Kubernetes → Automação/IaC → Entrega/GitOps → Segurança → Observabilidade → Backup.

Essa ordem é uma trilha, não uma dependência rígida. As páginas-mapa de cada domínio permitem entrar diretamente no assunto necessário sem ler a documentação inteira em sequência.
