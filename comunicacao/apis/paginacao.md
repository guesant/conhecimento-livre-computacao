# Paginação por cursor

Paginação por cursor é uma forma de atravessar uma coleção usando a posição do
último item recebido como ponto de continuação. Em vez de pedir "a página 20",
o cliente pede "os itens depois desta posição". O cursor normalmente codifica a
chave da ordenação e outros dados necessários para repetir a consulta de modo
determinístico.

O cursor não deve ser confundido com um cursor aberto no banco de dados. Ele é
um token de continuidade de uma API. A requisição seguinte pode ser atendida
por outra conexão, outra instância da aplicação ou outro processo, desde que o
estado necessário esteja no próprio token ou em um armazenamento compartilhado.

## Offset e cursor

Na paginação por offset, a requisição informa página e tamanho ou `offset` e
`limit`:

```sql
select id, title, published_at
from articles
where status = 'published'
order by published_at desc, id desc
limit 20 offset 380;
```

Essa forma é simples, permite saltar para uma página arbitrária e pode ser
suficiente para uma tabela pequena ou quase estática. Em uma coleção grande, o
banco frequentemente precisa percorrer ou descartar muitas linhas antes de
entregar o trecho desejado. Além disso, inserções e exclusões entre duas
requisições deslocam o offset. O cliente pode repetir itens, pular itens ou
receber uma página diferente da esperada.

Na paginação por cursor, a posição do último item vira uma condição de busca:

```sql
select id, title, published_at
from articles
where status = 'published'
  and (published_at, id) < (:last_published_at, :last_id)
order by published_at desc, id desc
limit :page_size;
```

O banco procura diretamente a região seguinte do índice. Se um item novo for
inserido no começo da coleção, ele não muda a posição já atravessada. Se um
item anterior for removido, a continuação ainda pode avançar porque a chave do
cursor não dependia do número de linhas removidas.

Cursor não elimina todos os efeitos de concorrência. Uma alteração de ordenação,
um relógio inadequado, atualização de um item já atravessado ou mudanças na
autorização podem fazer um item aparecer em outro lugar ou deixar de ser
visível. A API precisa declarar a semântica de consistência que oferece.

## Ordenação determinística

Uma ordenação por uma coluna não única não define uma posição completa. Se
vários artigos têm o mesmo `published_at`, somente esse campo não basta para
formar um cursor. Acrescente uma chave única e estável, normalmente `id`, como
desempate:

```sql
order by published_at desc, id desc
```

O cursor precisa carregar ambos os valores. A comparação da condição deve usar
a mesma ordem lógica. Para ordem crescente, a continuação usa `>`; para ordem
decrescente, usa `<`:

```sql
where (created_at, id) > (:last_created_at, :last_id)
order by created_at asc, id asc
```

Ordenações mistas, como `score desc, id asc`, não podem ser tratadas
ingenuamente como uma comparação de tupla com a mesma direção. Use uma condição
lexicográfica explícita, uma chave normalizada ou uma expressão de ordenação
que tenha semântica bem definida:

```sql
where score < :last_score
   or (score = :last_score and id > :last_id)
order by score desc, id asc
```

Filtros também fazem parte da posição lógica. Um cursor emitido para
`status=published` não deve ser reutilizado depois que o cliente remove o
filtro ou muda o tenant. O servidor deve rejeitar o cursor incompatível ou
tratar a requisição como uma nova consulta.

## Índices

O cursor só é eficiente quando a consulta pode aproveitar um índice compatível
com filtro e ordenação. Para a consulta do exemplo, um índice possível é:

```sql
create index concurrently articles_publication_feed_idx
on articles (status, published_at desc, id desc);
```

Em uma consulta multitenant, o tenant normalmente vem antes da chave de
ordenação:

```sql
create index concurrently articles_tenant_feed_idx
on articles (tenant_id, status, published_at desc, id desc);
```

Não crie índices apenas porque uma coluna aparece no cursor. Confirme o plano
com `explain (analyze, buffers)` em dados representativos. Se o filtro for
seletivo, a ordem dos campos do índice pode mudar o resultado. Se a consulta
precisar buscar uma coluna que não está no índice, o custo de heap fetch ainda
precisa ser medido.

Filtros opcionais complicam o desenho. Um único índice que atende todas as
combinações pode ser pior que índices específicos para as consultas de maior
volume. O limite máximo da página continua necessário mesmo quando existe um
índice, porque serializar milhares de registros, hidratar objetos e transferir
respostas também consome CPU, memória e rede.

## Formato do cursor

O cursor deve ser opaco para o cliente. Uma implementação pode serializar um
payload semelhante a este e codificá-lo em base64url:

```json
{
  "v": 1,
  "sort": "published_at,id:desc",
  "last": {
    "published_at": "2026-09-27T12:00:00Z",
    "id": 418
  },
  "filters_hash": "..."
}
```

Base64 não é criptografia. Se o cursor carregar identificadores internos ou
filtros que não devem ser alterados, assine-o com HMAC ou use um formato
cifrado. Mesmo assinado, ele não concede autorização: a consulta seguinte
precisa repetir o filtro de tenant e as políticas de acesso.

Inclua uma versão do formato. Quando a ordenação ou o schema mudar, o servidor
pode rejeitar versões antigas com um erro de cursor inválido, em vez de
interpretar os bytes segundo regras diferentes. Um prazo de expiração é útil
quando a posição revela dados temporários ou quando a aplicação precisa evitar
que um cursor seja reutilizado indefinidamente.

O servidor deve validar tamanho, assinatura, versão, ordem solicitada, filtros,
tenant e direção. Nunca concatene os valores do cursor diretamente em SQL.
Converta os campos para tipos esperados e use parâmetros preparados.

## Contrato HTTP

Uma API pode expor a continuação por `after`, `before`, `next_cursor` ou links.
O nome é menos importante que a semântica consistente. Um contrato simples para
avanço seria:

```http
GET /api/articles?limit=20&after=eyJ2IjoxLCJzb3J0IjoiLi4uIn0
```

```json
{
  "data": [
    {
      "id": "418",
      "title": "Exemplo"
    }
  ],
  "meta": {
    "limit": 20,
    "has_next_page": true
  },
  "links": {
    "next": "/api/articles?limit=20&after=..."
  }
}
```

O cursor não precisa aparecer em cada item. Se o cliente precisa atualizar uma
lista ou retomar exatamente após um item, pode ser útil retornar um cursor por
item ou um identificador estável separado. Em GraphQL, o padrão Relay costuma
usar `edges`, `node`, `cursor` e `pageInfo` com `hasNextPage` e `endCursor`.

## Total de itens

`count(*)` pode ser muito mais caro que buscar a primeira página, sobretudo
quando filtros complexos, autorização por linha ou joins participam da
consulta. Paginação por cursor normalmente retorna `has_next_page` e não um
total exato.

Se a interface realmente precisa do total, trate essa informação como uma
consulta diferente. Ela pode usar uma contagem pré-calculada, uma estimativa,
uma leitura assíncrona ou uma resposta explicitamente marcada como aproximada.
Não faça uma contagem pesada automaticamente em toda requisição de listagem.

## Próxima página e última página

Avançar é o caso natural do cursor: o servidor usa a última chave da resposta
como `after`. Voltar exige um cursor anterior, uma ordenação invertida ou um
histórico mantido pelo cliente. Uma API pode suportar `before` e `last`, mas
deve especificar se a resposta é invertida no SQL e depois restaurada para a
ordem pública.

Ir diretamente para a página 200 não é uma operação natural de cursor. Se o
produto exige saltos arbitrários, mantenha offset para essa tela, use uma tabela
de posições materializadas ou reveja o requisito. Não simule offset avançando
200 páginas no servidor, pois isso apenas esconde o custo.

## Consistência e snapshots

Para um feed em mudança contínua, o cursor fornece continuidade aproximada sob
uma ordenação estável. Ele não congela a coleção. Se o usuário precisa navegar
por uma fotografia exata, há alternativas:

- associar o cursor a uma versão ou instante de snapshot;
- ler de uma réplica ou projeção imutável;
- materializar uma lista de IDs para uma exportação ou relatório;
- usar uma transação longa apenas quando o custo e o isolamento forem aceitáveis.

Snapshots aumentam retenção, storage e complexidade de expiração. Não devem ser
criados apenas para substituir uma consulta que já possui chave de ordenação
estável.

## Quando usar

Prefira cursor quando a coleção é grande, cresce continuamente, recebe muitas
inserções ou exclusões, precisa de carregamento incremental, é percorrida por
workers ou exige latência previsível em páginas profundas. Feeds, histórico de
eventos, notificações, logs, catálogos e APIs internas de alto volume são
cenários comuns.

Offset continua apropriado para listas pequenas, relatórios em que o total e o
salto de página são requisitos centrais, consultas administrativas pouco
frequentes e coleções praticamente estáticas. Também pode ser uma primeira
implementação correta quando a simplicidade tem mais valor que a otimização
prematura.

Uma API pode oferecer ambos, mas não deve permitir que cada endpoint invente um
contrato. Padronize nomes, limites máximos, erros, ordenação padrão, campos de
cursor, comportamento de filtros e semântica de `has_next_page`.

## Implementação segura

Uma implementação deve seguir esta sequência:

1. definir a ordenação pública e seu desempate único;
2. identificar filtros, tenant e regras de autorização;
3. desenhar o índice com base no filtro e na ordenação;
4. definir e versionar o payload opaco do cursor;
5. validar e parametrizar todos os valores recebidos;
6. buscar `limit + 1` itens para calcular se existe próxima página;
7. remover o item sentinela antes de serializar a resposta;
8. emitir o cursor a partir do último item realmente retornado;
9. testar inserção, remoção, empate de ordenação e alteração concorrente;
10. medir plano, latência, memória, payload e consultas sob carga.

Buscar `limit + 1` evita uma consulta adicional para descobrir se há outra
página. O item extra não deve ser exposto. Se a coleção estiver vazia ou o
cursor apontar além do fim, retorne uma lista vazia e `has_next_page=false`,
sem transformar o caso normal em erro.

## Falhas comuns

- ordenar somente por timestamp e repetir itens com o mesmo valor;
- aceitar um cursor de outra consulta ou de outro tenant;
- tratar base64 como proteção de segredo;
- expor IDs internos acreditando que isso autoriza acesso;
- montar SQL concatenando valores do cursor;
- esquecer o filtro de autorização na página seguinte;
- permitir limite ilimitado;
- calcular total exato em toda listagem;
- criar cursor baseado em uma coluna que pode mudar enquanto o item é lido;
- usar um índice que atende a ordenação, mas não o filtro mais seletivo;
- retornar `has_next_page=true` sem buscar o item sentinela;
- prometer ausência de duplicação quando a ordenação ou a fonte muda.

## Relações

- [APIs](index.md) apresenta contratos, evolução e limites.
- [PostgreSQL, estatísticas e índices](../../dados/postgresql-pg-stat-indices-e-otimizacao.md)
  explica como medir planos e escolher índices.
- [Cache](../../dados/cache.md) trata a relação entre paginação, repetição de
  leitura e invalidação.
- [Event streaming](../../dados/mensageria/event-streaming.md) usa offsets
  para consumidores, uma posição diferente do cursor de uma API.

## Fontes

- [PostgreSQL, LIMIT e OFFSET](https://www.postgresql.org/docs/current/queries-limit.html)
- [Relay Cursor Connections Specification](https://relay.dev/graphql/connections.htm)
- [Stripe, pagination](https://docs.stripe.com/api/pagination)
