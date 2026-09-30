# Attribute-Based Access Control

Attribute-Based Access Control, ABAC, decide acesso avaliando atributos do principal, do recurso, da ação e do ambiente contra regras ou políticas. Em vez de perguntar apenas qual papel o usuário possui, ABAC pode perguntar se o departamento do principal coincide com o departamento do documento e se a requisição veio de uma rede permitida.

## Atributos

Os atributos podem vir de fontes diferentes:

- principal: subject, departamento, vínculo, nível de autenticação;
- recurso: proprietário, classificação, tenant, estado;
- ação: operação, finalidade, sensibilidade;
- ambiente: horário, localização, endereço de rede, risco ou dispositivo.

A decisão só é confiável se essas fontes forem autenticadas, atualizadas e semanticamente consistentes. Um atributo ausente não deve ser interpretado como permissão.

## Política

Uma política ABAC descreve uma relação entre atributos. Um exemplo conceitual seria permitir leitura quando `principal.department == resource.department`, `resource.state == published` e `context.mfa == true`.

O modelo deve definir tipos, normalização, precedência de regras, comportamento de conflito e efeito de erros. Políticas separadas do código podem ser revisadas por segurança, mas precisam de testes para evitar diferenças entre intenção e implementação.

## Fluxo XACML e equivalente

Uma arquitetura ABAC costuma separar o PEP, que intercepta a requisição, o PDP, que avalia a política, o PIP, que fornece atributos, e o PAP, que administra regras. O fluxo pode ser local ou remoto. O nome dos componentes não exige XACML, mas ajuda a localizar responsabilidades.

O PEP deve enviar o mínimo necessário ao PDP. O PIP precisa ter donos definidos para atributos como departamento, classificação e postura do dispositivo. O PAP deve validar e publicar políticas com controle de versão. Sem essa divisão, uma aplicação pode buscar atributos de fontes inconsistentes e produzir decisões diferentes.

## Combinação de políticas

Conjuntos de políticas precisam definir como combinar resultados. Estratégias comuns incluem deny-overrides, permit-overrides, first applicable e decisão por prioridade. Default deny deve ser explícito. Erro, ausência de atributo e indeterminação não podem ser convertidos silenciosamente em permit.

Políticas também precisam definir o que acontece com conflito entre uma regra global e uma regra de tenant. Uma ordem implícita baseada no arquivo ou na ordem de consulta é frágil.

## Desempenho e cache

ABAC pode ser rápido quando atributos já estão no processo, mas pode ficar lento quando cada decisão chama diretórios, bancos e serviços de risco. Agrupe atributos, use cache com TTL coerente e observe a idade de cada valor. Para escrita crítica, prefira dados atuais a um cache cuja revogação não possa ser garantida.

Uma política que exige dezenas de atributos deve ser questionada. Muitas dependências ampliam o domínio de falha e dificultam explicar a decisão ao usuário.

## Vantagens

ABAC reduz a quantidade de papéis e representa contexto, multi-tenancy e classificação de dados com precisão. Ele é útil quando pessoas desempenham funções diferentes em recursos diferentes ou quando regras precisam se aplicar a usuários que não foram previamente cadastrados em uma lista de papéis.

## Custos

O modelo depende de muitos dados no momento da decisão. Atributos podem estar desatualizados, sofrer spoofing, ter semântica diferente em serviços distintos ou exigir consultas adicionais. Uma policy que parece pequena pode ter uma cadeia grande de fontes e chamadas.

Documente o dono de cada atributo, seu TTL, formato, origem e comportamento quando estiver indisponível. Cache de atributos deve considerar revogação. Não passe ao PDP um objeto inteiro quando apenas alguns campos são necessários.

## Relação com RBAC e PBAC

RBAC pode ser uma fonte de atributos, como `principal.roles`. ABAC pode incorporar papéis e condições. PBAC é o enquadramento mais amplo de decisão por políticas, enquanto ABAC descreve a parte da política que usa atributos. Cedar é uma linguagem que pode expressar ABAC. Casbin possui modelos ABAC e matchers que avaliam atributos.

## Segurança

Não confie em atributos enviados diretamente pelo cliente. Valide a identidade, busque atributos no backend ou em fontes confiáveis e vincule-os ao tenant. Teste valores ausentes, tipos incorretos, relógio alterado, rede desconhecida e atributos conflitantes.

## Explicabilidade

Uma decisão ABAC deve permitir descobrir quais regras foram avaliadas e quais atributos foram determinantes, sem registrar valores sensíveis desnecessariamente. Mensagens para o usuário podem ser genéricas, enquanto a auditoria guarda uma referência à policy, ao modelo e à versão dos atributos.

## Exemplo de decisão

Uma API de documentos pode exigir `principal.tenant == resource.tenant`, `principal.department == resource.department`, `action == read` e `resource.state == published`. Uma operação de publicação pode exigir papel específico, MFA e uma relação de aprovação. Esses critérios podem permanecer em uma política, mas o serviço deve garantir que os quatro conjuntos de dados foram obtidos de fontes confiáveis.

## Fontes

- [NIST SP 800-162, ABAC guide](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)
- [NIST, ABAC project](https://csrc.nist.gov/projects/attribute-based-access-control)
- [NIST ABAC glossary](https://csrc.nist.gov/glossary/term/ABAC)
