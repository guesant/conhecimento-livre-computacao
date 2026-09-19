# Diagnóstico de Pod, nó, certificado e Argo CD

Um cluster Kubernetes reporta seu estado por meio de recursos e eventos, não por um log central único, e a maior parte do trabalho de diagnóstico consiste em saber qual recurso descrever para chegar à causa mais rápido.

`kubectl describe` é o comando mais informativo nesse sentido: além de mostrar os campos do recurso, ele lista os eventos recentes que o controlador responsável emitiu ao tentar reconciliar aquele objeto, e é nesses eventos, não nos logs de um container que talvez nem tenha chegado a iniciar, que normalmente está a causa direta de um problema.

## Pod em Pending

Um Pod em `Pending` significa que o scheduler ainda não encontrou um nó compatível com os requisitos declarados, ou não pôde usar o nó que encontrou.

A seção `Events` ao final de `kubectl describe pod` costuma nomear a causa diretamente:

| Causa reportada em `Events` |
| --- |
| `Insufficient cpu` |
| `Insufficient memory` |
| `node(s) had taint that the pod didn't tolerate` |
| `didn't find available persistent volumes` |

Num cluster de um único nó, "nenhum nó disponível" quase sempre significa que esse nó específico não atende a algum requisito, o que reduz o espaço de causas a poucas possibilidades:

| Possibilidade |
| --- |
| `requests` de CPU ou memória maiores que a capacidade livre (visível em `kubectl describe node` na seção `Allocated resources`, que reflete reserva declarada, não uso real, um Pod pode ficar pendente num nó com uso de CPU baixo se os requests já somam perto de 100% do alocável) |
| um taint no nó sem a toleration correspondente no Pod |
| um `nodeSelector` ou afinidade que não bate com as labels do único nó existente |
| ou um `PersistentVolumeClaim` pendente por falta de `StorageClass` ou de capacidade |

Corrigir o requisito identificado, e não reaplicar o mesmo manifesto na esperança de um resultado diferente, é o que resolve o `Pending`.

## Nó NotReady

Um nó `NotReady` deixou de reportar heartbeats saudáveis ao control plane. Em um cluster de nó único, isso equivale à indisponibilidade do cluster inteiro, porque não existe um segundo nó para onde as cargas migrarem, e por isso merece tratamento de incidente imediato em vez de item de rotina.

`kubectl describe node` expõe a condição específica na seção `Conditions`:

| Condição | O que indica |
| --- | --- |
| `MemoryPressure`, `DiskPressure`, `PIDPressure` | cada uma remediável olhando o consumidor correspondente (uso de disco, um processo vazando memória) |
| `Ready: Unknown` | indica perda de comunicação entre o control plane e o kubelet daquele nó |

Quando control plane e kubelet rodam no mesmo host, como acontece num nó único, essa perda de comunicação normalmente não é um problema de rede e sim o próprio serviço parado ou o host travado; olhar o status do serviço e seus logos mais recentes no próprio host costuma revelar se ele caiu, travou reiniciando em loop, ou nunca chegou a subir.

Um relógio desalinhado no host também pode se manifestar como falha de heartbeat, porque componentes que validam certificados TLS entre si dependem de horários próximos; vale conferir a sincronização de horário antes de assumir uma causa mais complexa.

Na maioria dos casos um reinício do serviço resolve um estado travado; se o host inteiro não volta (hardware perdido, disco corrompido), a resposta correta deixa de ser tentar recuperar aquele host e passa a ser reconstruir o cluster a partir do zero com a automação existente, é para isso que serve um runbook de disaster recovery testado.

## Certificate que não fica Ready

Quando a emissão de TLS é automatizada por um controlador que fala o protocolo ACME (a mecânica está descrita em [TLS automático](tls-automatico.md)), um `Certificate` que fica preso sem atingir `Ready` significa que essa automação ainda não completou a emissão ou a renovação, e o serviço que dependia desse certificado continua servindo o anterior, ou nenhum, até o problema se resolver.

A cadeia de recursos por trás de uma emissão ACME segue uma hierarquia fixa: `Certificate` deriva um CertificateRequest, que deriva uma Order, que deriva um ou mais Challenge; listar os quatro tipos de recurso juntos no mesmo namespace mostra em qual elo a cadeia travou.

Um `Challenge` preso em `pending` por muito tempo é a causa mais comum, e normalmente aponta para uma de duas coisas: o registro DNS do desafio ainda não propagou (challenges de validação por DNS podem levar minutos até os servidores autoritativos responderem de forma consistente), ou a credencial usada para escrever nesse DNS não tem permissão suficiente.

Antes de investigar o Challenge, porém, vale confirmar que o emissor referenciado pelo `Certificate` está ele mesmo `Ready`; um emissor quebrado impede qualquer certificado que o use de emitir, e corrigir o emissor primeiro evita investigar sintomas de uma causa já conhecida em múltiplos certificados ao mesmo tempo.

Depois de corrigir a causa raiz, o controlador tenta de novo automaticamente no próximo ciclo; para não esperar esse ciclo, remover a tentativa travada (o `CertificateRequest` associado) faz o controlador recriar uma tentativa nova a partir do `Certificate` já existente.

## Application OutOfSync ou Degraded no Argo CD

O padrão GitOps descrito em [ArgoCD e GitOps](argocd.md) faz o Argo CD comparar continuamente o que está declarado no Git com o que existe no cluster, e reportar o resultado dessa comparação em duas dimensões independentes que é importante não confundir.

`OutOfSync` descreve a comparação em si: o estado do cluster diverge do que está no Git, o que pode ser uma mudança manual não versionada feita diretamente no cluster, ou uma mudança já commitada que ainda não foi sincronizada porque a sincronização automática está desligada para aquela Application.

`Degraded` descreve outra coisa, a saúde dos recursos que já estão sincronizados, independentemente de estarem ou não alinhados com o Git; uma Application pode estar perfeitamente sincronizada e ainda assim `Degraded`, se o que o Git descreve não sobe de forma saudável no cluster.

Tratar os dois como o mesmo problema leva a diagnosticar a coisa errada: um `describe` da Application mostra o diff entre desejado e observado além dos eventos recentes de sincronização.

Mas quando o sintoma é `Degraded` a investigação real está nos Pods daquele namespace, não na Application em si, porque a causa costuma ser um `CrashLoopBackOff/ImagePullBackOff` ou uma falha de probe comuns a qualquer workload, sem nada de específico do Argo CD.

Uma causa recorrente de `OutOfSync` permanente mesmo com correção automática habilitada é um campo que um controller externo além do Argo CD também escreve, como um autoscaler ajustando réplicas; sem declarar esse campo como uma diferença a ignorar, o Argo CD e o outro controller entram num ciclo de reescrever um ao outro.

Depois de corrigir a causa raiz, forçar uma nova sincronização substitui os recursos existentes em vez de aplicar um patch incremental, o que deve ser usado com atenção quando outro controller também gerencia parte do mesmo recurso.

## Continue por aqui

[ArgoCD e GitOps](argocd.md) e [TLS automático](tls-automatico.md) explicam os mecanismos que este texto pressupõe. [Rollout de imagens](../arquitetura/rollout-de-imagens.md), na arquitetura, mostra como o hl-infrastructure recuperou de um conflito de campo imutável num apply de chart real.
