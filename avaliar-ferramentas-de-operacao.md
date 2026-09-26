# Avaliar ferramentas de operação

Uma interface gráfica ou uma TUI que se conecta a um cluster ou a um daemon de containers não cria uma fronteira de segurança nova; ela herda exatamente o que a credencial que recebe já permite.

Um kubeconfig administrativo entregue a um cliente Kubernetes de terceiros, ou o socket do Docker montado num container de gerenciamento, concede a essa ferramenta as mesmas operações que qualquer outro portador daquela credencial poderia fazer, incluindo as destrutivas. A conveniência de uma interface não reduz esse alcance, só muda a forma de acioná-lo.

Isso torna a pergunta relevante ao avaliar qualquer ferramenta de operação não "ela é confiável", mas "o que ela pode fazer com a credencial que eu pretendo dar a ela". A resposta certa é sempre avaliar com uma identidade de privilégio mínimo, nunca com o acesso administrativo de produção só para simplificar o primeiro teste.

Uma avaliação completa antes de adotar uma ferramenta cobre bem mais do que "ela resolve o problema": o modelo de execução, já que um cliente local que só lê credenciais existentes é uma categoria de risco diferente de um componente rodando dentro do cluster, que por sua vez difere de um serviço SaaS de terceiro recebendo dados do ambiente.

Ela também cobre quais credenciais, portas, agentes ou volumes privilegiados a ferramenta exige para funcionar, e se e o que ela envia para fora do ambiente, telemetria incluída.

A avaliação também cobre licença, custo e o quanto a operação passa a depender daquele fornecedor continuar existindo, além de como fazer backup da própria configuração da ferramenta e o que acontece com a operação do ambiente se ela ficar indisponível.

Uma ferramenta de diagnóstico ou de conveniência que se torna, sem ninguém decidir isso conscientemente, um passo obrigatório do fluxo de trabalho diário é um risco silencioso: o dia em que ela falha ou muda de plano vira um incidente, não um inconveniente.

## Categorias e o que cada uma resolve, não substitui

Interfaces para Kubernetes, seja uma aplicação desktop multi-cluster, uma interface web que roda dentro do próprio cluster respeitando o RBAC de quem acessa, ou uma TUI local rápida para inspeção, complementam a linha de comando; elas não substituem manifests versionados, revisão de mudança antes de aplicar, nem um fluxo GitOps.

Para uma operação destrutiva, confirmar cluster, namespace e identidade fora da interface, antes de prosseguir, continua sendo o hábito que evita o erro mais caro dessa categoria: aplicar a ação certa no cluster errado.

O mesmo raciocínio vale para interfaces de gerenciamento de Docker e Swarm: acesso ao daemon ou à API do Docker equivale, na prática, a controle total do host, porque um container privilegiado criado através dele alcança recursos que um usuário comum não alcançaria diretamente. Publicar essa API sem uma fronteira de autenticação forte é, por isso, equivalente a publicar acesso root.

Ferramentas de varredura de segurança, como as que identificam vulnerabilidades conhecidas em imagens e código, avaliam a postura de configuração de um cluster contra um conjunto de boas práticas, checam controles específicos como o CIS Benchmark, ou detectam comportamento suspeito a partir de eventos do kernel, produzem evidência auxiliar, não uma prova de segurança completa.

Um resultado sem nenhum achado não comprova que a cadeia de suprimentos é confiável, nem que a configuração é segura em produção, apenas que aquela ferramenta, com aquele conjunto de regras, não encontrou nada digno de nota.

Regras de verificação de postura frequentemente precisam de contextualização: nem todo controle pensado para uma distribuição Kubernetes genérica se aplica da mesma forma a uma distribuição mais enxuta como o K3s. Tratar cada divergência como uma falha automática, sem revisar a correspondência real, gera ruído que acaba treinando quem opera a ignorar os alertas.

Ferramentas de acesso remoto ao host, como um cliente SSH com catálogo de conexões salvas ou uma interface web de administração de sistema, são convenientes precisamente porque escondem trabalho repetitivo. Nenhuma delas substitui os fundamentos que continuam sendo a fronteira de segurança real: identidade individual em vez de compartilhada, hardening do próprio serviço, um firewall correto, e um log de auditoria de quem fez o quê.

Uma ferramenta assim some, ou muda de plano de negócio, sem esses fundamentos deixarem de existir; o inverso, depender só da ferramenta e nunca dos fundamentos, é o que transforma a saída dela do mercado num incidente.

## Automação de configuração e execução de tarefas

Ansible aplica configuração num conjunto de hosts via SSH, sem exigir agente instalado permanentemente; ele usa a mesma identidade e as mesmas chaves que uma sessão SSH manual já usaria. Uma tarefa que precisa de privilégio elevado soma um equivalente a `sudo` na própria definição da tarefa.

O risco real dessa categoria não é o acesso em si, e sim um procedimento mal escrito: sem módulos declarativos verdadeiramente idempotentes, ele pode reexecutar uma ação destrutiva a cada rodada em vez de convergir para um estado estável. Rodar em modo de simulação antes de aplicar contra produção revisa o que mudaria sem alterar nada ainda; o projeto é licenciado sob GPL-3.0.

| Ferramenta | Papel |
| --- | --- |
| `ansible-core` | automação de configuração de hosts via SSH |
| `--check --diff` | simula a execução de um playbook sem aplicar nada |
| `become: true` | eleva privilégio numa tarefa específica |

Um executor de tarefas como o `just` resolve um problema menor e diferente: lê um `justfile` na raiz do projeto e expõe cada bloco nomeado como um comando descobrível via `just --list`, documentando os atalhos do dia a dia em vez de deixá-los espalhados só num README.

Ele não substitui um orquestrador de automação: roda comandos locais ao host onde é invocado, sem inventário, sem SSH e sem o conceito de convergência para um estado declarado. O risco de segurança que ele introduz é o mesmo de rodar qualquer script local, não um risco novo; licença CC0, binário único em Rust.

## Clientes de banco de dados

Um cliente de banco de dados, seja de linha de comando ou uma interface gráfica, não introduz um nível de acesso próprio na maioria dos casos: autentica com usuário e senha, ou certificado, e os privilégios dentro do banco são os da conta usada para conectar, os mesmos que qualquer outra ferramenta teria com a mesma credencial.

A exceção é uma interface administrativa web servida via HTTP, como o pgAdmin rodando em container: publicar essa porta em todas as interfaces de rede, em vez de restringi-la a `127.0.0.1`, equivale a publicar uma interface administrativa completa do banco para qualquer coisa que alcance a rede do host.

| Categoria | Ferramentas |
| --- | --- |
| CLI oficial | `psql` (PostgreSQL), `mysql` (MySQL/MariaDB) |
| CLI com autocompletar | `mycli` |
| GUI multi-banco | DBeaver |
| GUI web (PostgreSQL) | pgAdmin |
| IDE paga | DataGrip |

A escolha entre um cliente de linha de comando e uma GUI multi-banco como o DBeaver depende do quanto administrar múltiplos tipos de banco com uma única ferramenta pesa mais que a leveza de um cliente sem dependência além do próprio pacote. A edição paga de uma IDE como o DataGrip só se justifica para quem já usa outras ferramentas do mesmo fabricante, ou precisa de refatoração de schema assistida.

Um backup feito com `pg_dump` ou `mysqldump` pela linha de comando é lógico, não físico com PITR: para dados que exigem recuperação em ponto no tempo, esse comando manual não substitui uma estratégia de backup contínuo do próprio banco gerenciado.

## Transferência de arquivos

As ferramentas de transferência entre hosts se dividem por operação, não por qual é "melhor": cópia pontual sobre SSH sem servidor adicional, sincronização incremental que só transfere o que mudou, navegação visual do filesystem remoto (uma GUI, ou montagem local do sistema de arquivos) e sincronização com armazenamento de objetos compatível com S3.

Todas herdam a identidade e o privilégio da sessão usada para autenticar; nenhuma introduz um controle de acesso próprio além do que a conta remota já permite.

| Ferramenta | Uso típico |
| --- | --- |
| `scp` | cópia pontual, sem retomar transferência interrompida |
| `sftp` | sessão interativa para navegar antes de copiar |
| `rsync` | sincronização recorrente, transfere só o que mudou |
| FileZilla | GUI multiplataforma para transferência manual frequente |
| `sshfs` | monta o filesystem remoto via FUSE para edição pontual |
| `mc` | espelha diretórios locais com um bucket S3-compatível |

O risco específico de cada uma aparece fora do modelo de credencial: um comando de sincronização com a opção de espelhar o destino remove ali o que não existe mais na origem, então invertê-lo por engano apaga dados do lado errado. Um ponto de montagem de filesystem remoto esquecido numa máquina compartilhada expõe esse filesystem a qualquer usuário local com permissão de leitura sobre ele.

| Ferramenta | Onde o risco mora |
| --- | --- |
| `rsync --delete` | espelha o destino, apagando ali o que não existe mais na origem |
| FileZilla | guarda credenciais de conexões salvas em `sitemanager.xml` sem criptografia por padrão |
| `mc` | guarda o par de chaves de acesso em `~/.mc/config.json` em texto claro |

## Observabilidade complementar

Além do `kube-prometheus-stack` e do Loki já cobertos como template operacional, algumas ferramentas pontuais preenchem lacunas específicas sem duplicar esse desenho. `promtool` e `logcli` consultam Prometheus e Loki diretamente do terminal, sem passar pelo Grafana; nenhum dos dois é uma operação destrutiva, e a validação de regras nem chega a fazer uma chamada de rede.

O `blackbox-exporter` sonda um endpoint HTTP, TCP, ICMP ou DNS que não expõe métricas nativamente e transforma o resultado em métricas Prometheus. Ele roda dentro do cluster, então falha junto com ele numa perda total do host, e não substitui uma verificação de disponibilidade externa, só complementa a cobertura interna.

O Grafana Tempo é uma alternativa ao Jaeger como backend de traces, que se integra ao mesmo painel do Grafana já usado para métricas e logs em vez de exigir uma interface própria. A escolha entre os dois depende mais de onde a equipe já centraliza a observação do que de uma diferença técnica decisiva.

Um serviço de monitoramento externo de disponibilidade, seja um SaaS de uptime, um serviço de heartbeat para jobs periódicos, ou um servidor autogerenciado fora do cluster, precisa ter sua própria indisponibilidade percebida por outro canal antes de ser adotado; um monitor não pode ser o único ponto de verificação de si mesmo.

## Continue por aqui

[Modelo de ameaças](../arquitetura/modelo-de-ameacas.md) aplica esse mesmo raciocínio de credencial e raio de dano à arquitetura real deste repositório. [RBAC do Kubernetes](kubernetes/access/rbac.md) detalha o mecanismo que uma interface Kubernetes bem desenhada respeita em vez de contornar.
