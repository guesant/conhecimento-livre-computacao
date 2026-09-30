# SAML

Security Assertion Markup Language, SAML, é uma família de especificações para
trocar assertions de segurança entre domínios. Uma assertion é uma afirmação
estruturada, normalmente XML assinado, sobre um subject, sua autenticação ou
seus atributos.

O uso mais conhecido é o perfil Web Browser SSO. Um Identity Provider, IdP,
autentica o usuário e envia uma assertion para um Service Provider, SP, que
cria a sessão local. SAML também define protocolos, bindings, metadata e
outros perfis, portanto não deve ser reduzido ao formulário de login único.

## Participantes

| Participante | Papel |
| --- | --- |
| Principal ou subject | Entidade descrita pela assertion. |
| End-User | Pessoa que usa o navegador e autentica no IdP. |
| Identity Provider | Autentica o usuário e emite assertions. |
| Service Provider | Confia no IdP e oferece o serviço protegido. |
| User agent | Navegador que transporta mensagens entre IdP e SP. |
| Metadata consumer | Componente que lê metadata de entidades confiáveis. |
| Attribute authority | Fonte que fornece atributos, quando separada do IdP. |

Um produto pode reunir IdP e diretório, mas a assertion deve ser avaliada pelo
SP segundo a confiança estabelecida, não apenas pelo nome do produto.

## Assertion

Uma assertion pode conter statements de autenticação, atributos e autorização.
Elementos importantes incluem issuer, subject, NameID, condições, audiência,
validade, destinatário, momento de autenticação, contexto de autenticação e
atributos.

O SP deve validar assinatura, issuer, audience, Recipient, `InResponseTo`,
NotBefore, NotOnOrAfter, Destination e o vínculo entre a resposta e a
requisição. O relógio dos participantes precisa estar sincronizado dentro da
tolerância definida.

Uma assertion assinada não significa que todos os atributos são verdadeiros
para sempre. Ela é uma afirmação emitida em determinado contexto e com uma
janela de validade.

## Protocolos e bindings

O protocolo SAML define mensagens e operações. Binding define como a mensagem
é transportada por HTTP Redirect, HTTP POST, SOAP ou outro mecanismo. Profile
combina protocolos e bindings em um fluxo interoperável.

O mesmo conceito de login pode usar HTTP-Redirect para uma AuthnRequest e
HTTP-POST para enviar a SAMLResponse, dependendo do perfil e do tamanho da
mensagem. Não confunda binding com o conteúdo da assertion.

## Metadata

Metadata descreve entidades confiáveis, entity ID, endpoints, bindings,
certificados de assinatura ou criptografia e capacidades. SP e IdP podem
publicar metadata individual ou por federação.

Metadata precisa de autenticidade, integridade, rotação de certificados e
controle de quem pode introduzir uma nova entidade. Baixar XML de qualquer
URL e aceitá-lo sem validação cria uma nova autoridade de confiança não
revisada.

## Web Browser SSO, iniciado pelo SP

1. O usuário acessa um recurso protegido no SP.
2. O SP cria uma AuthnRequest com issuer, ACS e estado de correlação.
3. O navegador é redirecionado para o IdP.
4. O IdP autentica o usuário e aplica MFA ou reautenticação, se necessário.
5. O IdP cria uma SAMLResponse com assertion assinada.
6. O navegador envia a resposta ao Assertion Consumer Service, ACS, do SP.
7. O SP valida resposta, assertion, assinatura, condições e correlação.
8. O SP mapeia NameID e atributos para uma conta local e cria a sessão.

O SP deve aceitar apenas a ACS registrada e rejeitar resposta para outro
destino. O identificador da requisição evita aceitar uma resposta antiga ou
gerada para outra sessão.

## Web Browser SSO, iniciado pelo IdP

O usuário começa no portal do IdP e escolhe uma aplicação. O IdP envia uma
assertion ao SP sem que o SP tenha iniciado uma AuthnRequest.

Esse fluxo é conveniente para portais, mas reduz a correlação com uma
requisição específica do SP. A política do SP precisa aceitar explicitamente
esse modo e ainda validar issuer, audiência, ACS, assinatura e validade.

## Atributos e mapeamento

O IdP pode enviar nome, e-mail, grupos, departamento, função, identificadores
e atributos específicos da aplicação. O SP deve declarar quais atributos
necessita, como os nomes são mapeados e o que acontece quando estão ausentes.

Não use e-mail como identificador imutável sem uma política de verificação e
alteração. Não transforme um grupo recebido em acesso administrativo sem um
mapeamento explícito, um escopo de confiança e uma revisão de privilégio.

## Assinatura e criptografia

Assinatura prova integridade e autoria conforme a chave confiável do IdP. Uma
assertion pode ser criptografada para o SP quando atributos não devem ser
visíveis ao navegador ou a intermediários.

Assinatura e criptografia têm finalidades diferentes. O SP precisa validar a
cadeia e os algoritmos permitidos, acompanhar expiração e rotação de
certificados e rejeitar algoritmos fracos ou configurações ambíguas.

## Logout

SAML define perfis de Single Logout que podem propagar uma solicitação entre
SPs e IdP. Logout distribuído é sensível a indisponibilidade, sessões abertas,
timeouts e falhas parciais. A aplicação deve deixar claro se logout local
encerra apenas a sessão no SP ou também tenta encerrar a sessão federada.

## SAML versus OpenID Connect

| Dimensão | SAML | OpenID Connect |
| --- | --- | --- |
| Representação | XML | JSON e JWT |
| Interação comum | Navegador e POST/Redirect | OAuth Authorization Code e PKCE |
| Papel da aplicação | Service Provider | Relying Party |
| Provedor | Identity Provider | OpenID Provider |
| Contrato | Metadata, profiles e assertions | Discovery, JWKS e claims |
| Uso histórico | SSO corporativo e federações | Web, mobile, APIs e SSO moderno |
| Complexidade operacional | XML, certificados, bindings e profiles | Tokens, redirect, PKCE e validação JWT |

SAML não é inseguro por ser XML e OIDC não é seguro apenas por usar JSON.
Ambos dependem de validação rigorosa, chaves, relógio, metadata e mapeamento
de atributos.

## Segurança e privacidade

- Faça validação completa de issuer, assinatura, audiência, destino e validade.
- Proteja metadata e trate rotação de certificados como mudança de confiança.
- Evite aceitar assertions não solicitadas sem política explícita.
- Reduza atributos ao mínimo necessário para o SP.
- Proteja ACS contra CSRF, replay e confusão de destinatário.
- Não registre assertions completas quando elas contêm dados pessoais.
- Defina comportamento para conta desativada e alteração de atributos.
- Use tolerância de relógio pequena e monitore sincronização de tempo.

## Fontes

- [OASIS SAML 2.0](https://www.oasis-open.org/standard/security/)
- [SAML 2.0 Core](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)
- [SAML 2.0 Bindings](https://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf)
- [SAML 2.0 Profiles](https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf)

## Continue por aqui

[OpenID Connect](openid-connect.md) descreve federação baseada em OAuth e JWT.
[LDAP](ldap.md) explica diretórios que podem servir de fonte ao IdP. [FreeIPA](freeipa.md)
mostra uma composição Linux que integra diretório, Kerberos, CA e DNS.
