# Tutorial de Kargo

Kargo é uma camada de promoção para ambientes GitOps. Ele acompanha artefatos, associa revisões a evidências de entrega e promove uma revisão entre estágios. O reconciler, como Argo CD ou Flux, continua responsável por aplicar a configuração no cluster.

Este tutorial apresenta um fluxo completo com um repositório de imagens, um repositório GitOps e três ambientes chamados `test`, `uat` e `prod`.

## O modelo mental

Kargo organiza a promoção em objetos com responsabilidades diferentes:

| Objeto | Responsabilidade |
| --- | --- |
| `Project` | Isola recursos, credenciais, permissões e histórico de uma equipe ou produto |
| `Warehouse` | Descobre imagens ou commits que podem gerar novas revisões |
| `Freight` | Representa uma combinação concreta de artefatos candidata à promoção |
| `Stage` | Representa um ambiente e suas regras de entrada e saída |
| `Promotion` | Registra a tentativa de mover um Freight para um Stage |
| `PromotionTask` | Reúne os passos reutilizáveis de uma promoção |
| `PromotionTemplate` | Define os passos específicos de uma promoção de Stage |

Um `Warehouse` observa fontes e cria Freight. Um Stage escolhe qual Freight está disponível, verifica se há promoção automática e executa um template. Os passos normalmente atualizam um branch ou diretório do repositório GitOps. O Argo CD percebe a nova revisão e reconcilia o cluster.

Kargo não deve ser tratado como um segundo reconciler. Se o commit de promoção foi criado, mas o ambiente continua divergente, o próximo diagnóstico é do reconciler e não da descoberta do artefato.

## Pré-requisitos

Antes de criar os recursos, prepare:

1. Um cluster Kubernetes onde Kargo e o reconciler possam ser executados.
2. Um repositório de imagens com tags ou digests rastreáveis.
3. Um repositório GitOps com uma base e uma configuração por ambiente.
4. Uma credencial Git com o menor escopo necessário.
5. Uma credencial de leitura do registry, quando o registry não for público.
6. Uma estratégia para testar a saúde do ambiente antes da promoção seguinte.

O nome do projeto Kargo deve ser um namespace válido. Recursos do mesmo projeto usam esse namespace, o que simplifica a concessão de permissões e a separação de credenciais.

## Estrutura do repositório GitOps

Uma estrutura simples separa a base comum da composição de cada ambiente:

```text
gitops-repository/
  base/
    deployment.yaml
    service.yaml
    kustomization.yaml
  stages/
    test/
      kustomization.yaml
    uat/
      kustomization.yaml
    prod/
      kustomization.yaml
```

O branch `main` contém a base e os arquivos de origem. Branches de ambiente podem conter a saída promovida, ou podem ser substituídas por diretórios gerados por uma convenção do repositório. O importante é que o caminho usado no `Application` do Argo CD seja determinístico.

Uma promoção deve alterar somente o dado que identifica o artefato, como tag ou digest. Mudanças de infraestrutura, permissões e políticas continuam passando por revisão normal no repositório.

## Criando um projeto

Crie o projeto antes de qualquer `Warehouse` ou `Stage`:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Project
metadata:
  name: catalog
```

Aplicar o manifesto é uma operação de bootstrap. Depois disso, trate os recursos do projeto como código declarativo, versionado e revisado.

```bash
kubectl apply -f project.yaml
kubectl get projects
kubectl get namespaces
```

## Credenciais

Kargo identifica credenciais por labels e usa o namespace do projeto para limitar o escopo. Um repositório Git pode ser configurado com um Secret como o seguinte:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: catalog-git
  namespace: catalog
  labels:
    kargo.akuity.io/cred-type: git
type: Opaque
stringData:
  repoURL: https://github.com/example/catalog-gitops.git
  username: git-bot
  password: ${GIT_TOKEN}
```

O valor `${GIT_TOKEN}` deve ser resolvido por um mecanismo de secret durante a aplicação. Ele não deve ser substituído por um valor real em um arquivo versionado. A credencial deve permitir somente leitura e escrita no repositório necessário, sem acesso administrativo à organização.

Para registries privados, crie uma credencial de registry conforme a versão de Kargo instalada e associe-a à fonte correspondente. Prefira digests quando a imutabilidade do artefato for mais importante que a conveniência de uma tag.

## Descobrindo artefatos com Warehouse

O `Warehouse` descreve uma fonte e uma restrição de descoberta:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Warehouse
metadata:
  name: catalog
  namespace: catalog
spec:
  subscriptions:
    - image:
        repoURL: ghcr.io/example/catalog
        constraint: ^1.4.0
        discoveryLimit: 5
```

O `constraint` limita quais versões podem ser consideradas. O limite de descoberta evita que um warehouse acumule um volume desnecessário de versões. Quando a sequência de release tem significado operacional, use convenções de tags previsíveis ou promova por digest.

Verifique a descoberta antes de investigar uma falha de promoção:

```bash
kubectl get warehouse -n catalog
kubectl get freight -n catalog
kubectl describe warehouse catalog -n catalog
```

Se não houver Freight, o problema está na origem, na restrição, na credencial ou na reconciliação do Warehouse. Ainda não é um problema do Stage.

## PromotionTask reutilizável

Uma `PromotionTask` reúne operações que serão executadas em mais de um Stage. O exemplo abaixo clona a origem, cria ou limpa a saída do ambiente, atualiza a imagem, renderiza Kustomize, faz commit, publica a branch e atualiza o Argo CD:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: PromotionTask
metadata:
  name: promote-catalog
  namespace: catalog
spec:
  vars:
    - name: gitopsRepo
      value: https://github.com/example/catalog-gitops.git
    - name: imageRepo
      value: ghcr.io/example/catalog
  steps:
    - uses: git-clone
      config:
        repoURL: ${{ vars.gitopsRepo }}
        checkout:
          - branch: main
            path: ./src
          - branch: stage/${{ ctx.stage }}
            create: true
            path: ./out
    - uses: git-clear
      config:
        path: ./out
    - uses: kustomize-set-image
      as: update
      config:
        path: ./src/base
        images:
          - image: ${{ vars.imageRepo }}
            tag: ${{ imageFrom(vars.imageRepo).Tag }}
    - uses: kustomize-build
      config:
        path: ./src/stages/${{ ctx.stage }}
        outPath: ./out
    - uses: git-commit
      as: commit
      config:
        path: ./out
        message: ${{ task.outputs.update.commitMessage }}
    - uses: git-push
      config:
        path: ./out
    - uses: argocd-update
      config:
        apps:
          - name: catalog-${{ ctx.stage }}
            sources:
              - repoURL: ${{ vars.gitopsRepo }}
                desiredRevision: ${{ task.outputs.commit.commit }}
```

As variáveis que identificam repositórios, caminhos e aplicações devem ser parametrizadas. Isso permite usar o mesmo task em vários estágios sem copiar o processo e reduz divergência entre ambientes.

## Definindo o Stage

O primeiro Stage pode consumir diretamente o Warehouse:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Stage
metadata:
  name: test
  namespace: catalog
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: catalog
      sources:
        direct: true
  promotionTemplate:
    spec:
      steps:
        - task:
            name: promote-catalog
```

O Stage seguinte pode consumir Freight verificado pelo Stage anterior:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Stage
metadata:
  name: uat
  namespace: catalog
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: catalog
      sources:
        stages:
          - test
        autoPromotionOptions:
          selectionPolicy: MatchUpstream
  promotionTemplate:
    spec:
      steps:
        - task:
            name: promote-catalog
```

Em `prod`, `availabilityStrategy: All` exige que o Freight esteja disponível em todos os estágios anteriores configurados. Essa opção representa um fluxo mais conservador, em que cada ambiente precisa registrar sua evidência antes que o próximo avance.

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Stage
metadata:
  name: prod
  namespace: catalog
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: catalog
      sources:
        stages:
          - uat
          - test
        availabilityStrategy: All
        autoPromotionOptions:
          selectionPolicy: MatchUpstream
  promotionTemplate:
    spec:
      steps:
        - task:
            name: promote-catalog
```

## Modos de promoção

Kargo pode ser usado com diferentes graus de automação:

| Modo | Como funciona | Quando usar |
| --- | --- | --- |
| Manual pela UI | Um operador escolhe Freight e Stage no painel | Primeira adoção e incidentes controlados |
| Manual pela CLI | Um operador solicita promoção e acompanha o histórico | Runbooks e acesso remoto |
| Declarativo | `Stage`, tasks e políticas vivem no GitOps | Configuração auditável |
| Automático | Uma política habilita promoção ao surgir um candidato | Ambientes de baixo risco |
| Por branch | Cada Stage publica em uma branch distinta | Repositórios que usam revisão por branch |
| Por revisão | O reconciler recebe um commit ou digest explícito | Reprodutibilidade e rollback |
| Com verificação | A promoção aguarda análise ou health check | Produção e mudanças de maior risco |

Automação deve começar em `test`. Em ambientes críticos, combine promoção manual, aprovação de mudança e verificações de saúde antes de habilitar autopromoção.

## Habilitando autopromoção

Autopromoção é uma decisão de projeto e deve ser habilitada no `ProjectConfig`:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: ProjectConfig
metadata:
  name: catalog
  namespace: catalog
spec:
  promotionPolicies:
    - stageSelector:
        name: test
      autoPromotionEnabled: true
```

Manter essa política separada do Stage ajuda a revisar a autorização de autopromoção sem alterar o processo de promoção. Para `uat` e `prod`, habilite somente quando a seleção de Freight, as verificações e a estratégia de rollback estiverem claras.

`NewestFreight` escolhe o candidato mais novo disponível. `MatchUpstream` prefere a revisão promovida no estágio anterior. O segundo comportamento é mais previsível para uma cadeia de ambientes, pois evita que cada Stage escolha uma revisão diferente do fluxo principal.

## Promoção manual e histórico

Inspecione primeiro o estado do projeto e os candidatos:

```bash
kubectl get freight -n catalog
kubectl get stages -n catalog
kubectl describe stage test -n catalog
```

Depois solicite a promoção pela interface ou pela CLI da versão instalada. Uma promoção deve ser identificada pelo Stage e pelo Freight, e não apenas por uma tag humana. O histórico precisa permitir responder qual digest foi promovido, em qual commit e com quais passos.

Após a promoção, observe os dois sistemas separadamente:

```bash
kubectl get promotions -n catalog
kubectl get applications -n argocd
argocd app get catalog-test
argocd app wait catalog-test
```

Uma promoção concluída não garante que o Argo CD terminou a sincronização. O estado final precisa incluir a saúde da aplicação e dos workloads.

## Verificação, hold e rollback

Uma verificação deve medir o comportamento que justifica a promoção, como saúde dos pods, resposta de uma rota, migração concluída ou métrica de erro. Uma verificação que só confirma que o commit existe não comprova que o serviço está funcionando.

Ao promover um Freight que não é o candidato selecionado, Kargo pode criar um hold para impedir avanço automático inesperado. O hold deve ser entendido como um bloqueio explícito do fluxo, não como erro de descoberta. Promover o candidato esperado remove a condição quando a política permitir.

Rollback é a promoção de uma revisão anterior que ainda esteja disponível e seja conhecida como saudável. O procedimento deve preservar o histórico e evitar reescrever branches de forma destrutiva. Se a falha estiver no reconciler, primeiro corrija ou suspenda a sincronização nesse reconciler.

Promotion windows permitem restringir autopromoções a períodos operacionais. Auto rollback pode reduzir o tempo de recuperação, mas só é seguro quando a verificação mede uma falha confiável e não confunde uma dependência externa temporariamente indisponível com uma regressão da aplicação.

## Diagnóstico

Separe o diagnóstico em quatro camadas:

1. O Warehouse descobriu o artefato?
2. O Freight está disponível para o Stage?
3. A PromotionTask executou todos os passos?
4. O Argo CD ou Flux aplicou e deixou saudável a revisão promovida?

Comandos úteis:

```bash
kubectl get warehouses,freights,stages,promotions -n catalog
kubectl describe warehouse catalog -n catalog
kubectl describe stage test -n catalog
kubectl get events -n catalog --sort-by=.lastTimestamp
kubectl logs -n kargo deploy/kargo-controller
argocd app diff catalog-test
argocd app history catalog-test
argocd app resources catalog-test
```

Credenciais inválidas aparecem na camada de Warehouse ou nos passos Git. Um conflito no repositório aparece durante clone, commit ou push. Um manifesto inválido aparece na renderização Kustomize ou no Argo CD. Um workload não saudável aparece depois da sincronização e não deve ser mascarado como falha de promoção.

## Segurança e operação

Use namespaces separados por projeto, credenciais com escopo mínimo e revisão de todos os `PromotionTask`. Não coloque tokens em `vars` versionadas nem em mensagens de commit. Restrinja o acesso à UI e à API de Kargo e audite quem pode solicitar ou aprovar promoção.

Fixe imagens e actions por digest quando o risco justificar. Prefira digests de imagem em produção, retenha os artefatos necessários para rollback e teste a restauração do repositório GitOps. Evite permitir que uma task execute comandos arbitrários sem necessidade; cada passo deve ter a menor permissão possível.

## Evolução do fluxo

Comece com uma promoção manual em um único Stage. Depois adicione um segundo Stage que consome a evidência do primeiro. Só então automatize `test`, adicione verificações e estabeleça uma política para `prod`.

Quando o fluxo crescer, extraia tarefas comuns, estabeleça convenções para branches e commits, escolha uma estratégia de disponibilidade e documente o contrato de cada verificação. A complexidade deve estar na política e na evidência, não em cópias divergentes de manifestos.

## Relações

- [GitOps](gitops.md) explica a fonte declarativa de verdade.
- [Reconciliação](reconciliation.md) explica a convergência no cluster.
- [Application](application.md) explica o objeto do Argo CD que recebe a revisão.
- [Entrega progressiva](progressiva/argo-rollouts.md) trata tráfego e rollout.

## Fontes primárias

- [Kargo quickstart](https://docs.kargo.io/quickstart)
- [Working with Projects](https://docs.kargo.io/user-guide/how-to-guides/working-with-projects)
- [Working with Stages](https://docs.kargo.io/user-guide/how-to-guides/working-with-stages)
- [Promotion Tasks](https://docs.kargo.io/user-guide/reference-docs/promotion-tasks)
- [Promotion Templates](https://docs.kargo.io/user-guide/reference-docs/promotion-templates)
