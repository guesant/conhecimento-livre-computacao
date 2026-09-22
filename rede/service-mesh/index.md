# Service mesh

Service mesh introduz uma camada de infraestrutura para controlar e observar comunicação entre serviços, normalmente oferecendo identidade de workload, mTLS, políticas e telemetria.

## Casos de uso

É útil quando requisitos de comunicação entre muitos serviços justificam uma camada comum de identidade, segurança e traffic management.

## Má prática

Adicionar mesh a poucos serviços simples sem requisito concreto pode custar mais em complexidade do que entrega em valor.

## Implementações

[Istio](istio.md) e [Linkerd](linkerd.md) ocupam esse espaço com arquiteturas e superfícies operacionais diferentes.