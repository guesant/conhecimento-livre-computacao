# Casdoor

Casdoor é uma plataforma de identidade e acesso com interface de administração, SSO e integração com aplicações. Seu escopo é mais amplo que o de uma biblioteca de autorização: ele gerencia usuários, organizações, aplicações, provedores de identidade e configurações de login, além de expor protocolos como OAuth 2.0 e OpenID Connect.

## Posição arquitetural

Casdoor fica entre um provedor de identidade e uma plataforma de IAM. Ele pode autenticar usuários localmente ou federar provedores externos, emitir tokens e disponibilizar dados de identidade para aplicações. Também possui recursos de papéis e permissões, com autorização baseada em Casbin.

Isso significa que Casdoor pode ocupar duas funções relacionadas, mas distintas:

1. emitir uma identidade autenticada e os tokens que a representam;
2. administrar parte das permissões e associações de usuários da plataforma.

A aplicação ainda precisa validar tokens, definir seus recursos e impedir que uma permissão administrada no Casdoor seja interpretada além do escopo esperado. A existência de um grupo no provedor não substitui uma policy guard no serviço que protege o dado.

## Conceitos

Os conceitos centrais incluem:

- **organization**, o limite administrativo que agrupa usuários e aplicações;
- **user**, a identidade administrada pelo sistema;
- **application**, a configuração de um cliente que integra login e emissão de tokens;
- **provider**, a conexão com um mecanismo externo de identidade ou comunicação;
- **role e permission**, os objetos de autorização administrados;
- **adapter**, a persistência usada pelo serviço;
- **token**, a credencial que a aplicação consumidora deve validar.

Os nomes e campos exatos devem ser conferidos na versão implantada. O fato de um usuário ter um campo estendido de papéis ou permissões não significa que essa informação deva ser aceita cegamente por qualquer API. O consumidor deve validar issuer, audience, assinatura, expiração, escopos e o mapeamento entre organização e tenant.

## Fluxo OIDC

Em uma integração OIDC típica, a aplicação registra um cliente, redireciona o navegador para o Casdoor, recebe um authorization code e troca esse código por tokens usando o endpoint de token. Com PKCE, o cliente envia um code challenge no início e prova o code verifier no resgate.

Depois da troca, a aplicação valida o ID token como artefato de identidade e usa o access token para chamar recursos autorizados. O ID token não deve ser usado como access token de uma API apenas porque é um JWT. A aplicação deve consultar a discovery document e usar as chaves do issuer configurado.

Para aplicações web com backend, é preferível manter tokens no servidor e expor ao navegador uma sessão protegida. Para clientes públicos, o código com PKCE é o fluxo apropriado. Client secrets não podem ser embutidos em frontend distribuído.

## Multi-tenancy e autorização

Organizations podem fornecer uma fronteira administrativa, mas a aplicação precisa decidir se esse limite coincide com seu tenant de negócio. Quando não coincide, inclua o tenant no modelo de autorização e teste explicitamente casos de usuário com vínculos em múltiplas organizações.

Papéis globais e papéis por aplicação têm riscos diferentes. Um papel administrativo global deve ser raro, protegido por MFA e auditado. Permissões de leitura, edição e publicação devem ser escopadas ao recurso ou organização quando a regra de negócio exigir.

Casdoor usa Casbin como base de autorização, mas a política Casbin e o modelo editorial da aplicação não são automaticamente idênticos. Se a aplicação precisa de relações profundas entre usuários, projetos, pastas e documentos, OpenFGA ou uma camada relacional própria pode representar esse grafo com mais clareza.

## Administração e segurança

O painel de IAM é uma superfície privilegiada. Ele deve ter autenticação forte, autorização separada para administração, proteção contra CSRF quando aplicável, logs de alterações e backup das configurações. A conta global de administração não deve ser usada como identidade de integração.

As integrações devem configurar explicitamente:

- issuer e audience esperados;
- algoritmos e chaves aceitos;
- scopes exigidos;
- mapeamento de subject para usuário local;
- política de expiração e renovação;
- comportamento para usuário desativado;
- rotação de credenciais e chaves;
- limites de requisição e observabilidade.

O logout local, a revogação de sessão e a invalidação de tokens emitidos não são necessariamente a mesma operação. A aplicação deve definir qual sessão continua válida depois de uma alteração de senha, remoção de papel ou desativação da conta.

## Casos adequados

Casdoor é uma opção quando se deseja uma plataforma de identidade self-hosted com UI, múltiplos provedores e protocolos padronizados, sem montar todos os componentes de IAM do zero. Ele pode servir aplicações próprias, integrações B2B e cenários multi-organização.

Ele não é simplesmente um banco de usuários para ser consultado diretamente pela aplicação. Também não elimina a necessidade de um modelo de autorização local. A decisão entre Casdoor, Keycloak, Authentik ou outro IdP deve considerar maturidade operacional, protocolos exigidos, governança, extensão, suporte e o custo de manter mais uma superfície privilegiada.

## Relação com as outras páginas

Para os fluxos de identidade, veja [OpenID Connect](../identidade/openid-connect.md), [OAuth 2.0](../identidade/oauth2.md) e [SAML](../identidade/saml.md). Para enforcement embutido, veja [Casbin](casbin.md) e [CASL](casl.md). Para políticas separadas do código, veja [Cedar](cedar.md). Para relações em grafo, veja [OpenFGA](openfga.md).

## Fontes

- [Casdoor, documentation overview](https://casdoor.ai/docs/overview/)
- [Casdoor, basic concepts](https://casdoor.ai/docs/basic-concepts/)
- [Casdoor, authentication](https://casdoor.ai/docs/user/overview/)
- [Casdoor, source repository](https://github.com/casdoor/casdoor)
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)
