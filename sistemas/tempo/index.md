# Tempo, relógios e fusos

Data e hora envolvem propriedades diferentes: um instante global, um horário de calendário,
um fuso político, um offset, o relógio do sistema, o relógio de hardware e uma representação
persistida no banco. Muitos bugs aparecem quando esses conceitos são tratados como se fossem
apenas uma string com hora.

## Mapa do domínio

- [Fusos, UTC e IANA](fusos-horarios.md) explica identificadores, offsets, horário de verão
  e a diferença entre região e abreviação.
- [Timestamps e bancos](timestamps.md) compara `timestamp`, `timestamptz`, Unix timestamp,
  RFC 3339 e valores de calendário.
- [Relógio do sistema e firmware](relogio-do-sistema-e-firmware.md) explica RTC, BIOS,
  UEFI, `localtime`, UTC, NTP e dual boot.
- [NTP e sincronização](../linux/ntp.md) explica como hosts mantêm seus relógios próximos.

## Três perguntas diferentes

Antes de escolher um tipo, pergunte:

1. preciso representar um instante único no mundo?
2. preciso representar a hora local de um evento recorrente?
3. preciso representar somente uma data ou uma hora sem localização?

Um pagamento concluído precisa de um instante. Uma reunião marcada para 9h em
`America/Sao_Paulo` precisa de horário local e fuso, porque o offset pode mudar. Um
aniversário pode precisar apenas de uma data civil. Converter todos os três para UTC destrói
informação em pelo menos dois dos casos.

## Regra prática

Para eventos ocorridos, armazene um instante em UTC ou em `timestamptz`, e exiba usando o
fuso do usuário. Para eventos futuros que dependem de uma hora local, armazene a zona IANA
e a regra de calendário, não somente o offset atual. Para logs e APIs, use ISO 8601 ou
RFC 3339 com `Z` ou offset explícito.

Não use abreviações ambíguas como o valor persistido de um fuso. Prefira `America/Sao_Paulo`
ou `America/New_York` a `BRT`, `EST` ou `EPT`.
