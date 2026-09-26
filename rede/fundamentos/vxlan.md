# VXLAN

VXLAN, definido na RFC 7348, encapsula um quadro Ethernet inteiro dentro de
um pacote UDP/IP. Ele permite estender uma rede de camada 2 sobre uma rede de
camada 3 já roteada, sem exigir que os switches intermediários conheçam a
rede virtual transportada.

## VNI e transporte

Cada rede virtual usa um VNI de 24 bits, permitindo muito mais segmentos que
o espaço de VLANs 802.1Q. A porta UDP padronizada pela IANA é 4789. O plano de
controle pode aprender os destinos por flooding ou por mecanismos como EVPN e
BGP, conforme a implementação.

O encapsulamento acrescenta cabeçalhos e reduz o MTU efetivo. A rede física
precisa permitir o tráfego UDP entre os endpoints VXLAN, e o desenho deve
considerar fragmentação, PMTUD e observabilidade do túnel.

## Uso em clusters

O Flannel pode usar VXLAN para transportar tráfego entre Pods em nós
distintos. No K3s, esse backend usa UDP/8472 por compatibilidade histórica,
em vez da porta 4789 normalmente associada ao VXLAN genérico.

Proxmox VE SDN também modela zonas VLAN, VXLAN e EVPN. EVPN combina VXLAN com
BGP para distribuir informações de alcance e oferecer roteamento de camada 3
entre redes virtuais.

## Continue por aqui

[VLAN](vlan.md) trata a segmentação local. [Encapsulamento de CNI](../cni/encapsulamento.md)
mostra como redes de cluster usam túneis para transportar tráfego entre nós.
