# Barramento interno

Um barramento interno é uma abstração para despachar comandos, consultas ou eventos
dentro de um processo. Ele pode organizar as dependências de um monólito modular, mas
não cria isolamento de processo, independência de deploy ou tolerância a falhas de rede.

Essa distinção é importante porque a palavra bus também é usada para brokers de
mensagens, como Kafka, RabbitMQ e NATS. Um broker normalmente tem armazenamento, entrega
entre processos, retry, retenção e consumidores independentes. Um barramento em memória
pode não ter nenhuma dessas propriedades.

## Chamada direta

Uma chamada direta expressa a dependência de forma explícita:

```java
var result = catalog.findProduct(productId);
```

Ela é simples de rastrear e adequada quando o consumidor conhece a API do módulo. O
problema aparece quando todos os módulos passam a chamar internals uns dos outros.

## Command bus

Um command bus recebe uma intenção de alteração, localiza o handler correspondente e
executa o caso de uso. O comando deve representar uma operação, e não ser apenas uma
estrutura genérica com vários campos opcionais.

```java
public record RegisterCustomerCommand(String name, String email) {}

public interface CommandHandler<C, R> {
  R handle(C command);
}
```

Em geral há um handler para cada tipo de comando. O bus pode aplicar validação,
autorização, transação, logging e métricas antes de chamar o handler. Esses comportamentos
transversais devem ser previsíveis e não esconder regras de negócio.

## Query bus

Um query bus usa a mesma ideia para leituras. A consulta declara o que o consumidor
precisa e o handler retorna um DTO ou uma projeção. Isso evita que a camada de transporte
conheça repositórios, entidades ORM ou joins internos.

Queries não devem alterar estado. Se uma leitura precisar popular cache, registrar
auditoria ou disparar processamento, essa consequência precisa ser tratada como uma
decisão explícita, porque deixa de ser uma consulta sem efeitos colaterais.

## Event bus

Um evento representa um fato que já ocorreu, como `CustomerRegistered`. O publicador não
deve depender de um retorno de cada listener. Vários módulos podem reagir ao evento, e
novos consumidores podem ser adicionados sem alterar o módulo que publicou o fato.

Não confunda evento com comando. `CustomerRegistered` descreve algo concluído. `RegisterCustomer`
é uma solicitação para executar uma operação. Um evento pode ser ignorado, atrasado ou
reprocessado conforme o contrato. Um comando precisa de um destinatário responsável.

## Síncrono e assíncrono

Um bus síncrono chama o handler na mesma pilha de execução. Ele preserva uma transação
local e facilita a resposta imediata, mas latência, exceção e consumo de recursos do
handler afetam a requisição original.

Um bus assíncrono entrega o trabalho para outro executor ou fila. A requisição pode
terminar antes do handler. Isso exige um modelo de estado intermediário, retry, controle
de duplicidade, observabilidade, limites de fila e tratamento de falhas.

Executar um listener em outra thread não é o mesmo que entregar uma mensagem durável.
Se o processo morrer antes da execução, o trabalho pode ser perdido. Quando a entrega
for importante, a publicação deve ser registrada de forma transacional e processada por
um mecanismo que permita retry.

## Transações e publicação

Um evento publicado antes do commit pode ser consumido enquanto a alteração ainda pode
ser revertida. Publicá-lo depois do commit evita esse problema, mas abre uma janela entre
o commit e a publicação.

As soluções comuns têm custos diferentes:

- listener síncrono dentro da transação, simples, porém acoplado e sujeito à falha do
  consumidor;
- listener assíncrono depois do commit, com risco de perda se não houver registro;
- registro de publicação em tabela, permitindo recuperação e retry;
- outbox, quando o evento precisa sair do processo para um broker ou outro serviço.

O Spring Modulith oferece um registro de publicações para acompanhar eventos pendentes.
O nome da ferramenta não muda o princípio: a confiabilidade precisa ser parte do modelo
de entrega, não uma promessa implícita do método `publish`.

## Barramento interno e broker

| Propriedade | Barramento em processo | Broker de mensagens |
| --- | --- | --- |
| Localização | Memória do processo | Serviço ou infraestrutura separada |
| Falha principal | Falha da aplicação ou executor | Rede, broker, consumidor e aplicação |
| Persistência | Opcional e normalmente ausente | Pode oferecer retenção e confirmação |
| Deploy | Acompanha a aplicação | Pode evoluir independentemente |
| Escala | Limitada ao processo e seus workers | Consumidores podem escalar separadamente |
| Uso típico | Modularidade e coordenação local | Integração entre processos e sistemas |

Um barramento interno é uma boa ferramenta para tornar contratos de módulos explícitos.
Ele não deve ser usado para simular uma arquitetura distribuída antes que existam
requisitos para isso.

## Java e módulos

Em um monólito Java, um módulo pode publicar um evento por uma interface da aplicação e
manter seus listeners internos fora da API pública. O framework pode descobrir handlers,
mas o contrato deve continuar sendo representado por tipos estáveis e nomes semânticos.

O Spring Modulith trata os pacotes de aplicação como módulos, documenta dependências e
oferece eventos de aplicação, listeners transacionais e testes de módulos. A mesma
arquitetura pode ser implementada sem Spring, usando interfaces, um registry de handlers
e regras de pacotes.

Uma composição saudável costuma separar:

- transporte HTTP, que traduz a entrada em um comando ou query;
- aplicação, que valida autorização, transação e orquestra o caso de uso;
- domínio, que executa regras e produz eventos de domínio;
- infraestrutura, que persiste, publica ou entrega eventos;
- módulos consumidores, que dependem do contrato e não do banco interno do publicador.

## Anti-patterns

Evite um bus universal que recebe `Object`, seleciona handlers por reflexão e permite que
qualquer classe publique qualquer coisa. Esse design desloca erros de compilação para o
runtime e torna o grafo de dependências difícil de enxergar.

Também evite usar eventos para chamadas que exigem uma resposta imediata, criar listeners
que dependem da ordem acidental de execução ou fazer retry de uma alteração sem uma chave
de idempotência. Um evento duplicado é uma possibilidade normal em sistemas assíncronos.

Se o único objetivo do bus for reduzir duas linhas de chamada direta, ele provavelmente
está adicionando indireção sem resolver um problema arquitetural.

## Quando usar

Use um bus interno quando houver contratos de módulos que se beneficiem de um ponto de
despacho, comportamentos transversais consistentes ou eventos com múltiplos consumidores.
Prefira chamadas diretas quando a dependência for simples e intencional.

Antes de assíncronizar, estabeleça o comportamento de erro, a durabilidade, a ordem, a
duplicidade, o retry e a observabilidade. A ausência de uma resposta síncrona não reduz a
complexidade, apenas muda onde ela aparece.

## Fontes

- [Spring Modulith, fundamentos](https://docs.spring.io/spring-modulith/reference/fundamentals.html)
- [Spring Modulith, eventos da aplicação](https://docs.spring.io/spring-modulith/reference/events.html)
- [Spring Modulith, testes](https://docs.spring.io/spring-modulith/reference/testing.html)
- [Enterprise Integration Patterns, Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html)
- [Enterprise Integration Patterns, Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html)
