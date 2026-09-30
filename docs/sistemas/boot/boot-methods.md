# Métodos de boot

O método de boot descreve de onde o firmware obtém a primeira aplicação ou o primeiro código de inicialização. USB, disco interno, rede, mídia óptica e mídia virtual podem cumprir essa função. O método escolhido depende da disponibilidade do dispositivo, do modo UEFI ou legado, da política de segurança e do objetivo da operação.

O método de boot não é a mesma coisa que a ferramenta usada para preparar a mídia. Rufus, Ventoy, `dd` e balenaEtcher gravam ou organizam uma mídia; eles não definem sozinhos se o firmware a iniciará em UEFI ou em modo legado.

## USB

No boot por USB, o firmware inicializa uma unidade removível. Em modo UEFI, a mídia normalmente contém uma ESP e o caminho removível, como `EFI/BOOT/BOOTX64.EFI`. Em modo legado, a mídia precisa conter código de boot compatível com o fluxo antigo.

USB é adequado para instalação, recuperação, testes e transferência de ferramentas entre máquinas. Ele também aumenta o risco de inicializar um ambiente não autorizado ou de expor dados a uma mídia comprometida. Em máquinas administradas, a política deve controlar a ordem de boot e o uso de dispositivos removíveis.

## Disco interno

O boot pelo HDD ou SSD interno é o caminho persistente de uma instalação normal. Em UEFI, o firmware usa uma entrada NVRAM e uma aplicação na ESP. Em modo legado, ele lê o setor de boot conforme o esquema de particionamento e as convenções do bootloader.

Discos NVMe e SATA aparecem em camadas diferentes para o sistema operacional, mas podem desempenhar o mesmo papel de armazenamento persistente. O diagnóstico deve distinguir falha de detecção do dispositivo, falha de leitura, ausência de entrada de boot, corrupção da ESP e falha do carregador.

## Boot de rede

No boot de rede, o cliente obtém parâmetros de inicialização pela rede e carrega código ou uma imagem de um servidor. PXE tradicional usa DHCP para configuração e TFTP para as primeiras etapas. Implementações modernas podem encadear para iPXE e buscar scripts, kernels ou imagens por HTTP ou HTTPS.

O boot de rede é útil para instalar muitos equipamentos, recuperar hosts sem sistema local e operar ambientes em que o disco não contém uma imagem persistente. Ele depende de DHCP, DNS quando usado, servidor de arquivos, switches e políticas de rede. Um problema em qualquer dependência pode impedir a inicialização de uma frota inteira.

PXE e iPXE não são sinônimos. PXE é um conjunto de mecanismos de pré-boot integrado a muitos firmwares e placas de rede. iPXE é um firmware ou carregador de rede que amplia o fluxo com scripts, HTTP, HTTPS e outros transportes. [Instalação pela rede](network-install.md) detalha a cadeia e inclui as decisões de PXE e iPXE.

## Mídia óptica e mídia virtual

CD e DVD ainda podem ser úteis em recuperação de equipamentos antigos, embora tenham capacidade e velocidade limitadas. A mídia virtual fornecida por um BMC ou por uma console remota apresenta uma ISO ao host como se fosse uma unidade local. Isso é valioso em servidores sem acesso físico, mas depende da rede e da implementação do controlador.

O BMC deve ser tratado como uma fronteira de administração. Credenciais, firmware, isolamento de rede e registro de acesso são tão importantes quanto a imagem usada para boot. Uma ISO de recuperação montada remotamente pode modificar discos com o mesmo poder de uma mídia física.

## Comparação

| Método | Persistência | Dependências principais | Uso comum |
| --- | --- | --- | --- |
| USB | Temporária | Mídia física e firmware | Instalação e recuperação |
| HDD ou SSD interno | Permanente | Disco, ESP ou setor de boot | Sistema instalado |
| Rede PXE ou iPXE | Externa ao host | DHCP, transporte e servidor | Instalação em escala |
| Mídia óptica | Temporária | Unidade e disco óptico | Equipamentos antigos |
| Mídia virtual BMC | Temporária | BMC, rede e console | Servidor remoto |

## Segurança e confiabilidade

Secure Boot deve ser considerado em todos os métodos UEFI. Uma mídia ou carregador encontrado pelo firmware ainda precisa ser autorizado quando a política estiver ativa. Para boot de rede, assinar o carregador é apenas uma parte do problema: a infraestrutura também precisa proteger DHCP, distribuição, integridade das imagens e acesso administrativo.

Para operações repetíveis, registre o modo de boot, a versão da imagem, o checksum, a origem do artefato, o servidor usado e o resultado. Essa informação reduz a ambiguidade quando o mesmo equipamento consegue iniciar por mais de um caminho.

## Fontes primárias

- [UEFI Forum, especificações](https://uefi.org/specifications)
- [iPXE](https://ipxe.org/)
- [Documentação do iPXE](https://ipxe.org/docs)
- [netboot.xyz](https://netboot.xyz/docs/)
- [Documentação do systemd-boot](https://www.freedesktop.org/software/systemd/man/latest/systemd-boot.html)
