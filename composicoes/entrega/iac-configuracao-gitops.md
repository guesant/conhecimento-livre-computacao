# IaC, gestão de configuração e GitOps

Essas três famílias podem coexistir porque reconciliam objetos diferentes em momentos diferentes.

## Provisionamento

Terraform/OpenTofu/Pulumi normalmente criam recursos por APIs: redes, VMs, DNS, buckets, identidades ou serviços gerenciados. Seu estado acompanha objetos externos.

## Gestão de configuração

Ansible, Puppet, Chef e Salt configuram sistemas que já existem: pacotes, arquivos, usuários e serviços. Em hosts físicos, essa camada frequentemente começa depois que firmware, disco e sistema operacional básico já existem.

## GitOps

Argo CD e Flux reconciliam recursos de uma plataforma a partir de Git. No Kubernetes, eles normalmente começam depois que o cluster e o próprio reconciler existem.

## Uma composição comum

IaC cria VM/rede → configuration management prepara OS e instala Kubernetes → bootstrap instala o reconciler GitOps → GitOps passa a gerir workloads e componentes declarativos do cluster.

As fronteiras podem variar. OpenTofu pode instalar Helm; Ansible pode aplicar manifests; CI pode executar kubectl. O fato de ser possível não significa que a responsabilidade deva ser compartilhada.

## Boa prática

Escolha um owner principal para cada recurso. Se OpenTofu e Argo CD tentam reconciliar o mesmo objeto Kubernetes, cada um pode desfazer a mudança do outro.

## Cenário físico single-node

Não há VM para provisionar. O fluxo pode começar em configuração do host, depois bootstrap da plataforma e finalmente GitOps. IaC continua útil para APIs externas mesmo que não crie o servidor físico.

## Cenário cloud

IaC pode criar rede, cluster gerenciado e identidades; GitOps assume addons e workloads. Configuration management pode desaparecer quase completamente se não existem hosts administrados diretamente.

## Anti-patterns

Não use uma ferramenta como martelo universal apenas porque ela possui provider/módulo capaz de tocar outro domínio. Minimizar número de ferramentas pode aumentar acoplamento se uma única execução passa a controlar recursos com ciclos de vida muito diferentes.

## Continue por aqui

[Infraestrutura como código](../../iac-provisionamento.md), [Ansible](../../ansible.md) e [Argo CD](../../argocd.md) explicam as peças.