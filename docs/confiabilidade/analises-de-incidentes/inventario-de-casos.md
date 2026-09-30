# Inventário de casos de engenharia

Nem todo material relevante é um post-mortem. Há relatos escritos depois de um
incidente, estudos de migração, reconstruções de plataforma, mudanças de banco
e ferramentas criadas para remover um gargalo operacional. Todos são úteis, mas
respondem perguntas diferentes.

Um post-mortem explica impacto, causa, resposta e prevenção. Um estudo de
migração explica como preservar compatibilidade durante uma mudança estrutural.
Um relato de plataforma mostra como transformar trabalho manual recorrente em
uma capacidade operável. Nenhum desses materiais prova que o desenho escolhido
é universalmente adequado.

## Como estudar cada caso

Ao ler um relato, não se limite à tecnologia citada. Extraia pelo menos:

1. qual propriedade estava sendo protegida, como disponibilidade, durabilidade,
   consistência, latência ou segurança;
2. qual mudança ou evento alterou o estado do sistema;
3. qual suposição deixou de ser verdadeira;
4. quais sinais apareceram primeiro e quais estavam ausentes;
5. que decisão reduziu o blast radius;
6. por que a recuperação demorou mais que a detecção;
7. quais efeitos derivados ficaram atrasados ou foram perdidos;
8. qual controle pode ser reproduzido em uma escala menor.

Essa leitura evita copiar números de empresas grandes sem entender a propriedade
que eles estavam tentando preservar.

## Banco de dados e armazenamento

| Caso | Tipo | Mecanismo ou problema | O que estudar |
| --- | --- | --- | --- |
| [Project Mezzanine, Uber](https://www.uber.com/us/en/blog/mezzanine-codebase-data-migration/) | Migração de dados e código | Dados de viagens saíram de um PostgreSQL monolítico para uma camada particionada, com mudança de identificadores | Compatibilidade de leitura, migração de código, UUID, partição e preservação de comportamento durante a troca |
| [PostgreSQL para MySQL, Uber](https://www.uber.com/us/en/blog/postgres-to-mysql-migration/) | Reavaliação de arquitetura | Limitações observadas em uma geração do PostgreSQL levaram ao Schemaless e depois ao MySQL | Separar limitações do produto, da versão e da arquitetura, sem transformar a decisão histórica em regra universal |
| [MySQL na Uber](https://www.uber.com/us/en/blog/mysql-at-uber/) | Plataforma de bancos | Milhares de clusters exigiram automação de failover, substituição de nós e controle de configuração | Como uma operação de banco vira produto interno, quais partes precisam de control plane e como disponibilidade é medida |
| [Trilhões de mensagens, Discord](https://discord.com/blog/how-discord-stores-trillions-of-messages) | Migração de Cassandra para ScyllaDB | Partições quentes, pressão de armazenamento e limites de consulta | Modelagem por padrão de leitura, controle de concorrência, serviços de dados e migração sem fingir que NoSQL remove trade-offs |
| [Múltiplos bancos, Figma](https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/) | Particionamento online de PostgreSQL | Um banco grande e colaboração em tempo real precisavam de distribuição | Identificação de fronteiras de dados, roteamento, dual write, rollback e custo de operar múltiplos bancos |
| [GitLab em 2017](gitlab-2017.md) | Recuperação após perda de banco | Réplica atrasada, WAL não arquivado, backup incompatível e comando no host errado | Diferença entre réplica, backup, snapshot e recuperação testada |
| [GitHub em 2018](github-2018.md) | Reconciliação após divergência | Promoção entre regiões depois de partição de rede | Fencing, autoridade de escrita, consistência e backlog de efeitos assíncronos |

### Perguntas comuns aos casos de banco

Uber, Discord e Figma começaram de problemas diferentes, mas todos precisaram
responder perguntas semelhantes: quais dados mudam juntos, como uma requisição
encontra sua partição, como uma operação antiga pode ser lida depois de uma
migração e como o sistema volta atrás se a hipótese estiver errada.

O aprendizado não é "usar sharding" ou "trocar PostgreSQL por outro banco". É
que a migração muda a semântica do sistema. Identificadores, ordem de eventos,
transações, índices, consultas e ferramentas de operação precisam ser tratados
como parte do contrato.

## Controle de rede e plano de controle

| Caso | Tipo | Mecanismo ou problema | O que estudar |
| --- | --- | --- | --- |
| [Cloudflare 1.1.1.1 em 2024](cloudflare-2024.md) | Hijack e route leak | `/32` mais específico e vazamento de `/24` desviaram tráfego | Longest prefix match, RPKI, ROV, limites de origem e monitoramento por ASN |
| [Vazamento da Verizon em 2019](verizon-2019.md) | Erro de exportação | BGP optimizer dividiu prefixos e a rota saiu do escopo | More-specifics, filtros IRR, `max-prefix`, política de exportação e supply chain de rede |
| [Telegram na Índia em 2026](telegram-2026.md) | Bloqueio nacional que vazou | Blackhole doméstico apareceu em fontes externas e more-specifics entraram em disputa | Escopo geográfico, RPKI, ROV, communities de não exportação e limites da atribuição |
| [Meta em 2021](meta-2021.md) | Perda de backbone | Comando de manutenção desconectou a rede e a recuperação perdeu o caminho normal | Plano de dados, controle e recuperação, BGP, DNS, acesso fora de banda e retries |
| [Google Cloud em junho de 2019](https://status.cloud.google.com/incident/cloud-networking/19009) | Falha de automação do plano de controle | Dois defaults benignos e um bug desagendaram componentes em locais diferentes | Dependências entre control plane e data plane, fail-static, retirada BGP e observabilidade independente |
| [Windows Azure em fevereiro de 2012](https://azure.microsoft.com/en-us/blog/summary-of-windows-azure-service-disruption-on-feb-29th-2012/) | Rollout incompatível | Um pacote combinou versões incompatíveis do host agent e do plugin de rede | Teste de servidor que não representa VMs, rollout por cluster, compatibilidade e rollback |
| [Azure Storage em novembro de 2014](https://azure.microsoft.com/en-us/blog/final-root-cause-analysis-and-improvement-areas-nov-18-azure-storage-service-interruption/) | Falha de armazenamento com efeitos derivados | Timeout de montagem, provisionamento de VMs, programação de rede e status também falharam | Como uma falha de storage se propaga para compute, rede, telemetria e comunicação |

Esses casos mostram que BGP e DNS não devem ser tratados como detalhes de
infraestrutura sem relação com o produto. A publicação de rota define se o
usuário consegue chegar à aplicação. O DNS pode estar correto e ainda assim
retornar `SERVFAIL` porque a rota ao autoritativo desapareceu.

## Migrações de plataforma

| Caso | Tipo | O que estudar |
| --- | --- | --- |
| [Ambientes de desenvolvimento remoto, Discord](https://discord.com/blog/how-discord-moved-engineering-to-cloud-development-environments) | Migração organizacional e de infraestrutura | Mudança de Sysbox para VMs, latência, isolamento, rede, beta e comunicação com usuários internos |
| [Migração para Kubernetes, Figma](https://www.figma.com/blog/how-we-migrated-onto-k8s-in-less-than-12-months/) | Migração de plataforma de execução | Abstrações, caminhos de adoção, limites de risco e padronização sem obrigar cada equipe a reconstruir a plataforma |
| [Automação de clusters ScyllaDB, Discord](https://discord.com/blog/how-discord-automates-scylladb-clusters-at-scale) | Plataforma operacional | Provisionamento repetível, réplicas, manutenção e tráfego real em dezenas de nós |
| [MySQL containerizado, Uber](https://www.uber.com/qa/en/blog/dockerizing-mysql/) | Padronização operacional | Container, storage persistente, recuperação, substituição de nós e limites do host |

Uma migração de plataforma fracassa quando só move processos. Ela precisa mover
também observabilidade, permissões, suporte, rollback, documentação e modelo de
responsabilidade. A equipe que usa a plataforma deve saber qual comportamento
continua igual e qual passa a exigir uma decisão nova.

## Incidentes de dependência compartilhada

Os bloqueios descritos em [Bloqueios silenciosos](bloqueios-silenciosos.md)
formam uma categoria própria. O evento não precisa nascer dentro da plataforma
para derrubá-la. Uma CDN, uma hospedagem compartilhada ou uma faixa BGP pode ser
filtrada por uma decisão que tinha outro alvo.

Ao estudar Vercel, GitHub Pages, Cloudflare e LaLiga, separe:

- objeto jurídico ou regulatório do bloqueio;
- camada técnica que aplicou a regra;
- identidade que foi perdida entre domínio, IP e conteúdo;
- domínios legítimos que compartilham a infraestrutura;
- evidência de impacto, distinguindo medição de relato;
- caminho de contestação e duração da regra.

Essa separação impede que a documentação transforme uma disputa regulatória em
uma afirmação técnica sem fonte ou em uma atribuição política que os dados não
sustentam.

## Padrões que atravessam os casos

### Uma mudança local pode atravessar a fronteira de confiança

BGP optimizer, rollout de pacote, comando de backbone e mudança de schema têm
algo em comum: a ação foi formulada em um escopo menor que o escopo observado.
O controle precisa testar exportação, dependências e impacto real, não somente o
resultado local do comando.

### Recuperar o processo não é recuperar o produto

Banco aceitando conexão não significa que filas, webhooks, builds, caches,
índices e consumidores estejam sincronizados. O RTO deve incluir o que o usuário
considera parte do serviço.

### Uma cópia não cobre todos os modos de falha

Réplica cobre alguns atrasos e falhas de nó. Snapshot cobre um ponto de
recuperação. Backup lógico ajuda na portabilidade. WAL permite recuperação
incremental. Nenhum deles substitui os demais sem uma análise explícita de
RPO, RTO, corrupção lógica e erro humano.

### O plano de recuperação deve sobreviver ao plano protegido

Se o mesmo caminho transporta dados, administração, telemetria e rollback, uma
falha de rede remove todas essas capacidades. Acesso fora de banda, console,
backup externo e observabilidade independente não são luxo em sistemas que
precisam recuperar a própria rede.

## Fontes de processo

- [Microsoft, evolução dos post-incident reviews](https://azure.microsoft.com/en-us/blog/advancing-the-outage-experience-automation-communication-and-transparency/).
- [Microsoft, threat modeling de resiliência](https://azure.microsoft.com/en-us/blog/advancing-resiliency-threat-modeling-for-large-distributed-systems/).
- [Microsoft, engenharia de observabilidade de redes](https://azure.microsoft.com/en-us/blog/the-network-is-a-living-organism/).

## Como comparar uma migração

Uma migração de banco ou de plataforma não deve ser avaliada somente pelo fato
de ter terminado. O resultado precisa ser comparado com o contrato que existia
antes da mudança e com os estados intermediários que podem ser observados pelos
usuários.

| Dimensão | Pergunta de revisão | Evidência esperada |
| --- | --- | --- |
| Compatibilidade | Clientes antigos continuam funcionando? | Testes de leitura e escrita com versões suportadas |
| Identidade | Chaves, ordenação e referências preservam o significado? | Amostras comparadas e validações de integridade |
| Consistência | Há uma janela de dual write ou leitura divergente? | Métrica de diferença e regra de reconciliação |
| Desempenho | A operação compete com tráfego normal? | Latência, I/O, locks e limite de concorrência |
| Rollback | É possível voltar sem apagar mudanças novas? | Procedimento exercitado e critério de parada |
| Observabilidade | A equipe sabe em qual fase a migração está? | Progresso, erro, backlog e alertas independentes |
| Responsabilidade | Quem decide pausar, continuar ou reverter? | Dono explícito e janela de decisão |

Uma migração irreversível exige uma prova mais forte antes do cutover. Quando a
operação usa dual write, o sistema precisa registrar qual fonte venceu cada
conflito e por quanto tempo o caminho antigo permanecerá disponível. Quando o
cutover é feito por roteamento, a mudança deve poder ser aplicada a uma fração
dos usuários ou partições antes de alcançar toda a plataforma.

## Como comparar um post-mortem

Um relato é mais útil quando permite reconstruir a cadeia sem depender de
informações ausentes. Ao revisar uma fonte, procure:

- horário em UTC e duração do impacto;
- escopo por região, produto, cliente e tipo de operação;
- diferença entre causa técnica, fator contribuinte e condição latente;
- controles que existiam, mas falharam, e controles que nunca existiram;
- impacto em dados, filas, jobs, caches e integrações;
- evidência que encerrou cada fase da recuperação;
- ações com dono, prazo e critério de conclusão.

Um texto que só diz "adicionamos mais monitoramento" não permite verificar a
correção. A ação precisa dizer qual propriedade será observada, qual limiar
representa risco, quem recebe o alerta e qual decisão o alerta autoriza.
