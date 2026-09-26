# Internet Exchange Point

Um provedor de acesso não precisa carregar todo o tráfego de seus assinantes
até um terceiro. Ele pode estabelecer peering direto com outras redes. Um
Internet Exchange Point, IXP, concentra esse peering em uma infraestrutura
física e lógica compartilhada.

## Problema de escala

Sem um ponto de troca comum, cada par de redes precisaria de uma conexão
dedicada. Com um IXP, cada participante conecta um único enlace ao switch
compartilhado e troca tráfego com os demais participantes por essa malha.
Isso reduz custo, caminhos indiretos e latência.

O IX.br, mantido pelo NIC.br, possui pontos distribuídos em várias cidades
brasileiras. O peering local ajuda a manter o tráfego entre redes brasileiras
dentro do país quando existe uma rota adequada entre os participantes.

## Observação de contexto

Serviços como o Cloudflare Radar exibem dados agregados sobre tráfego,
protocolos e incidentes por região. Eles ajudam a entender o contexto da
conectividade, mas não substituem testes de uma conexão específica nem a
análise de rota entre dois pontos.

## Continue por aqui

[BGP](../roteamento/bgp.md) explica como redes anunciam caminhos e
[conectividade WAN](wan.md) explica como o enlace de uma rede chega ao
provedor.
