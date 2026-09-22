# Cilium

Cilium é uma plataforma de networking, segurança e observabilidade para ambientes como Kubernetes. Seu dataplane usa eBPF extensivamente e pode assumir responsabilidades que, em outros desenhos, ficam distribuídas entre CNI, kube-proxy, observabilidade de rede e componentes de service mesh.

## O que ele é e o que não é

Como CNI, Cilium conecta Pods e integra políticas de rede. Recursos adicionais incluem kube-proxy replacement, Hubble para observabilidade, Gateway API/Ingress e capacidades de service mesh.

Adotar Cilium como CNI não obriga a habilitar todas essas funções. "Usar Cilium" descreve uma família de modos operacionais, não uma configuração única.

## Dataplane e eBPF

eBPF permite executar programas verificados no kernel em hooks de rede e outros pontos. Cilium usa esses mecanismos para encaminhamento, policy, load balancing e observabilidade.

Isso reduz dependência de algumas cadeias tradicionais de iptables em determinados modos, mas também torna versão e capacidades do kernel parte importante da compatibilidade.

## Modos de rede

Clusters podem usar encapsulamento ou roteamento nativo conforme topologia. MTU, infraestrutura subjacente, cloud e necessidade de anunciar rotas influenciam a escolha.

Não existe um modo universalmente correto. Encapsulamento simplifica algumas topologias ao custo de overhead; native routing expõe mais diretamente a topologia e exige que a rede saiba encaminhar os prefixes relevantes.

## Network policy

Cilium suporta políticas Kubernetes e extensões próprias. Políticas L3/L4 controlam identidades/endpoints e portas; capacidades L7 podem impor regras mais específicas em protocolos suportados.

Política de rede não substitui autorização de aplicação. Permitir que workload A alcance B não significa que A possa executar qualquer operação em B.

## Hubble

Hubble observa fluxos de rede e decisões de policy. Ele é útil para responder "quem falou com quem?" e "qual policy bloqueou o fluxo?", reduzindo dependência de inferência a partir de logs de aplicação.

Observabilidade de rede complementa métricas e traces da aplicação; ela não conhece automaticamente a semântica de negócio da requisição.

## Kube-proxy replacement

Cilium pode implementar funções normalmente realizadas por kube-proxy. Essa decisão altera uma peça central do dataplane e precisa ser tratada como modo arquitetural, não como simples otimização.

## Cenário pequeno

Em um cluster pequeno, Cilium pode ser usado apenas como CNI/policy. Habilitar Hubble pode valer pelo diagnóstico. Service mesh, BGP e recursos avançados devem entrar somente se houver requisito.

## Cenário de plataforma

Em clusters compartilhados, identidade de workload, policy, observabilidade e integração com Gateway API podem reduzir o número de produtos. O trade-off é concentrar mais funções e upgrades em uma peça crítica.

## Boas práticas

Fixe explicitamente o modo de dataplane; valide requisitos de kernel; documente MTU; teste políticas default-deny antes de produção; monitore agentes e operator; trate upgrade de CNI como mudança de infraestrutura crítica.

## Más práticas

Habilitar kube-proxy replacement, BGP, mesh e L7 policy simultaneamente sem necessidade. Migrar CNI sem plano de recuperação. Comparar performance sem reproduzir encapsulamento e policies. Usar Hubble como justificativa para não instrumentar aplicações.

## Alternativas

[Calico](calico.md) é uma alternativa relevante para networking e policy. CNIs de provedores cloud podem integrar melhor com suas redes nativas. A escolha depende do conjunto de responsabilidades desejado.

## Fontes

- Cilium documentation: https://docs.cilium.io/
- Cilium networking: https://docs.cilium.io/en/stable/network/concepts/
- Cilium network policy: https://docs.cilium.io/en/stable/security/policy/
- Hubble: https://docs.cilium.io/en/stable/observability/hubble/

## Continue por aqui

[CNI](index.md) explica a categoria. [Cilium e Calico](../../comparacoes/rede/cilium-calico.md) compara as implementações. [CNI, Service, Gateway e service mesh](../../composicoes/kubernetes/rede-e-trafego.md) mostra como as responsabilidades se relacionam.