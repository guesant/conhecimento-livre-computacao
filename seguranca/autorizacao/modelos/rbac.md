# Role-Based Access Control

Role-Based Access Control, RBAC, associa permissões a papéis e papéis a usuários, grupos ou outros papéis. A pessoa não recebe cada permissão diretamente; ela ativa ou herda os papéis que representam suas responsabilidades.

## Elementos

Um modelo RBAC completo costuma distinguir:

- usuários ou subjects;
- papéis;
- permissões;
- operações e objetos;
- atribuições de usuário para papel;
- atribuições de permissão para papel;
- sessões e papéis ativos;
- hierarquia entre papéis;
- restrições, como separação de funções.

RBAC0 é o núcleo. RBAC1 adiciona hierarquia. RBAC2 adiciona restrições. RBAC3 combina os componentes. Uma aplicação que apenas chama um campo `role` de RBAC pode não implementar esses elementos de forma completa, mas deve declarar sua simplificação.

## Hierarquia e escopo

Hierarquia permite que um papel sênior herde permissões de um papel inferior. A relação precisa ser acíclica e ter semântica clara. Em aplicações multi-tenant, o papel deve ser escopado ao tenant, organização ou projeto quando a função não for global.

`editor` em uma organização não deve ser interpretado como `editor` em todas as organizações apenas porque o token contém o mesmo nome. O escopo deve fazer parte da associação ou da decisão.

## Separação de funções

Separação estática impede que uma pessoa receba papéis incompatíveis, como solicitante e aprovador financeiro. Separação dinâmica impede que os papéis sejam ativados simultaneamente na mesma sessão ou fluxo.

Essas restrições reduzem fraude e erro, mas exigem modelar o estado da sessão e registrar tentativas de atribuição. Um simples menu de papéis não demonstra que a restrição foi aplicada.

## Fluxo de decisão

Um fluxo RBAC normalmente começa com a autenticação do usuário. O serviço resolve seus grupos e atribuições, determina o tenant e a sessão ativa, encontra as permissões do papel e compara a ação e o recurso solicitados. O check precisa ocorrer no serviço que controla o recurso, depois de carregar o estado atual quando a regra depende de propriedade ou status.

Não coloque toda a autorização em um grupo do token. Tokens têm validade própria, podem ficar obsoletos e não conhecem necessariamente o estado atual do recurso. O backend deve tratar o token como uma entrada para resolver o principal, não como uma prova permanente de todas as permissões.

## Administração do ciclo de vida

O ciclo de vida inclui criação do papel, definição de permissões, atribuição, ativação, revisão, suspensão e remoção. Atribuições temporárias devem ter expiração. Papéis sem dono, sem descrição ou sem uso conhecido acumulam privilégio e devem ser encontrados por revisão periódica.

Uma matriz de acesso ajuda a comparar usuários, papéis e permissões, mas não deve ser a única fonte de verdade. Registre quem alterou a associação, qual justificativa foi fornecida e qual aprovação foi necessária.

## Variantes

Além do RBAC básico, considere:

- **hierarchical RBAC**, com herança entre papéis;
- **constrained RBAC**, com separação de funções e cardinalidade;
- **scoped RBAC**, com papel limitado a tenant, projeto ou recurso;
- **session-based RBAC**, com subconjunto de papéis ativados na sessão;
- **resource roles**, em que o papel é relativo a um objeto, como `editor` de um projeto específico.

Resource roles aproximam RBAC de ReBAC. O nome do modelo não importa tanto quanto documentar onde a associação vive e como ela é revogada.

## Vantagens

RBAC reduz a administração quando papéis refletem funções reais e relativamente estáveis. Ele facilita revisão, onboarding e remoção de acesso. Também combina bem com diretórios, grupos OIDC, LDAP e contas de serviço.

## Limitações

O problema clássico é role explosion. Quando cada combinação de projeto, cliente, recurso e condição vira um papel, o modelo fica difícil de administrar. RBAC também representa mal regras como "pode editar durante o expediente, a partir de uma rede aprovada, se o recurso pertencer ao seu departamento".

Essas regras podem ser complementadas por ABAC, PBAC ou ReBAC. Não crie papéis apenas para esconder atributos que deveriam estar explícitos na política.

## Sinais de role explosion

Se os papéis começam a incluir usuário, tenant, região, horário, estado do recurso e uma combinação de exceções, o modelo está carregando atributos demais. Extraia as dimensões para ABAC ou relações para ReBAC. Um papel deve representar uma responsabilidade compreensível e revisável, não uma linha gerada para cada caso.

## Aplicação segura

Use nomes de permissão estáveis, associe papéis a um escopo explícito, valide o tenant no servidor e defina default deny. O backend deve reavaliar autorização em cada operação sensível. Tokens com grupos ou papéis devem ter expiração, audiência e issuer validados.

Para clusters Kubernetes, veja [RBAC do Kubernetes](../../../kubernetes/access/rbac.md). Ele protege operações na API do Kubernetes, mas não substitui NetworkPolicy, capabilities, admission policies ou permissões do banco.

## Testes

Teste cada permissão com pelo menos um caso permitido, um caso negado, um papel semelhante, um tenant diferente, uma atribuição expirada e uma revogação recente. Teste também a ausência de papel e a impossibilidade de ativar papéis conflitantes. A cobertura precisa incluir endpoints, jobs e comandos administrativos.

## Fontes

- [NIST, RBAC project](https://csrc.nist.gov/projects/role-based-access-control)
- [NIST RBAC FAQs](https://csrc.nist.gov/Projects/Role-Based-Access-Control/faqs)
- [INCITS 359-2012, referência indicada pelo NIST](https://csrc.nist.gov/projects/role-based-access-control)
