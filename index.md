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
- [Fail2ban, atualizações automáticas e journal persistente](fail2ban-atualizacoes-automaticas-e-journal.md): a camada que reage a tentativas repetidas depois que o firewall já deixou passar, e por que o journal persistente e a sincronização de horário custam pouco e evitam diagnósticos às cegas.
- [Cilium e Calico como CNI](cilium-e-calico-como-cni.md): eBPF contra regras iptables/nftables, e quando cada modelo se encaixa.
- [Reverse proxy e split-horizon DNS](reverse-proxy-e-split-horizon-dns.md): roteamento por path, host e SNI, e como resolver um nome interno sem expor porta nenhuma.
- [Gateway API: GatewayClass, Gateway e HTTPRoute](gateway-api.md): a separação de posse entre infraestrutura e aplicação que o `Ingress` clássico não tinha, e por que isso torna o controlador trocável.
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
- [Topologias, rede e falhas num K3s multinó](topologias-rede-e-falhas-em-k3s-multino.md): as três topologias entre nó único e HA completo, as portas exigidas entre servidores e agentes, e como cada cenário de falha se comporta segundo o quorum.
- [Modelo de armazenamento do Kubernetes](modelo-de-armazenamento-do-kubernetes.md): PVC, StorageClass e PV, modos de acesso e política de reclamação.
- [Armazenamento local, distribuído e Longhorn](armazenamento-local-distribuido-e-longhorn.md): a arquitetura do Longhorn, e por que replicação não é backup.
- [Policy enforcement e Kubescape](policy-enforcement-e-kubescape.md): Pod Security Admission, Kyverno e OPA/Gatekeeper contra a admissão, Kubescape como diagnóstico.
- [RBAC do Kubernetes](rbac-do-kubernetes.md): a diferença entre definir um papel e atribuí-lo, e por que uma ServiceAccount é a identidade real de um Pod perante a API.
- [TLS automático](tls-automatico.md): o protocolo ACME, a Let's Encrypt, e o padrão de operator aplicado à emissão de certificado.
- [ArgoCD e GitOps](argocd.md): o conceito de GitOps, o que é uma `Application` e um `AppProject`, e o padrão app-of-apps.
- [Operators do Kubernetes](kubernetes-operators.md): o par CRD mais controller, e o loop de reconciliação que sustenta boa parte do que este cluster instala.
- [Helm e charts](helm-e-charts.md): o que compõe um chart, a sintaxe de template, e a diferença entre `helm template` e `helm install`.
- [Gerar várias instâncias com Helm](helm-templating-de-lista.md): o padrão `range` sobre uma lista em `values.yaml`, e o risco de colisão com outra sintaxe de chaves duplas.
- [Requests, limits e QoS de um Pod](requests-limits-e-qos-de-um-pod.md): por que ultrapassar o limit de memória mata o container e ultrapassar o de CPU só o deixa mais lento, e as três classes que decidem quem é sacrificado primeiro.
- [Prontidão de workload: probes, PDB e desligamento gracioso](prontidao-de-workload-probes-pdb-e-desligamento.md): a `startupProbe` que separa inicialização lenta de trava em runtime, o que um PodDisruptionBudget protege e o que ele não protege, e o que acontece entre o `SIGTERM` e o `SIGKILL`.
- [Jobs, CronJobs e securityContext de um Pod](jobs-cronjobs-e-securitycontext.md): por que um Job precisa terminar em vez de rodar para sempre, e os campos de `securityContext` que reduzem o que um container comprometido consegue fazer.
- [Manutenção de nó: cordon, drain e disco](manutencao-de-no-cordon-drain-e-disco.md): a diferença entre parar de agendar e evacuar, e os dois consumidores de disco que competem pelo mesmo espaço.

## Observabilidade e backup

- [Sinais de observabilidade e saúde de aplicação](sinais-de-observabilidade-e-saude-de-aplicacao.md): métricas, logs e traces, e por que um Pod `Running` não prova que a aplicação está disponível.
- [Stack Prometheus, Loki e Grafana](stack-prometheus-loki-grafana.md): como os três se conectam, e o trade-off entre retenção e cardinalidade.
- [Alertas acionáveis e distributed tracing](alertas-acionaveis-e-distributed-tracing.md): o que torna um alerta útil em vez de ruído, e o que um trace mostra que uma métrica isolada não mostra.
- [Fundamentos de backup, RPO e RTO](fundamentos-de-backup-rpo-e-rto.md): a diferença entre réplica, snapshot e backup, e as duas metas que toda estratégia precisa responder.
- [Retenção, testes de restauração e Velero](retencao-testes-e-velero.md): por que um Job `Completed` não prova que um backup restaura, e o que o Velero cobre além do snapshot do etcd.
- [Backup do etcd, do CloudNativePG e da chave age](backup-do-etcd-cnpg-e-chave-age.md): o snapshot nativo do K3s, WAL contínuo mais backup agendado, e por que a chave privada age é o ponto de falha única de todos os outros segredos.
- [Reconstrução de cluster single-node e recuperação de segredos](reconstrucao-de-cluster-single-node-e-recuperacao-de-segredos.md): restaurar do snapshot contra reconstruir via GitOps, e por que um snapshot de Secrets não é o mesmo que recuperar a capacidade de decifrar segredos novos.

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

## Diagnóstico

- [Diagnóstico de Pod, nó, certificado e Argo CD](diagnostico-de-pod-no-cluster-e-do-argocd.md): por que `kubectl describe` costuma valer mais que os logs de um container, e como ler a causa de um `Pending`, um `NotReady`, um `Certificate` travado ou um `Degraded`.

## Ferramentas e estudo

- [Avaliar ferramentas de operação](avaliar-ferramentas-de-operacao.md): por que uma interface gráfica não cria uma fronteira de segurança nova, e os critérios que decidem se vale adotar uma.
- [Certificações de infraestrutura e nuvem](certificacoes-de-infraestrutura-e-nuvem.md): a diferença entre certificação, badge e avaliação prática, e por que o formato da prova importa mais que a organização que a emite.

## Continue por aqui

A [arquitetura](../arquitetura/index.md) explica por que este repositório usa cada uma dessas ferramentas do jeito que usa.
