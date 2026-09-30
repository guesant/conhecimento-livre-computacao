# Vertical Slice Architecture

Vertical Slice Architecture organiza o sistema por funcionalidade ou caso de uso. Cada fatia reúne as partes necessárias para realizar um comportamento, em vez de espalhar todas as classes por diretórios técnicos globais.

## Horizontal e vertical

Horizontal Slicing separa por tipo técnico:

```text
controllers/
services/
repositories/
dtos/
validators/
```

Ao implementar uma funcionalidade, o leitor precisa percorrer vários diretórios. Vertical slicing aproxima os arquivos da mesma capacidade:

```text
features/orders/place-order/
  PlaceOrderController.php
  PlaceOrderCommand.php
  PlaceOrderHandler.php
  PlaceOrderValidator.php
  PlaceOrderResult.php
```

As duas organizações podem coexistir. Uma aplicação pode manter um diretório compartilhado para primitives e usar fatias para os casos de uso. O nome da pasta não corrige dependências ruins por si só.

## Feature e Use Case

Feature é uma capacidade percebida pelo usuário ou negócio, como "publicar conteúdo". Use Case é um comportamento mais específico, como "publicar uma revisão aprovada". Uma feature pode conter vários use cases e consultas.

O use case deve descrever o resultado e as regras da operação, não apenas o endpoint. O mesmo comportamento pode ser chamado por HTTP, CLI, fila ou um job agendado.

## Exemplo de fatia

```text
features/orders/
  place-order/
    PlaceOrderController.php
    PlaceOrderInput.php
    PlaceOrderCommand.php
    PlaceOrderHandler.php
    PlaceOrderValidator.php
    PlaceOrderResult.php
  get-order/
    GetOrderController.php
    GetOrderQuery.php
    GetOrderQueryHandler.php
    GetOrderResult.php
```

Uma fatia de escrita pode compartilhar o modelo de domínio com outras operações, mas não precisa compartilhar o mesmo DTO de leitura. O handler deve continuar pequeno o bastante para mostrar o fluxo e delegar regras ao domínio.

## Feature Folder e Technical Layer Folder

Feature Folder coloca no mesmo diretório os artefatos de uma capacidade. Technical Layer Folder agrupa controllers, repositories e DTOs por tipo. A escolha deve considerar navegação, ownership, tamanho do sistema, regras de dependência e frequência de mudança.

Uma equipe pequena pode começar com camadas e migrar apenas os fluxos que ficaram difíceis de acompanhar. Um sistema grande pode usar fatias para features e uma área `shared` muito restrita. Se todo arquivo acaba importando internals de toda feature, a organização visual não criou uma fronteira real.

## Relação com camadas e DDD

Uma fatia vertical não elimina Presentation, Application, Domain e Infrastructure. Ela muda a forma de agrupar os arquivos. Um controller continua sendo apresentação, um handler continua coordenando a aplicação e um repository continua sendo infraestrutura, mesmo quando vivem próximos.

DDD organiza significado e fronteiras do domínio. Vertical Slice organiza o caminho de implementação de uma capacidade. CQRS pode fornecer uma fatia para cada command e query. São decisões complementares, não sinônimos.

## Critérios de escolha

Use fatias quando mudanças em uma feature normalmente atravessam várias camadas, quando ownership é por capacidade ou quando os diretórios técnicos viraram um catálogo difícil de navegar. Use camadas globais quando o sistema é pequeno, as fronteiras ainda são incertas ou a equipe se beneficia de uma convenção simples.

Não extraia artificialmente cada endpoint para uma arquitetura própria. A fatia deve representar uma mudança ou comportamento coerente, não apenas uma rota.

## Fontes

- [Jimmy Bogard, Vertical Slice Architecture](https://www.jimmybogard.com/vertical-slice-architecture/)
- [Martin Fowler, Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
- [Use Cases](../../engenharia-software/requisitos/use-cases.md)
