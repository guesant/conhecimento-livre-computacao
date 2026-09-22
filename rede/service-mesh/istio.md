# Istio

Istio é uma implementação de service mesh com recursos de traffic management, segurança e observabilidade. Sua arquitetura moderna pode operar com sidecars ou com o modo ambient, conforme o caso.

## Casos de uso

Políticas de comunicação, identidade/mTLS e controle avançado de tráfego em plataformas com muitos serviços são casos típicos.

## Boa prática

Introduza recursos por necessidade e mantenha clara a fronteira entre gateway, CNI, mesh e aplicação.

## Má prática

Usar traffic management do mesh para compensar contratos de aplicação frágeis ou introduzir múltiplas camadas de retry sem orçamento de latência pode amplificar falhas.

## Fontes

- Istio documentation: https://istio.io/latest/docs/