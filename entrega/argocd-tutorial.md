# Tutorial de Argo CD

Argo CD é um reconciler GitOps para Kubernetes. Ele observa uma fonte declarativa, renderiza os manifestos e converge o cluster para a revisão selecionada. GitOps define o fluxo e a fonte de verdade; Argo CD implementa esse ciclo de observação, comparação, aplicação e health check.

Este tutorial apresenta uma instalação básica, uma `Application`, políticas de projeto, automação de sincronização e padrões de composição.

## Pré-requisitos

Você precisa de um cluster Kubernetes, um repositório acessível pelo Argo CD e uma configuração renderizável por YAML puro, Helm, Kustomize ou plugin. O repositório deve permitir que uma revisão seja identificada por branch, tag ou commit.

Instale uma versão fixada do manifesto oficial. Não copie uma URL mutável para um processo de produção sem revisar a versão:

```bash
kubectl create namespace argocd
kubectl apply --server-side -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.14.0/manifests/install.yaml
kubectl get pods -n argocd
```

O `--server-side` ajuda com CRDs grandes e reduz problemas de tamanho no `last-applied-configuration`. Antes de atualizar a versão, leia as notas de compatibilidade e faça backup dos manifests e dados necessários ao ambiente.

## Acesso inicial

Para um acesso local temporário, use port-forward:

```bash
kubectl -n argocd port-forward svc/argocd-server 8080:443
argocd login localhost:8080 --insecure
```

O `--insecure` neste exemplo corresponde ao túnel local e não deve ser usado como justificativa para remover TLS na exposição externa. Em um ambiente compartilhado, publique o servidor por um endpoint protegido, com autenticação, certificado e política de rede.

Valide a instalação antes de registrar aplicações:

```bash
kubectl get deployments -n argocd
argocd version
argocd cluster list
```

## Application

Uma `Application` associa uma fonte, um caminho, uma revisão e um destino:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: catalog
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/catalog-gitops.git
    targetRevision: main
    path: stages/dev
  destination:
    server: https://kubernetes.default.svc
    namespace: catalog
  syncPolicy:
    syncOptions:
      - CreateNamespace=true
```

O campo `path` é interpretado de acordo com a fonte. Em um repositório Helm, ele aponta para o chart e recebe `helm.values` ou `helm.parameters`. Em Kustomize, aponta para a pasta da composição. Para YAML puro, aponta para a pasta de manifestos.

A aplicação deve ter um projeto explícito, mesmo que comece no `default`. Um `AppProject` restringe a origem, o destino e os recursos que podem ser criados.

## Fontes de configuração

Os formatos mais usados são:

| Fonte | Quando usar |
| --- | --- |
| YAML puro | Recursos pequenos e composição simples |
| Kustomize | Bases e overlays por ambiente |
| Helm | Charts parametrizados e distribuição de pacotes |
| Plugin | Renderização que exige uma ferramenta adicional |
| Múltiplas fontes | Separar chart, values e repositórios relacionados |

O formato não deve ser escolhido apenas pela quantidade de YAML. Kustomize expõe a diferença entre base e overlay; Helm expõe parâmetros e templates; um plugin amplia a capacidade, mas cria uma superfície operacional adicional.

## Sincronização manual

A sincronização manual mantém aprovação humana no momento do apply:

```bash
argocd app create catalog \
  --repo https://github.com/example/catalog-gitops.git \
  --revision main \
  --path stages/dev \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace catalog
argocd app get catalog
argocd app diff catalog
argocd app sync catalog
argocd app wait catalog --health
```

Use a revisão que foi revisada e aprovada. O comando `sync` renderiza e aplica o estado desejado; `wait` verifica a conclusão, mas a saúde final ainda depende das probes e dos recursos da aplicação.

## Sincronização automática

Automação pode sincronizar quando uma nova revisão for detectada:

```yaml
spec:
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
```

`prune` permite remover recursos que deixaram de existir na fonte. `selfHeal` reconcilia drift causado por alterações manuais. `allowEmpty: false` impede que uma revisão que renderiza zero recursos remova uma aplicação inteira por engano.

Uma aplicação automática não deve ser habilitada apenas porque o apply manual é trabalhoso. Primeiro estabeleça revisão protegida, validação no CI, permissões do projeto, estratégia de rollback e observabilidade. Rollback de uma aplicação com sync automático exige uma revisão revertida no Git ou uma forma explícita de suspender a automação; voltar a uma revisão antiga no servidor sem corrigir a fonte pode ser desfeito pelo próximo ciclo.

## AppProject

Um `AppProject` limita o raio de ação de uma aplicação:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: catalog
  namespace: argocd
spec:
  sourceRepos:
    - https://github.com/example/catalog-gitops.git
  destinations:
    - namespace: catalog
      server: https://kubernetes.default.svc
  namespaceResourceWhitelist:
    - group: ""
      kind: ConfigMap
    - group: ""
      kind: Secret
    - group: apps
      kind: Deployment
    - group: ""
      kind: Service
```

Comece com uma allowlist pequena e adicione recursos somente quando o workload precisar. Restrinja repositórios e destinos separadamente. Permitir qualquer namespace ou qualquer cluster transforma o projeto em uma credencial ampla de administração.

## App of apps

O padrão app of apps usa uma `Application` raiz para gerenciar outras `Application`s. A raiz aponta para uma pasta de aplicações filhas:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/platform-gitops.git
    targetRevision: main
    path: applications
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Esse padrão é simples e auditável, mas a raiz tem alto impacto. Um erro no diretório de aplicações pode criar, alterar ou remover muitos workloads. Use AppProjects, revisão obrigatória e cuidado com `prune`.

## ApplicationSet

`ApplicationSet` gera Applications a partir de uma lista, diretórios, clusters ou outras fontes. É útil quando a mesma composição precisa ser aplicada a vários ambientes:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: catalog
  namespace: argocd
spec:
  generators:
    - list:
        elements:
          - environment: dev
            namespace: catalog-dev
          - environment: prod
            namespace: catalog-prod
  template:
    metadata:
      name: catalog-{{environment}}
    spec:
      project: catalog
      source:
        repoURL: https://github.com/example/catalog-gitops.git
        targetRevision: main
        path: stages/{{environment}}
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{namespace}}'
```

O gerador deve produzir nomes, destinos e caminhos determinísticos. Antes de habilitar remoção automática, verifique o que acontece quando um elemento some da lista.

## Múltiplas fontes

Múltiplas fontes permitem combinar um chart e valores mantidos em outro local. Use esse recurso quando a separação tiver uma responsabilidade clara. Ele não deve ser uma forma de esconder a origem real do manifesto.

```yaml
spec:
  sources:
    - repoURL: https://charts.example.test
      chart: catalog
      targetRevision: 1.4.0
      helm:
        valueFiles:
          - $values/stages/prod/values.yaml
    - repoURL: https://github.com/example/catalog-gitops.git
      targetRevision: main
      ref: values
```

Revise colisões de nomes e a precedência quando fontes diferentes renderizam o mesmo recurso. A simplicidade do fluxo de revisão é mais importante que reduzir o número de repositórios a qualquer custo.

## Segredos

Argo CD não deve receber segredos em texto claro no Git. Use um mecanismo de secret externo, um plugin controlado ou um fluxo de decifragem como SOPS com ksops quando essa decisão fizer parte da arquitetura. A chave de decifragem precisa estar disponível somente no componente que renderiza o manifesto e não deve ser gravada no repositório.

O segredo de acesso ao repositório também deve ter escopo mínimo. Separe credenciais de leitura de repositórios de credenciais que promovem alterações. Revise logs de renderização para confirmar que valores secretos não aparecem no output.

## Sync, health e drift

`Synced` significa que a revisão renderizada coincide com o estado desejado. `Healthy` significa que os recursos passaram pelas verificações de saúde definidas pelo Argo CD e pelo Kubernetes. Uma aplicação pode estar sincronizada e não saudável.

```bash
argocd app get catalog
argocd app resources catalog
argocd app diff catalog
argocd app history catalog
argocd app logs catalog
```

Se alguém alterar o cluster manualmente, `selfHeal` pode restaurar o valor do Git. Durante um incidente, suspenda a automação de forma explícita se a correção temporária precisar permanecer até que o commit seja preparado. A correção duradoura deve voltar para a fonte declarativa.

## Diagnóstico por camadas

Quando uma aplicação falhar, siga a sequência:

1. O repositório está acessível e a revisão existe?
2. O caminho e o formato renderizam localmente?
3. O AppProject permite fonte, destino e recursos?
4. O Argo CD consegue aplicar os objetos?
5. O Kubernetes criou os recursos e as dependências?
6. As probes e health checks indicam que o serviço está pronto?

Comandos adicionais:

```bash
argocd app manifests catalog
argocd app sync catalog --dry-run
kubectl get events -n catalog --sort-by=.lastTimestamp
kubectl describe deployment catalog -n catalog
kubectl logs deployment/catalog -n catalog
```

Erro de renderização deve ser corrigido na fonte ou no plugin. Erro de permissão pode estar no AppProject, no ServiceAccount ou no RBAC do destino. Erro de health precisa ser investigado no workload, não resolvido removendo a verificação.

## Atualização e recuperação

Antes de atualizar Argo CD, leia a matriz de compatibilidade e faça backup dos manifestos, configurações de acesso e objetos necessários ao bootstrap. Atualize em uma janela que permita observar controllers, repo-server, API server e aplicações.

Se o Argo CD parar de reconciliar, o cluster continua com o último estado aplicado, mas não receberá novas alterações nem necessariamente corrigirá drift. Preserve os repositórios e reconstrua a instalação pela versão documentada. Uma aplicação raiz e os AppProjects devem ser suficientes para recriar o grafo quando a instalação estiver saudável novamente.

## Segurança operacional

Use RBAC para separar leitura, sincronização e administração. Restrinja repositórios, destinos e tipos de recursos. Proteja o endpoint do Argo CD, fixe versões de imagens, monitore falhas de sincronização e evite permitir plugins arbitrários no repo-server.

O repositório GitOps precisa de revisão, proteção de branch e validação de manifestos. Argo CD aumenta a velocidade da convergência, mas não substitui testes, aprovação, backup ou gestão de mudanças.

## Relações

- [GitOps](gitops.md) explica o modelo de operação.
- [Application](application.md) detalha o recurso principal.
- [AppProject](appproject.md) detalha as políticas de escopo.
- [ApplicationSet](applicationset.md) explica geração de aplicações.
- [App of apps](app-of-apps.md) explica o bootstrap declarativo.
- [Sync, prune e self-heal](sync-prune-self-heal.md) detalha as opções de reconciliação.
- [Kargo](kargo.md) promove revisões antes de o Argo CD aplicá-las.

## Fontes primárias

- [Getting started](https://argo-cd.readthedocs.io/en/latest/getting_started/)
- [Automated sync policy](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- [Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/)
- [Cluster bootstrapping](https://argo-cd.readthedocs.io/en/stable/operator-manual/cluster-bootstrapping/)
- [Application specification](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/)
