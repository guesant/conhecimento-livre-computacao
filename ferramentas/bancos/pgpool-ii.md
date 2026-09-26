# Pgpool-II

Pgpool-II é um proxy e pooler para PostgreSQL. Ele mantém conexões com os backends, pode reutilizá-las, distribuir algumas leituras, executar health checks e participar de failover conforme a topologia configurada.

Ele não transforma um PostgreSQL isolado em um cluster, não substitui replicação, não cria consistência entre servidores e não substitui um sistema de backup. O PostgreSQL continua sendo responsável por transações, WAL, locks e armazenamento. O Pgpool-II fica no caminho entre clientes e servidores e acrescenta suas próprias decisões e failure modes.

## Onde fica

Uma composição típica possui:

```text
cliente -> Pgpool-II -> PostgreSQL primary
                    -> PostgreSQL standby
```

O primary recebe escritas. A standby pode receber WAL e atender determinadas leituras. O Pgpool-II pode detectar indisponibilidade, alterar o destino de conexões ou executar scripts de failover, mas a promoção e a autoridade de escrita precisam ser coordenadas com a solução de replicação e com o mecanismo de fencing.

Adicionar Pgpool-II introduz uma camada a mais para autenticação, TLS, limites de conexão, observabilidade e troubleshooting. Um problema no proxy pode afetar clientes mesmo que o PostgreSQL esteja saudável.

## Pooling de conexões

O pool reutiliza conexões persistentes com propriedades compatíveis, como usuário, banco e parâmetros de execução. Isso reduz o custo de criar conexões repetidamente e pode proteger o PostgreSQL contra uma explosão de conexões curtas.

O dimensionamento precisa considerar os processos do Pgpool-II e o cache por processo. O número de conexões nos backends pode crescer aproximadamente com a combinação de processos filhos e conexões armazenadas, além de conexões de health check, administração, replicação e outros componentes. Não configure o limite do proxy ignorando `max_connections` do PostgreSQL.

Uma conexão reutilizada precisa ser limpa entre sessões. Estado de sessão, transação aberta, temporary tables, prepared statements, `SET`, advisory locks, `LISTEN`, cursores e `search_path` podem vazar comportamento de uma aplicação para outra se a política de reset não for adequada.

O pooling também não corrige uma aplicação que mantém transações abertas enquanto espera por rede ou usuário. A conexão pode continuar ocupada e reter locks mesmo estando atrás de um pool.

## Load balancing de leituras

O Pgpool-II consegue distribuir algumas consultas de leitura para backends elegíveis, especialmente em configurações com streaming replication. A decisão depende do modo, do estado da sessão e da forma da consulta.

Uma leitura não deve ser enviada para uma réplica apenas porque começa com `SELECT`. Consultas com `FOR UPDATE`, `FOR SHARE`, funções que escrevem, DDL, `VACUUM`, transações read-write, `SERIALIZABLE` e operações que precisam observar uma escrita recente devem permanecer no primary conforme as regras da configuração.

Mesmo quando o roteamento é tecnicamente permitido, a réplica pode estar atrasada. Depois de uma escrita, uma leitura no standby pode não enxergar o resultado. O contrato precisa decidir entre read-after-write no primary, espera por posição de replay, atraso máximo aceito ou consistência eventual explícita.

O load balancing distribui leituras, mas não cria capacidade de escrita. Consultas pesadas também podem apenas deslocar a pressão do primary para a réplica ou saturar a rede e o armazenamento.

## Health checks e failover

Health checks conectam periodicamente aos backends e podem acionar failover ou marcar um nó como indisponível. Cada check consome conexão e carga; o número de conexões disponíveis precisa incluir essa margem.

Falha de rede transitória não é prova de que o PostgreSQL morreu. Configure timeout, intervalo e quantidade de retries para evitar flapping. Um failover incorreto pode produzir dois nós aceitando escrita, perder read-after-write ou direcionar tráfego para uma réplica ainda atrasada.

O Pgpool-II não deve ser o único mecanismo de eleição. Para promover um PostgreSQL, a arquitetura precisa definir:

- quem possui a autoridade de escrita;
- como o primary antigo é isolado ou desabilitado;
- como o endpoint é atualizado;
- como a réplica escolhida é validada;
- como conexões existentes são encerradas ou renovadas;
- como o nó antigo volta sem causar split brain;
- como a aplicação trata retry sem duplicar efeitos.

Watchdog e múltiplas instâncias do Pgpool-II podem reduzir o ponto único de falha do proxy, mas também exigem quorum, endereço virtual ou mecanismo equivalente, fencing, sincronização de configuração e testes de partição.

## Query cache

Cache de consulta no proxy pode retornar dados antigos e não entende automaticamente todos os efeitos de funções, mudanças externas, permissões, invalidadores e dependências. Para dados editoriais ou leituras explicitamente tolerantes a staleness, um cache na aplicação ou em uma camada de dados costuma tornar o contrato mais visível. Não habilite cache de query como tentativa genérica de corrigir SQL lento.

## Segurança

O Pgpool-II deve ficar em uma rede de aplicação ou administrativa, não exposto diretamente à internet. Use autenticação individual ou credenciais de serviço com menor privilégio, TLS quando o caminho exigir, regras de rede, rotação de secrets e logs sem senhas.

Health checks também usam credenciais. Essas credenciais precisam existir nos backends necessários e não devem ser compartilhadas com a aplicação sem motivo. O arquivo de senhas do Pgpool-II e os secrets de backend devem ter permissões restritas.

## Observabilidade

Monitore separadamente:

- conexões de clientes e backends;
- conexões em espera e fila de accept;
- hit rate e descarte do pool;
- tempo de health check e quantidade de retries;
- backend selecionado e motivo de failover;
- latência no proxy e latência observada no PostgreSQL;
- erros de autenticação, reset e protocolo;
- atraso de replay das réplicas;
- estado do watchdog e da autoridade de escrita.

Uma latência alta no cliente não prova que o PostgreSQL está lento. Compare o tempo antes do proxy, no proxy e no backend, mantendo um identificador de requisição ou `application_name` quando possível.

## Quando usar

Pgpool-II é interessante quando a arquitetura realmente precisa combinar pooling, roteamento de leituras, health checks ou integração operacional com uma topologia PostgreSQL existente. Para um único servidor pequeno, ele pode adicionar complexidade maior que o benefício. Para pooling simples, compare também um pooler com escopo mais estreito e escolha pela necessidade real de failover e roteamento.

Antes de adotar, teste:

1. conexão, autenticação e reset de sessão;
2. transações longas e prepared statements;
3. leitura depois de escrita;
4. atraso de réplica;
5. queda do primary e retorno do nó antigo;
6. queda do próprio Pgpool-II;
7. partição de rede e comportamento do watchdog;
8. saturação de conexões e backpressure.

## Relações

- [Replicação](../../dados/replicacao.md) explica primary, réplica, lag e failover.
- [Clustering, redundância e distribuição](../../dados/clustering-redundancia-e-distribuicao.md) diferencia proxy, replicação e cluster.
- [PostgreSQL: `pg_stat`, índices e otimização](../../dados/postgresql-pg-stat-indices-e-otimizacao.md) ajuda a separar latência do banco e da camada intermediária.
- [Migrações de schema, locks e transações](../../dados/migracoes-schema-locking.md) trata operações que podem bloquear o backend.

## Fontes

- [Documentação oficial do Pgpool-II](https://www.pgpool.net/docs/latest/en/html/)
- [Pgpool-II, connection pooling](https://www.pgpool.net/docs/latest/en/html/runtime-config-connection-pooling.html)
- [Pgpool-II, load balancing](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html)
- [Pgpool-II, health check](https://www.pgpool.net/docs/latest/en/html/runtime-config-health-check.html)
- [Pgpool-II, watchdog](https://www.pgpool.net/docs/latest/en/html/runtime-watchdog-config.html)
