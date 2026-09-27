# Integrações de terceiros

Controllers, operators, admission webhooks, drivers de storage, plugins de
rede, agentes de observabilidade e componentes de CI ampliam o cluster com
código que não faz parte do núcleo do Kubernetes. Eles precisam de permissões
para cumprir sua função, mas uma permissão ampla pode equivaler a acesso de
administrador mesmo quando o nome do componente parece limitado.

## Ler Secrets é uma fronteira administrativa

Um componente que pode ler todos os Secrets de todos os Namespaces pode
obter credenciais de banco, tokens de cloud, chaves de assinatura e
identidades de outros workloads. O acesso deve ser restringido a Namespaces,
tipos e nomes necessários. Não conceda `get`, `list` ou `watch` de Secrets a
um controller apenas porque ele também observa Pods.

List e watch merecem atenção especial: mesmo sem conhecer o nome de um
objeto, eles podem revelar muitos valores. Se o componente só precisa de um
Secret conhecido, use uma permissão nominal quando a operação e o cliente
suportarem esse escopo.

## Criar Pods é uma permissão de alto impacto

Quem cria Pods pode escolher uma ServiceAccount, volumes, host namespaces,
capabilities, imagem e node placement. Mesmo que o componente não tenha uma
permissão explícita para ler um Secret, ele pode criar um Pod que use uma
ServiceAccount autorizada ou que tente alcançar o host. A revisão de RBAC
deve considerar essa capacidade indireta.

O mesmo cuidado vale para Deployment, Job, CronJob, DaemonSet, ReplicaSet,
PodTemplate, ephemeral containers e subrecursos de execução. Não é suficiente
negar `get secrets` se a identidade pode criar um workload privilegiado.

## Escopo de Namespaces

Instale componentes de terceiros em um Namespace dedicado, com uma
ServiceAccount própria, quotas, NetworkPolicies e Pod Security compatíveis.
Limite a leitura e a escrita ao conjunto necessário. Evite dar a um operator
acesso a `kube-system`, Namespaces de infraestrutura e objetos de outro
produto apenas para simplificar a instalação.

Namespaces usados pelo control plane ou pelo CNI podem precisar de
privilégios. Isso deve ser uma exceção explícita, associada à versão do
componente e à necessidade documentada. Não use o Namespace privilegiado como
destino para workloads de aplicação porque a policy de segurança já está
relaxada.

## Webhooks e availability

Admission webhooks podem bloquear o caminho de criação e atualização. Revise
CA bundle, certificado, DNS, timeout, `failurePolicy`, regras de escopo e
versão de API. Um webhook que valida somente um Namespace de aplicação não
deve interceptar `kube-system` por acidente.

Uma falha de segurança e uma falha de disponibilidade podem exigir respostas
diferentes. Para uma policy que impede privilégio, aceitar a falha pode
permitir um objeto perigoso. Para uma integração informativa, rejeitar toda a
API durante uma indisponibilidade pode ser desproporcional. A decisão precisa
ser testada durante rollout, upgrade e perda do backend.

## Supply chain

Use imagens pinadas por digest quando o processo permitir, valide origem e
assinatura, mantenha SBOM e acompanhe vulnerabilidades do controller. Revise
as permissões pedidas pelo chart ou manifesto antes de instalar. Um chart pode
criar ClusterRole, webhook, ServiceAccount privilegiada e acesso a Secrets
mesmo que o componente principal pareça uma simples aplicação.

Não confie somente no namespace ou no nome da imagem. Confira o conteúdo do
manifesto renderizado, a origem do registry, o processo de atualização e o
usuário que pode alterar os valores.

## Processo de revisão

Para cada integração, documente:

- recursos lidos e escritos;
- Namespaces alcançados;
- verbos e subrecursos;
- capacidade de criar Pods ou alterar admission;
- ServiceAccount e credenciais externas;
- portas e destinos de rede;
- volumes e acesso ao host;
- processo de atualização e rollback;
- logs, métricas e evidência de ações.

Revalide a matriz quando o componente mudar de versão. Permissões que eram
necessárias para uma implementação antiga podem se tornar obsoletas ou
perigosas depois de uma mudança de arquitetura.

## Fontes primárias

- [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [Admission webhooks good practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
- [Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
