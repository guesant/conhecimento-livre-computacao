# Redes mesh

Uma rede mesh é uma topologia em que vários nós cooperam para oferecer
conectividade. Em uma rede sem fio doméstica, os nós normalmente são pontos de
acesso que compartilham identidade, configuração e algum mecanismo de
backhaul. Em outras arquiteturas, os nós podem encaminhar tráfego entre si e
formar uma malha de múltiplos saltos.

## Backhaul

O backhaul liga o nó ao restante da rede. Há três modelos comuns:

| Modelo | Característica | Consequência |
| --- | --- | --- |
| Cabeado | cada nó usa Ethernet ou fibra | preserva mais capacidade de rádio para os clientes |
| Rádio dedicado | uma banda ou rádio separado carrega o backhaul | reduz a disputa, mas aumenta custo e uso de espectro |
| Rádio compartilhado | clientes e backhaul dividem o mesmo rádio | simplifica a instalação, mas cada salto pode reduzir capacidade |

Quando é possível instalar cabo, o chamado mesh com backhaul cabeado costuma
ser mais previsível. Mesh não é sinônimo de extensor simples: é necessário
entender como os nós escolhem caminho, como evitam loops, como distribuem
configuração e como um cliente troca de célula.

## Mesh, roaming e repetição

Roaming é a mudança do cliente entre pontos de acesso. Mesh é uma propriedade
da conectividade entre nós. Uma rede pode ter vários pontos de acesso com
backhaul cabeado e roaming sem formar uma malha de múltiplos saltos. Da mesma
forma, uma malha pode existir sem que o roaming do cliente seja rápido.

Mecanismos como 802.11k, 802.11v e 802.11r podem ajudar na descoberta,
orientação e autenticação, mas o resultado também depende do cliente. O
controlador pode sugerir uma mudança, porém normalmente o cliente participa da
decisão final.

## Casos apropriados

Mesh é útil quando não é possível levar cabo a todos os pontos, quando a área
tem obstáculos ou quando a instalação precisa crescer gradualmente. É comum
em residências, espaços temporários, áreas externas, redes de sensores e
alguns enlaces comunitários.

Ele é menos apropriado quando a capacidade precisa ser previsível, o tráfego
é alto ou o backhaul pode ser cabeado. Antes de adicionar nós, meça o sinal no
local onde cada nó será instalado. Um nó colocado em uma área sem bom enlace
com o restante apenas estende uma conexão ruim.

## Operação

Documente canais, potência, localização, uplinks, versão de firmware e
dependências do controlador. Defina o que acontece quando o controlador, o
backhaul, a energia ou a nuvem ficam indisponíveis. Separe SSIDs de usuários,
convidados e dispositivos usando VLANs e políticas de firewall, em vez de
tratar a associação ao SSID como único controle de segurança.

## Fontes primárias

- [IEEE 802.11 Working Group](https://www.ieee802.org/11/)
- [Wi-Fi Alliance](https://www.wi-fi.org/discover-wi-fi)
