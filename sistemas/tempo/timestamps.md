# Modelagem temporal

Timestamp é um termo usado para várias representações. Ele pode significar um instante,
um horário local, um número desde uma época ou uma coluna de banco. Antes de escolher o
tipo, defina se a informação representa um instante ou um valor de calendário.

## `timestamp` e `timestamptz` no PostgreSQL

No PostgreSQL, `timestamp without time zone`, normalmente escrito `timestamp`, representa
data e hora sem fuso. O banco não sabe qual instante isso significa e não deve converter o
valor como se soubesse a região.

`timestamp with time zone`, normalmente escrito `timestamptz`, representa um instante. A
entrada com offset ou zona é convertida e o valor é armazenado internamente em UTC. Na
leitura, ele é exibido usando o timezone da sessão; o banco não preserva o nome original da
zona como parte do valor.

| Tipo | Representa | Exemplo de uso |
| --- | --- | --- |
| `timestamp` | Calendário sem zona | aniversário, horário de abertura local, data editorial sem conversão |
| `timestamptz` | Instante global | criação de registro, pagamento, deploy, evento e log |
| `date` | Data civil | feriado, nascimento, competência mensal |
| `time` | Hora sem data e sem zona | horário de funcionamento local, quando a zona fica em outro campo |
| `time with time zone` | Hora com offset | caso raro, geralmente prefira data, hora e zona juntos |

Escolher `timestamp` para um evento global faz o valor depender do timezone de quem o lê.
Escolher `timestamptz` para um aniversário pode deslocar a data ao exibir para outro fuso.

## Entrada e saída

O timezone da sessão do PostgreSQL afeta a interpretação de entrada sem offset e a forma
de exibição de `timestamptz`. Isso pode fazer duas consultas mostrarem textos diferentes
para o mesmo instante.

Defina timezone de sessão deliberadamente, não dependa do timezone do host e teste ORM,
driver, serializador e frontend em zonas diferentes. Uma aplicação pode armazenar UTC e
formatar no navegador; o driver não deve converter duas vezes.

O PostgreSQL possui regras específicas de conversão entre `timestamp` e `timestamptz`.
Consulte a [documentação de data e hora do PostgreSQL](https://www.postgresql.org/docs/current/datatype-datetime.html)
antes de alterar uma coluna de produção.

## Unix timestamp

Unix timestamp é uma contagem numérica de segundos, milissegundos ou outra unidade desde
uma época, normalmente `1970-01-01T00:00:00Z`. A unidade precisa ser parte do contrato:
`1700000000` e `1700000000000` não têm a mesma interpretação.

Vantagens:

- comparação e ordenação simples;
- representação compacta;
- interoperabilidade com protocolos que adotam uma época;
- independência do texto de exibição.

Limitações:

- não carrega o fuso do usuário;
- não expressa uma data civil ou uma recorrência local;
- pode sofrer confusão entre segundos e milissegundos;
- tipos de tamanho insuficiente podem sofrer overflow, como o problema de 2038 em alguns
  contadores de 32 bits;
- conversões erradas de unidade produzem datas plausíveis, mas incorretas.

Use um tipo inteiro grande ou um tipo de tempo da linguagem, documente a unidade e valide
limites. Não aceite número sem saber se ele representa segundos, milissegundos ou microssegundos.

## RFC 3339 e logs

Para APIs e logs, strings ISO 8601 compatíveis com RFC 3339 são mais legíveis e carregam
`Z` ou offset explícito:

```text
2026-09-26T15:30:00Z
2026-09-26T12:30:00-03:00
```

Os dois valores acima representam o mesmo instante quando o offset corresponde à conversão.
Para logs, use um formato estável, precisão definida, relógio sincronizado e um campo
separado para timezone quando ele tiver significado de negócio.

Não use o texto formatado como chave de ordenação quando eventos possuem precisão ou fusos
variáveis. Parseie para um instante antes de comparar.

## Eventos futuros e recorrência

Um evento ocorrido pode ser convertido definitivamente para UTC. Um evento futuro recorrente
precisa preservar a regra local. "Toda segunda às 9h em America/Sao_Paulo" não é equivalente
a "a cada 604800 segundos", porque transições de calendário e regras de zona podem alterar
o intervalo entre instantes.

Armazene, conforme o caso:

- instante da próxima ocorrência;
- data e hora locais solicitadas;
- identificador da zona IANA;
- regra de recorrência;
- política para horários inexistentes ou ambíguos.

## Regra de decisão

Use `timestamptz` ou um instante equivalente para fatos ocorridos. Use `timestamp` somente
quando o valor for deliberadamente sem zona e essa ausência fizer parte do significado. Use
`date` para datas civis. Para horários locais futuros, armazene zona IANA além da data e hora.

## Fontes primárias

- [PostgreSQL date/time types](https://www.postgresql.org/docs/current/datatype-datetime.html)
- [PostgreSQL date/time input interpretation](https://www.postgresql.org/docs/current/datetime-input-rules.html)
- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
- [POSIX time definitions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html)
