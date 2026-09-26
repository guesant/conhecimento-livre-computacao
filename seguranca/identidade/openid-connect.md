# OpenID Connect

OpenID Connect, OIDC, é uma camada de identidade sobre OAuth 2.0. OAuth
responde como um cliente obtém autorização para acessar um recurso. OIDC
adiciona uma forma interoperável de autenticar o usuário e comunicar claims
sobre ele ao cliente.

O cliente OIDC é chamado de Relying Party, RP. O provedor é chamado de OpenID
Provider, OP. O usuário é o End-User. O OP pode usar senha, MFA, passkey,
LDAP, Kerberos, SAML upstream ou outro mecanismo para autenticar, mas o RP
valida o resultado OIDC, não a credencial original do usuário.

## Origem e relação histórica

OAuth 2.0 surgiu primeiro como um framework para delegar autorização. Ele
resolveu a pergunta "como um cliente obtém acesso limitado a um recurso em
nome de um proprietário?", mas deixou fora do escopo uma resposta interoperável
para "quem é o usuário que autorizou?".

Na prática, provedores começaram a colocar informações de identidade em cima
de OAuth por meio de endpoints e claims proprietários. Essa diversidade
funcionava dentro de cada fornecedor, mas dificultava trocar o provedor ou
implementar um cliente que funcionasse em mais de uma plataforma.

O OpenID Connect foi criado depois para padronizar essa camada de identidade.
Ele aproveita os endpoints e grants do OAuth 2.0, acrescenta o scope `openid`,
o ID token, o UserInfo endpoint, discovery, claims e regras de validação.

Por isso, OIDC virou uma especificação própria e uma família de implementações,
mas não se separou conceitualmente do OAuth. OIDC continua sendo uma camada de
autenticação sobre OAuth 2.0: OAuth fornece a delegação e os tokens de acesso;
OIDC fornece uma forma padronizada de comunicar a autenticação e a identidade.

Uma aplicação pode usar OAuth sem OIDC para acessar uma API, OIDC para login
federado e os dois juntos quando autentica o usuário e depois chama uma API em
nome dele.

## Componentes

| Componente | Papel |
| --- | --- |
| End-User | Pessoa cuja identidade será usada pela aplicação. |
| OpenID Provider | Authorization server que autentica e emite ID token. |
| Relying Party | Aplicação que confia no OP e cria sua sessão local. |
| Authorization endpoint | Interação do navegador para autenticação e consentimento. |
| Token endpoint | Troca code por tokens. |
| UserInfo endpoint | Retorna claims adicionais com access token. |
| Discovery document | Publica endpoints, issuer, scopes, algoritmos e capabilities. |
| JWKS endpoint | Publica chaves públicas para validação de assinaturas. |
| ID token | JWT que descreve o evento de autenticação e o subject. |
| Access token | Credencial para UserInfo ou resource server, não uma prova universal de identidade. |

## Scope `openid`

Uma requisição OIDC inclui o scope `openid`. Esse valor diferencia uma
requisição de autenticação OIDC de uma requisição OAuth que pede apenas acesso
a uma API.

Scopes como `profile`, `email`, `address` e `phone` indicam famílias de claims
que podem ser retornadas, sempre sujeitas à política do OP e ao consentimento.
Um scope não garante que todos os claims serão emitidos.

## Discovery

O RP pode conhecer o OP por configuração ou descobrir sua metadata em um
documento `.well-known/openid-configuration`. O documento informa `issuer`,
endpoints, `jwks_uri`, tipos de response, métodos de autenticação do token
endpoint, scopes e algoritmos suportados.

O RP deve comparar o issuer descoberto com o issuer esperado e buscar o JWKS
por HTTPS. Discovery não deve ser usado para aceitar qualquer OP indicado por
entrada do usuário sem política de confiança.

## Registro de cliente

Um RP pode ser pré-registrado com client ID, redirect URIs, scopes, métodos de
autenticação e chaves. Dynamic Client Registration permite registrar clientes
por protocolo, mas só deve ser exposto com controle de quem pode registrar,
quais redirect URIs são aceitas e qual política de revisão existe.

Clients públicos, como SPA e aplicações nativas, não conseguem proteger um
client secret embutido no binário ou JavaScript. Eles devem usar PKCE e
redirect URIs específicas.

## Authorization Code Flow

1. O RP gera `state`, `nonce` e, no OAuth moderno, `code_verifier` e
   `code_challenge`.
2. O RP envia o navegador ao authorization endpoint com `client_id`,
   `redirect_uri`, `response_type=code`, `scope=openid` e os valores de
   proteção.
3. O OP autentica o End-User e executa consentimento ou política silenciosa.
4. O OP retorna um code para a redirect URI.
5. O RP valida `state` e troca o code no token endpoint.
6. O OP retorna ID token, access token e possivelmente refresh token.
7. O RP valida o ID token antes de criar a sessão local.
8. O RP usa o access token no UserInfo endpoint ou em APIs destinadas a ele.

O RP não deve criar sessão apenas porque recebeu um parâmetro `code` ou porque
o token tem uma aparência de JWT. A validação precisa incluir todos os campos
obrigatórios e o vínculo ao fluxo iniciado.

## ID token

O ID token é um JWT assinado pelo OP. Claims comuns incluem:

| Claim | Função |
| --- | --- |
| `iss` | Identifica o issuer que emitiu o token. |
| `sub` | Identifica o usuário dentro do issuer. |
| `aud` | Identifica o client ao qual o token se destina. |
| `azp` | Identifica o client autorizado quando há mais de uma audiência. |
| `exp` | Limite de validade. |
| `iat` | Momento de emissão. |
| `nonce` | Vincula o token à requisição iniciada pelo RP. |
| `auth_time` | Momento da autenticação do usuário. |
| `acr` | Classe ou nível de autenticação, se o OP publicar. |
| `amr` | Métodos usados para autenticar, se o OP publicar. |
| `at_hash` | Vínculo opcional entre ID token e access token. |

O RP deve validar assinatura com algoritmo permitido, `iss`, `aud`, `azp`,
`exp`, `iat`, `nonce` e os requisitos de `auth_time`, `acr` e `amr` quando a
política exigir. `sub` é o identificador estável no contexto do issuer, não
necessariamente um e-mail.

## UserInfo

UserInfo é um endpoint protegido pelo access token que pode devolver claims
adicionais do End-User. O RP deve verificar que o claim `sub` do UserInfo
coincide com o `sub` esperado do ID token. Não substitua essa verificação por
nome ou endereço de e-mail.

Claims podem mudar, ser omitidos, depender do consentimento ou depender de
escopos. A aplicação deve definir quais são obrigatórios e qual fallback é
seguro quando não estiverem disponíveis.

## Tipos de cliente

### Web server confidential client

O backend guarda credencial do cliente e troca o code no servidor. A sessão
local pode ser um cookie HttpOnly, deixando tokens fora do JavaScript e
reduzindo exposição a XSS.

### SPA public client

O código roda no navegador e não protege client secret. Usa Authorization Code
com PKCE e precisa de políticas cuidadosas para armazenamento de tokens,
refresh, logout, CORS e XSS.

### Native application

A aplicação usa o navegador do sistema e uma redirect URI apropriada, como
loopback ou universal link. PKCE protege o code contra interceptação por outro
aplicativo.

### Device client

Um dispositivo com entrada limitada usa o Device Authorization Grant. O usuário
autentica em outro dispositivo e o dispositivo original recebe tokens após
aprovação.

## Sessão, logout e reautenticação

OIDC autentica no OP, mas a RP normalmente mantém uma sessão própria. Expiração
ou revogação no OP não encerra magicamente toda sessão local. A RP precisa
definir duração, revalidação, refresh e comportamento diante de erro no token.

Logout pode ser iniciado na RP, no OP ou por comunicação entre eles. Front-
channel logout depende do navegador e de iframes; back-channel logout usa
comunicação direta do OP para as RPs. Cada implementação precisa validar o
`sid`, issuer e assinatura conforme o mecanismo adotado.

`prompt=login`, `max_age`, `auth_time` e MFA exigido são mecanismos diferentes
de pedir autenticação recente. Não use apenas a presença de uma sessão do OP
quando uma operação de alto risco exige reautenticação.

## Identificadores e claims

O par issuer e subject forma a identidade OIDC básica. E-mail pode mudar,
ser reutilizado ou não ser verificado. Claims de grupos e roles podem ser
grandes, atrasados ou específicos de um produto. Mapeie claims em permissões
locais com uma política explícita e não use texto livre como autorização.

Subjects pairwise podem oferecer identificadores diferentes para RPs
distintos, reduzindo correlação entre aplicações. Subjects públicos simplificam
integração, mas ampliam possibilidade de correlação.

## OIDC versus OAuth

| Pergunta | OAuth 2.0 | OpenID Connect |
| --- | --- | --- |
| Objetivo | Delegar acesso a recurso | Autenticar End-User e publicar claims |
| Artefato central | Access token | ID token mais artefatos OAuth |
| Identidade do usuário | Não definida pelo framework | `iss` e `sub` no ID token |
| UserInfo | Não é requisito do OAuth | Endpoint padronizado do OIDC |
| Discovery | OAuth metadata | OpenID Provider configuration |
| Uso típico | Serviço para serviço ou API delegada | Login federado e SSO |

Não aceite um access token como se fosse um ID token. A audiência, o issuer,
os claims e a finalidade são diferentes.

## Segurança e privacidade

- Use Authorization Code com PKCE.
- Valide `state` e `nonce` por sessão e rejeite reutilização.
- Faça match exato de redirect URI.
- Valide assinatura, issuer, audience, expiração e algoritmo permitido.
- Não aceite `alg=none` ou downgrade de algoritmo.
- Não coloque tokens em URLs ou logs.
- Proteja cookies com `Secure`, `HttpOnly` e `SameSite` conforme o fluxo.
- Limite escopos, claims e duração.
- Defina política para contas desativadas, e-mail alterado e logout.
- Trate claims pessoais como dados sujeitos a minimização e retenção.

## Fontes

- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)
- [OpenID Connect Dynamic Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html)
- [OpenID Connect Back-Channel Logout](https://openid.net/specs/openid-connect-backchannel-1_0.html)
- [OpenID Foundation specifications](https://openid.net/developers/specs/)

## Continue por aqui

[OAuth 2.0](oauth2.md) define os grants e tokens subjacentes. [SAML](saml.md)
é uma alternativa de federação baseada em assertions XML. [Autenticação e
autorização](auth.md) explica a separação de responsabilidades.
