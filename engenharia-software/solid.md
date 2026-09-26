# SOLID

SOLID é um acrônimo para cinco princípios de desenho orientado a objetos: Single
Responsibility, Open/Closed, Liskov Substitution, Interface Segregation e Dependency
Inversion. Eles ajudam a controlar acoplamento e tornar mudanças localizadas, mas não
são regras para criar interfaces, classes ou abstrações em quantidade arbitrária.

## Single Responsibility Principle

Uma unidade deve ter uma responsabilidade coerente e uma razão de mudança relacionada a
um mesmo ator ou preocupação. Responsabilidade não significa possuir apenas um método.
Uma classe de caso de uso pode orquestrar várias operações sem assumir também persistência,
renderização, envio de email e política de retry.

Uma classe que valida entrada, calcula regra, salva no banco e publica uma mensagem pode
ter várias razões independentes para mudar. Separe responsabilidades quando isso tornar
ownership, teste e mudança mais claros. Extrair métodos sem reduzir acoplamento apenas
move o problema.

## Open/Closed Principle

Uma unidade deve permitir extensão por um contrato estável sem exigir alteração constante
do código que já funciona. Estratégias, handlers e adapters são formas possíveis de
adicionar comportamento.

O princípio não significa nunca modificar código existente. Alterar uma regra central
quando o requisito mudou pode ser mais simples e seguro que criar uma hierarquia de
plugins. A extensão deve ser justificada por variação real e protegida por testes.

## Liskov Substitution Principle

Um subtipo deve poder ser usado onde o tipo base é esperado sem quebrar as propriedades
que o consumidor depende. Isso envolve pré-condições, pós-condições, invariantes, erros e
efeitos observáveis, não apenas compatibilidade de assinatura.

Uma implementação que aceita menos entradas que o contrato, retorna um significado
diferente para o mesmo resultado ou lança uma exceção inesperada pode violar substituição
mesmo que compile. Herança não é necessária para o problema aparecer; implementações de
uma interface também precisam respeitar o contrato.

## Interface Segregation Principle

Consumidores não devem depender de métodos que não usam. Interfaces pequenas e orientadas
ao papel reduzem mudanças desnecessárias e tornam substitutos mais simples.

Isso não exige criar uma interface para cada método. Uma interface com operações que sempre
mudam juntas pode ser melhor que várias interfaces artificiais. O critério é observar os
consumidores e separar contratos quando eles possuem necessidades ou ritmos de mudança
diferentes.

## Dependency Inversion Principle

Regras de alto nível não devem depender diretamente de detalhes de baixo nível. Ambos
devem depender de abstrações estáveis, e os detalhes devem implementar os contratos que a
regra precisa.

Em um caso de uso, uma porta de persistência pode expressar a operação necessária sem
expor o ORM, SQL ou cliente HTTP. A implementação concreta é conectada na composição da
aplicação. Isso não significa que toda classe precisa de uma interface; uma abstração sem
variação ou teste relevante só aumenta indireção.

## Relação entre os princípios

Os princípios se reforçam, mas não são independentes de forma rígida. Uma interface
segregada pode facilitar substituição. Inversão de dependência pode proteger um módulo de
detalhes e permitir extensão. Uma classe com responsabilidade coerente pode ficar mais
fácil de testar.

Também podem entrar em tensão. Muitas abstrações criadas para antecipar extensão podem
violar simplicidade e tornar a responsabilidade menos clara. Uma herança introduzida para
reutilizar código pode piorar substituição. A solução deve ser avaliada pelo contrato e
pelas mudanças reais, não pela contagem de interfaces.

## SOLID e monólito modular

Em um monólito modular, SOLID é útil para manter APIs públicas pequenas e impedir que um
módulo conheça detalhes internos de outro. Interfaces podem representar portas do módulo,
handlers podem organizar casos de uso e adapters podem encapsular infraestrutura.

O princípio não define a divisão dos módulos. Essa decisão deve partir de capacidades de
negócio e ownership. Um pacote por classe ou uma interface por tabela não cria um
monólito modular.

## SOLID em sistemas distribuídos

Uma interface pequena não elimina timeout, compatibilidade, autenticação, observabilidade
ou falhas parciais quando a implementação está em outro processo. A abstração deve deixar
visível que a operação é remota quando latência, erro e consistência fazem parte do
contrato.

Esconder uma chamada HTTP atrás de uma interface com aparência de função local pode
facilitar testes unitários e piorar o modelo operacional. O contrato precisa expor
deadline, cancelamento, idempotência e classificação de erro quando esses aspectos forem
relevantes.

## Como aplicar sem dogmatismo

Use SOLID para investigar sintomas:

- mudanças não relacionadas quebram a mesma unidade;
- testes precisam de infraestrutura inteira para exercitar uma regra;
- módulos importam detalhes internos uns dos outros;
- substitutos lançam erros ou retornam estados não previstos;
- contratos são grandes porque agregam consumidores diferentes;
- regras de negócio dependem diretamente de SDKs e frameworks.

Se nenhum desses problemas existe, uma abstração adicional pode não ser melhoria. Código
direto, coeso e bem testado costuma ser preferível a uma arquitetura que apenas parece
extensível.

## Relações

- [Monólito modular](../arquitetura-aplicacoes/monolito-modular.md) aplica fronteiras de
  módulos e contratos internos.
- [CQRS e camadas de aplicação](../arquitetura-aplicacoes/backend.md) separa casos de uso,
  leitura, escrita e infraestrutura quando a decisão exigir.
- [Barramento interno](../arquitetura-aplicacoes/bus-interno.md) mostra quando comandos,
  queries e eventos são contratos reais.
- [Resiliência](../confiabilidade/resiliencia.md) trata falhas que abstrações de código
  não eliminam.

## Fontes

- [Robert C. Martin, Principles of Object Oriented Design](https://principles.dev/p/tags/solid/)
- [SOLID, princípios de design](https://principles.design/examples/solid-design-principles)
- [Clean Code, capítulo sobre SOLID](https://www.oreilly.com/library/view/clean-code-a/9780135398586/ch19.xhtml)
