# Redis

Redis é um servidor de estruturas de dados em memória que oferece comandos
para strings, hashes, lists, sets, sorted sets, streams, bitmaps e outros tipos.
Ele pode atuar como cache, store de sessão, contador, lock coordenado, fila,
stream ou banco primário em alguns domínios. O uso correto depende das
garantias de persistência, consistência, durabilidade e recuperação escolhidas.

## Modelo de dados

Cada chave aponta para um valor de um tipo Redis. Expiração, atomicidade de
comandos e estruturas especializadas permitem operações rápidas sem carregar
um documento inteiro para a aplicação. O design da chave é parte do schema:
inclua tenant, recurso, versão e finalidade quando houver risco de colisão.

TTL não é uma política de retenção universal. Um cache pode aceitar expiração
silenciosa; uma sessão precisa considerar renovação; um lock precisa evitar
que o proprietário antigo continue atuando; um dado editorial não deve
desaparecer apenas porque foi modelado como chave temporária.

## Persistência

RDB cria snapshots. AOF registra operações em um log com política de fsync.
As opções oferecem compromissos diferentes entre durabilidade, tamanho,
latência e tempo de recuperação. Replicação não é backup: um erro apagado no
primário pode ser replicado, e um cluster sem cópia restaurável não protege o
histórico.

Faça backups, teste restore, monitore crescimento do AOF, espaço, latência de
fork, memória e comportamento durante reescrita. Em container, o volume
persistente e o limite de memória são parte do desenho.

## Concorrência e atomicidade

Comandos individuais são executados atomicamente no servidor, mas uma sequência
de comandos não é automaticamente uma transação isolada. MULTI/EXEC, Lua e
Functions podem agrupar operações, cada um com semântica e riscos próprios.
Watch ou scripts que dependem de leitura anterior precisam tratar retry e
concorrência.

Pub/Sub não é uma fila durável. Streams oferecem histórico, consumer groups,
acknowledgement e reprocessamento, mas exigem política para pending entries,
retention e consumidores parados.

## Memória e eviction

Como os dados ficam em memória, a capacidade efetiva é menor que o disco
disponível. Maxmemory, política de eviction, fragmentação, estruturas grandes
e clientes lentos precisam ser observados. Eviction é aceitável para cache,
mas perigosa para estado primário, fila ou lock.

## Cluster e segurança

Redis Cluster distribui chaves por slots e impõe limites a operações que
atravessam slots sem uma estratégia explícita. Replicação e failover melhoram
disponibilidade, mas não eliminam janelas de perda conforme a durabilidade.

Restrinja rede, autentique clientes, use TLS quando necessário, limite comandos
administrativos e não exponha Redis à Internet. Segredos, dumps, AOF e logs
devem receber a mesma proteção do dado que representam.

## Relações

- [Bancos chave-valor](key-value.md) explica o modelo geral.
- [Cache](../cache.md) trata TTL, invalidação e consistência.
- [Filas](../mensageria/filas.md) diferencia fila durável de estruturas em
  memória.

## Fontes primárias

- [Redis documentation](https://redis.io/docs/latest/)
- [Redis data types](https://redis.io/docs/latest/develop/data-types/)
- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [Redis security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
