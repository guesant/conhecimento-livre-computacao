# Acesso seguro ao API server

O API server é a fronteira comum entre usuários, automações, componentes do
control plane e workloads que usam a API. Proteger essa fronteira exige
separar quatro perguntas: como o tráfego é protegido, como a identidade é
reconhecida, quais ações ela pode executar e quais objetos podem ser
rejeitados ou mutados antes de serem persistidos.

## TLS e transporte

O tráfego da API deve usar TLS com certificados e autoridades confiáveis. Isso
protege credenciais e objetos contra observação e alteração no caminho, mas
não decide se o cliente deveria poder executar uma ação. A validação do
certificado precisa cobrir a autoridade correta, os nomes do endpoint e a
rotação planejada.

Portas HTTP locais ou modos de compatibilidade sem autenticação não devem ser
tratados como uma alternativa segura apenas porque escutam em loopback. Um
processo comprometido no nó pode acessar loopback. Se uma porta não for
necessária, a opção segura é desabilitá-la e verificar com uma varredura local
que ela não está disponível.

TLS também aparece em outras conexões do cluster. O API server conversa com
Kubelets, etcd, webhooks e serviços auxiliares. Cada conexão precisa ter
confiança e identidade próprias. Reutilizar um certificado de cliente entre
componentes torna a investigação e a revogação mais difíceis e aumenta o raio
de dano.

## Autenticação

Autenticação responde quem está fazendo a requisição. Todas as chamadas
administrativas precisam ter uma identidade, inclusive chamadas produzidas
por componentes internos. Entre os mecanismos comuns estão certificados de
cliente, tokens de ServiceAccount, OIDC, autenticação integrada a um provedor
externo e, em ambientes menores, tokens estáticos. A escolha depende do
modelo de operação, mas tokens estáticos long-lived são difíceis de revogar e
auditar e não devem ser a solução padrão para um grupo grande de usuários.

Uma chamada autenticada não recebe permissão automaticamente. O nome de um
usuário OIDC, o subject de um certificado ou a ServiceAccount de um Pod só
ganham significado administrativo quando estão vinculados a regras de
autorização. A identidade usada por uma automação deve ser específica para a
automação, e não uma conta humana compartilhada.

Para revisar a autenticação, registre:

- quem emite cada certificado, token ou assertion;
- onde a credencial é armazenada e como é rotacionada;
- como um usuário ou componente é revogado;
- qual relógio e qual validade são exigidos;
- qual identidade aparece no audit log;
- se o mecanismo continua funcionando durante a indisponibilidade do IdP.

## Autorização

Autorização responde se a identidade pode executar a ação solicitada. RBAC
combina sujeito, grupo, verbo, grupo de API, recurso, nome opcional e escopo.
Uma `Role` é limitada a um Namespace. Uma `ClusterRole` pode ser usada para
recursos de cluster ou vinculada a um Namespace por uma `RoleBinding`. Uma
`ClusterRoleBinding` concede acesso no escopo de todo o cluster e por isso
deve ser tratada como uma mudança de alto impacto.

O modelo é aditivo. Não existe um deny posterior que reduza uma permissão
concedida por outra regra. Por isso, a revisão precisa procurar permissões
redundantes, `*` em verbos ou recursos, leitura de todos os Secrets, criação
de Pods e acesso a subrecursos como `exec`, `attach` e `portforward`.

O [RBAC do Kubernetes](../../access/rbac.md) explica os objetos básicos. Uma
revisão de segurança precisa ir além de `kubectl auth can-i`: deve avaliar o
que a permissão permite criar indiretamente. Quem pode criar um Deployment
pode criar um Pod. Quem pode criar um Pod pode tentar usar uma ServiceAccount
mais privilegiada, montar um volume do host ou acessar um endpoint de nó se
outras políticas permitirem. Quem pode apagar um Node pode provocar a
recriação ou o reagendamento de workloads, alterando disponibilidade e
topologia.

## Node authorizer e NodeRestriction

Kubelets precisam consultar informações dos Pods atribuídos ao seu nó, mas não
devem poder agir como administradores do cluster. O Node authorizer limita o
acesso da identidade de um nó aos objetos necessários para a operação. O
admission plugin NodeRestriction impede que uma identidade de kubelet altere
atributos que poderiam influenciar o scheduling ou se apresentar como outro
nó.

Usar apenas o nome de uma identidade de nó sem a restrição de admission não
produz a mesma fronteira. A configuração deve ser revisada em conjunto: modo
de autorização, grupos de identidade, certificado do kubelet e plugins de
admission realmente habilitados.

## Admission depois da autorização

Depois de autenticar e autorizar, o API server pode enviar o objeto para
admission. Mutating admission pode adicionar defaults ou injeções. Validating
admission pode rejeitar o objeto. A sequência significa que uma requisição
autorizada ainda pode falhar por uma policy de segurança, schema, quota ou
webhook indisponível.

Admission não corrige RBAC. Um webhook pode impedir uma combinação perigosa,
mas não deve ser usado como desculpa para conceder permissão ampla a uma
identidade. O webhook também vira uma dependência do caminho de escrita. Seu
escopo, timeout, `failurePolicy`, certificado e disponibilidade precisam ser
compatíveis com o impacto de bloquear o control plane.

## DRA e subrecursos sintéticos

O Dynamic Resource Allocation introduz relações de autorização que não são
óbvias quando se olha somente para o recurso principal. Por exemplo,
permissões sobre `resourceclaims/binding` e `resourceclaims/driver` podem
alterar a associação de recursos. Toda nova API deve ser revisada pelos
subrecursos e verbos específicos, não apenas pelo nome do recurso pai.

## Diagnóstico mínimo

```bash
kubectl auth can-i --list --as=system:serviceaccount:namespace:account
kubectl auth can-i get secrets -n namespace \
  --as=system:serviceaccount:namespace:account
kubectl get clusterrolebindings -o wide
kubectl get rolebindings --all-namespaces -o wide
```

Esses comandos ajudam a verificar a permissão efetiva, mas não substituem a
revisão da capacidade de criar recursos e da cadeia de admission. O resultado
deve ser comparado ao acesso necessário para o caso de uso, e não usado para
conceder uma ClusterRole genérica até o erro desaparecer.

## Fontes primárias

- [Authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
- [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Node authorization](https://kubernetes.io/docs/reference/access-authn-authz/node/)
- [Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
