# Namespace do Kubernetes

Um Namespace do Kubernetes é uma fronteira de nomeação e de escopo dentro de um único cluster, não uma fronteira de isolamento de processo. Dois objetos do mesmo tipo podem ter o mesmo nome se viverem em Namespaces diferentes, e a maior parte dos controles que dependem de "a que grupo este objeto pertence" (uma política de RBAC, uma política de rede, uma cota de recursos) se declara por Namespace. Alguns recursos não pertencem a nenhum Namespace, como um nó ou uma definição de tipo customizado, porque fazem sentido para o cluster inteiro, não para uma fatia dele.

Isso não tem relação com o namespace do kernel Linux, coberto em [Processo, namespaces e usuários num container](processo-namespaces-e-usuarios.md); os dois compartilham o nome porque resolvem o mesmo problema geral, separar o que um grupo de coisas enxerga do que outro grupo enxerga, mas operam em camadas diferentes. Um Namespace do Kubernetes é um objeto da API, guardado no etcd; um namespace do kernel é um mecanismo do sistema operacional que isola o que um processo consegue ver. Um Pod dentro de um Namespace do Kubernetes chamado `producao` roda, por baixo, com vários namespaces de kernel próprios (PID, rede, montagem), e as duas palavras coincidem por acidente histórico, não porque uma implemente a outra.

## Continue por aqui

[RBAC do Kubernetes](rbac-do-kubernetes.md) cobre como uma política de acesso se escopa a um Namespace específico ou ao cluster inteiro; [Processo, namespaces e usuários num container](processo-namespaces-e-usuarios.md) cobre o mecanismo de isolamento do kernel que empresta o nome.
