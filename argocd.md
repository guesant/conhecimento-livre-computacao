# ArgoCD e GitOps

GitOps é uma forma de operar infraestrutura onde um repositório git é a única fonte da verdade sobre o que deveria estar rodando, e um agente dentro do próprio ambiente de destino (não uma pipeline externa empurrando mudanças) observa esse repositório continuamente e converge o estado real para o que está declarado nele. A diferença central em relação a uma pipeline de deploy tradicional (que roda `kubectl apply` a partir de um servidor de CI, por exemplo) é essa inversão: em vez de algo de fora empurrando mudanças para dentro do cluster, algo de dentro do cluster puxa o que precisa aplicar, comparando continuamente contra o git. Isso tem uma consequência prática importante: uma mudança feita manualmente no cluster, fora do git, é detectada como uma divergência (chamada de *drift*) e pode ser revertida automaticamente, porque o agente sempre volta a convergir para o que o git declara.

ArgoCD é a implementação de GitOps mais usada para Kubernetes. Ele roda dentro do próprio cluster, observa um ou mais repositórios git, e mantém o estado do cluster sincronizado com o que esses repositórios declaram.

## `Application` e `AppProject`

Uma `Application`, no ArgoCD, é o objeto que declara "sincronize este caminho deste repositório git para este destino": qual repositório, qual branch ou tag, qual pasta dentro dele, e para qual cluster e namespace o resultado deve ir. Um `AppProject` agrupa `Application`s sob uma política de permissão comum: de quais repositórios elas podem vir, para quais destinos podem apontar, e quais tipos de recurso Kubernetes elas têm permissão de criar. Isso permite, por exemplo, que um projeto restrinja `Application`s de terceiros a só criarem recursos de namespace, nunca um recurso de escopo de cluster inteiro, sem precisar confiar cegamente no conteúdo de cada repositório.

## O padrão app-of-apps

Em vez de configurar manualmente cada `Application` uma por uma dentro do cluster, o padrão app-of-apps usa uma `Application` raiz cujo próprio conteúdo, no git, é uma pasta de manifestos de outras `Application`s. O ArgoCD sincroniza essa raiz como sincronizaria qualquer outra aplicação, e o resultado dessa sincronização é a criação (ou remoção) das `Application`s filhas. O efeito prático é que registrar uma aplicação nova no cluster inteiro se torna "adicionar um arquivo numa pasta e dar `git push`", sem nenhum passo manual dentro do cluster.

## Modos de sincronização

Uma `Application` pode exigir aprovação manual para cada sincronização, ou pode ser configurada com sincronização automática (`selfHeal`, que reverte drift automaticamente, e `prune`, que remove do cluster o que foi removido do git). Automação total é conveniente, mas amplia o raio de dano de um erro no git: um manifesto errado commitado por engano é aplicado sem revisão humana nenhuma no momento do apply. Um projeto que decide automatizar tudo geralmente compensa isso com mais rigor na revisão antes do merge, não menos.

## Continue por aqui

["GitOps: root e satélites"](../arquitetura/gitops-root-e-satelites.md), na arquitetura, mostra como o hl-infrastructure usa exatamente esse padrão app-of-apps, com dois `AppProject`s de permissão bem diferente (`infra` e `satellites`), e como um satélite novo é registrado em [Adicionar um satélite novo](../operacional/adicionar-um-satelite.md).
