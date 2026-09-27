# TTL

TTL, ou Time To Live, é uma duração máxima associada a um valor, mensagem, lease,
registro ou cache. Quando o prazo termina, o consumidor deve tratar o item como expirado,
mesmo que ele ainda exista fisicamente no armazenamento.

TTL é uma regra de validade, não necessariamente uma operação de deleção. Muitos caches
removem o valor somente quando ele é consultado ou quando um processo de limpeza passa
por ele. A idade lógica e a presença física são propriedades diferentes.

## TTL em diferentes sistemas

| Uso | O que expira | Risco principal |
| --- | --- | --- |
| Cache | Cópia derivada | Servir dado antigo ou provocar avalanche de misses. |
| Lease | Direito temporário de executar | O dono antigo continuar escrevendo depois de perder a validade. |
| Mensagem | Trabalho que deixou de ser útil | Perder trabalho sem uma política de compensação. |
| DNS | Resposta de um resolvedor | Mudança não ser observada antes do prazo. |
| Sessão ou token | Autoridade ou estado de login | Janela de revogação e renovação mal definidas. |
| Retenção | Dado que pode ser removido | Excluir evidência, backup ou requisito legal cedo demais. |

O significado precisa estar no contrato. `expires_at` pode indicar o instante absoluto de
expiração, enquanto `ttl` indica uma duração calculada a partir de um relógio. Misturar
os dois em máquinas com clock divergente produz resultados inconsistentes.

## Relógio e cálculo

Para medir duração dentro de um processo, prefira relógio monotônico. O relógio civil pode
ser ajustado por NTP, mudança de fuso ou sincronização manual. Para uma data de validade
que precisa ser comparada entre sistemas, use um instante UTC ou um contador emitido por
uma autoridade, mas considere skew, latência e precisão.

Não considere um TTL expirado como prova de que nenhuma atividade ainda está usando o
recurso. O consumidor pode ter recebido o valor antes da expiração, estar executando uma
operação ou ter perdido a renovação sem que o servidor tenha removido o registro.

## TTL e cache

TTL curto reduz a idade máxima, mas aumenta misses, carga na origem e risco de thundering
herd. TTL longo reduz custo e latência, mas prolonga uma invalidação ausente. Use versão
na chave, invalidação explícita, stale-while-revalidate e single flight quando o custo de
regeneração for alto.

Jitter evita que milhares de chaves criadas juntas expirem no mesmo instante. A duração
aleatória deve permanecer dentro do limite de frescor aceito pelo contrato.

Um item stale pode continuar sendo servido se o produto tiver essa política. Isso é
distinto de tratar qualquer dado expirado como válido. Declare se o sistema é fail-open,
fail-closed ou stale-while-revalidate quando a origem estiver indisponível.

## TTL e leases

Lease é uma autorização temporária, não apenas um cache com expiração. Um worker precisa
renovar o lease antes do vencimento e parar quando a renovação falhar. O recurso protegido
deve verificar um fencing token ou uma versão para rejeitar o antigo proprietário.

Sem fencing, este cenário é possível: o worker A pausa, seu TTL expira, o worker B adquire
o lease e começa a trabalhar, A retorna e grava usando a autoridade antiga. O TTL detectou
abandono, mas não impediu a escrita atrasada.

## TTL e mensagens

Expirar mensagem pode ser correto quando ela só é útil até uma janela, como atualização de
presença ou preço. Pode ser incorreto para uma cobrança, migração ou evento de auditoria.
Defina se a mensagem expirada vai para dead letter, será compactada, será reprocessada ou
será descartada com métrica e alerta.

TTL não deve ser usado para esconder backlog permanente. Se a fila cresce porque o
consumidor está lento, aumentar ou diminuir o TTL apenas muda a forma da perda. Meça idade,
profundidade e taxa de consumo.

## Segurança

TTL de token limita a janela de uso, mas não substitui revogação, audience, rotação ou
verificação de assinatura. TTL de segredo reduz exposição, mas não remove cópias em logs,
backups, filas ou memória de processos.

Quando o requisito é apagar dados, use política de deleção e verificação de storage. Uma
expiração lógica em cache não é uma garantia de apagamento criptográfico.

## Relações

- [Heartbeat](../confiabilidade/heartbeat.md) trata renovação e detecção de atividade.
- [Cache](cache.md) trata invalidação, stale-while-revalidate e thundering herd.
- [Filas](mensageria/filas.md) trata expiração, retry, ack e dead letter.
- [Mutex](../engenharia-software/concorrencia/mutex.md) explica por que TTL sozinho não
  protege um lock distribuído.

## Fontes

- [RFC 9111, HTTP caching](https://www.rfc-editor.org/rfc/rfc9111)
- [RFC 1035, DNS TTL](https://www.rfc-editor.org/rfc/rfc1035)
- [Redis, EXPIRE](https://redis.io/docs/latest/commands/expire/)
