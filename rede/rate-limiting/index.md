# Rate limiting

Rate limiting limita consumo de uma operação por janela, identidade, origem,
rota ou recurso. Ele protege capacidade e pode representar uma quota contratual,
mas não substitui autenticação, autorização ou controle de concorrência.

## Dimensões

Defina quem é limitado, qual operação conta, qual resposta é produzida e qual
estado precisa ser compartilhado entre réplicas. Limitar por IP pode agrupar
clientes legítimos atrás de NAT; limitar por consumer exige identidade confiável.

## Estado

Estado local é rápido e não depende de rede, mas conta por réplica. Estado
compartilhado representa o total agregado, ao custo de latência, disponibilidade
e uma dependência adicional.

## Algoritmos

- [Fixed window](fixed-window.md) é simples e pode permitir rajadas na borda.
- [Sliding window](sliding-window.md) suaviza a borda com mais estado.
- [Token bucket](token-bucket.md) controla taxa e permite burst configurado.
- [Leaky bucket](leaky-bucket.md) drena em ritmo constante.

## O que cada algoritmo controla

Rate limiting pode controlar duas propriedades diferentes. A primeira é a
quantidade máxima de eventos aceitos em um intervalo. A segunda é a velocidade
com que o sistema deixa esses eventos chegarem ao próximo componente. Um
algoritmo de contagem costuma rejeitar a requisição excedente, enquanto um
algoritmo com fila pode atrasá-la ou processá-la em ritmo controlado.

| Algoritmo | Estado principal | Taxa média | Rajada | Decisão excedente |
| --- | --- | --- | --- | --- |
| Fixed window | contador por janela | aproximada | artificial na borda | rejeita ou espera |
| Sliding window | eventos ou subcontadores | precisa | menor na borda | rejeita ou espera |
| Token bucket | tokens, taxa e capacidade | explícita | explícita | rejeita ou espera |
| Leaky bucket | fila e drenagem | explícita | absorvida pela fila | bloqueia, descarta ou rejeita |

O fixed window é uma boa escolha quando o limite é uma quota simples e uma
rajada na mudança de janela não causa dano. O sliding window é mais adequado
quando a fronteira do intervalo não pode criar uma capacidade momentânea quase
duas vezes maior. O token bucket costuma ser a escolha mais clara para APIs,
porque separa a taxa sustentável da rajada que o serviço aceita. O leaky
bucket é útil quando o objetivo principal é regular a saída para um recurso
mais lento, mas a fila precisa de um limite próprio para não converter excesso
de tráfego em consumo ilimitado de memória.

## Contagem sob concorrência

O algoritmo não é correto apenas porque a fórmula está correta. Duas
requisições concorrentes precisam observar e atualizar o mesmo estado de forma
atômica. Um fluxo que lê o contador, compara o limite e só depois grava o novo
valor pode aceitar requisições a mais quando várias réplicas executam o fluxo
ao mesmo tempo.

Uma implementação compartilhada normalmente combina uma operação atômica de
incremento com expiração da chave. Em token bucket, a atualização precisa
calcular o tempo transcorrido, limitar o número de tokens à capacidade máxima,
consumir o custo da operação e persistir o novo saldo sem permitir que duas
requisições usem os mesmos tokens. O relógio usado para medir intervalos deve
ser monotônico sempre que a plataforma oferecer essa opção, porque o relógio
civil pode ser ajustado por sincronização de tempo.

## Chave, custo e escopo

A chave do limite deve corresponder à identidade que a política pretende
proteger. Uma chave pode combinar tenant, usuário autenticado, rota e método
HTTP. O IP pode ser uma dimensão auxiliar, mas não deve ser tratado como
identidade universal quando muitos clientes legítimos compartilham NAT.

Nem toda operação precisa custar um evento. Uma consulta barata pode consumir
um token, enquanto uma exportação pesada pode consumir dez. O custo deve ser
definido junto do limite, porque contar apenas requisições pode deixar uma
operação cara consumir a mesma capacidade que uma operação trivial.

## Falha do armazenamento de estado

Quando o contador compartilhado fica indisponível, a política precisa declarar
se o caminho será fail-open ou fail-closed. Fail-open preserva disponibilidade,
mas pode remover a proteção contra abuso justamente durante a falha. Fail-closed
preserva a quota, mas pode transformar a indisponibilidade do mecanismo de
contagem em indisponibilidade da API.

Uma alternativa intermediária usa um limite local de emergência, com uma
capacidade pequena e uma duração curta, registra a degradação e reavalia a
política quando o estado compartilhado voltar. Isso não preserva a mesma
garantia agregada, portanto deve ser tratado como modo degradado, não como
equivalente ao contador distribuído.

## Resposta HTTP

Quando uma requisição é rejeitada por excesso de consumo, uma API HTTP costuma
retornar `429 Too Many Requests`. `Retry-After` informa quando a tentativa pode
ser repetida, desde que o algoritmo consiga calcular esse momento. Headers de
limite podem expor capacidade, restante e janela, mas esses valores precisam
ser documentados porque arredondamento, réplicas e estado eventual podem fazer
com que sejam apenas uma estimativa.

O cliente não deve repetir imediatamente toda resposta `429`. Ele deve
respeitar `Retry-After` quando presente, aplicar backoff com jitter quando não
houver uma indicação precisa e limitar também o número total de tentativas.
Caso contrário, o mecanismo de retry de cada cliente pode produzir uma nova
rajada e aumentar a sobrecarga que o rate limiting tentou conter.

## Relações

- [API gateway](../api-gateway/index.md) aplica limite na borda.
- [Rate limiting local e compartilhado](../../rate-limiting-politica-local-e-compartilhada.md)
  compara o estado.
- [Filas](../../dados/mensageria/filas.md) podem absorver trabalho em vez de
  rejeitar tudo.
- [Falhas recorrentes e limitação adaptativa](falhas-recorrentes.md) trata de
  limitar progressivamente identidades que acumulam falhas recentes, sem
  transformar uma falha legítima em bloqueio permanente.

## Fonte primária

- [IETF HTTP 429](https://www.rfc-editor.org/rfc/rfc6585)
