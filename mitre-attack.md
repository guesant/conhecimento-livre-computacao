# MITRE ATT&CK

ATT&CK (Adversarial Tactics, Techniques and Common Knowledge) é uma base de conhecimento mantida pela MITRE, organização sem fins lucrativos financiada pelo governo dos Estados Unidos, que cataloga o comportamento observado de atacantes reais. Ao contrário do [OWASP](owasp.md) Top 10, que lista categorias de vulnerabilidade, o ATT&CK descreve o que um atacante faz depois de encontrar uma: as fases pelas quais uma intrusão passa (as táticas) e as maneiras concretas de cumprir cada fase (as técnicas), cada uma com exemplos de grupos que a usaram, formas de detectar e mitigações conhecidas. É a linguagem comum com que times de defesa, fornecedores de ferramentas e relatórios de incidente se referem ao mesmo comportamento, e a razão de o kubescape falar em "framework MITRE": ele avalia manifestos Kubernetes contra as técnicas da matriz de contêineres.

## Táticas e técnicas

Uma tática é o objetivo do atacante num momento da intrusão, e a matriz as ordena mais ou menos na sequência em que aparecem: reconhecimento, acesso inicial, execução, persistência, escalada de privilégio, evasão de defesa, acesso a credenciais, descoberta, movimento lateral, coleta, comando e controle, exfiltração e impacto. Uma técnica é um jeito de alcançar a tática, com um identificador estável (`T1078`, por exemplo, é "Valid Accounts": entrar com uma credencial legítima roubada); muitas têm subtécnicas. A matriz Enterprise cobre sistemas operacionais, nuvem e identidade; a matriz de contêineres, publicada em 2021, recorta o que se aplica a Docker e Kubernetes, como implantar um contêiner malicioso (`T1610`), escapar para o host (`T1611`) ou abusar de uma conta de serviço do Kubernetes (`T1078.001`).

O valor prático do ATT&CK não está em ler a matriz inteira, e sim em usá-la como lista de verificação orientada pelo atacante: para cada técnica que faria sentido contra o seu ambiente, perguntar o que a impede, o que a detectaria e o que aconteceria se ela funcionasse. É o complemento natural do [threat modeling](threat-modeling.md), que parte dos ativos e das fronteiras; o ATT&CK parte do adversário.

## Como este repositório se lê pela matriz

Sem pretensão de cobertura completa, as técnicas mais plausíveis contra um node só, público pelo túnel e administrado de um Mac, e o que o repositório opõe a cada uma:

| Tática | Técnica | O que barra ou detecta aqui |
| --- | --- | --- |
| Acesso inicial | Serviço remoto externo (`T1133`), força bruta (`T1110`) | Só SSH por chave fica exposto, na rede local e pela tailnet; a API do k3s não abre em zona nenhuma do firewall, alcançável só de dentro do próprio node. Nada na Internet além do túnel Cloudflare, que só encaminha para o blog. fail2ban e o `bruteForceProtected` dos realms do Keycloak limitam tentativas. |
| Acesso inicial | Contas válidas (`T1078`) | Login único pelo Keycloak com TOTP obrigatório; nenhuma aplicação interna tem senha própria alcançável de fora, e as que sobram (Portainer) só respondem pela tailnet. |
| Execução, persistência | Implantar contêiner (`T1610`), imagem maliciosa | Políticas de admissão exigem imagem por digest de um registry da lista, contêiner sem root, sem escalada de privilégio e sem capabilities; o Argo CD só aplica o que está em `main`, e o Kargo só promove o digest que a CI do satélite publicou e escaneou. |
| Escalada de privilégio | Fuga para o host (`T1611`) | Pod Security `restricted` em todo namespace de workload; `privileged` só onde `hostNetwork` é a razão de existir (ingress e node-exporter), com raiz somente leitura e `drop: ALL` mesmo assim. |
| Acesso a credenciais | Credenciais em arquivos (`T1552`), roubo de token de conta de serviço (`T1528`) | Nenhum segredo em claro no git, `Secret` cifrados no datastore do k3s, ServiceAccount sem token montado em quem não precisa, `secrets.map` para o OpenTofu não guardar cópia, e o gitleaks sobre todo o histórico. |
| Descoberta, movimento lateral | Descoberta de rede e serviços (`T1046`), movimento entre pods | Políticas de rede do Cilium por namespace com lista de liberação, em `policyEnforcementMode: always` e com o modo auditoria desligado: cada namespace só fala com o que declara, de verdade, não só em registro. A tailnet é a única fronteira dos nomes internos. |
| Evasão de defesa | Apagar logs (`T1070`), desabilitar controles (`T1562`) | auditd vigiando identidade, SSH, firewall, módulos do kernel e a configuração do k3s; audit log do API server para toda escrita; a reconciliação do firewall e das chaves SSH desfaz alterações não declaradas a cada bootstrap. |
| Comando e controle, exfiltração | Canal de saída (`T1071`), exfiltração por serviço web (`T1567`) | Egresso restrito por namespace (DNS, API server, e 443 só para quem precisa da Internet); o blog nem tem egresso além do banco e do túnel. |
| Impacto | Destruição de dados (`T1485`), ransomware | `prevent_destroy` nos registros DNS, backup do Postgres ainda pendente (a maior lacuna listada em [estado fora do git](../operacional/estado-fora-do-git.md)). |

O kubescape, na CI, automatiza uma parte disso: o framework MITRE dele confere os manifestos renderizados contra controles derivados da matriz de contêineres (acesso ao `Secret` por ServiceAccount, `hostPath`, capacidades, exposição de dashboard, e outros), e a nota não pode cair abaixo do piso registrado no `justfile`. O que a matriz mostra que a CI não vê são as técnicas que acontecem em execução, no host ou na identidade, e é para essas que existem o auditd, o Keycloak e a [revisão periódica](../operacional/revisao-periodica.md).

## Continue por aqui

[Threat modeling](threat-modeling.md) é o outro lado da mesma moeda, partindo dos ativos em vez do atacante; o [modelo de ameaças](../arquitetura/modelo-de-ameacas.md) deste repositório é o resultado dos dois olhares, e o [mapa de controles](../arquitetura/mapa-de-controles.md) diz onde está a evidência de cada defesa citada na tabela.
