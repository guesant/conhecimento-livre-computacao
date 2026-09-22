# Executar serviços em um pequeno cluster

Adicionar um segundo ou terceiro host muda o problema: agora existem placement, rede entre hosts, estado distribuído, manutenção parcial e possibilidade de sobreviver à perda de uma máquina. Mas "multi-node" ainda não implica que toda carga precise de uma plataforma complexa.

## Forças de decisão

Pergunte se workloads precisam migrar automaticamente entre hosts, se há serviços stateful, qual indisponibilidade é aceitável, quem opera a plataforma, como volumes são acessados, se existe load balancer e quantos failure domains reais existem.

Três máquinas no mesmo filtro de linha e no mesmo switch não representam três failure domains independentes para energia e rede.

## Padrão: orquestração simples

Um cluster pequeno e estável pode usar uma solução com superfície menor quando os requisitos são basicamente scheduling, service discovery e rolling update. A vantagem é reduzir a quantidade de abstrações.

A limitação aparece quando a plataforma começa a exigir extensibilidade, políticas, operators, integração cloud-native ou uma API que muitas ferramentas já assumem ser Kubernetes.

## Padrão: Kubernetes leve

K3s é uma forma de manter a API Kubernetes reduzindo parte do custo de instalação e empacotamento. Em três ou mais servidores, o desenho do datastore e quorum passa a ser uma decisão real.

Workers adicionais aumentam capacidade, mas não aumentam automaticamente disponibilidade do control plane. Servidores adicionais precisam respeitar quorum; armazenamento persistente precisa sobreviver ou mover dados de forma coerente com o workload.

## Estado muda a arquitetura

Stateless workloads são relativamente fáceis de reagendar. Um banco com volume local não se torna altamente disponível porque seu Pod pode ser recriado em outro nó; os dados precisam estar acessíveis e consistentes.

Antes de adotar storage distribuído, compare o custo dele com alternativas: manter o serviço stateful fixo em um nó com backup/restore rápido, usar replicação nativa do banco ou consumir um serviço externo.

## Anti-patterns

Não conte réplicas de Pod como redundância se todas dependem do mesmo banco, disco, ingress ou energia. Não distribua control plane em número par esperando maior tolerância de falha. Não introduza storage distribuído apenas para remover qualquer afinidade a host quando o custo de operação supera o requisito.

## Caminho de evolução

Um pequeno cluster pode crescer em duas dimensões diferentes: mais capacidade e mais requisitos de plataforma. Mais CPU não implica automaticamente mais complexidade de controle. Reavalie arquitetura quando surgirem multi-tenancy, SLOs mais rígidos, equipes independentes, compliance, dezenas de serviços ou necessidade de upgrades sem janela ampla.

## Continue por aqui

[Quando Kubernetes faz sentido](quando-kubernetes.md) isola os critérios da plataforma. [K3s](../../k3s.md) aprofunda a distribuição.
