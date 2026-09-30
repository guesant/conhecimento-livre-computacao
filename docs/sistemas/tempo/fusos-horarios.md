# Fusos horários

Um fuso horário é uma regra que relaciona um horário civil local a um instante. Essa regra
pode incluir offset, horário de verão, mudanças políticas e histórico. Um offset como
`-03:00` é somente uma diferença em relação ao UTC em um momento; não identifica sozinho
uma região nem suas regras futuras.

## UTC

UTC, Coordinated Universal Time, é a referência global usada para comparar instantes. Ele
não é o horário local de um país e não muda por horário de verão. Um timestamp terminado em
`Z` representa UTC, por exemplo:

```text
2026-09-26T15:30:00Z
```

UTC é uma boa base para persistência, logs, eventos e comunicação entre serviços. A
interface pode converter o instante para o fuso do usuário sem alterar o valor original.

## IANA time zone database

A base de fusos da IANA fornece nomes regionais como `America/Sao_Paulo`, `Europe/London`
e `America/New_York`. Esses nomes representam regras, histórico e transições, e não apenas
um número de horas.

Uma aplicação deve armazenar o identificador IANA quando precisar preservar a intenção
local. A base muda quando governos alteram regras, portanto imagens de container, sistemas
operacionais e runtimes precisam receber atualizações de tzdata.

## Offset, abreviação e identificador

| Representação | O que informa | Limitação |
| --- | --- | --- |
| `UTC` | Referência sem offset local | Não expressa a região pretendida |
| `-03:00` | Diferença naquele instante | Não expressa regras históricas ou futuras |
| `America/Sao_Paulo` | Região e regras do tzdata | Depende da versão da base instalada |
| `BRT` | Abreviação informal de horário brasileiro | Pode ser ambígua e não é adequada para persistência |
| `EST` | Pode significar Eastern Standard Time | Não distingue regiões e pode não representar horário de verão |
| `EPT` | Abreviação não padronizada e ambígua | Não deve ser usada como identificador universal |

`EPT` não é uma escolha segura para persistir um fuso. Se a intenção for Eastern Time nos
Estados Unidos, use `America/New_York`; se for outra região, use o identificador IANA
correspondente. Se o requisito for realmente um offset fixo, armazene `-05:00` e deixe
explícito que regras de horário de verão não serão aplicadas.

## Horário de verão e transições

Em uma transição de horário de verão, alguns horários locais não existem e outros podem
ocorrer duas vezes. Uma reunião marcada para 02:30 pode ser inválida em um dia e ambígua em
outro.

Bibliotecas de data e hora precisam de uma política para:

- horário local inexistente, como deslocar, rejeitar ou pedir confirmação;
- horário local ambíguo, como escolher o primeiro, o segundo ou pedir offset;
- atualização do tzdata depois de uma regra política mudar;
- notificações e recorrências já agendadas;
- fusos do usuário e do recurso quando eles forem diferentes.

Não calcule horário de verão adicionando uma hora manualmente. Use uma biblioteca que
conheça a versão do tzdata e preserve o identificador da zona.

## Conversão

Uma conversão segura precisa de um instante ou de uma data local com zona. Um horário sem
zona, como `2026-09-26 12:00:00`, pode representar instantes diferentes em São Paulo,
Londres ou Nova York.

O fluxo recomendado é:

1. interpretar a entrada com o formato e zona declarados;
2. resolver ambiguidades conforme uma política explícita;
3. obter o instante correspondente;
4. persistir o instante e, se necessário, a zona original;
5. formatar somente na borda para o usuário ou consumidor.

## APIs e contratos

Em JSON, prefira strings RFC 3339 como `2026-09-26T15:30:00Z` ou
`2026-09-26T12:00:00-03:00`. Não envie uma data local sem dizer qual zona a interpreta.
Para eventos futuros, o contrato pode precisar de `local_date`, `local_time`, `time_zone` e
uma regra de recorrência, em vez de um único campo UTC.

## Fontes primárias

- [IANA Time Zone Database](https://www.iana.org/time-zones)
- [RFC 3339, date and time on the Internet](https://www.rfc-editor.org/rfc/rfc3339)
- [IANA time zone theory](https://data.iana.org/time-zones/theory.html)
- [Unicode CLDR, time zone names](https://cldr.unicode.org/translation/time-zones-and-city-names)
