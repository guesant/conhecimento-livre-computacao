# Autenticação e autorização

Autenticação e autorização são decisões diferentes dentro do controle de
acesso. Autenticação, frequentemente abreviada como AuthN, responde quem é o
ator. Autorização, AuthZ, responde o que esse ator pode fazer sobre qual
recurso e em qual contexto.

Um login bem-sucedido não implica acesso irrestrito. Uma requisição pode
carregar uma identidade autenticada e ainda ser negada por falta de permissão,
tenant incorreto, recurso inexistente, política de horário ou estado do
recurso.

## Vocabulário

| Termo | Significado |
| --- | --- |
| Identidade | Representação administrada de uma pessoa, serviço, dispositivo ou organização. |
| Principal | Entidade que pode ser autenticada e receber uma decisão de acesso. |
| Subject | Identificador do principal em um protocolo ou token. |
| Credential | Evidência usada para autenticar, como senha, chave, certificado ou fator. |
| Authenticator | Mecanismo que prova posse ou controle de uma credencial. |
| Autenticação | Verificação de uma identidade ou de uma prova de posse. |
| Autorização | Decisão sobre uma ação em um recurso. |
| Resource owner | Entidade que pode autorizar acesso a um recurso. |
| Client | Aplicação que age em nome de uma pessoa ou de si própria. |
| Resource server | Serviço que hospeda e protege o recurso. |
| Authorization server | Serviço que autentica, consente e emite credenciais de acesso. |
| Identity Provider | Serviço que autentica o usuário e publica sua identidade para consumidores. |
| Relying Party | Aplicação que confia na autenticação publicada por um provedor. |
| Directory | Serviço consultável que organiza identidades e atributos. |
| Claim | Afirmação sobre um subject, como nome, grupo ou método de autenticação. |
| Scope | Conjunto nomeado de permissões ou de dados solicitados. |
| Role | Agrupamento de responsabilidades que pode ser atribuído a um principal. |
| Permission | Ação específica permitida sobre um recurso. |
| Policy | Regra que combina identidade, recurso, ação e contexto para decidir acesso. |
| Session | Estado temporário que representa uma interação autenticada. |
| Token | Credencial ou artefato que representa uma autorização, identidade ou contexto. |

Os significados concretos variam por protocolo. `scope` no OAuth é uma
linguagem de autorização solicitada ao servidor, enquanto um claim `groups` em
um ID token é uma afirmação sobre o usuário. Nenhum dos dois deve ser tratado
automaticamente como uma permissão final sem uma política local.

## Ciclo de uma decisão de acesso

Uma requisição protegida costuma passar por estas etapas:

1. O cliente apresenta uma credencial, sessão ou token.
2. O componente de autenticação valida origem, assinatura, expiração,
   audience, nonce, certificado ou outro vínculo exigido.
3. O sistema identifica o subject e recupera atributos necessários.
4. A autorização avalia recurso, ação, tenant, método, estado e contexto.
5. O serviço executa ou nega a operação.
6. O evento pode ser registrado para auditoria sem gravar segredos ou tokens.

Um gateway pode executar parte dessas etapas, mas o serviço de destino deve
continuar responsável por validar o contexto que só ele conhece. Autenticar no
gateway não autoriza automaticamente uma operação de negócio no backend.

## Fatores e métodos de autenticação

Os fatores podem ser classificados como conhecimento, posse e inerência. Uma
senha é conhecimento. Um dispositivo ou uma chave privada é posse. Uma
característica biométrica é inerência. MFA combina fatores independentes, mas
dois elementos derivados da mesma senha não formam dois fatores independentes.

Outros mecanismos incluem certificados X.509, passkeys, WebAuthn, smart cards,
Kerberos, tokens de hardware e autenticação federada. A escolha depende do
risco, do dispositivo, da recuperação de conta, da resistência a phishing e
da capacidade operacional.

## Sessão, cookie e token

Uma sessão de servidor mantém o estado no backend e entrega ao navegador um
identificador aleatório, normalmente em cookie protegido por `Secure`,
`HttpOnly` e `SameSite` conforme o fluxo. O navegador não precisa conhecer os
atributos da identidade.

Um token pode ser opaco ou conter claims assinados. Um JWT assinado permite
validação local, mas não é automaticamente revogável antes de expirar. Um
token opaco exige introspecção ou lookup, mas permite que o servidor controle
estado e revogação centralmente.

Não coloque tokens de longa duração em URLs. Não trate um cookie como prova de
autorização sem proteção contra CSRF quando o navegador o envia
automaticamente.

## Identidade, diretório e federação

Um diretório LDAP organiza identidades e atributos, mas não precisa ser o
componente que autentica ou emite tokens. Kerberos autentica por tickets, mas
não é o diretório de atributos. OpenID Connect publica identidade sobre OAuth.
SAML publica assertions para federação. Um provedor como Keycloak pode
integrar diretórios e emitir tokens, mas continua sendo necessário definir
claims, mapeamentos e políticas.

[LDAP](ldap.md), [MIT Kerberos](kerberos.md), [OpenID Connect](openid-connect.md)
e [SAML](saml.md) detalham essas funções separadamente.

## SSO e federação

Single Sign-On, SSO, permite que uma autenticação seja reutilizada por várias
aplicações dentro de um domínio de confiança. Federação ocorre quando um
provedor e uma aplicação pertencem a domínios administrativos distintos e
estabelecem confiança por metadados, certificados, issuer, audience e regras
de claims.

SSO não elimina a necessidade de logout, expiração, revogação, reautenticação,
MFA, autorização local e isolamento entre aplicações. Uma sessão central pode
estar válida enquanto a aplicação específica removeu a conta ou reduziu suas
permissões.

## Erros e respostas

Use `401 Unauthorized` quando a requisição não tem uma autenticação válida ou
não apresenta a credencial exigida. Use `403 Forbidden` quando a identidade
foi reconhecida, mas a política não permite a operação. A distinção depende do
protocolo e do risco de revelar existência de recursos, portanto APIs podem
usar uma resposta uniforme em alguns casos.

Não redirecione uma API JSON para uma página de login. Redirecionamento é
adequado para o navegador em um fluxo interativo, mas consumidores de API
precisam receber um erro estruturado e um mecanismo explícito de renovação ou
obtenção de token.

## Princípios de segurança

- Conceda o menor escopo e a menor duração necessários.
- Valide issuer, audience, assinatura, algoritmo, expiração e nonce conforme o protocolo.
- Use redirect URIs exatas e não aceite valores arbitrários.
- Separe autenticação de autorização por recurso e ação.
- Não confie em claims recebidos pelo cliente sem validar a origem.
- Evite tokens em URLs, logs, histórico e mensagens de erro.
- Proteja refresh tokens e credenciais de cliente como segredos de alto impacto.
- Planeje revogação, rotação, logout e recuperação de conta.
- Trate sincronização de relógio e rotação de chaves como dependências operacionais.
- Audite decisões sem armazenar material secreto desnecessário.

## Relação entre os protocolos

| Protocolo ou mecanismo | Pergunta principal |
| --- | --- |
| LDAP | Como consultar e alterar identidades e atributos em um diretório? |
| Kerberos | Como autenticar por tickets em um domínio de confiança? |
| OAuth 2.0 | Como delegar acesso a um recurso sem compartilhar a credencial do proprietário? |
| OpenID Connect | Como autenticar o usuário e publicar claims interoperáveis sobre sua identidade? |
| SAML | Como federar autenticação e atributos entre um IdP e um service provider? |
| UMA | Como permitir que o proprietário controle acesso delegado a recursos protegidos? |

## Fontes

- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700)
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)
- [SAML 2.0 Technical Specifications](https://www.oasis-open.org/standard/security/)

## Continue por aqui

[OAuth 2.0](oauth2.md) trata delegação de autorização. [OpenID Connect](openid-connect.md)
adiciona identidade. [UMA](uma.md) detalha autorização gerenciada pelo
proprietário do recurso.
