# Modelos de autorização

Não existe uma lista única e fechada de tipos de autorização. Alguns nomes descrevem um modelo formal de decisão, outros descrevem a estrutura em que as permissões são armazenadas e outros descrevem uma estratégia de administração. Uma ACL, por exemplo, é uma forma de associar permissões a um objeto; ABAC é um modelo que decide com base em atributos.

A classificação desta seção separa esses níveis para evitar comparações enganosas. Os modelos podem ser combinados. Um sistema pode usar RBAC para permissões gerais, ABAC para tenant e horário, ReBAC para compartilhamento e uma regra de risco para exigir MFA.

## Mapa dos modelos

| Modelo | Pergunta principal | Unidade de decisão | Exemplo típico |
| --- | --- | --- | --- |
| ACL | Quais sujeitos estão listados neste objeto? | Entrada sujeito, ação | Permissão em arquivo |
| DAC | O proprietário pode delegar o acesso? | Identidade e propriedade | Unix, POSIX ACL |
| MAC | A política central permite este fluxo? | Rótulos e política global | SELinux, MLS |
| RBAC | Qual papel ativo possui esta permissão? | Usuário, papel, permissão | Administrador, editor |
| ABAC | Os atributos satisfazem a política? | Principal, recurso e contexto | Departamento e classificação |
| ReBAC | Existe uma relação autorizadora? | Grafo de entidades | Membro de organização |
| Capability-based | O solicitante possui o token de autoridade? | Capability | Handle com direitos limitados |
| PBAC | Qual política declarativa se aplica? | Regra e efeito | `permit` condicionado |
| UCON | A autorização continua válida durante o uso? | Estado, obrigação e condição | Licença, sessão e consumo |
| RAdAC | O risco atual está dentro do limite? | Risco e contexto | Exigir MFA em rede desconhecida |

## Famílias clássicas

DAC, MAC e RBAC são modelos clássicos de controle de acesso. DAC dá ao proprietário uma capacidade de decisão. MAC usa uma política que não pode ser alterada livremente pelo usuário. RBAC introduz papéis entre identidades e permissões. Eles não são sinônimos de autenticação e podem coexistir em diferentes camadas do mesmo sistema.

ACLs e listas de capabilities são estruturas de autorização. A ACL fica associada ao objeto; a capability fica com o sujeito ou com o processo que recebeu uma autoridade. Essa inversão muda a forma de revogar, delegar e auditar.

## Famílias orientadas a política

ABAC avalia atributos de sujeitos, recursos, ações e ambiente. PBAC é uma formulação mais ampla em que políticas declarativas determinam a decisão. Uma implementação PBAC pode usar ABAC, RBAC, relações, listas ou uma combinação deles.

Cedar é um exemplo de linguagem de políticas. Casbin implementa diversos modelos por meio de um arquivo de modelo e um conjunto de regras. Essas ferramentas não são modelos adicionais independentes; são mecanismos capazes de expressar alguns modelos.

## Relação, estado e risco

ReBAC representa relações persistentes entre entidades e é adequado para colaboração e multi-tenancy. UCON considera que uma autorização pode depender de obrigações, condições e mudanças durante o uso do recurso. RAdAC incorpora uma avaliação de risco que pode alterar a decisão ou exigir uma etapa adicional de autenticação.

Modelos históricos, como Chinese Wall e separação dinâmica de funções, também são relevantes quando a autorização depende do que já foi acessado ou executado. Eles não devem ser reduzidos a um papel estático.

## Como escolher

Comece pelo tipo de regra, não pelo produto:

1. Se o objeto tem uma lista pequena e estável, uma ACL pode ser suficiente.
2. Se o proprietário deve conceder acesso, DAC representa essa autoridade.
3. Se uma política central deve impedir que usuários deleguem privilégios, MAC é mais apropriado.
4. Se a organização possui funções estáveis, RBAC reduz a administração direta de usuários.
5. Se a decisão depende de contexto, ABAC ou PBAC expressa a regra com mais precisão.
6. Se o acesso atravessa grupos, organizações e hierarquias, ReBAC evita uma explosão de papéis.
7. Se a autoridade precisa ser delegada como um objeto, capabilities podem ser mais naturais.
8. Se o direito muda durante o uso ou depende de consumo, UCON é a família relevante.
9. Se o risco muda de acordo com contexto e sinais, RAdAC pode complementar o modelo escolhido.

## Segurança comum a todos os modelos

Qualquer modelo precisa de default deny, normalização de identidades, escopo de tenant, revogação, auditoria e testes negativos. O nome do modelo não garante least privilege. Um RBAC com um papel global de superadministrador pode ser mais perigoso que uma ABAC bem limitada.

A decisão deve ocorrer no backend ou no sistema que controla o recurso. O frontend pode apresentar uma projeção de capabilities, mas não é uma fronteira de confiança. A política também deve ser aplicada a jobs, comandos, integrações e endpoints internos.

## Modelos especializados

Os modelos especializados possuem páginas próprias em [modelos especializados](especializados/index.md). Eles podem ser usados como restrições dentro de RBAC, ABAC ou PBAC. O modelo selecionado deve refletir o requisito de segurança, não apenas o vocabulário usado pelo produto.

## Verificação

Políticas precisam ser verificadas quanto a negação indevida, permissões excessivas, conflitos e casos não cobertos. Teste também a revogação e o comportamento quando um atributo, um diretório, um serviço de relações ou o PDP está indisponível.

Veja [autorização](../index.md), [comparativo das bibliotecas e serviços](../comparativo.md), [NIST ABAC](https://csrc.nist.gov/projects/attribute-based-access-control), [NIST RBAC](https://csrc.nist.gov/projects/role-based-access-control) e [NIST SP 800-192 sobre verificação de políticas](https://csrc.nist.gov/pubs/sp/800/192/final).
