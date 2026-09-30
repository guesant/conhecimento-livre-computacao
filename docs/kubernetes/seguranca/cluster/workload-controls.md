# Controles de segurança de workloads

Um Pod deve ser analisado como um processo que pode falhar ou ser
comprometido. O objetivo não é confiar que a imagem permanecerá correta, mas
reduzir o que o processo pode fazer, quanto recurso pode consumir, quais redes
pode alcançar e quais credenciais recebe.

## ResourceQuota

`ResourceQuota` limita consumo agregado em um Namespace. Pode restringir
quantidade de Pods, Services, Jobs, PVCs, Secrets e ConfigMaps, além de
requests e limits de CPU, memória e storage. Ele protege o cluster contra
consumo acidental ou abusivo, mas também pode impedir um rollout legítimo se a
quota não considerar o pico temporário de réplicas.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: workload-budget
  namespace: application
spec:
  hard:
    requests.cpu: "2"
    requests.memory: 4Gi
    limits.cpu: "4"
    limits.memory: 8Gi
    pods: "40"
    services.loadbalancers: "0"
    services.nodeports: "0"
    persistentvolumeclaims: "20"
```

A quota de `services.nodeports` ou `services.loadbalancers` é útil quando a
exposição externa deve ser criada somente por uma camada de entrada. A quota
não substitui autorização: quem tem permissão para editar a quota pode
alterar o limite e quem pode criar recursos com uma ServiceAccount privilegiada
pode continuar criando objetos dentro do limite.

## LimitRange

`LimitRange` define mínimos, máximos e defaults para containers e recursos do
Namespace. Ele evita Pods sem limites em um ambiente que exige previsibilidade
e rejeita solicitações fora do intervalo permitido.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: container-defaults
  namespace: application
spec:
  limits:
    - type: Container
      min:
        cpu: 10m
        memory: 16Mi
      max:
        cpu: "2"
        memory: 2Gi
      default:
        cpu: 500m
        memory: 512Mi
      defaultRequest:
        cpu: 100m
        memory: 128Mi
```

Defaults são uma política de plataforma, não uma medição da aplicação. Devem
ser definidos com base em observação e revisados quando o perfil do workload
mudar. Um default de memória muito baixo causa OOM e um default alto pode
reduzir a capacidade de scheduling de todos os Pods.

## SecurityContext

`SecurityContext` reúne controles do processo e do container. O Pod pode
declarar identidade, grupo, `fsGroup`, `seccomp`, capacidades, acesso ao
filesystem e comportamento de privilege escalation. O container pode
restringir ainda mais esses valores, mas não deve ampliar uma política que o
nível do Pod já proibiu.

Uma base razoável para um container que não precisa de privilégios é:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL
  seccompProfile:
    type: RuntimeDefault
```

O exemplo não é universal. Processos que escrevem em diretórios temporários
precisam de um `emptyDir` ou outro volume para manter o root filesystem
somente leitura. Aplicações que exigem uma capability específica devem receber
somente aquela capability, e não usar `privileged: true` como atalho.

`hostNetwork`, `hostPID`, `hostIPC`, `hostPath`, portas do host e containers
privilegiados conectam o workload a recursos do nó. Cada uso precisa de uma
justificativa operacional, escopo mínimo e revisão de quem pode criar o Pod.
Um Pod que pode criar outro Pod não deve ser avaliado somente pelos campos do
seu próprio SecurityContext, pois ele pode produzir um workload diferente.

## ServiceAccounts e tokens

Cada workload deve ter uma ServiceAccount própria quando precisa acessar a
API. Evite usar a conta `default` com permissões ampliadas. Quando a aplicação
não consulta a API, prefira não montar o token:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: frontend
  namespace: application
automountServiceAccountToken: false
```

Também é possível definir `automountServiceAccountToken: false` no Pod e
permitir explicitamente somente onde necessário. Tokens projetados e de curta
duração são preferíveis a cópias estáticas persistidas em imagens, ConfigMaps
ou arquivos de configuração.

## Pod Security Standards e Admission

Pod Security Standards define perfis `Privileged`, `Baseline` e `Restricted`.
O primeiro deixa o Namespace aberto para casos de infraestrutura. `Baseline`
remove classes comuns de escalada, enquanto `Restricted` exige uma postura
mais forte, como non-root, seccomp e ausência de privilégios desnecessários.

Pod Security Admission aplica esses perfis por labels de Namespace. Os modos
`enforce`, `audit` e `warn` têm efeitos diferentes: o primeiro rejeita, o
segundo registra e o terceiro informa o usuário. Uma migração segura começa
com audit e warn, corrige os workloads e depois promove o perfil para enforce.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: application
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/audit-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: latest
```

Namespaces do control plane, CNI, storage e observabilidade podem precisar de
exceções. A exceção deve ser restrita ao componente, e não usada para manter
qualquer workload arbitrário no Namespace privilegiado.

## Relações e verificação

Quotas e LimitRange tratam consumo. SecurityContext e Pod Security tratam
privilégios. NetworkPolicy trata tráfego. RBAC trata acesso à API. Essas
camadas se complementam e nenhuma substitui as outras.

Verifique a política efetiva criando um Pod de teste não privilegiado,
consultando eventos de admission e observando as decisões de quota. Teste
também rollouts, Jobs, init containers, ephemeral containers e operações de
debug, porque eles podem possuir regras de segurança diferentes do caminho
principal da aplicação.

## Fontes primárias

- [Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/)
- [Configure a SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
