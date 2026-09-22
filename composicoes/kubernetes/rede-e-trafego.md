# CNI, Service, Gateway e service mesh

Essas tecnologias aparecem juntas em clusters Kubernetes, mas não são camadas substituíveis.

## Caminho básico

A CNI fornece conectividade de Pod e, dependendo da implementação, policy e recursos adicionais. Um Service fornece um endpoint estável e seleção de backends. Gateway API ou Ingress descrevem como tráfego entra ou é roteado em L7 por uma implementação de gateway/controller. Um service mesh adiciona capacidades ao tráfego entre workloads, como identidade, mTLS, policy e telemetria.

## Composição mínima

Um cluster não precisa de service mesh para ter rede. CNI + Services já suportam comunicação básica. Um gateway só é necessário quando há tráfego que precisa da função que ele oferece.

Essa propriedade é útil para manter a arquitetura incremental: adicione uma camada quando existir um requisito que a camada anterior não resolve.

## Sobreposição

Cilium pode implementar CNI, NetworkPolicy e partes de observabilidade e service mesh. Istio pode controlar tráfego L7 e identidade entre workloads. Um gateway também pode terminar TLS e aplicar políticas.

Quando duas peças oferecem a mesma função, escolha explicitamente quem é responsável. Duplicar retries, mTLS ou autorização em várias camadas sem modelo claro produz comportamento difícil de prever.

## Cenário 1: cluster pequeno

CNI + Service + um gateway para entrada pode ser suficiente. Service mesh adiciona pouco se existem poucos serviços e nenhuma necessidade de identidade/policy L7 entre eles.

## Cenário 2: plataforma compartilhada

NetworkPolicy na camada de rede, Gateway API na borda e mesh para identidade e políticas entre serviços podem formar responsabilidades distintas, desde que cada fronteira seja documentada.

## Anti-patterns

Não instale mesh para "ter observabilidade" se métricas e traces da aplicação já resolvem a pergunta. Não use um gateway como substituto de NetworkPolicy. Não presuma que mTLS entre proxies corrige autenticação e autorização de usuário na aplicação.

## Continue por aqui

[CNI](../../rede/cni/index.md), [Gateway API](../../gateway-api.md) e [service mesh](../../rede/service-mesh/index.md) aprofundam cada responsabilidade.