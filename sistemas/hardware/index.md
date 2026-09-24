# Gerenciamento de hardware e boot remoto

Esta área trata da camada que continua acessível quando o sistema operacional ainda não iniciou ou deixou de responder. O objetivo é separar gerenciamento de plataforma, instalação pela rede e diagnóstico por mídias externas.

[IPMI](ipmi.md) explica o modelo comum de gerenciamento de plataforma. [OpenIPMI](openipmi.md) descreve a integração Linux entre kernel, dispositivo e biblioteca. [FreeIPMI](freeipmi.md) apresenta as ferramentas de linha de comando. [iDRAC](idrac.md) mostra o caso de um BMC Dell.

Essas páginas não substituem o manual da placa ou do fabricante. Sensores, licenças, comandos OEM e nomes de menus variam por modelo.

## Fronteiras

O BMC possui processador, memória, firmware, rede e credenciais próprios. Ele pode continuar ligado quando o processador principal está desligado, desde que a plataforma esteja alimentada. Isso permite diagnóstico de energia e hardware, mas cria uma superfície de administração que precisa ser isolada.

Gerenciamento remoto não é provisionamento completo. Para instalar um sistema operacional em escala, combine acesso de plataforma, boot pela rede, um instalador e uma fonte de configuração. Para recuperar arquivos, use uma mídia de diagnóstico adequada e uma cópia de backup validada.

## Segurança

Coloque a rede de gerenciamento em uma VLAN ou segmento separado, limite origens por firewall e desabilite serviços que não serão usados. Troque credenciais padrão, atualize firmware, registre acessos e evite publicar interfaces BMC diretamente na Internet.

IPMI sobre LAN é um legado útil, mas não deve ser tratado como uma API moderna sem controles compensatórios. Quando o equipamento oferecer Redfish, compare suporte, autenticação, automação e maturidade antes de escolher uma interface nova.

## Relações

- [Instalação pela rede](../boot/network-install.md) explica PXE e iPXE.
- [netboot.xyz](../boot/netboot-xyz.md) apresenta um menu de boot de rede.
- [GParted Live](../boot/gparted-live.md) trata particionamento e recuperação.
- [Hiren's BootCD PE](../boot/hirens-bootcd-pe.md) trata recuperação em Windows PE.
- [MemTest86 e Memtest86+](../boot/memtest.md) trata diagnóstico de memória.

## Fontes primárias

- [Intel IPMI](https://www.intel.com/content/www/us/en/products/docs/servers/ipmi/ipmi-home.html)
- [OpenIPMI](https://openipmi.sourceforge.io/)
- [FreeIPMI](https://www.gnu.org/software/freeipmi/)
- [DMTF Redfish](https://www.dmtf.org/standards/redfish)
