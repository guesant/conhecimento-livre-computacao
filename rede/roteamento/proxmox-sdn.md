# Proxmox SDN

Proxmox SDN é o subsistema de rede definida por software do Proxmox VE. Ele modela zonas, VNets e sub-redes para redes virtuais em nós de um cluster, com opções como VLAN, VXLAN e EVPN conforme a versão e a topologia.

## Modelo

Uma zona define a tecnologia e o domínio de alcance. A VNet representa uma rede virtual dentro da zona, e a sub-rede associa endereçamento e gateway. O desenho precisa separar o underlay físico do overlay e definir onde o roteamento, o DHCP e o anúncio de rotas acontecem.

## Quando usar

Proxmox SDN é útil quando múltiplos tenants, redes de laboratório ou overlays precisam ser administrados junto do ciclo de vida das máquinas virtuais. Uma única máquina ou uma rede plana pode não justificar a complexidade operacional.

## Failure modes

MTU inconsistente, VNI duplicada, bridge mal configurada ou dependência de BGP sem vizinhança funcional podem produzir conectividade parcial. Teste o caminho entre nós, o plano de controle e a comunicação de convidados antes de atribuir o problema à aplicação.

## Relações

- [VLAN, VXLAN e EVPN](../../interfaces-rotas-e-l2-no-linux.md) explica os mecanismos de rede.
- [Provider Proxmox](../../iac/providers/proxmox.md) trata automação pela API do Proxmox.

## Fonte primária

- [Proxmox SDN](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#pvesdn_setup)
