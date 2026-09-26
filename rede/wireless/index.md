# Redes sem fio

Redes sem fio usam rádio para transportar quadros de uma rede local ou de uma
rede de acesso. A qualidade percebida não depende apenas da geração anunciada
no ponto de acesso. Espectro disponível, largura de canal, interferência,
distância, obstáculos, capacidade do backhaul, número de clientes e políticas
de roaming costumam determinar mais o resultado prático.

## Conceitos relacionados

- [Gerações de Wi-Fi](wifi-generations.md) explica a nomenclatura comercial e
  a relação com as emendas IEEE 802.11.
- [Redes mesh](mesh.md) explica como vários pontos de acesso ou nós cooperam
  para formar uma cobertura maior.
- [VLAN](../fundamentos/vlan.md) trata da separação lógica que frequentemente
  acompanha SSIDs de usuários, convidados e dispositivos.
- [Categorias de cabos](../cabeamento/categorias-de-cabos.md) explica como o
  cabeamento e o backhaul influenciam uma implantação sem fio.

## Capacidade, cobertura e mobilidade

Cobertura é a área onde o sinal atende ao requisito mínimo. Capacidade é o
volume de tráfego que a célula consegue transportar para todos os clientes.
Mobilidade é a capacidade de um cliente mudar de ponto de acesso sem uma
interrupção perceptível. Aumentar potência para obter mais cobertura pode
reduzir a reutilização do canal e dificultar o roaming, portanto essas metas
precisam ser tratadas separadamente.

Um projeto deve escolher canais, potência, largura de canal e posicionamento a
partir de medições. Em redes densas, canais menores e mais células podem
produzir resultado melhor do que um único ponto de acesso com canal largo.

## Fontes primárias

- [IEEE 802.11 Working Group](https://www.ieee802.org/11/)
- [Wi-Fi Alliance](https://www.wi-fi.org/discover-wi-fi)
- [Wi-Fi CERTIFIED 7](https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-7)
