# Cedar

Cedar é uma linguagem declarativa e um motor de avaliação de políticas para autorização. A aplicação constrói uma requisição com principal, ação, recurso e contexto, fornece as entidades necessárias e pede ao authorizer uma decisão `Allow` ou `Deny`.

Cedar separa a lógica de autorização da lógica de negócio sem exigir que a decisão seja um serviço remoto. O motor pode ser embutido no processo, enquanto políticas e schemas podem ser versionados, validados e publicados por uma plataforma externa.

## Modelo PARC

Uma requisição Cedar é descrita pelo acrônimo PARC:

- **principal**, a identidade que quer agir;
- **action**, a operação solicitada;
- **resource**, o objeto protegido;
- **context**, dados transitórios da requisição.

As entidades fornecem atributos e relações usados pela política. O schema define tipos, ações, atributos e relações aceitas. O schema valida a forma das políticas, mas não substitui os dados concretos que a aplicação precisa fornecer durante uma decisão.

## Sintaxe

Uma policy básica declara `permit` ou `forbid`, delimita principal, ação e recurso, e pode adicionar `when` ou `unless`:

```cedar
permit (
  principal in Group::"editors",
  action == Action::"read",
  resource is Document
)
when {
  resource.project == principal.project
};
```

Uma política `forbid` satisfeita sempre produz deny final. Na ausência de uma política `permit` aplicável, a decisão também é deny. Essa combinação de default deny e deny explícito facilita representar exceções, mas exige testes para garantir que um `forbid` não foi aplicado a uma entidade errada.

Cedar possui políticas estáticas e templates vinculados. Templates permitem expressar um padrão reutilizável e instanciá-lo para principais ou recursos específicos. O uso de templates não elimina a necessidade de revisar as instâncias geradas.

## Avaliação e dados

O authorizer não busca automaticamente todos os dados da aplicação. O PEP precisa montar a lista relevante de entidades, relações, atributos e contexto. Se um atributo necessário não for carregado, a decisão pode ser deny ou produzir erro, conforme o caso. Se dados demais forem enviados, aumenta-se custo, latência e risco de exposição.

Uma integração deve normalizar identificadores antes da avaliação. Não use `context` como depósito de principal, ação ou recurso, pois isso dificulta o schema e pode permitir que a aplicação bypass a estrutura declarada. Dados de identidade e recursos devem aparecer nos tipos próprios do modelo.

## Validação e análise

O schema ajuda a detectar ações, tipos e atributos inválidos quando a política é criada ou atualizada. Ferramentas do ecossistema Cedar podem analisar políticas e verificar propriedades do conjunto, mas nenhuma ferramenta garante que os dados de negócio enviados pelo PEP representam corretamente o estado real.

Políticas devem ter testes de autorização, incluindo:

- decisão permitida esperada;
- decisão negada por ausência de permissão;
- negação explícita;
- isolamento entre tenants;
- relações indiretas;
- atributos ausentes ou inválidos;
- expiração de sessão e autenticação forte;
- casos de alteração ou remoção de vínculo.

## Deployment

Há duas formas principais de usar Cedar:

1. **engine embutido**, com policies e entidades no processo ou fornecidas pela aplicação;
2. **serviço de autorização**, que hospeda políticas e fornece uma API para decisões.

O engine embutido reduz latência e dependências de rede, mas torna a distribuição de políticas e entidades responsabilidade da aplicação. O serviço centraliza publicação, auditoria e integração entre múltiplos consumidores, mas introduz disponibilidade, autenticação entre serviços, latência e consistência.

Em ambos os modelos, defina versões de schema e política. Uma atualização precisa ser validada antes de substituir a versão ativa. O rollback deve ser rápido e não depender de editar políticas manualmente em produção.

## Segurança e limites

Cedar fornece uma semântica de avaliação, mas não autentica o principal, não emite tokens, não armazena usuários e não corrige um PEP que omite uma chamada de autorização. O serviço chamador continua responsável por validar a identidade, carregar entidades corretas e aplicar a decisão antes da operação.

O desempenho depende do tamanho dos dados e da complexidade da política. Não é correto assumir que uma engine local torna qualquer modelo barato. Meça o caminho quente, limite a quantidade de entidades e evite políticas que exigem reconstituir uma grande hierarquia a cada pedido.

## Quando escolher Cedar

Cedar é interessante quando a equipe quer uma linguagem de autorização independente da aplicação, com schemas, validação, políticas legíveis e uma engine local ou hospedada. Ele é especialmente adequado para ABAC, RBAC com atributos e políticas de recursos.

OpenFGA tende a ser mais natural quando o problema principal é consultar relações persistentes em um grafo. Casbin pode ser mais simples quando o modelo cabe em uma biblioteca integrada e uma configuração de matcher. CASL é mais direto para abilities em aplicações JavaScript e TypeScript. Casdoor entra quando também é necessário administrar identidade e SSO.

## Fontes

- [Cedar Policy Language Reference](https://docs.cedarpolicy.com/)
- [Cedar authorization](https://docs.cedarpolicy.com/auth/authorization.html)
- [Cedar terminology](https://docs.cedarpolicy.com/overview/terminology.html)
- [Cedar policy syntax](https://docs.cedarpolicy.com/policies/syntax-policy.html)
- [Cedar security](https://docs.cedarpolicy.com/other/security.html)
- [Cedar project](https://www.cedarpolicy.com/)
