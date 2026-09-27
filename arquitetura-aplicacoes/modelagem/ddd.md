# DDD

Domain-Driven Design, ou DDD, é uma abordagem para modelar software a partir do domínio do negócio. O foco não é escolher um framework ou produzir uma hierarquia de diretórios, mas construir um modelo que represente conceitos, regras, eventos e fronteiras relevantes para o problema.

DDD é mais útil quando o domínio possui regras importantes, vocabulário próprio, mudanças frequentes ou várias partes que parecem usar as mesmas palavras com significados diferentes. Para um CRUD sem comportamento relevante, aplicar todos os padrões de DDD pode adicionar cerimônia sem proteger uma decisão importante.

## Domínio e modelo de domínio

O domínio é a parte do problema que o sistema precisa compreender. Em um sistema de pedidos, ele pode incluir disponibilidade, preço, desconto, pagamento, expedição e cancelamento. O domínio não é sinônimo de banco de dados, telas ou endpoints.

O domain model é a representação desses conceitos e regras no software. Ele pode conter entidades, objetos de valor, aggregates, serviços e eventos. Um modelo de domínio não precisa reproduzir todas as tabelas, e uma tabela pode ser apenas um detalhe de persistência de um conceito mais rico.

O modelo deve ser testável sem depender de HTTP ou de uma conexão com PostgreSQL. Isso não significa que todo comportamento precise estar em entidades grandes. A regra deve viver no lugar que melhor expressa sua responsabilidade.

## Linguagem ubíqua

Ubiquitous Language é o vocabulário compartilhado por pessoas do negócio e desenvolvimento dentro de um bounded context. O termo deve ter o mesmo significado em conversa, documentação, código, testes e observabilidade.

Se a equipe usa "publicar" para significar tornar um conteúdo visível, não convém usar `publish` em um ponto e `approve` em outro sem declarar a diferença. Quando dois grupos usam "cliente" para conceitos diferentes, a ambiguidade é um sinal de que existem modelos ou contextos distintos.

## Bounded Context

Um bounded context é uma fronteira dentro da qual um modelo e sua linguagem permanecem consistentes. A mesma palavra pode ter significados diferentes em contextos diferentes sem que exista uma contradição.

Por exemplo, "produto" pode ser um item comercial no contexto de vendas e um item de catálogo no contexto editorial. O limite pode ser um módulo de um monólito, um serviço, uma equipe ou uma combinação dessas dimensões. Um bounded context não exige microsserviço.

As relações entre contextos devem ser explícitas. Uma integração pode usar uma API, eventos, um anti-corruption layer ou um processo de tradução. Compartilhar tabelas e classes entre contextos reduz o custo inicial, mas acopla os modelos e torna as mudanças mais difíceis de governar.

## Aggregates e consistência

Um aggregate é um conjunto de objetos tratado como uma unidade de consistência. O aggregate root é a entidade que representa sua entrada pública. Alterações externas devem passar pela raiz, que protege invariantes e decide quais objetos internos podem mudar.

Considere um pedido:

```text
Order, aggregate root
  OrderItem, entidade interna
  Money, value object
  regras: itens precisam existir, total não pode ser negativo, pedido pago não pode ser cancelado
```

O código que cancela o pedido chama `order.cancel()`. Ele não altera diretamente uma coluna interna de `OrderItem` para contornar a regra. O aggregate não deve ser confundido com uma transação que inclui todas as tabelas relacionadas ao pedido. O limite deve ser pequeno o bastante para preservar consistência sem criar contenção desnecessária.

Uma referência a outro aggregate normalmente é um identificador, não uma árvore inteira de objetos. Se `Order` precisa conhecer todos os detalhes de `Customer`, o limite pode estar errado ou a operação pode precisar de uma política de aplicação que coordene dois aggregates.

## Entidade e value object

Uma entity possui identidade que permanece relevante ao longo do tempo. Dois pedidos com os mesmos valores podem ser pedidos diferentes porque possuem identificadores e históricos diferentes.

Um value object é definido por seus valores e normalmente é imutável. Duas instâncias de `Money(100, BRL)` representam o mesmo valor conceitual. Endereço, intervalo de datas, código de moeda e e-mail podem ser value objects quando suas regras justificam essa modelagem.

```php
final class Money
{
  public function __construct(
    public readonly int $cents,
    public readonly string $currency,
  ) {
    if ($cents < 0) {
      throw new InvalidArgumentException('Amount cannot be negative');
    }
  }
}
```

O exemplo mostra uma regra no value object, mas não define que toda string precisa virar uma classe. A abstração deve proteger invariantes ou expressar um conceito que tenha significado no domínio.

## Repository e domain service

Um repository é uma abstração para carregar e persistir aggregates sem expor ao domínio o mecanismo de armazenamento. O contrato pertence ao lado que precisa dele; a implementação pode usar PostgreSQL, uma API ou outro meio.

```php
interface OrderRepository
{
  public function find(OrderId $id): ?Order;
  public function save(Order $order): void;
}
```

Um domain service representa uma regra que não pertence naturalmente a uma única entidade ou value object. Ele não deve virar um depósito para qualquer lógica. Se uma regra usa apenas dados de `Order`, provavelmente pertence ao aggregate. Se coordena uma política entre vários conceitos, um serviço de domínio pode ser adequado.

## Business capability

Business capability descreve uma capacidade que o negócio precisa exercer, como cobrança, identidade, catálogo ou expedição. Ela é uma lente útil para descobrir fronteiras, mas não determina automaticamente a divisão técnica.

Uma capability pode ser implementada por um módulo, vários componentes ou um processo manual. O mapeamento deve considerar ownership, dados, regras, ciclo de vida e mudança esperada, não apenas o organograma.

## Exemplo de caso de uso

Para "fazer pedido", a aplicação pode seguir este fluxo:

1. o controller converte a requisição em um input DTO;
2. o application service ou command handler carrega o `Order` por seu repository;
3. o aggregate verifica estoque, itens e invariantes;
4. a aplicação persiste o aggregate dentro de uma transação;
5. um domain event `OrderPlaced` é publicado depois do commit, diretamente ou via outbox;
6. consumidores atualizam projeções, enviam notificações ou iniciam expedição.

O domínio não precisa saber se o controller é HTTP, se a persistência usa Eloquent ou se o evento será entregue por RabbitMQ. Essas decisões ficam nas bordas.

## DDD estratégico e tático

DDD estratégico trata limites, linguagem, relações entre contextos e capacidades. DDD tático trata os elementos usados dentro de um contexto, como entities, value objects, aggregates, repositories, domain services e domain events.

Os padrões táticos não devem ser aplicados antes de esclarecer o problema. Um sistema pode usar bounded contexts e linguagem ubíqua sem transformar cada linha em um aggregate. Também pode ter um modelo rico em um módulo e uma leitura simples em outro.

## O que DDD não é

DDD não é sinônimo de orientação a objetos, microsserviços, Event Sourcing, CQRS ou uma coleção obrigatória de classes. Esses estilos podem compor uma solução, mas são decisões independentes. O objetivo do DDD é reduzir ambiguidade e proteger regras do domínio, não aumentar o número de abstrações.

## Relações

- [Arquitetura em camadas](../fronteiras/arquitetura-em-camadas.md) separa responsabilidades técnicas sem substituir o modelo de domínio.
- [Arquitetura Hexagonal](../fronteiras/arquitetura-hexagonal.md) protege o domínio por portas e adapters.
- [Vertical Slice Architecture](../organizacao/vertical-slice.md) organiza o código por comportamento e pode ser usada dentro de um bounded context.
- [CQRS](../cqrs/cqrs.md) separa modelos e operações de leitura e escrita quando isso resolve um problema real.
- [Event Sourcing](../event-sourcing/event-sourcing.md) armazena mudanças como eventos e não é requisito para DDD.
- [Use Cases](../../engenharia-software/requisitos/use-cases.md) descreve objetivos e fluxos observáveis da aplicação.

## Fontes

- [Domain-Driven Design, Eric Evans](https://www.domainlanguage.com/ddd/)
- [Domain-Driven Design Reference, Eric Evans](https://www.domainlanguage.com/ddd/reference/)
- [Vaughn Vernon, Implementing Domain-Driven Design](https://vaughnvernon.com/)
- [Martin Fowler, Bounded Context](https://martinfowler.com/bliki/BoundedContext.html)
- [Martin Fowler, Aggregate](https://martinfowler.com/bliki/DDD_Aggregate.html)
