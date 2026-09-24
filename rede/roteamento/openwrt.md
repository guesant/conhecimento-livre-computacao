# OpenWrt

OpenWrt é uma distribuição Linux para roteadores e dispositivos de rede, com pacotes, configuração declarativa por UCI e uma comunidade ampla de hardware suportado. Ele permite substituir o firmware do fabricante por um sistema mais controlável.

## Quando usar

OpenWrt é adequado quando o equipamento suporta a imagem e a necessidade é controlar roteamento, firewall, VLANs, Wi-Fi, VPN ou serviços auxiliares. A capacidade de CPU, memória, armazenamento e aceleração de rede limita o que pode ser executado no dispositivo.

## Segurança e recuperação

Confirme o modelo e a imagem antes de atualizar. Preserve um método de recuperação, mantenha a configuração mínima e restrinja LuCI e SSH às redes administrativas. Um backup de configuração não substitui uma imagem de recuperação nem testa se o equipamento ainda inicia.

## Relações

- [OPNsense](opnsense.md) e [pfSense](pfsense.md) são opções mais orientadas a appliances x86.
- [Netfilter](../../netfilter-nftables-e-diagnostico.md) explica parte da base de filtragem Linux.

## Fonte primária

- [OpenWrt documentation](https://openwrt.org/docs/start)
