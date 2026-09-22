# Argo Rollouts

Argo Rollouts é um controller Kubernetes que adiciona estratégias de deployment progressivo como canary e blue-green, incluindo etapas, pausas e integração com análise de métricas e roteamento de tráfego.

## Casos de uso

É apropriado quando Deployments padrão não oferecem controle suficiente sobre progressão e rollback e a plataforma já possui observabilidade e, quando necessário, integração de tráfego.

## Boa prática

Mantenha critérios de análise simples e relacionados à saúde real do serviço. Teste abort e rollback. Entenda qual componente controla o tráfego antes de depender de pesos.

## Má prática

Adicionar Rollouts sem métricas confiáveis aumenta complexidade sem produzir segurança adicional. Automatizar promoção com sinais ruidosos pode tornar o controller um amplificador de decisões ruins.

## Fontes

- Argo Rollouts: https://argo-rollouts.readthedocs.io/

## Continue por aqui

[Canary](canary.md) e [blue-green](blue-green.md) explicam as estratégias independentemente da ferramenta.