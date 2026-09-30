# Casbin

Casbin é uma biblioteca de controle de acesso que avalia requisições contra um modelo e um conjunto de políticas. O formato clássico de uma decisão é sujeito, objeto e ação, mas o modelo pode definir outras dimensões, como domínio, tenant, segundo sujeito ou atributos.

Casbin é adequado quando a aplicação quer manter o enforcement próximo ao código e controlar a forma da política sem introduzir necessariamente um serviço remoto. Há implementações para várias linguagens, incluindo Go, Java, Node.js, PHP, Python, C# e Rust.

## O que Casbin não faz

Casbin não é provedor de identidade. Ele não autentica senha, não substitui OIDC, SAML ou LDAP e não é um diretório de usuários. A aplicação precisa fornecer o principal autenticado e as informações necessárias à decisão.

Ele também não torna automaticamente correta a modelagem de autorização. Um matcher permissivo, uma associação de papel não validada ou um adapter que não persiste mudanças de forma confiável pode produzir uma decisão insegura.

## Modelo

Um modelo Casbin separa a estrutura da requisição, das políticas e da avaliação. As seções mais comuns são:

```ini
[request_definition]
r = sub, obj, act

[policy_definition]
p = sub, obj, act, eft

[policy_effect]
e = some(where (p.eft == allow)) && !some(where (p.eft == deny))

[matchers]
m = r.sub == p.sub && r.obj == p.obj && r.act == p.act
```

O modelo pode ainda definir `[role_definition]` para RBAC, funções para correspondência de caminhos, domínios para multi-tenancy e políticas com atributos. O enforcer recebe a requisição, encontra as regras aplicáveis, executa o matcher e combina os efeitos segundo a seção `policy_effect`.

O exemplo acima usa a forma comum de configuração. Em um projeto real, o nome das colunas, a ordem das avaliações e a semântica de negar devem ser testados com casos positivos e negativos. A ausência de uma regra deve resultar em deny quando o domínio exige default deny.

## Políticas e relações

Políticas podem descrever permissões diretas, enquanto grouping policies descrevem relações como usuário pertencente a papel ou papel herdando de outro papel. RBAC com domínio permite escopos como organização, projeto ou tenant:

```text
p, editor, project:42, write
g, alice, editor, tenant:acme
```

O matcher precisa interpretar o domínio. Sem uma dimensão de tenant, uma associação de papel pode vazar entre organizações. Em ReBAC, as relações podem ser modeladas com funções ou estruturas de políticas, mas o custo e a clareza devem ser avaliados contra uma solução especializada como OpenFGA.

## Persistência e distribuição

O enforcer pode carregar políticas de arquivo, banco de dados ou outro adapter. O adapter é responsável pela persistência, não pela decisão. Adapters filtrados permitem carregar somente um subconjunto, o que reduz memória e tempo de inicialização em aplicações grandes.

Watchers e dispatchers permitem avisar outras instâncias quando políticas mudam. Eles não devem ser tratados como uma garantia automática de consistência. É necessário definir o comportamento quando uma notificação é perdida, quando duas instâncias atualizam a política ao mesmo tempo e quando uma instância continua usando cache antigo.

Uma configuração distribuída precisa esclarecer:

- quem pode alterar políticas;
- como a alteração é autenticada e auditada;
- quando cada instância deve recarregar o modelo;
- como ocorre rollback de uma política incorreta;
- qual é a janela máxima de permissão obsoleta;
- como o serviço se comporta se o storage ficar indisponível.

## Desempenho

O custo do enforcement depende do número de regras, da complexidade do matcher, das consultas de papéis e das funções auxiliares. O próprio modelo pode ser otimizado colocando comparações baratas antes de consultas de relação mais custosas. Isso não substitui benchmark com a distribuição real de usuários, papéis e recursos.

Cache de decisão pode reduzir latência, mas aumenta o risco de servir uma permissão revogada. O TTL deve refletir o requisito de revogação. Para operações críticas, a aplicação pode preferir recarregar ou invalidar explicitamente políticas depois de uma mudança.

## Integração na aplicação

O PEP normalmente valida o token ou a sessão antes de chamar Casbin. Depois, passa um principal normalizado, um identificador de recurso e uma ação estável. A ação deve representar uma capacidade de negócio, como `content.publish`, e não apenas uma string de rota que muda durante uma refatoração.

Não é suficiente proteger apenas o menu ou o controller. Jobs, comandos administrativos, endpoints internos e operações em lote também precisam chamar o mesmo serviço de autorização ou um serviço de domínio que o encapsule.

Para listas, não se deve buscar todos os registros e chamar `Enforce` individualmente sem medir o padrão N+1. Use filtros no banco, adapters de dados autorizados ou operações em lote quando a semântica do modelo permitir.

## Casos adequados

Casbin funciona bem quando:

- o serviço já possui o ciclo de vida dos usuários e papéis;
- a decisão precisa ser local e de baixa latência;
- o modelo de autorização pode ser expresso em matchers;
- a equipe quer uma biblioteca em vez de mais um serviço operacional;
- há necessidade de usar a mesma ideia em diferentes linguagens.

Ele é menos apropriado quando o problema principal é atravessar um grafo grande de relações, consultar permissões em muitas entidades ou centralizar autorização de dezenas de serviços sem duplicar dados de relacionamento.

## Relação com outras soluções

Casbin e CASL são bibliotecas embutidas, mas Casbin é orientado a modelos e políticas com suporte amplo a linguagens, enquanto CASL é especialmente natural no ecossistema JavaScript e TypeScript. Cedar oferece uma linguagem com schema e ferramentas próprias. OpenFGA oferece um serviço especializado em relações. Casdoor inclui identidade, SSO e administração, além de usar Casbin para parte do controle de acesso.

## Fontes

- [Apache Casbin, overview](https://casbin.apache.org/docs/overview/)
- [Apache Casbin, syntax for models](https://casbin.apache.org/docs/syntax-for-models/)
- [Apache Casbin, access control models](https://casbin.apache.org/docs/access-control-model/)
- [Apache Casbin, adapters](https://casbin.apache.org/docs/adapters/)
- [Apache Casbin, watchers](https://casbin.apache.org/docs/watchers/)
