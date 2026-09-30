# Problemas de modelagem temporal

Os bugs mais difíceis de data e hora normalmente não acontecem na conversão de uma hora
visível. Eles aparecem quando uma regra de negócio usa palavras como "hoje", "ontem",
"início do dia" ou "até o fim do dia" sem dizer em qual fuso a regra deve ser avaliada.

O problema fica mais provável quando o computador da pessoa está em UTC-3, o servidor está
em UTC e o banco ou o navegador converte valores automaticamente. Cada componente pode estar
correto isoladamente, mas interpretar a mesma informação como uma categoria diferente de
tempo.

## Servidor em UTC e cliente em UTC-3

Suponha que uma pessoa em Rondônia ou em outra região UTC-3 crie um registro às 23:30 do dia
26. Para ela, o registro pertence ao dia 26. O instante correspondente é 02:30 do dia 27 em
UTC:

```text
horário local: 2026-09-26 23:30:00-03:00
instante UTC:  2026-09-27 02:30:00Z
```

Se o servidor agrupar registros pela data UTC, ele classificará esse registro no dia 27.
Se a interface converter o instante para o fuso da pessoa antes de exibir, mostrará o dia
26. Nenhum dos dois relógios está necessariamente errado. Eles estão respondendo perguntas
distintas:

- qual é a data do instante na linha do tempo global;
- qual é a data civil desse instante para uma pessoa em uma zona específica.

O erro é usar a primeira resposta para uma regra que exige a segunda.

## O significado de "hoje"

Uma consulta como esta é incompleta:

```sql
where created_at >= current_date
```

O resultado depende do timezone da sessão do banco. Mesmo que `created_at` seja
`timestamptz`, `current_date` representa a data civil da sessão, e não necessariamente a
data civil da pessoa que está usando a aplicação.

Também é perigoso comparar a representação textual convertida pelo servidor com a data que o
navegador mostra. A aplicação precisa definir o fuso da operação e construir o intervalo
nesse fuso. Para buscar os registros do dia 26 em `America/Porto_Velho`, por exemplo:

1. interpretar `2026-09-26` como data civil nessa zona;
2. calcular o início local, `2026-09-26 00:00:00`;
3. calcular o início do dia seguinte, `2026-09-27 00:00:00`;
4. converter os dois limites para instantes;
5. consultar usando `created_at >= inicio` e `created_at < proximo_inicio`.

O intervalo deve ser fechado à esquerda e aberto à direita. Assim, não é necessário inventar
`23:59:59.999`, e a consulta continua correta quando o banco armazena microssegundos ou
nanossegundos.

## Início e fim do dia

O fim de um dia local não é um instante universal fixo. Ele depende do fuso e, em zonas com
transições, a duração do dia civil pode não ser exatamente 24 horas. Uma regra que sempre
adiciona 24 horas ao início local pode produzir resultados incorretos quando uma transição de
horário ocorre entre os dois limites.

Para relatórios, expiração e filtros por data:

- receba a data e a zona explicitamente;
- derive o início da data e o início da data seguinte usando uma biblioteca de calendário;
- converta os limites para o tipo de instante usado pelo banco;
- use intervalo semiaberto;
- não dependa do timezone do processo, do container ou da sessão do banco;
- teste datas próximas à meia-noite e às transições da zona.

Uma expiração que significa "no começo do dia 27 no fuso do cliente" deve ser calculada a
partir da data civil e da zona do cliente. Uma expiração que significa "24 horas depois da
criação" deve ser calculada sobre um instante. Essas regras não são intercambiáveis.

## Quando a pessoa quer somente uma data

Nascimento, feriado, competência, vencimento civil, data de publicação editorial e data de
validade podem representar uma data sem hora. Colocar meia-noite UTC nesse campo cria um
instante artificial e permite que a conversão mude o dia exibido.

Este padrão é perigoso:

```text
valor de negócio: 2026-09-26
valor artificial: 2026-09-26T00:00:00Z
```

Ao interpretar o segundo valor em UTC-3, o navegador pode mostrar 21:00 do dia 25. A pessoa
salvou o dia 26, mas a interface apresenta o dia 25 porque uma data civil foi transformada
em instante.

Para uma data sem hora:

- transporte `YYYY-MM-DD` como texto validado ou tipo de data civil;
- use `date` no PostgreSQL;
- não aplique `Date`, `timestamp`, `timestamptz` ou Unix timestamp sem uma razão semântica;
- não acrescente `Z` apenas para tornar a string "completa";
- formate a data sem conversão de zona;
- mantenha a zona separada se a regra de negócio realmente depender dela.

Se o negócio quer "o aniversário no calendário local do usuário", a informação é uma data
civil. Se quer "o instante em que o nascimento foi registrado no hospital", são necessários
um instante e, eventualmente, a zona original.

## JavaScript: `Date` não é `DateOnly`

O objeto `Date` do JavaScript representa um instante como milissegundos desde a época Unix.
Ele não representa nativamente uma data civil sem hora. Os métodos `getFullYear`, `getMonth`
e `getDate` interpretam esse instante no fuso local do ambiente; os métodos com sufixo `UTC`
interpretam o mesmo instante em UTC.

Por isso, este código pode mudar o dia apresentado:

```js
const value = new Date("2026-09-26");
const day = value.getDate();
```

Uma string somente com data segue a interpretação de data civil em UTC na análise de `Date`.
Em um navegador UTC-3, a meia-noite UTC pode ser exibida como a noite do dia anterior. O
problema não está em `getDate` isoladamente, mas em ter usado uma classe de instante para
representar um valor que não possuía horário.

Para datas civis em JavaScript, as opções são:

- manter e validar a string `YYYY-MM-DD` quando o domínio só precisa desse contrato;
- usar `Temporal.PlainDate` quando o runtime e os navegadores suportarem a API;
- usar um polyfill ou biblioteca que possua um tipo explícito de data civil;
- evitar converter a data civil para `Date` durante transporte, comparação e renderização.

`Temporal.PlainDate` foi projetado para uma data sem hora e sem fuso, mas a disponibilidade
em navegadores ainda precisa ser verificada. A documentação da [MDN sobre
`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
e a tabela de compatibilidade devem orientar a escolha.

Para instantes, `Date` ainda pode ser usado quando o contrato e as conversões estiverem
claros. Para novos códigos que tenham suporte à API, os tipos `Temporal.Instant`,
`Temporal.ZonedDateTime` e `Temporal.PlainDate` tornam a intenção mais explícita.

## .NET: `DateOnly` separa a intenção

O .NET possui `DateOnly`, que representa ano, mês e dia sem hora e sem fuso, e `TimeOnly`, que
representa uma hora do relógio sem data e sem fuso. Essas estruturas evitam que uma data civil
seja confundida com `DateTime` ou `DateTimeOffset`.

Uma escolha comum é:

| Significado | Tipo apropriado |
| --- | --- |
| Data civil | `DateOnly` |
| Hora civil sem zona | `TimeOnly` |
| Data e hora sem zona, deliberadamente local | `DateTime` com regra explícita |
| Instante com offset | `DateTimeOffset` |
| Conversão entre regiões | `TimeZoneInfo` com uma política definida |

`DateOnly` não torna automaticamente uma data compatível com todos os formatos de API. O
contrato ainda precisa dizer que o valor é `YYYY-MM-DD` e o serializador precisa manter esse
significado. Não transforme `DateOnly` em meia-noite UTC apenas para reutilizar um campo de
timestamp.

A documentação oficial de [DateOnly](https://learn.microsoft.com/dotnet/api/system.dateonly)
e de [datas, horas e fusos no .NET](https://learn.microsoft.com/dotnet/standard/datetime/)
separa explicitamente datas civis, instantes, offsets e conversões de zona.

## Fronteiras entre camadas

Um sistema distribuído costuma ter pelo menos quatro interpretações diferentes:

1. o banco armazena um instante ou uma data civil;
2. a API serializa o valor em JSON;
3. o cliente transforma o JSON em um tipo da linguagem;
4. a interface formata o valor no fuso do usuário.

Cada fronteira deve preservar a categoria do valor. Exemplos de contratos coerentes:

```json
{
  "published_at": "2026-09-27T02:30:00Z",
  "birth_date": "1990-04-18",
  "opens_at": "09:00:00",
  "time_zone": "America/Porto_Velho"
}
```

`published_at` é um instante. `birth_date` é uma data civil. `opens_at` é uma hora local
que só pode ser interpretada completamente se a zona estiver definida no próprio registro,
na configuração do recurso ou no contexto da operação.

O contrato fica frágil quando todos esses campos são enviados como strings com `Z`, como
números Unix ou como datas sem indicação de categoria. A implementação pode parecer
consistente até alguém usar o sistema em outra zona ou perto da meia-noite.

## Serialização e desserialização

Mesmo quando o modelo interno está correto, a informação pode ser alterada ao atravessar
uma API. Serialização transforma um tipo da aplicação em JSON, texto ou número. Desserialização
faz o caminho inverso. O erro aparece quando o serializador escolhe um formato sem preservar
se a origem era um instante, uma data civil, uma hora local ou uma duração.

JSON não possui um tipo nativo para data e hora. Em geral, o protocolo usa uma string ou um
número, e o contrato precisa definir como interpretar o valor. Estes campos representam
coisas diferentes:

| Campo | Significado | Representação recomendada |
| --- | --- | --- |
| `published_at` | Instante | RFC 3339 com `Z` ou offset |
| `birth_date` | Data civil | `YYYY-MM-DD` sem `Z` |
| `opens_at` | Hora local | `HH:mm:ss` com zona definida no contexto |
| `time_zone` | Regra de zona | Identificador IANA |
| `duration_seconds` | Duração | Número com unidade explícita |

### Formatos que parecem equivalentes, mas não são

Uma API pode receber estes valores como strings:

```json
{
  "a": "2026-09-26",
  "b": "2026-09-26T00:00:00Z",
  "c": "2026-09-26T00:00:00-03:00"
}
```

`a` é uma data civil. `b` é o instante da meia-noite UTC. `c` é um instante diferente,
correspondente à meia-noite em UTC-3. Se o desserializador transformar os três em `Date`,
`DateTime` ou `timestamptz`, ele apagará a diferença semântica antes que a regra de negócio
possa decidir o que fazer.

### Falhas comuns no transporte

- O servidor serializa um horário local sem offset, e o cliente presume UTC.
- O servidor serializa uma data civil como meia-noite UTC, e o cliente a exibe no dia anterior.
- O cliente recebe um instante RFC 3339, mas o transforma em texto local e o envia de volta.
- Um valor Unix em segundos é lido como milissegundos, ou o contrário.
- O driver retorna um `timestamptz` como string, mas o ORM o converte novamente usando o fuso do processo.
- A serialização arredonda microssegundos ou nanossegundos sem que o contrato aceite a perda.
- O offset é preservado, mas o identificador regional, como `America/Sao_Paulo`, é descartado.
- `null`, string vazia e campo ausente são tratados como meia-noite ou como a data atual.
- A comparação é feita com o texto serializado em vez de ser feita sobre o tipo temporal correto.

Uma conversão dupla é particularmente perigosa. Se o banco entrega um instante já convertido
para UTC, o backend não deve aplicar novamente o offset do host. Se o backend entrega uma
data civil, o cliente não deve convertê-la para um instante apenas para usar uma API que
aceita `Date`.

### JavaScript e JSON

`JSON.stringify` não cria um tipo de data no protocolo. Quando recebe um objeto `Date`, ele
normalmente produz uma string ISO em UTC. Ao chamar `new Date` no cliente, essa string volta a
ser interpretada como instante. Esse ciclo é adequado para `published_at`, mas é inadequado
para `birth_date`.

O caminho seguro para data civil é manter a string validada ou usar um tipo próprio, como
`Temporal.PlainDate` quando disponível. Para instante, use uma string RFC 3339 ou um tipo de
instante. A decisão deve ocorrer antes da desserialização, com base no contrato do campo, e
não depois de observar qual objeto a biblioteca criou.

### .NET e JSON

No .NET, `DateOnly`, `TimeOnly`, `DateTime` e `DateTimeOffset` expressam intenções diferentes,
mas o serializador ainda precisa estar alinhado ao contrato da API. Um campo `DateOnly` deve
continuar sendo uma data `YYYY-MM-DD`; um `DateTimeOffset` deve manter o offset ou ser
normalizado segundo uma regra documentada.

Não substitua `DateOnly` por `DateTime` em um DTO apenas porque a biblioteca de transporte
possui suporte mais conveniente ao segundo tipo. Essa troca introduz uma hora artificial e
pode mudar o dia quando o valor for convertido no cliente.

### Teste de round trip

Um teste de round trip deve serializar e desserializar o valor sem mudar seu significado:

1. criar um valor de domínio com o tipo correto;
2. serializar para o formato do contrato;
3. desserializar em outra camada ou linguagem;
4. comparar a categoria e o valor, não somente a string resultante;
5. repetir em UTC, UTC-3 e uma zona com horário de verão;
6. testar `null`, ausência, precisão e limites de data.

Para um instante, compare o instante normalizado. Para uma data civil, compare ano, mês e
dia sem aplicar timezone. Para um evento recorrente, compare a data, a hora, a zona e a regra
de recorrência. Uma igualdade textual pode falhar mesmo quando dois instantes são iguais,
enquanto uma igualdade numérica pode esconder que duas datas civis foram convertidas
incorretamente.

## Testes que encontram esses bugs

Testes de data e hora precisam mudar deliberadamente o contexto temporal. No mínimo, teste:

- cliente em UTC-3 e servidor em UTC;
- cliente em UTC e servidor em uma zona regional;
- criação antes e depois da meia-noite local;
- consulta por hoje, ontem e intervalo mensal;
- datas civis no primeiro e no último dia do mês;
- transições de horário de verão em zonas que as utilizam;
- strings `YYYY-MM-DD` no navegador;
- precisão de microssegundos e nanossegundos no banco;
- serialização e desserialização em cada linguagem;
- uma API que não conhece o fuso do cliente e outra que o recebe explicitamente.

Um teste que executa sempre na timezone da máquina do desenvolvedor não protege contra esse
tipo de regressão. A zona deve ser uma variável explícita do teste, e o relógio atual deve
ser injetável quando a lógica depender de "agora".

## Checklist de revisão

Antes de aprovar uma alteração relacionada a tempo, pergunte:

- o valor é um instante, uma data civil, uma hora local ou uma duração?
- qual componente é responsável por escolher o fuso?
- o contrato contém offset ou identificador IANA quando precisa conter?
- uma conversão pode atravessar a meia-noite?
- o banco usa `date`, `timestamp` ou `timestamptz` por uma razão documentada?
- o cliente está usando `Date` para algo que não tem hora?
- o cálculo de fim do dia usa o início do próximo dia e intervalo aberto à direita?
- o teste roda com o processo, banco e navegador em zonas diferentes?

Se essas respostas não estiverem claras, a aplicação ainda não definiu o significado do seu
tempo. Corrigir a formatação sem corrigir esse significado apenas muda a aparência do bug.

## Fontes primárias

- [MDN, `Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
- [MDN, `Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
- [Microsoft Learn, `DateOnly`](https://learn.microsoft.com/dotnet/api/system.dateonly)
- [Microsoft Learn, datas, horas e fusos no .NET](https://learn.microsoft.com/dotnet/standard/datetime/)
- [PostgreSQL date/time types](https://www.postgresql.org/docs/current/datatype-datetime.html)
