# Centralizado, distribuído e microsserviços

Centralizado, distribuído e microsserviços descrevem propriedades relacionadas, mas não equivalentes. Um sistema centralizado concentra estado, processamento ou controle. Um sistema distribuído executa componentes em processos ou hosts que se comunicam. Microsserviços são uma forma específica de organizar um sistema distribuído por capacidades de negócio, com autonomia de deploy e ownership.

## Comparação

| Dimensão | Sistema centralizado | Sistema distribuído | Microsserviços |
| --- | --- | --- | --- |
| Fronteira | Processo, cluster ou autoridade comum | Processos, hosts ou domínios separados | Serviços por capacidade de negócio |
| Comunicação | Local ou por um endpoint central | Rede, IPC, RPC ou mensagens | APIs e eventos entre serviços |
| Estado | Frequentemente concentrado | Replicado, particionado ou delegado | Dono por serviço, idealmente sem banco compartilhado |
| Falha | Pode concentrar impacto | Falhas parciais e partições | Falha parcial por serviço e dependência |
| Deploy | Geralmente coordenado | Pode ser coordenado ou independente | Independente por serviço |
| Consistência | Transações locais são mais simples | Coordenação e consistência explícitas | Consistência eventual é comum |
| Operação | Menos componentes | Mais mecanismos de coordenação | Plataforma, contratos e observabilidade distribuída |

## Sistema centralizado não significa máquina única

Uma aplicação com três réplicas atrás de um balanceador pode continuar centralizada em sua autoridade, banco e ciclo de deploy. Alta disponibilidade replica execução, mas não necessariamente distribui ownership de dados ou decisões.

Do mesmo modo, um sistema distribuído pode possuir um coordenador, uma autoridade de identidade, um banco primário ou um broker central. Distribuição não elimina pontos centrais; ela exige explicitar seus failure domains.

## Microsserviços não são sinônimo de distribuição

Microsserviços normalmente usam rede e, portanto, são distribuídos. Mas uma arquitetura distribuída não precisa ser microsserviço. Um cluster de banco, um sistema de arquivos distribuído, uma aplicação com workers e um pipeline de eventos são distribuídos sem necessariamente separar o produto em serviços por domínio.

Para chamar uma decomposição de microsserviços, procure autonomia de ciclo de vida, fronteira de capacidade, contrato estável, ownership de dados e operação independente. Containers separados ou repositórios separados não são suficientes.

## O que muda no caminho da requisição

Em um sistema centralizado, a chamada entre módulos pode ser uma função ou método, com uma transação local e uma pilha de diagnóstico única. Em um sistema distribuído, a chamada passa por DNS, conexão, TLS, proxy, autenticação, serialização e um processo remoto. O resultado pode ficar desconhecido mesmo depois que o servidor executou a operação.

Microsserviços adicionam uma preocupação adicional: o contrato precisa corresponder à capacidade de negócio. Se uma tela chama cinco serviços para montar uma resposta e todos precisam estar disponíveis, a independência pode ter sido apenas deslocada para uma cadeia de dependências.

## Dados

Centralizar dados facilita joins, transações e relatórios, mas concentra carga e acopla módulos. Distribuir dados permite ownership e escala diferente, mas exige APIs, eventos, migração, reconciliação e uma estratégia para consultas cruzadas.

Microsserviços devem evitar que consumidores leiam tabelas de outro serviço. Se a consistência de uma operação exige alterar vários domínios de maneira atômica, considere manter a operação em um módulo ou desenhar um workflow compensatório conscientemente.

## Quando cada abordagem faz sentido

Prefira centralização quando o domínio ainda está mudando, a equipe é pequena, consistência e transações locais são importantes e a operação distribuída não tem benefício medido.

Prefira distribuição quando existe requisito real de isolamento, localização, disponibilidade, escala, autonomia ou integração que não cabe em um único processo.

Prefira microsserviços quando os limites de negócio estão maduros, há equipes que podem operar serviços, o pipeline suporta releases independentes e o custo de coordenação é menor que o benefício obtido.

## Evolução

Uma sequência comum é começar com um monólito modular, extrair jobs lentos, publicar contratos estáveis e separar apenas a capacidade que apresenta um problema concreto de escala, disponibilidade ou ownership. A arquitetura também pode evoluir no sentido inverso, reunindo serviços quando a distribuição deixou de compensar seu custo.

Cada etapa deve ser reversível ou representar uma melhoria isolada. Não faça uma migração integral baseada em uma arquitetura final hipotética.

## Relação com comunicação

RPC é adequado quando o consumidor precisa de uma resposta dentro de um deadline. Comunicação assíncrona é adequada quando trabalho ou fatos podem ser processados depois. Sistemas centralizados também usam filas e workers; microsserviços também usam RPC. O estilo de comunicação não determina sozinho a topologia do sistema.

Veja [sistemas centralizados](sistemas-centralizados.md), [sistemas distribuídos](sistemas-distribuidos.md), [microsserviços](microsservicos.md), [RPC e comunicação assíncrona](../comunicacao/rpc-e-comunicacao-assincrona.md) e [comunicação assíncrona](../comunicacao/comunicacao-assincrona.md).

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Martin Fowler, microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html)
- [Google SRE book](https://sre.google/sre-book/)
