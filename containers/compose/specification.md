# Compose Specification

Compose Specification define um modelo para aplicações compostas por serviços, redes, volumes, configs e secrets.

Compose é um modelo de composição, não um scheduler de cluster equivalente a Kubernetes. Docker Compose é uma implementação; outras ferramentas podem consumir total ou parcialmente a especificação.

É especialmente útil para uma aplicação multi-container executada como unidade em um ambiente simples. Veja [single-node](../../cenarios/execucao/single-node.md).