# Aprender

Esta seção explica, sem depender de nenhuma decisão específica do hl-infrastructure, o que cada ferramenta e conceito usado no repositório é e por que existe. Ela não ensina como este repositório usa a ferramenta, isso é o trabalho da [arquitetura](../arquitetura/index.md), nem como executar uma tarefa com ela, isso é o trabalho do [operacional](../operacional/index.md). Uma página daqui deve continuar fazendo sentido fora deste repositório, para qualquer pessoa estudando a ferramenta em si.

Se você nunca ouviu falar de uma ferramenta que aparece no [primeiro bootstrap](../operacional/primeiro-bootstrap.md), comece por ela aqui antes de rodar o comando.

## Automação e provisionamento

- [DevOps, IaC e GitOps](devops-iac-gitops.md): o que é prática e o que é ferramenta, e por que uma ferramenta como o [Ansible](ansible.md) ou um guarda-chuva como o Argo Project não pertencem a uma única categoria.
- [Infraestrutura como código](iac-provisionamento.md): o que separa provisionamento de gestão de configuração, e onde o [Ansible](ansible.md) se encaixa nisso.
- [Ansible](ansible.md): push versus pull, idempotência, modo de verificação, tags e o Vault.
- [SSH](ssh.md): chave pessoal versus deploy key, `~/.ssh/config`, `known_hosts` e tunelamento.
- [firewalld](firewalld.md): zonas, regra permanente versus regra de runtime, e o recarregamento atômico.

## Plataforma Kubernetes

- [k3s](k3s.md): o que diferencia essa distribuição do Kubernetes completo, e o que é um kubeconfig.
- [Rede interna do cluster](rede-interna-do-cluster.md): o papel de uma CNI, a rede overlay entre pods e a descoberta de serviço via CoreDNS.
- [TLS automático](tls-automatico.md): o protocolo ACME, a Let's Encrypt, e o padrão de operator aplicado à emissão de certificado.
- [ArgoCD e GitOps](argocd.md): o conceito de GitOps, o que é uma `Application` e um `AppProject`, e o padrão app-of-apps.
- [Operators do Kubernetes](kubernetes-operators.md): o par CRD mais controller, e o loop de reconciliação que sustenta boa parte do que este cluster instala.
- [Helm e charts](helm-e-charts.md): o que compõe um chart, a sintaxe de template, e a diferença entre `helm template` e `helm install`.
- [Gerar várias instâncias com Helm](helm-templating-de-lista.md): o padrão `range` sobre uma lista em `values.yaml`, e o risco de colisão com outra sintaxe de chaves duplas.

## CI/CD, segurança e qualidade

- [CI/CD](ci-cd.md): a diferença entre integração contínua, entrega contínua e implantação contínua.
- [Scanning de vulnerabilidade](vulnerability-scanning.md): as categorias de scanner (dependência, código, segredo, infraestrutura) e o que cada uma pega que as outras não pegam.
- [Supply chain e SBOM](supply-chain-e-sbom.md): por que a cadeia de suprimentos de software virou alvo, e o que um SBOM declara.
- [Threat modeling](threat-modeling.md): como nomear ameaças de forma sistemática antes de desenhar uma mitigação.
- [OWASP](owasp.md): o que é a fundação, seus projetos, e o que o Top 10 realmente lista.
- [MITRE ATT&CK](mitre-attack.md): a base de conhecimento de comportamento de atacantes, o que são táticas e técnicas, e como este repositório se lê pela matriz de contêineres.
- [Zero trust](zero-trust.md): o princípio de não confiar por posição na rede, e o que ele substitui.

## Continue por aqui

A [arquitetura](../arquitetura/index.md) explica por que este repositório usa cada uma dessas ferramentas do jeito que usa.
