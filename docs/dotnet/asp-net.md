# ASP.NET

ASP.NET é a plataforma web do .NET. Ela fornece hosting, middleware,
roteamento, binding, validação, autenticação, autorização, observabilidade e
integração com servidores HTTP. Não é uma linguagem: aplicações ASP.NET podem
ser escritas em C#, F# ou outras linguagens compatíveis com .NET.

## Pipeline

Uma requisição entra pelo servidor, normalmente Kestrel ou um proxy que o
antecede, passa por middleware e chega a um endpoint. Middleware pode tratar
TLS terminado no proxy, headers, logging, autenticação, autorização,
compressão, rate limiting e erros. A ordem é parte da semântica: autenticar
depois de executar uma operação sensível não protege essa operação.

O processo precisa distinguir timeout do cliente, timeout do proxy, cancelamento
da requisição e conclusão do trabalho no backend. Uma resposta encerrada não
garante que o código downstream parou de executar.

## Formas de construir aplicações

Minimal APIs reduzem cerimônia para endpoints pequenos. MVC organiza controllers
e views. Razor Pages aproxima página e handler. Blazor usa componentes .NET em
modelos de execução diferentes. Web APIs podem usar serialização JSON,
OpenAPI, autenticação e validação, mas o framework não define sozinho o
contrato de negócio.

Escolha a forma de composição pela fronteira da aplicação, não por preferência
de sintaxe. Misturar modelos sem uma convenção comum aumenta filtros duplicados,
tratamento de erro inconsistente e regras espalhadas.

## Segurança

Valide entrada, limite tamanho de payload, configure CORS com origem explícita,
use antiforgery quando houver cookies, proteja secrets fora do código e
aplique autorização em cada recurso. Authentication middleware identifica o
usuário; authorization policies decidem o que ele pode fazer.

Não confie no IP encaminhado por proxy sem uma lista de trusted proxies e
networks. Headers de forwarding podem ser forjados quando o caminho não é
controlado.

## Desempenho e operação

Use cancellation token, limites de concorrência e timeouts para dependências.
Não faça consulta síncrona bloqueante no caminho assíncrono. Meça tempo de
fila, binding, handler, banco, serialização e resposta. Em containers, trate
graceful shutdown, readiness, liveness e limites de memória.

## Fontes primárias

- [ASP.NET Core documentation](https://learn.microsoft.com/en-us/aspnet/core/)
- [ASP.NET Core fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/)
- [ASP.NET Core security](https://learn.microsoft.com/en-us/aspnet/core/security/)
