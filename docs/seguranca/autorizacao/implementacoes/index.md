# Implementações de autorização

Esta categoria reúne implementações concretas de autorização. Uma
implementação pode ser uma biblioteca embutida na aplicação, um motor de
políticas, um PDP independente, um serviço de relações ou uma integração de
plataforma.

Essas soluções não ocupam o mesmo espaço. Uma biblioteca como CASL decide no
processo da aplicação. Um motor como Cedar ou OPA avalia políticas. OpenFGA e
SpiceDB armazenam relações e respondem consultas de autorização fina. O
servidor de identidade pode emitir credenciais sem ser o PDP da aplicação.

## Como comparar

Compare o modelo de dados, o local do PDP, a fonte dos atributos, a latência,
o comportamento diante de indisponibilidade, a consistência e o modo de
auditar decisões. Também é necessário saber se o sistema autoriza uma ação
sobre um objeto, uma linha, um campo ou apenas uma rota.

As páginas desta categoria explicam uma implementação. Os conceitos de
subject, resource, action, policy, PDP e PEP estão em [Conceitos de
autorização](../conceitos/index.md). Os modelos ACL, RBAC, ABAC, PBAC e ReBAC
continuam em [Modelos de autorização](../modelos/index.md).
