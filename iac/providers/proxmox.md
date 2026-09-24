# Provider Proxmox

O provider Proxmox gerencia recursos de virtualização e armazenamento expostos pelo Proxmox VE. Ele pode declarar máquinas virtuais, containers, discos, redes e configurações associadas conforme a versão do provider e da API.

## Cuidados

Prefira tokens de API com escopo limitado e uma conta sem privilégios além dos recursos administrados. O provider não elimina decisões operacionais sobre backup, quorum, storage, migração e disponibilidade do cluster.

## Relações

[Proxmox SDN](../../rede/roteamento/proxmox-sdn.md) trata a rede declarada no próprio Proxmox, enquanto o provider trata a API de gerenciamento de recursos.

## Fonte primária

- [Proxmox provider](https://registry.opentofu.org/providers/bpg/proxmox/latest)
