# Autorização

Autorização é a decisão sobre o que uma identidade autenticada pode fazer em um recurso, em determinado contexto. Ela não substitui a autenticação. A autenticação estabelece quem é o principal; a autorização avalia a operação solicitada, o recurso, as relações e as políticas aplicáveis.

## O problema que a camada resolve

Uma aplicação precisa transformar uma requisição como "Gabriel pode editar o documento 42?" em uma decisão previsível. Essa decisão normalmente envolve o principal, a ação, o recurso, o tenant, os papéis, a propriedade do recurso, o estado do objeto e atributos do contexto, como horário, rede ou nível de autenticação.

Se essa lógica for espalhada por controllers, componentes de interface, queries e jobs, as regras divergem. A aplicação pode esconder um botão no frontend e ainda aceitar a operação indevida no backend. Por isso, a decisão deve ser aplicada no ponto que protege o recurso, com o frontend funcionando apenas como conveniência de experiência do usuário.

## Componentes

Os nomes variam entre produtos, mas uma arquitetura de autorização costuma conter:

- **PEP, Policy Enforcement Point**, o ponto que intercepta a operação e aplica a decisão;
- **PDP, Policy Decision Point**, o componente que avalia políticas e retorna permitir ou negar;
- **PIP, Policy Information Point**, as fontes de atributos e relações usadas na avaliação;
- **PAP, Policy Administration Point**, a superfície que cria, revisa e publica políticas;
- **policy store**, o armazenamento das políticas, modelos, relações ou versões;
- **principal**, o usuário, serviço, dispositivo ou workload que inicia a ação;
- **resource**, o objeto protegido;
- **action**, a operação que será autorizada;
- **context**, dados do pedido que podem alterar a decisão.

O PEP pode ser um middleware HTTP, uma policy guard em um resolver GraphQL, uma checagem no serviço de domínio ou uma regra em um gateway. O PDP pode ser uma biblioteca embutida no processo ou um serviço remoto. Essa escolha define o custo de rede, a consistência das alterações e a forma de operar indisponibilidade.

## Modelos de autorização

### ACL

Uma lista de controle associa sujeitos e permissões diretamente a recursos. É simples de entender para poucos objetos, mas tende a ficar difícil de administrar quando há muitos usuários e recursos.

### RBAC

O controle baseado em papéis associa usuários a papéis e papéis a permissões. É adequado quando as responsabilidades da organização são estáveis. Hierarquia de papéis, escopo por tenant e separação de funções precisam ser definidos explicitamente para evitar privilégios acumulados sem controle.

### ABAC

O controle baseado em atributos avalia propriedades do principal, do recurso e do contexto. Ele expressa regras como permitir leitura quando o departamento do usuário coincide com o departamento do documento. É flexível, mas depende de atributos confiáveis, normalizados e disponíveis no momento da decisão.

### ReBAC

O controle baseado em relações representa relações como `viewer`, `editor`, `owner` ou `member` entre entidades. Ele é útil para compartilhamento, hierarquias de pastas, organizações, projetos e colaboração. A autorização depende de atravessar o grafo de relações, em vez de apenas comparar atributos locais.

### Policy-based access control

Uma política declarativa descreve as condições que permitem ou negam ações. Ela pode expressar RBAC, ABAC, ReBAC ou uma composição dos três. O benefício é separar a decisão do código de negócio; o risco é criar políticas difíceis de testar, revisar e observar.

Na prática, modelos costumam ser combinados. Um usuário pode pertencer a um grupo, o grupo pode ter uma relação com um projeto e uma política pode exigir MFA para uma ação sensível.

## Biblioteca, linguagem e serviço

As cinco soluções desta seção não ocupam o mesmo lugar:

- Casbin é principalmente uma biblioteca de enforcement com modelos configuráveis;
- Casdoor é uma plataforma de IAM e SSO que também gerencia papéis e permissões;
- Cedar é uma linguagem e engine de políticas, com validação e semântica própria;
- CASL é uma biblioteca JavaScript e TypeScript para expressar abilities no backend e frontend;
- OpenFGA é um serviço de autorização relacional baseado em modelos e tuplas.

Casdoor pode usar Casbin internamente, mas isso não transforma os dois em produtos equivalentes. CASL não substitui um provedor de identidade. Cedar não é um diretório de usuários. OpenFGA não é um servidor OIDC. Cada um resolve uma fronteira diferente. Os modelos de decisão estão detalhados na [taxonomia de modelos de autorização](modelos/index.md).

## Decisões operacionais

Uma solução de autorização deve definir, antes da implementação:

1. se a decisão acontece localmente ou por rede;
2. qual é a fonte de identidade, papéis, atributos e relações;
3. se a falha do PDP deve negar ou permitir;
4. qual consistência é aceitável depois de uma mudança de permissão;
5. como políticas e modelos são versionados, revisados e publicados;
6. como decisões são auditadas sem registrar dados sensíveis desnecessários;
7. como consultas em lote ou filtragem de listas evitam o padrão N+1;
8. como revogação e remoção de usuário se propagam.

O padrão mais seguro para operações mutáveis é fail closed. Para uma tela de leitura não crítica, pode existir uma degradação controlada, mas ela não deve converter indisponibilidade do autorizador em acesso privilegiado.

## Autorização no frontend

O frontend pode consultar uma ability para esconder ações impossíveis, desabilitar controles e evitar chamadas que certamente seriam rejeitadas. Isso melhora a experiência, mas não protege o recurso. O backend precisa repetir a decisão usando uma identidade validada e dados confiáveis.

Também é importante separar filtragem de autorização. `Listar apenas os documentos permitidos` requer que a query ou o serviço de autorização produza um conjunto seguro. Buscar todos os documentos e filtrar apenas no cliente expõe dados indevidos, mesmo que a interface não os mostre.

## Relação com identidade

OIDC, OAuth 2.0, SAML e LDAP ajudam a autenticar ou transportar identidade e atributos. Eles não definem, por si só, se uma pessoa pode editar um recurso de negócio. Um token pode carregar grupos ou scopes, mas o serviço responsável ainda precisa interpretar esses dados dentro do seu modelo de autorização.

Veja também [autenticação e autorização](../identidade/fundamentos/index.md), [OAuth 2.0](../identidade/oauth2.md), [OpenID Connect](../identidade/openid-connect.md), [RBAC do Kubernetes](../../kubernetes/access/rbac.md), [policy enforcement](../iac/policy-enforcement.md) e o [comparativo das soluções](comparativo.md).

## Fontes

- [NIST, Guide to Attribute Based Access Control](https://csrc.nist.gov/publications/detail/sp/800-162/final)
- [NIST, Role Based Access Control](https://csrc.nist.gov/projects/role-based-access-control)
- [OAuth 2.0, RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)
