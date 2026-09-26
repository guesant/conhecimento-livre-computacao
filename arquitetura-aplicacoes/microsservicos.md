# Microsserviços

Microsserviços são uma arquitetura formada por serviços relativamente pequenos, organizados em capacidades de negócio, com processos de desenvolvimento, deploy e operação independentes. O tamanho do serviço não é a propriedade central. A autonomia, o contrato e a responsabilidade pelos dados são mais importantes que uma contagem de linhas.

## Características

Uma arquitetura de microsserviços costuma ter:

- serviços alinhados a capacidades ou bounded contexts;
- deploy e escala independentes;
- contratos de rede ou mensagens;
- ownership de dados por serviço;
- automação de build e entrega;
- observabilidade distribuída;
- tolerância a falhas parciais;
- equipes capazes de operar o que constroem.

Uma coleção de containers que compartilha um banco, exige deploy conjunto e possui chamadas síncronas encadeadas pode ser uma aplicação distribuída, mas não oferece todas as propriedades normalmente esperadas de microsserviços.

## Fronteiras

Fronteiras devem seguir regras de negócio que mudam juntas, têm vocabulário próprio e podem ter dados governados pelo mesmo dono. Separar por `users-service`, `database-service` e `controller-service` geralmente cria chamadas entre camadas, não serviços autônomos.

Um serviço deve expor uma API ou eventos suficientes para seus consumidores, sem exigir que eles leiam suas tabelas. Compartilhar banco de dados permite uma transição, mas cria acoplamento de schema e dificulta mudanças independentes.

## Comunicação

HTTP, gRPC e mensageria são opções. Chamadas síncronas são simples de entender, mas acoplam disponibilidade e latência. Mensagens reduzem acoplamento temporal, mas introduzem duplicação, ordenação, reprocessamento e consistência eventual.

Chamadas remotas devem ser mais grossas que chamadas internas. Converter cada função de um monólito em uma chamada RPC cria um sistema chatty, com latência multiplicada e falhas difíceis de localizar.

## Dados e consistência

Cada serviço deve ser responsável pelo seu modelo de dados. Isso não exige um produto de banco diferente para cada serviço, mas exige que outros serviços acessem o dado pela API ou por eventos, e não diretamente por tabelas internas.

Transações distribuídas são caras e frágeis. Use invariantes locais, outbox, idempotência, consumidores reprocessáveis e operações compensatórias quando consistência eventual for aceitável. Se a regra exige uma transação única e forte, manter a capacidade no mesmo módulo pode ser a decisão correta.

## Operação

Microsserviços exigem descoberta, identidade entre serviços, configuração, secrets, rate limiting, timeouts, retries, circuit breakers, tracing, logs correlacionados, métricas e testes de contrato. Cada serviço também precisa de health checks, limites de recursos, rollback e política de compatibilidade.

O custo não é apenas Kubernetes. Mesmo em containers simples, a equipe precisa diagnosticar rede, dependências, filas, bancos e versões parcialmente atualizadas.

## Migração

Uma migração segura começa por uma capacidade com baixo acoplamento e alto valor operacional. Publique o novo serviço, introduza uma interface, mova consumidores gradualmente, migre dados e remova a dependência antiga. Cada passo deve ser uma melhoria que possa ser mantida se a migração parar.

Não faça uma reescrita integral como requisito para obter o primeiro benefício. Um monólito modular e serviços ao redor podem coexistir durante a evolução.

## Quando evitar

Evite microsserviços quando a equipe não consegue operar a plataforma, quando os domínios ainda não são compreendidos ou quando a maior parte das mudanças atravessa todos os serviços. A distribuição não corrige limites ruins; ela torna seus custos mais difíceis de esconder.

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Martin Fowler, microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html)
- [Martin Fowler, breaking a monolith](https://martinfowler.com/articles/break-monolith-into-microservices.html)
