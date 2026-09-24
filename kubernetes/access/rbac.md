# RBAC Kubernetes

Role-Based Access Control, RBAC, é o mecanismo pelo qual o Kubernetes decide se
uma identidade pode executar uma ação sobre um recurso. A decisão combina o
sujeito, o verbo, o grupo de API, o recurso, o nome opcional e o escopo do
objeto.

RBAC protege a API do Kubernetes. Ele não substitui NetworkPolicy, Security
Context, admission control ou controles de um sistema operacional.

## Objetos e escopo

Uma Role declara permissões restritas a um Namespace. Uma ClusterRole declara
permissões que podem abranger o cluster ou recursos sem Namespace. Nenhuma das
duas concede acesso sozinha: elas são definições nomeadas.

Uma RoleBinding atribui uma Role a sujeitos dentro de um Namespace. Ela também
pode referenciar uma ClusterRole e aplicar esse conjunto de regras somente ao
Namespace da binding. Uma ClusterRoleBinding atribui uma ClusterRole em escopo
de cluster inteiro. Essa distinção define o raio de dano de uma identidade.

| Elemento | Responsabilidade |
| --- | --- |
| Role | Define regras em um Namespace |
| ClusterRole | Define regras reutilizáveis ou cluster-scoped |
| RoleBinding | Atribui permissões dentro de um Namespace |
| ClusterRoleBinding | Atribui permissões em todo o cluster |

## Regras e menor privilégio

Uma regra enumera verbos como `get`, `list`, `watch`, `create` e `delete`,
grupos de API, recursos e, quando necessário, nomes de objetos. RBAC é
aditivo. Uma regra ampla não é reduzida por uma regra posterior de deny.

Prefira sujeitos, recursos, verbos e Namespaces específicos. O uso de
`*` em grupos, recursos ou verbos deve ser tratado como uma exceção de alto
risco, porque a alteração futura da API pode ampliar a permissão sem que a
binding seja modificada. Separar ServiceAccounts por responsabilidade também
mantém controllers diferentes fora do mesmo blast radius.

## ServiceAccounts

Um Pod usa uma ServiceAccount como identidade perante a API. Quando nenhuma é
declarada, usa a conta default do Namespace, o que torna fácil conceder
permissão acidentalmente a workloads que não deveriam ter acesso.

Um controller que precisa observar Pods em vários Namespaces precisa de uma
binding compatível com esse escopo. Sem ela, a API retorna Forbidden. Esse
sintoma é diferente de falha de DNS, rede ou descoberta de Service.

## Verificação e diagnóstico

Aplicar manifestos sem erro de sintaxe não prova que a identidade recebeu a
permissão esperada. Um sujeito incorreto, um verbo ausente ou uma binding no
Namespace errado podem produzir o comportamento de ausência de acesso.

Use `kubectl auth can-i --list --as <identidade>` para consultar as permissões
efetivas do sujeito e uma pergunta específica para confirmar a operação. Em
uma investigação, confirme a ServiceAccount do Pod, as bindings visíveis no
Namespace e o escopo do recurso consultado.

Não diagnostique um Forbidden apenas aumentando permissões. Primeiro compare a
ação pedida com a regra mínima que deveria atendê-la.

## Relações

- [ServiceAccount](../core/serviceaccount.md) fornece a identidade do workload.
- [Namespace](../core/namespace.md) define um dos escopos administrativos.
- [API server](../control-plane/api-server.md) executa autenticação e
  autorização.
- [NetworkPolicy](../networking/network-policy.md) controla tráfego, não
  autorização da API.
- [Admission control](../extensibility/admission-control.md) pode impor
  regras adicionais antes da persistência.

## Fonte primária

- [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
