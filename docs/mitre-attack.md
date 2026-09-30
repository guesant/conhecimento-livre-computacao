# MITRE ATT&CK

ATT&CK (Adversarial Tactics, Techniques and Common Knowledge) é uma base de conhecimento mantida pela MITRE, organização sem fins lucrativos financiada pelo governo dos Estados Unidos, que cataloga o comportamento observado de atacantes reais. Ao contrário do [OWASP](owasp.md) Top 10, que lista categorias de vulnerabilidade, o ATT&CK descreve o que um atacante faz depois de encontrar uma: as fases pelas quais uma intrusão passa (as táticas) e as maneiras concretas de cumprir cada fase (as técnicas), cada uma com exemplos de grupos que a usaram, formas de detectar e mitigações conhecidas. É a linguagem comum com que times de defesa, fornecedores de ferramentas e relatórios de incidente se referem ao mesmo comportamento. É também a razão de o kubescape falar em "framework MITRE": ele avalia manifestos Kubernetes contra as técnicas da matriz de contêineres.

## Táticas e técnicas

Uma tática é o objetivo do atacante num momento da intrusão, e a matriz as ordena mais ou menos na sequência em que aparecem: reconhecimento, acesso inicial, execução, persistência, escalada de privilégio, evasão de defesa, acesso a credenciais, descoberta, movimento lateral, coleta, comando e controle, exfiltração e impacto. Uma técnica é um jeito de alcançar a tática, e vem com um identificador estável: `T1078`, por exemplo, é "Valid Accounts", entrar com uma credencial legítima roubada. Muitas técnicas têm subtécnicas, que recortam a mesma ideia por meio ou por ambiente, o que permite ser tão específico quanto o caso exigir. O identificador é o que torna o catálogo utilizável na prática, porque sobrevive a mudanças de nome e deixa ferramenta, relatório e regra de detecção apontarem para exatamente o mesmo comportamento.

Esse catálogo não é único: existe mais de uma matriz, cada uma recortando o conjunto de técnicas que faz sentido para um tipo de ambiente. A matriz Enterprise cobre sistemas operacionais, nuvem e identidade. A matriz de contêineres recorta o que se aplica a Docker e Kubernetes, como implantar um contêiner malicioso (`T1610`), escapar para o host (`T1611`) ou abusar de uma conta de serviço do Kubernetes (`T1078.001`). A matriz escolhida deve corresponder ao escopo que está sendo analisado.

O valor prático do ATT&CK não está em ler a matriz inteira, e sim em usá-la como lista de verificação orientada pelo atacante. Para cada técnica que faria sentido contra o seu ambiente, a pergunta se repete em três partes: o que a impede, o que a detectaria e o que aconteceria se ela funcionasse. É o complemento natural do [threat modeling](threat-modeling.md), que parte dos ativos e das fronteiras; o ATT&CK parte do adversário. As duas leituras convergem no mesmo lugar, e uma técnica sem resposta para nenhuma das três perguntas é exatamente a lacuna que o exercício existe para expor.

## Como um sistema pode ser analisado pela matriz

Sem pretensão de cobertura completa, a tabela abaixo mostra como relacionar técnicas a controles e evidências durante uma análise:

| Tática | Técnica | O que barra ou detecta aqui |
| --- | --- | --- |
| Acesso inicial | Serviço remoto externo (`T1133`), força bruta (`T1110`) | Restringir serviços expostos, exigir autenticação resistente a força bruta e monitorar tentativas anômalas. |
| Acesso inicial | Contas válidas (`T1078`) | Aplicar autenticação multifator, menor privilégio e revisão periódica de identidades e sessões. |
| Execução, persistência | Implantar contêiner (`T1610`), imagem maliciosa | Verificar origem e integridade das imagens, restringir privilégios e exigir revisão antes da entrega. |
| Escalada de privilégio | Fuga para o host (`T1611`) | Aplicar políticas de segurança de workload, reduzir capabilities e bloquear configurações privilegiadas desnecessárias. |
| Acesso a credenciais | Credenciais em arquivos (`T1552`), roubo de token de conta de serviço (`T1528`) | Manter segredos fora do código em claro, limitar tokens e observar acessos a material sensível. |
| Descoberta, movimento lateral | Descoberta de rede e serviços (`T1046`), movimento entre pods | Aplicar segmentação de rede e permitir apenas os fluxos necessários entre serviços e namespaces. |
| Evasão de defesa | Apagar logs (`T1070`), desabilitar controles (`T1562`) | Centralizar logs, auditar mudanças administrativas e detectar alterações em controles de segurança. |
| Comando e controle, exfiltração | Canal de saída (`T1071`), exfiltração por serviço web (`T1567`) | Restringir egress, observar destinos e revisar transferências de dados fora do domínio esperado. |
| Impacto | Destruição de dados (`T1485`), ransomware | Controles de retenção, backups testados e mecanismos que impedem destruição acidental. |

Ferramentas como o kubescape automatizam uma parte disso, conferindo manifestos renderizados contra controles derivados da matriz de contêineres. O que a matriz mostra e uma análise estática não vê são as técnicas que acontecem em execução, no host ou na identidade. Nenhum manifesto renderizado denuncia um login suspeito, uma regra de firewall alterada ou um log apagado, por isso a análise precisa combinar configuração, telemetria e revisão periódica.

## Continue por aqui

[Threat modeling](threat-modeling.md) é o outro lado da mesma moeda, partindo dos ativos em vez do atacante. Um mapa de controles relaciona as defesas às evidências que permitem verificar sua existência e eficácia.
