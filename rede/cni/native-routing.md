# Roteamento nativo de Pods

No roteamento nativo, a rede encaminha tráfego para prefixes de Pods sem encapsular cada pacote numa rede overlay.

## Vantagem

Evita overhead de encapsulamento e torna o caminho de rede mais direto.

## Requisito

A infraestrutura precisa saber alcançar os prefixes corretos, por rotas estáticas, integração com a rede ou protocolos como BGP conforme a arquitetura.

## Trade-off

A simplicidade do pacote transfere parte da complexidade para roteamento e integração da rede física.

## Continue por aqui

[Encapsulamento](encapsulamento.md) apresenta o modelo alternativo.
