# SPICE

SPICE, Simple Protocol for Independent Computing Environments, é um protocolo de display remoto voltado principalmente a máquinas virtuais. Ele transporta imagem, input, cursor, áudio, clipboard, USB e outros canais entre um guest e um cliente, normalmente por integração entre QEMU, libvirt e um cliente SPICE.

## Modelo

O servidor é o processo ou dispositivo que possui a sessão gráfica, como QEMU expondo uma VM. O cliente recebe atualizações do display e envia teclado e mouse. Canais separados permitem tratar display, inputs, cursor e dispositivos de forma independente.

SPICE é mais consciente de virtualização que VNC. O guest pode usar drivers virtio e um agente para melhorar resolução, clipboard e integração. O ganho depende da imagem, do driver, do cliente e da latência.

## Segurança

Não exponha um socket SPICE diretamente à internet. Prefira socket Unix local, túnel SSH, VPN ou um gateway autenticado. Quando TCP é necessário, configure TLS, autenticação, firewall e controle de identidade. Acesso ao console de uma VM pode equivaler a acesso físico ao sistema convidado.

## Quando usar

SPICE é adequado para console gráfico de VMs, instalação de sistemas, diagnóstico de boot e interação com guests em um hypervisor. Para acesso recorrente a um desktop físico ou a uma sessão de usuário, VNC, RDP ou uma ferramenta de suporte podem ter integração mais apropriada.

## Fontes primárias

- [SPICE protocol](https://www.spice-space.org/spice-protocol.html)
- [SPICE project](https://www.spice-space.org/)
- [QEMU display documentation](https://www.qemu.org/docs/master/system/display.html)
