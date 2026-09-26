# User-Managed Access

User-Managed Access, UMA, é um perfil de OAuth 2.0 para autorização delegada
e centrada no proprietário do recurso. Ele permite que uma pessoa ou entidade
controle o acesso a recursos protegidos mesmo quando o cliente que pede acesso
e o proprietário não são a mesma entidade.

O caso clássico é um serviço que protege fotos, documentos ou dados de uma
pessoa. Um cliente quer acessar um recurso, o Resource Server descobre que
falta uma permissão, obtém um permission ticket no Authorization Server e o
cliente troca esse ticket por um token associado ao resultado da autorização.

UMA não é uma forma de autenticar a senha do usuário e não substitui OAuth,
OIDC, LDAP ou SAML. Ele define uma relação de autorização mais rica sobre a
base de tokens OAuth.

## Participantes

| Participante | Papel em UMA |
| --- | --- |
| Resource owner | Decide ou delega quem pode acessar seus recursos. |
| Requesting party | Pessoa ou entidade em nome de quem o cliente busca acesso. |
| Client | Aplicação usada pela requesting party. |
| Resource server | Hospeda o recurso e aplica a proteção na API. |
| Authorization server | Avalia política, interação e permissões, emitindo RPT. |
| Protection API | API usada pelo resource server para registrar recursos e permissões. |
| User agent | Navegador que participa de autenticação ou interação de claims. |

O resource owner e a requesting party podem ser a mesma pessoa, mas não são
o mesmo papel. Um usuário pode autorizar outro usuário, um serviço ou um
processo automatizado a acessar um recurso.

## Artefatos

### Resource set

É uma representação do recurso ou conjunto de recursos no authorization
server. O resource server registra identificador, scopes e relações que a
política poderá avaliar.

### Scope

É a ação possível sobre o recurso, como `view`, `edit`, `print` ou `share`.
O scope precisa ter semântica definida pelo domínio e não deve ser confundido
com um grupo genérico do usuário.

### Protection API token

O resource server usa um access token com escopo `uma_protection` para operar
endpoints de registro de resource sets, permissões e introspecção, conforme a
implementação UMA. Esse token é uma credencial administrativa do resource
server e não deve ser entregue ao cliente final.

### Permission ticket

É um identificador de curta duração que representa uma solicitação de
permissões. O authorization server cria ou controla o ticket, e o resource
server o entrega ao client quando precisa que a autorização prossiga.

O ticket não é um access token e não autoriza diretamente o recurso. Ele deve
ser imprevisível, de uso único ou invalidado conforme a política, ter audiência
e expiração adequadas e não aparecer em logs públicos.

### Requesting Party Token

O RPT é um access token associado ao resultado da decisão UMA. Ele representa
permissões concedidas para uma requesting party, client, resource owner,
resource server e authorization server específicos.

Um RPT não deve ser tratado como um bearer universal. O resource server precisa
validar issuer, audience, expiração, assinatura ou introspecção, scopes,
permissões e qualquer vínculo exigido pela implementação.

### Claims e PCT

O authorization server pode solicitar claims adicionais para avaliar a
política. A aplicação pode fornecer um claim token em formato suportado ou
redirecionar o user agent para uma interação de claims.

Persisted Claims Token, PCT, pode representar claims que serão reutilizados em
processos posteriores, conforme a especificação e a implementação. Claims
podem conter dados pessoais e devem ser minimizados, protegidos e limitados à
finalidade que motivou a autorização.

## Fluxo principal do permission ticket

### Requisição sem token

1. O client pede um recurso ao resource server sem access token.
2. O resource server interpreta recurso e scopes solicitados.
3. O resource server registra ou solicita ao authorization server um permission ticket.
4. O resource server responde `401` com `WWW-Authenticate: UMA`.
5. A resposta informa `as_uri`, que identifica o authorization server, e
   `ticket`, que identifica a solicitação.

Exemplo conceitual:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: UMA realm="example",
  as_uri="https://as.example.com",
  ticket="opaque-permission-ticket"
```

Se o resource server não consegue obter o ticket porque o authorization
server está indisponível, ele pode responder como indisponível para autorização
em vez de entregar um ticket inexistente.

### Troca no token endpoint

O client envia o ticket ao token endpoint do authorization server com o grant
type específico de UMA:

```http
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:uma-ticket&ticket=...
```

O authorization server autentica o client conforme sua política, identifica a
requesting party, avalia resource owner, resource set, scopes, claims,
consentimento e contexto, e decide se pode emitir um RPT.

## `urn:ietf:params:oauth:grant-type:uma-ticket`

Esse valor é o identificador literal do grant de UMA usado no parâmetro
`grant_type`. Ele não é uma URL para abrir, não é um scope e não é o nome de
um token. É uma URN registrada para indicar ao token endpoint qual extensão de
OAuth deve processar.

O pedido normalmente contém:

| Parâmetro | Função |
| --- | --- |
| `grant_type` | Deve ser exatamente a URN do grant UMA. |
| `ticket` | Permission ticket mais recente recebido pelo client. |
| `claim_token` | Claims apresentados diretamente, quando necessários. |
| `claim_token_format` | Formato usado para interpretar `claim_token`. |
| `rpt` | RPT existente que o client quer atualizar, conforme a implementação. |
| `scope` | Escopos adicionais ou restrição solicitada, quando suportado. |
| `audience` | Resource server pretendido, quando necessário. |
| `response_mode` | Forma de receber resultado ou interação, quando suportada. |
| `state` | Estado de correlação devolvido em redirecionamento, quando usado. |

Nem todos os parâmetros são obrigatórios em toda tentativa. O client deve
seguir a especificação e a metadata do authorization server, ignorar
parâmetros de resposta desconhecidos e evitar repetir um ticket já consumido.

## Resultados da decisão

### Permissão concedida

O authorization server retorna um RPT, normalmente como access token. O client
usa o RPT no resource server para pedir o recurso. O resource server valida o
RPT e as permissões que ele representa.

### Autorização negada

Se a requesting party não pode obter a permissão, o authorization server
responde com erro ou com um estado de negação conforme o perfil. O client não
deve continuar tentando indefinidamente com o mesmo ticket.

### Interação necessária

O authorization server pode exigir que o resource owner aprove o acesso ou que
o client reúna claims adicionais. Nesse caso, pode retornar um novo ticket,
uma URI de interação, claims exigidas ou um intervalo mínimo de polling.

O recurso ainda não está autorizado. A aplicação deve mostrar uma interação
clara ao usuário e não fingir que um `403` temporário equivale a permissão.

### Polling

Depois que o usuário aprova uma solicitação em outra interação, o client pode
consultar o token endpoint com o ticket atualizado. Deve respeitar o `interval`,
usar backoff e parar quando houver sucesso, negação ou expiração.

Polling sem limite transforma uma decisão pendente em carga e pode permitir
negação de serviço. O ticket deve ser curto e o authorization server deve
detectar abuso.

## Proteção e registro

O resource server registra resource sets e scopes pela Protection API. Isso
separa a operação de proteger recursos da decisão de autorização. O
authorization server usa essas informações para avaliar políticas e emitir
permissões.

O registro deve ser idempotente e controlado. Um resource server comprometido
não pode registrar arbitrariamente todos os recursos de outro proprietário.
Identidade, audience, escopos e ownership precisam ser associados ao client
correto.

## Interação entre os componentes

O modelo pode ser lido como uma sequência de responsabilidades:

1. O resource server conhece o recurso e detecta a ausência de permissão.
2. O authorization server conhece política, owner, requesting party e claims.
3. O client mantém a interação com o usuário e apresenta o token.
4. O resource server aplica a decisão no ponto em que o recurso é servido.

O authorization server não precisa receber o conteúdo do recurso. O resource
server não deve decidir sozinho uma autorização que pertence ao owner. O
client não deve transformar o permission ticket em autorização local sem
receber e validar o RPT.

## UMA e OpenID Connect

OIDC pode autenticar o usuário que participa da interação. OAuth fornece o
token endpoint e o modelo de client e resource server. UMA adiciona a relação
entre resource owner, requesting party, permission ticket e RPT.

A autenticação do usuário pode vir de OIDC, SAML, LDAP, Kerberos ou outro
mecanismo. Isso não muda a semântica do ticket: o authorization server ainda
precisa avaliar a política de acesso ao recurso.

## Casos de uso

### Compartilhamento centrado no usuário

Uma pessoa mantém documentos em um resource server e autoriza outra pessoa a
ler ou editar apenas determinados documentos. Os scopes podem distinguir
`view`, `edit`, `download` e `share`.

### Delegação entre organizações

Uma aplicação de uma organização pede acesso a dados controlados por outra.
O owner pode aprovar o client, restringir scopes e exigir claims ou MFA sem
entregar credenciais ao client.

### Recursos de um dispositivo

Um dispositivo ou serviço protege dados em nome do proprietário, mas a
decisão pode ser tomada por um authorization server central. UMA separa o
serviço que armazena o recurso do serviço que administra a política.

### Autorização assíncrona

O client pode iniciar o pedido, aguardar aprovação e depois trocar o ticket por
um RPT. Isso é diferente de um fluxo em que o owner precisa estar conectado
no mesmo instante da chamada ao recurso.

## Segurança e privacidade

- Use TLS em resource server, protection API e token endpoint.
- Torne permission tickets imprevisíveis, curtos e não reutilizáveis.
- Valide issuer, audience, client, resource owner, scopes e expiração.
- Não aceite ticket destinado a outro authorization server ou resource server.
- Controle quem pode registrar resource sets e permissões.
- Evite revelar se um recurso existe quando isso for informação sensível.
- Proteja claims redirects contra open redirect e requisições forjadas.
- Limite polling e invalide tickets comprometidos.
- Não grave tickets, RPTs ou claims sensíveis em logs comuns.
- Mantenha separadas autenticação, consentimento e autorização de negócio.

## Limitações

UMA não resolve automaticamente descoberta de resource owners, governança de
clientes, revogação universal, consistência de políticas, sincronização de
permissões ou cache de decisão. Cada implementação precisa dizer como um RPT
é revogado, como alterações de policy se propagam e como o resource server
detecta um token desatualizado.

UMA também não é necessário para qualquer API protegida. OAuth com scopes
fixos é mais simples quando o proprietário, o client e o domínio de confiança
são conhecidos e não há autorização delegada assíncrona.

## Fontes

- [UMA 2.0 Core](https://docs.kantarainitiative.org/uma/rec-uma-core.html)
- [UMA 2.0 Grant for OAuth 2.0 Authorization](https://docs.kantarainitiative.org/uma/wg/rec-oauth-uma-grant-2.0.html)
- [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700)

## Continue por aqui

[OAuth 2.0](oauth2.md) explica grants e tokens. [OpenID Connect](openid-connect.md)
explica autenticação federada. [Autenticação e autorização](auth.md) apresenta
a separação entre identidade e permissão.
