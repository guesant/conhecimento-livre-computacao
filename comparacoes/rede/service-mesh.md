# Istio, Linkerd e Cilium Service Mesh

As três alternativas podem fornecer identidade de workload, mTLS, telemetria e controle de tráfego entre serviços, mas não ocupam exatamente o mesmo ponto da arquitetura. A comparação correta começa pela fronteira que se deseja adicionar: uma mesh dedicada, uma integração mais estreita com a rede existente ou uma superfície menor para os requisitos essenciais.

## Responsabilidade e acoplamento

Istio é uma plataforma de service mesh com uma superfície ampla de traffic management, segurança e observabilidade. Linkerd concentra-se no caminho de comunicação entre serviços e busca reduzir a quantidade de decisões operacionais. Cilium pode combinar funções de mesh com o CNI, políticas e dataplane já usados pelo cluster.

Isso não torna Cilium automaticamente a melhor escolha para quem já usa Cilium, nem torna Istio inadequado por ter mais recursos. A integração reduz componentes separados, mas concentra mais funções no CNI. Uma mesh dedicada separa o domínio de upgrade e de falha, mas acrescenta outro dataplane, outro ciclo de certificados e outra camada de diagnóstico.

## Dimensões de comparação

| Dimensão | Istio | Linkerd | Cilium Service Mesh |
| --- | --- | --- | --- |
| Escopo típico | mesh ampla, tráfego, segurança e telemetria | comunicação entre serviços com superfície menor | funções de mesh integradas ao CNI e ao dataplane |
| Relação com a rede | componente separado da CNI | componente separado da CNI | mais próxima da CNI Cilium |
| Modelo de proxy | sidecar ou ambient, conforme o modo | proxy leve por workload ou arquitetura adotada | recursos do dataplane Cilium e proxies conforme o recurso |
| Principal custo | quantidade de recursos e opções operacionais | cobertura menor quando requisitos avançados aparecem | concentração de responsabilidades e dependência do Cilium |
| Diagnóstico | exige separar gateway, mesh, proxy e aplicação | exige separar proxy, identidade e aplicação | exige separar CNI, policy, mesh e aplicação |

## Quando uma mesh dedicada faz sentido

Uma plataforma dedicada é plausível quando o cluster precisa de políticas de comunicação uniformes, identidade forte entre muitos serviços, retries e traffic shifting governados por uma camada comum ou uma equipe que já opera essa tecnologia em vários ambientes. O benefício vem da padronização, não do simples fato de haver mais componentes.

Istio tende a fazer sentido quando os requisitos de roteamento, segurança e integração são amplos o bastante para justificar sua superfície. Linkerd tende a fazer sentido quando o conjunto de capacidades necessárias é menor e a simplicidade operacional tem peso maior que recursos avançados.

## Quando integrar à CNI

Cilium Service Mesh pode ser uma composição coerente quando Cilium já é responsável por conectividade, identidade de rede, NetworkPolicy e observabilidade. A integração reduz duplicação de dataplane e pode simplificar a circulação de identidade entre camadas.

O custo é colocar mais comportamento crítico no mesmo componente. Uma regressão ou upgrade mal planejado do Cilium pode afetar conectividade, policy, observabilidade e funções de mesh ao mesmo tempo. O cluster precisa de testes que cubram cada responsabilidade separadamente e de uma estratégia de recuperação que não dependa de todas elas estarem saudáveis simultaneamente.

## Critérios de seleção

Compare, antes de escolher:

- quais protocolos e padrões de identidade a aplicação realmente usa;
- onde termina o gateway e começa o tráfego entre serviços;
- como certificados são emitidos, renovados e distribuídos;
- onde retries, timeouts e circuit breaking serão configurados;
- quanto CPU, memória e latência o proxy pode consumir;
- como será feito o diagnóstico quando CNI, proxy e aplicação relatarem estados diferentes;
- qual componente a equipe consegue atualizar e recuperar sem depender de outro componente indisponível.

Não introduza uma mesh apenas para obter mTLS em poucos serviços. Nesse caso, mTLS na borda ou uma política de identidade mais simples pode atender ao requisito com menos failure domains. Não use o gateway para resolver problemas que pertencem ao tráfego interno, nem a mesh para esconder contratos de aplicação frágeis.

## Migração e reversibilidade

Uma migração segura começa por um namespace ou caminho de tráfego pequeno, com métricas de latência, erros, consumo de recursos e falhas de handshake. O modo antigo deve continuar removível durante a janela de observação. A reversibilidade depende de manter explícitos os pontos de interceptação, as políticas e os certificados, e não apenas de poder desinstalar o chart.

## Páginas canônicas e fontes

- [Service mesh](../../rede/service-mesh/index.md) explica a responsabilidade geral.
- [Istio](../../rede/service-mesh/istio.md), [Linkerd](../../rede/service-mesh/linkerd.md) e [Cilium Service Mesh](../../rede/service-mesh/cilium-service-mesh.md) explicam cada implementação.
- [Istio documentation](https://istio.io/latest/docs/)
- [Linkerd overview](https://linkerd.io/2/overview/)
- [Cilium Service Mesh](https://docs.cilium.io/en/stable/network/servicemesh/)
