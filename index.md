# Aprender

Esta seção explica, sem depender de nenhuma decisão específica do hl-infrastructure, o que cada ferramenta e conceito usado no repositório é e por que existe. Ela não ensina como este repositório usa a ferramenta, isso é o trabalho da [arquitetura](../arquitetura/index.md), nem como executar uma tarefa com ela, isso é o trabalho do [operacional](../operacional/index.md). Uma página daqui deve continuar fazendo sentido fora deste repositório, para qualquer pessoa estudando a ferramenta em si. Na prática, isso significa que um exemplo pode citar um recurso deste cluster, mas o argumento da página não pode depender de conhecê-lo.

Se você nunca ouviu falar de uma ferramenta que aparece no [primeiro bootstrap](../operacional/primeiro-bootstrap.md), comece por ela aqui antes de rodar o comando. As páginas abaixo estão agrupadas na ordem em que as camadas se empilham, da automação que prepara o node até os gates de qualidade que rodam sobre o conjunto. Ler a página da ferramenta antes de executar o passo custa poucos minutos e evita o hábito de rodar um comando sem saber o que ele deixa no sistema.

## Fundamentos de sistemas, virtualização e containers

- [CPU, privilégios e syscalls](cpu-privilegios-e-syscalls.md): o ciclo de busca e execução, os anéis de privilégio, e o caminho de uma chamada de sistema.
- [Como os SOs expõem serviços](como-os-expoe-servicos.md): a mesma pergunta respondida por Linux, Windows e macOS, cada um com seu próprio conjunto de interfaces.
- [Famílias e padrões Unix](unix-familias-e-padroes.md): o que a POSIX padroniza, a linhagem BSD, e as famílias de distribuições Linux.
- [Shells e scripts](shells-e-scripts.md): os modos de invocação de um shell, o `sh` POSIX como piso comum, e as armadilhas de portabilidade entre GNU e BSD.
- [Coreutils e documentação](coreutils-e-documentacao.md): GNU Coreutils versus BusyBox, e onde procurar ajuda antes de adivinhar uma flag.
- [Máquinas virtuais e hipervisores](vms-e-hipervisores.md): VM versus container, QEMU/KVM, e o IOMMU por trás de um passthrough de dispositivo.
- [Isolamento leve: zones, jails e microVMs](isolamento-leve-zones-jails-e-microvms.md): o espectro entre um processo comum e uma VM completa.
- [Wine e compatibilidade](wine-e-compatibilidade.md): tradução de API contra emulação de hardware, e quando cada uma se aplica.
- [Processo, namespaces e usuários num container](processo-namespaces-e-usuarios.md): por que um container é um processo comum do host, e o que cada namespace isola.
- [Cgroups, capabilities e isolamento de filesystem](cgroups-capabilities-e-filesystem.md): os outros dois eixos de confinamento, quanto um processo consome e o que ele pode fazer.
- [Especificações OCI e a pilha de runtimes](especificacoes-oci-e-pilha-de-runtimes.md): o que Image, Distribution e Runtime Spec padronizam, e a diferença entre engine, runtime de alto nível e runtime de baixo nível.
- [Imagens, registries e Compose](imagens-registries-e-compose.md): `Dockerfile` contra a OCI Image Spec, tipos de registry, e o schema por trás de um `compose.yml`.

## Rede

- [Modelos OSI/TCP-IP e endereçamento IP](osi-tcpip-e-enderecamento-ip.md): CIDR, blocos privados, e por que IPv6 não é IPv4 com mais bits.
- [TLS, mTLS e confiança de rede](tls-mtls-e-confianca-de-rede.md): o handshake, a cadeia de certificados, e a mesma lógica de confiança aplicada a rotas BGP.
- [VPNs, túneis e bordas de rede](vpns-tuneis-e-bordas-de-rede.md): WireGuard, Tailscale, Cloudflare Tunnel, e onde um roteador dedicado entra na arquitetura.
- [Interfaces, rotas e camada 2 no Linux](interfaces-rotas-e-l2-no-linux.md): `ip link`/`ip address`, ARP/NDP, veth pairs e bridges, VLAN e VXLAN.
- [Netfilter, nftables e diagnóstico de rede](netfilter-nftables-e-diagnostico.md): hooks, conntrack, a diferença arquitetural entre `iptables` e `nftables`, e a ordem certa de investigar um problema de rede.
- [Resolução, zonas e registros DNS](resolucao-zonas-e-registros-dns.md): o caminho de uma consulta, delegação, NS e glue records, e os tipos de registro em uso real.
- [DNSSEC, mDNS e registro de domínio](dnssec-mdns-e-registro-de-dominio.md): a cadeia de assinaturas do DNSSEC, resolução sem servidor, e a diferença entre WHOIS/RDAP e resolução.
- [Servidores DNS e conectividade WAN](servidores-dns-e-conectividade-wan.md): PowerDNS, Unbound, BIND e CoreDNS, e por que PPPoE/DHCP exigem DNS dinâmico.
- [UFW e portas publicadas pelo Docker](ufw-e-portas-publicadas-pelo-docker.md): o modelo do UFW frente ao [firewalld](firewalld.md), e por que uma porta publicada pelo Docker escapa da política padrão do host.
- [Cilium e Calico como CNI](cilium-e-calico-como-cni.md): eBPF contra regras iptables/nftables, e quando cada modelo se encaixa.
- [Reverse proxy e split-horizon DNS](reverse-proxy-e-split-horizon-dns.md): roteamento por path, host e SNI, e como resolver um nome interno sem expor porta nenhuma.
- [Service mesh: Istio e Linkerd](service-mesh-istio-e-linkerd.md): o que um sidecar resolve, e quando o custo operacional de um mesh se paga.

## Automação e provisionamento

- [DevOps, IaC e GitOps](devops-iac-gitops.md): o que é prática e o que é ferramenta, e por que uma ferramenta como o [Ansible](ansible.md) ou um guarda-chuva como o Argo Project não pertencem a uma única categoria.
- [Infraestrutura como código](iac-provisionamento.md): o que separa provisionamento de gestão de configuração, e onde o [Ansible](ansible.md) se encaixa nisso.
- [Ansible](ansible.md): push versus pull, idempotência, modo de verificação, tags e o Vault.
- [SSH](ssh.md): chave pessoal versus deploy key, `~/.ssh/config`, `known_hosts` e tunelamento.
- [firewalld](firewalld.md): zonas, regra permanente versus regra de runtime, e o recarregamento atômico.

## Plataforma Kubernetes

- [k3s](k3s.md): o que diferencia essa distribuição do Kubernetes completo, e o que é um kubeconfig.
- [Rede interna do cluster](rede-interna-do-cluster.md): o papel de uma CNI, a rede overlay entre pods e a descoberta de serviço via CoreDNS.
- [Distribuições Kubernetes](distribuicoes-kubernetes.md): o vocabulário básico do Kubernetes, K3s vs. RKE2, e outras distribuições como k0s e kubeadm.
- [Orquestradores de containers: Compose, Swarm e Kubernetes](orquestradores-de-containers.md): quando cada escopo (um host, um cluster pequeno, produção escalável) faz sentido.
- [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md): por que o número de servidores precisa ser ímpar, e a alternativa Kine.
- [Kubernetes gerenciado e HA avançada](kubernetes-gerenciado-e-ha-avancada.md): EKS como exemplo de control plane delegado, e o que fica além de um cluster multinó comum.
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
- [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md): por que base64 não é criptografia, e a diferença entre SOPS e Sealed Secrets.
- [Bootstrap e rotação de segredos](bootstrap-e-rotacao-de-segredos.md): o problema recursivo da primeira credencial, e a ordem segura para trocar uma credencial em uso.
- [Secret store externo](secret-store-externo.md): o External Secrets Operator, e o mecanismo de unseal do OpenBao e do Vault.
- [OWASP](owasp.md): o que é a fundação, seus projetos, e o que o Top 10 realmente lista.
- [MITRE ATT&CK](mitre-attack.md): a base de conhecimento de comportamento de atacantes, o que são táticas e técnicas, e como este repositório se lê pela matriz de contêineres.
- [Zero trust](zero-trust.md): o princípio de não confiar por posição na rede, e o que ele substitui.

## Continue por aqui

A [arquitetura](../arquitetura/index.md) explica por que este repositório usa cada uma dessas ferramentas do jeito que usa.
