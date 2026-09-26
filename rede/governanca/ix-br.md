# IX.br

IX.br é o projeto brasileiro de pontos de troca de tráfego coordenado pelo CGI.br e operado no ecossistema do NIC.br. Ele fornece a infraestrutura para que sistemas autônomos troquem tráfego diretamente em uma localidade metropolitana, em vez de enviar todo o tráfego por redes de terceiros ou por caminhos mais longos.

## O que é um IXP

Um Internet Exchange Point, IXP, é uma infraestrutura compartilhada de interconexão. Participantes conectam seus roteadores a um ponto de presença, estabelecem sessões de peering e anunciam rotas conforme suas políticas. A matriz de comutação permite que o tráfego seja entregue diretamente entre redes participantes.

O IX.br não é um provedor de acesso e não substitui trânsito IP. Uma rede pode participar de um IX e continuar precisando de trânsito para alcançar destinos que não estejam presentes no ponto de troca.

## Benefícios

A troca local pode reduzir latência, custo e dependência de caminhos indiretos. Também pode melhorar o controle operacional sobre a entrega de tráfego e manter parte das comunicações entre redes brasileiras dentro do país quando existe uma rota de peering adequada.

Esses benefícios não são automáticos. Eles dependem da presença das redes relevantes, da configuração de BGP, da capacidade dos enlaces, da política de filtragem e da disponibilidade da localidade.

## Participação e BGP

O participante normalmente precisa de um sistema autônomo, conectividade até a localidade e configuração compatível com os requisitos técnicos do IX. As rotas são trocadas usando BGP. Route servers podem simplificar o peering multilateral, mas não eliminam a necessidade de uma política de roteamento bem definida.

A segurança continua sendo responsabilidade de cada participante. Filtros de prefixos, limites de sessão, validação de origem com RPKI quando aplicável, monitoramento e plano de retirada são necessários para reduzir vazamentos e anúncios indevidos.

## IX.br e outras camadas

- o CGI.br coordena o projeto e suas diretrizes;
- o NIC.br mantém o ecossistema operacional associado;
- os PIXes fornecem pontos de acesso físicos ou lógicos à localidade;
- os sistemas autônomos participantes controlam seus anúncios e sessões;
- os provedores de trânsito continuam necessários para destinos não alcançados pelo peering.

## Fontes primárias

- [Sobre o IX.br](https://www.ix.br/sobre)
- [FAQ do IX.br](https://www.ix.br/faq)
- [Route servers e communities](https://ix.br/route-server-and-commmunities)
- [Requisitos técnicos do IX.br](https://old.ix.br/doc/PRT_IX.br_V1.0_30_06_2017.pdf)
