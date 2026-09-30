# Monólito modular

Monólito modular é uma aplicação publicada como uma unidade de execução e deploy, mas
organizada internamente em módulos com fronteiras explícitas. O processo, o ciclo de
deploy e muitas vezes o banco de dados são compartilhados. O compartilhamento não deve
significar que qualquer módulo pode acessar qualquer classe, tabela ou estado interno.

O objetivo é obter uma unidade operacional simples sem transformar o código em um bloco
indivisível. A modularidade é uma propriedade do desenho interno, não uma consequência
de haver vários repositórios, vários containers ou várias APIs HTTP.

## O que um módulo representa

Um módulo deve representar uma capacidade de negócio, um contexto delimitado ou uma
responsabilidade que possa ser explicada sem depender de detalhes internos de outros
módulos. A escolha não precisa ser definitiva, mas deve ser mais estável do que uma
divisão por controller, tabela ou tipo de framework.

Um módulo normalmente possui:

- uma API pública para os demais módulos;
- casos de uso ou comandos que representam operações permitidas;
- consultas próprias e contratos de leitura;
- entidades, regras e adaptadores internos;
- testes que verificam seu comportamento e suas fronteiras;
- ownership explícito sobre seus dados e decisões.

O fato de dois módulos usarem o mesmo banco não torna todas as tabelas uma API pública.
O acesso aos dados deve passar por uma interface do módulo proprietário ou por uma
integração deliberadamente documentada.

## Fronteiras de código

Uma estrutura possível para uma aplicação Java é:

```text
com.example.application
  billing
    api
    application
    domain
    infrastructure
  catalog
    api
    application
    domain
    infrastructure
  shared
```

O pacote `api` contém os contratos que podem ser consumidos por outros módulos. Os
pacotes `application`, `domain` e `infrastructure` são detalhes internos. Uma regra de
arquitetura deve impedir que `catalog` importe diretamente uma classe interna de
`billing`.

A visibilidade da linguagem ajuda, mas não é suficiente. Classes públicas demais,
pacotes compartilhados sem critério e tabelas acessadas diretamente enfraquecem a
fronteira mesmo quando o compilador aceita o código. Testes de arquitetura devem
verificar dependências entre pacotes e módulos.

## Contratos entre módulos

O contrato pode ser uma chamada direta para uma interface pública, uma mensagem de
comando ou um evento. A escolha depende do significado da operação.

Uma chamada direta é apropriada quando o consumidor precisa de uma resposta imediata e
aceita depender do contrato síncrono. Um comando representa uma solicitação para que um
módulo execute uma mudança. Um evento informa que algo já aconteceu e permite que vários
consumidores reajam sem que o publicador conheça suas implementações.

Esses contratos devem usar tipos próprios, e não expor entidades persistentes, sessões do
ORM ou estruturas internas. Isso reduz o acoplamento com o modelo de dados e permite que
um módulo seja extraído posteriormente sem reproduzir toda a estrutura interna.

## Banco e transações

Um monólito modular pode utilizar um único banco e ainda assim manter ownership lógico
dos dados. Cada módulo deve saber quais tabelas pode escrever. Leituras cruzadas devem
ser raras, justificadas e preferencialmente encapsuladas por uma consulta pública ou por
um modelo de leitura específico.

Transações locais são uma vantagem do monólito. Um caso de uso pode atualizar mais de
uma tabela dentro da mesma transação sem introduzir coordenação distribuída. Essa
vantagem não autoriza qualquer módulo a modificar dados de outro módulo, porque o
acoplamento criado dificultará uma futura separação.

Quando uma operação precisa notificar outro módulo, o evento deve ser publicado em um
ponto coerente com a transação. Um evento publicado antes do commit pode anunciar uma
mudança que será revertida. Um evento publicado depois do commit precisa de um mecanismo
de publicação confiável se a perda da notificação for inaceitável.

## Barramento interno em Java

Um barramento em processo pode organizar a comunicação sem transformar o monólito em
uma arquitetura distribuída. Ele apenas despacha objetos dentro do mesmo runtime.

Os papéis mais comuns são:

| Abstração | Intenção | Retorno típico |
| --- | --- | --- |
| Chamada direta | Invocar uma operação conhecida | Resultado imediato |
| Command bus | Solicitar uma mudança | Resultado ou confirmação |
| Query bus | Consultar dados ou uma projeção | DTO de leitura |
| Event bus | Notificar algo que aconteceu | Nenhum retorno obrigatório |

Um command bus normalmente seleciona um único handler por tipo de comando. Um query bus
faz o mesmo para uma consulta, mantendo a separação entre leitura e escrita no nível da
aplicação. Um event bus pode chamar vários handlers e, por isso, não deve ser tratado
como uma função que sempre terá um resultado único.

Em Java com Spring, `ApplicationEventPublisher` fornece publicação de eventos da
aplicação. Em uma configuração síncrona, os listeners são executados na mesma chamada e
podem fazer a operação original falhar. Isso é útil quando a reação faz parte da mesma
transação, mas é inadequado quando o consumidor é opcional ou lento.

O Spring Modulith adiciona convenções para módulos, eventos e testes de fronteira. Um
listener transacional assíncrono pode executar depois do commit, em outra transação. A
publicação precisa ser persistida quando a entrega não puder ser perdida. O registro de
publicações de eventos permite acompanhar publicações pendentes e tentar novamente a
entrega.

O barramento deve continuar pequeno. Colocar cada chamada trivial atrás de um dispatcher
genérico cria rastreamento indireto, dificulta o debug e esconde as dependências. Use o
barramento quando ele representar uma semântica real, como comando, consulta ou evento,
e não apenas para evitar uma chamada de método explícita.

## Testes de modularidade

Os testes devem cobrir três níveis diferentes:

- testes do módulo, sem carregar toda a aplicação;
- testes de contrato da API pública do módulo;
- testes de arquitetura que proíbem imports e acessos internos indevidos.

Uma integração entre módulos pode usar um cenário que publica um comando ou evento e
verifica o resultado observável. O teste não deve depender de detalhes privados do
consumidor. Isso mantém o contrato estável mesmo quando a implementação muda.

Além dos testes, uma ferramenta de análise pode verificar ciclos, dependências proibidas,
pacotes públicos e módulos que acessam o banco de outro módulo. A verificação deve rodar
no CI para impedir a degradação gradual das fronteiras.

## Operação

O monólito modular continua sendo uma unidade de deploy. Logs, métricas, tracing,
configuração, health checks e rollback são operados no nível da aplicação, embora possam
expor dimensões por módulo e por caso de uso.

Essa propriedade reduz o número de componentes que precisam ser monitorados. Em
contrapartida, um módulo que consome muita CPU, memória ou conexões ao banco pode afetar
os demais. A aplicação pode precisar de filas internas, limites, pools separados ou
workers específicos antes de justificar um processo independente.

## Caminho para extração

Uma boa fronteira modular reduz o custo de extrair um serviço, mas não garante que a
extração será necessária ou simples. Antes de separar um módulo, verifique se ele possui:

- contrato público suficientemente estável;
- ownership claro dos dados;
- poucas dependências síncronas;
- requisitos de escala ou disponibilidade diferentes;
- observabilidade e operação próprias;
- uma estratégia para consistência e falhas de rede.

O primeiro passo costuma ser substituir acessos internos por contratos. Depois, a
persistência pode ser isolada, o transporte pode mudar para HTTP, gRPC ou mensagens, e
os testes de contrato passam a proteger a fronteira distribuída.

## Falhas comuns

Um monólito modular falha quando os módulos são apenas diretórios, quando todos importam
um pacote `common` que contém regras de negócio, quando há tabelas compartilhadas sem
ownership, ou quando um event bus esconde chamadas síncronas obrigatórias.

Outro problema é chamar a aplicação de modular apenas porque ela usa um framework que
possui módulos. A modularidade exige limites verificáveis, contratos explícitos e um
modelo de dependência que possa ser explicado.

## Fontes

- [Spring Modulith, fundamentos](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- [Spring Modulith, eventos da aplicação](https://docs.spring.io/spring-modulith/reference/events.html)
- [Spring Modulith, testes](https://docs.spring.io/spring-modulith/reference/testing.html)
- [Martin Fowler, monolith first](https://martinfowler.com/bliki/MonolithFirst.html)
- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
