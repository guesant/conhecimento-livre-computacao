# CDN

Content Delivery Network é uma rede de pontos de presença que recebe requisições perto
dos consumidores e pode servir respostas cacheáveis sem consultar a origem a cada vez.
Além de reduzir latência, uma CDN pode absorver parte dos picos, terminar TLS, aplicar
regras de segurança e proteger a origem.

CDN não é sinônimo de cache de aplicação. A CDN opera normalmente em uma fronteira HTTP;
um cache interno pode armazenar objetos de negócio, consultas ou respostas antes de uma
requisição chegar à borda.

## Fluxo

O cliente consulta um hostname. O ponto de presença calcula uma chave de cache, verifica
se possui uma resposta válida e, em caso de miss, consulta a origem. A resposta da origem
é armazenada conforme headers e política da CDN. O próximo consumidor pode receber a
resposta da borda.

A origem pode ser um load balancer, reverse proxy, aplicação, storage de objetos ou outra
CDN. Cada hop pode ter uma política diferente, e os headers devem ser analisados como um
contrato, não como uma garantia vaga de cache.

## Cache-Control e chave

`Cache-Control`, `ETag`, `Last-Modified`, `Vary` e status HTTP participam da decisão. A
chave deve considerar URL, método, host, query string e dimensões que realmente mudam a
resposta. Não inclua cookies ou headers irrelevantes sem necessidade, mas nunca omita uma
dimensão que separa conteúdo autorizado ou localizado.

Conteúdo público versionado, como JavaScript, CSS, imagens e fontes, pode usar nomes com
hash e TTL longo. Conteúdo dinâmico pode usar TTL curto, revalidação ou não ser cacheado.
Uma resposta privada não deve vazar para outro usuário apenas porque a URL é igual.

## Invalidação

Purge remove entradas antes do TTL. Invalidação por tag, URL, prefixo ou geração depende
da capacidade do provedor. Assets versionados geralmente reduzem a necessidade de purge:
um novo hash produz uma chave nova, enquanto a chave antiga pode expirar naturalmente.

Purge global é mais caro e pode causar uma onda de misses. Se o deploy invalida tudo ao
mesmo tempo, a origem recebe um pico. Prefira invalidação seletiva ou aquecimento
progressivo quando o conteúdo permitir.

## Conteúdo dinâmico e APIs

CDN pode cachear APIs públicas com parâmetros, locale e headers bem definidos. Requests
autenticados, respostas com dados pessoais e operações de escrita normalmente não devem
ser servidos de uma cache pública sem uma política muito clara.

Cachear uma API não substitui paginação, autorização, validação, limitação de taxa ou
cache de aplicação. Uma resposta pública stale pode ser aceitável; uma resposta de
permissão, saldo ou estado de manutenção pode exigir leitura na origem.

## Origem e segurança

Restrinja a origem para que consumidores não contornem a CDN quando a proteção dela for
necessária. Valide Host, método, headers encaminhados e identidade da conexão entre CDN
e origem. TLS entre consumidor, borda e origem precisa ser tratado separadamente.

Uma CDN pode aplicar WAF, rate limiting e bot management, mas essas camadas não substituem
autorização na aplicação. Headers recebidos da borda precisam ser autenticados ou
sobrescritos conforme a fronteira de confiança.

## Falhas

Quando a origem está indisponível, a CDN pode servir stale dentro de uma política, retornar
erro ou tentar outra origem. Servir stale pode preservar disponibilidade, mas precisa de
limite para não ocultar uma falha ou mudança editorial importante.

O cache da borda pode estar saudável enquanto a origem, o DNS, o TLS, o certificado, o
purge ou a chave de cache estão errados. Diagnostique hit, miss, idade, POP, origem e
status de revalidação separadamente.

## Relações

- [Cache](../dados/cache.md) explica cópias derivadas e invalidação.
- [Reverse proxy](proxy/reverse-proxy.md) explica terminação e encaminhamento na origem.
- [Rate limiting](rate-limiting/index.md) controla consumo na borda ou na aplicação.
- [HTTP caching, RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) define a semântica
  geral de cache HTTP.

## Fontes

- [RFC 9111, HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [MDN, HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
