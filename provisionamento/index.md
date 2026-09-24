# Imagens e provisionamento

Provisionar uma máquina é transformar hardware ou uma VM vazia em um sistema identificável, acessível, atualizado e pronto para receber workloads. Há duas estratégias complementares:

- instalar um sistema por mídia ou rede;
- iniciar uma imagem preparada e aplicar configuração de primeira inicialização.

[Cloud images](cloud-image.md) são discos pré-instalados destinados a plataformas de nuvem e virtualização. [cloud-init](cloud-init.md) lê metadados e user-data para personalizar uma instância. [Foreman](foreman.md) coordena descoberta, boot de rede, templates e inventário de hosts.

## Separação de responsabilidades

Uma imagem deve conter apenas a base que vale para muitas instâncias. Identidade, hostname, chaves SSH, endereço IP, credenciais e dados específicos devem ser aplicados no primeiro boot ou por uma camada de gestão posterior.

A mídia de instalação responde à pergunta de como colocar um sistema no disco. A cloud image responde à pergunta de qual disco inicializar. cloud-init responde à pergunta de como personalizar a instância. Foreman responde à pergunta de como orquestrar a frota, os serviços de boot e o ciclo de vida.

## Escolha

| Cenário | Abordagem |
| --- | --- |
| Uma máquina presencial | USB, ISO ou mídia oficial |
| Muitas máquinas no mesmo ambiente | PXE, iPXE ou Foreman |
| VMs efêmeras | Cloud image e cloud-init |
| Hardware heterogêneo | Foreman com discovery e templates |
| Recuperação de um host | Mídia live ou console BMC |

## Relações

- [Instalação pela rede](../sistemas/boot/network-install.md)
- [netboot.xyz](../sistemas/boot/netboot-xyz.md)
- [Ansible](../ansible.md)
- [OpenTofu](../iac/opentofu.md)

## Fontes primárias

- [cloud-init documentation](https://docs.cloud-init.io/)
- [Ubuntu public images](https://ubuntu.com/docs/public-images/)
- [Foreman documentation](https://docs.theforeman.org/)
