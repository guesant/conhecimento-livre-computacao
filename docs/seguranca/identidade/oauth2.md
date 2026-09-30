# OAuth 2.0

OAuth 2.0 é um framework para delegar autorização. Ele permite que um cliente
obtenha um access token com escopos definidos para acessar um resource server,
sem receber a senha ou a credencial principal do resource owner.

OAuth não é um protocolo de autenticação do usuário. O fato de uma aplicação
obter um access token não prova quem é a pessoa que autorizou a operação. Para
identidade federada, use OpenID Connect sobre OAuth 2.0.

Historicamente, OAuth 2.0 foi especificado antes do OpenID Connect. Provedores
usavam extensões próprias para devolver dados sobre o usuário, até que OIDC
padronizou uma camada de identidade interoperável sobre os mecanismos OAuth.
OIDC possui especificação e nomenclatura próprias, mas continua dependendo do
modelo OAuth para autorização, endpoints e tokens.

## Participantes

| Participante | Papel |
| --- | --- |
| Resource owner | Autoriza acesso ao recurso, geralmente uma pessoa ou serviço. |
| Client | Pede autorização e usa o token para chamar o recurso. |
| Authorization server | Emite authorization code, access token e, quando aplicável, refresh token. |
| Resource server | Valida access token e protege a API ou recurso. |
| User agent | Navegador ou agente que interage com a autenticação e consentimento. |

Um mesmo produto pode desempenhar mais de um papel, mas as responsabilidades
conceituais continuam diferentes. O authorization server emite a credencial;
o resource server decide se aceita o token e qual operação autoriza.

## Artefatos

### Authorization code

É um valor curto e temporário entregue ao cliente pelo authorization endpoint.
O cliente troca o code no token endpoint. O code deve ser de uso único,
vinculado ao client e à redirect URI e, para clientes públicos, protegido por
PKCE.

### Access token

É a credencial apresentada ao resource server. Pode ser opaca ou estruturada,
como JWT. O cliente deve tratá-la como segredo e enviar apenas ao resource
server e à audiência prevista.

### Refresh token

É usado apenas no authorization server para obter novos access tokens. Possui
vida mais longa e deve ser protegido com mais cuidado. Rotação, revogação,
vínculo ao cliente e detecção de reutilização reduzem o impacto de roubo.

### Scope

É uma string ou conjunto nomeado que representa acesso solicitado. O
authorization server pode conceder menos que o solicitado. O resource server
deve interpretar o scope em conjunto com subject, audience, tenant e política
local.

### State

É um valor criado pelo cliente para vincular a resposta ao fluxo iniciado e
proteger a aplicação contra respostas injetadas ou CSRF no redirecionamento.
Não é uma prova de identidade nem deve ser usado como nonce de um ID token.

### PKCE

Proof Key for Code Exchange vincula o authorization code a um segredo efêmero
gerado pelo cliente. O cliente envia `code_challenge` ao iniciar o fluxo e
`code_verifier` ao trocar o code. O authorization server compara os valores.

PKCE protege especialmente clientes públicos, como aplicações nativas e
SPAs, contra interceptação do code. Ele não transforma um client secret
embutido em uma SPA em segredo real.

## Endpoints

### Authorization endpoint

Recebe o navegador ou user agent. Autentica o resource owner, obtém
consentimento quando necessário e devolve um code ou outro resultado ao
redirect URI registrada.

### Token endpoint

Recebe code, refresh token, client credentials ou outro grant permitido e
emite access token. Deve exigir TLS, autenticar clientes confidenciais e
validar redirect URI, PKCE, grant, scope e audience.

### Resource endpoint

É a API protegida. Recebe o access token e deve validar assinatura ou
introspecção, issuer, audience, expiração, escopo e vínculo do token antes de
executar a operação.

### Introspection endpoint

Permite que um resource server consulte se um token está ativo e obtenha
atributos autorizados. É útil para tokens opacos e revogação centralizada, mas
adiciona latência e exige autenticação entre os componentes.

### Revocation endpoint

Recebe um token para invalidá-lo conforme a política do authorization server.
Revogar um refresh token não implica necessariamente invalidar imediatamente
access tokens JWT já emitidos, a menos que o resource server consulte estado
ou use uma estratégia de expiração curta.

### Metadata e JWKS

Metadata descreve endpoints e capacidades do authorization server. Um
endpoint JWKS publica chaves públicas que resource servers e clientes podem
usar para validar assinaturas. Cache e rotação de chaves precisam tratar
temporariamente tanto a chave antiga quanto a nova.

## Fluxo Authorization Code com PKCE

1. O cliente gera `state`, `code_verifier` e `code_challenge`.
2. O cliente redireciona o user agent para o authorization endpoint.
3. O authorization server valida client, redirect URI, scopes e request.
4. O usuário autentica e consente, conforme a política.
5. O authorization server retorna um authorization code à redirect URI.
6. O cliente valida `state`.
7. O cliente envia code e `code_verifier` ao token endpoint.
8. O servidor valida o code, PKCE, client e redirect URI.
9. O servidor emite access token e, opcionalmente, refresh token.
10. O cliente chama o resource server com o access token.

Esse é o fluxo recomendado para aplicações com usuário. A redirect URI deve
ser registrada exatamente. Não aceite uma URI informada livremente pelo
cliente nem misture ambientes com callbacks compartilhados sem necessidade.

## Outros grants e extensões

### Client Credentials

O cliente autentica a si próprio e obtém token para recursos que pertencem ao
próprio cliente ou foram previamente autorizados. Não representa um usuário.
É apropriado para jobs, serviços e automações, com credenciais protegidas e
scopes mínimos.

### Refresh Token

O cliente apresenta o refresh token ao token endpoint para receber outro
access token. O servidor pode rotacioná-lo, reduzir scopes ou exigir nova
autenticação. Refresh tokens não devem ser enviados ao resource server.

### Device Authorization Grant

Um dispositivo com entrada limitada exibe um código ao usuário. O usuário
completa a autenticação em outro dispositivo, enquanto o primeiro consulta o
authorization server em intervalos controlados. O polling deve respeitar
`interval` e backoff para não produzir carga.

### Token Exchange

Uma aplicação troca um token por outro destinado a uma audiência diferente,
por exemplo, quando um serviço recebe um token externo e precisa obter uma
credencial limitada para um serviço downstream. A troca deve restringir
audience, subject, scopes e cadeia de delegação.

### Implicit e Resource Owner Password

O implicit grant expõe o access token no fluxo do navegador e não é apropriado
para novas aplicações. O Resource Owner Password Grant faz a aplicação
receber a senha do usuário e não deve ser usado como substituto do Authorization
Code com PKCE. Migrações legadas precisam ser tratadas como exceções temporárias
com plano de remoção.

### UMA ticket grant

UMA define uma extensão de OAuth em que o cliente troca um permission ticket
por um token de acesso associado às permissões decididas para aquele recurso.
O fluxo está detalhado em [UMA](uma.md).

## Bearer e sender-constrained tokens

Um bearer token pode ser usado por qualquer pessoa que o possua. TLS protege o
trânsito, mas não impede uso posterior depois de um vazamento.

Tokens sender-constrained vinculam o token a uma prova adicional, como
certificado de mTLS ou uma chave DPoP. O resource server exige essa prova antes
de aceitar o token. Essa proteção reduz replay, mas aumenta complexidade de
chaves, proxies e bibliotecas clientes.

## Segurança e falhas comuns

- Não use OAuth apenas para descobrir quem é o usuário.
- Use Authorization Code com PKCE para fluxos interativos modernos.
- Valide `state`, PKCE, issuer, audience, expiração e redirect URI.
- Não use scopes genéricos como substituto de autorização por recurso.
- Não aceite um ID token como access token.
- Não envie access ou refresh token em URL, log ou mensagem de erro.
- Use TLS em authorization, token e resource endpoints.
- Rotacione client credentials, chaves de assinatura e refresh tokens conforme o risco.
- Defina retry, timeout e revogação sem transformar polling em avalanche.
- Não confie apenas na validação local de um JWT quando revogação imediata é requisito.

## Fontes

- [RFC 6749, OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 7636, PKCE](https://www.rfc-editor.org/rfc/rfc7636)
- [RFC 8628, Device Authorization Grant](https://www.rfc-editor.org/rfc/rfc8628)
- [RFC 8693, Token Exchange](https://www.rfc-editor.org/rfc/rfc8693)
- [RFC 8414, Authorization Server Metadata](https://www.rfc-editor.org/rfc/rfc8414)
- [RFC 8705, OAuth mTLS](https://www.rfc-editor.org/rfc/rfc8705)
- [RFC 9449, OAuth DPoP](https://www.rfc-editor.org/rfc/rfc9449)
- [RFC 9700, OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700)

## Continue por aqui

[OpenID Connect](openid-connect.md) adiciona autenticação e claims de
identidade. [UMA](uma.md) usa uma extensão de OAuth para permissões gerenciadas
pelo proprietário. [SAML](saml.md) resolve federação por assertions XML.
