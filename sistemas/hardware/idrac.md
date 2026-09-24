# iDRAC

iDRAC, Integrated Dell Remote Access Controller, é o controlador de gerenciamento remoto dos servidores Dell PowerEdge. Ele implementa funções de plataforma relacionadas a energia, inventário, sensores, firmware, console e mídia virtual, com capacidades que dependem da geração e da licença do servidor.

## O que ele oferece

A interface de gerenciamento pode fornecer console remoto de teclado, vídeo e mouse, mídia virtual, ciclo de energia, inventário de hardware e firmware, sensores, eventos e atualização de componentes. As interfaces disponíveis variam entre web, CLI, IPMI e Redfish.

O iDRAC permanece acessível quando o sistema operacional está parado. Isso torna possível instalar um sistema, entrar no firmware ou investigar uma falha de boot sem estar fisicamente diante do servidor.

## Rede e acesso

Configure o iDRAC em uma rede de gerenciamento separada. Defina endereço, gateway, DNS, NTP e controle de acesso antes de expor a interface para operadores. Não publique a interface diretamente na Internet.

O acesso web deve usar HTTPS e credenciais individuais quando o firmware suportar integração com diretório. A CLI pode usar RACADM ou outra ferramenta compatível com a geração do equipamento. IPMI over LAN pode ser útil para compatibilidade, mas não deve ser a única interface de automação considerada.

## Console e mídia virtual

A console virtual transporta teclado e vídeo do servidor para a estação do operador. A mídia virtual faz uma ISO ou dispositivo remoto aparecer para o servidor como mídia de boot. Isso é útil para instalar um sistema operacional, executar uma mídia de recuperação, atualizar firmware e acessar ferramentas quando o disco não inicia.

A mídia virtual pode ser muito mais lenta que uma mídia local ou um boot pela rede. Para instalações repetidas, considere netboot.xyz, PXE, iPXE ou um servidor de instalação local.

## Boot remoto

Uma sequência típica é:

1. acessar o iDRAC;
2. abrir a console virtual;
3. anexar a ISO ou selecionar um dispositivo de boot;
4. reiniciar ou executar um ciclo de energia;
5. acompanhar POST e instalador;
6. remover a mídia virtual depois do uso;
7. confirmar o próximo boot normal.

Confirme que a mídia foi desconectada. Uma ISO esquecida pode fazer o próximo reboot iniciar a recuperação em vez do sistema de produção.

## Licenciamento e geração

Recursos como console e mídia virtual podem depender do modelo, da licença e da versão de firmware. O comportamento de iDRAC6, iDRAC7, iDRAC8 e iDRAC9 não é idêntico. Um procedimento deve declarar o modelo e a versão testados, principalmente quando depende de um viewer específico.

Consulte a documentação Dell da geração correta antes de executar atualização de firmware ou alteração de configuração. Não use um pacote destinado a outro modelo apenas porque o nome comercial é parecido.

## Automação

| Tarefa | Interface possível |
| --- | --- |
| Sensores e eventos legados | IPMI |
| Inventário e ciclo de vida Dell | Redfish ou OpenManage |
| Console e mídia interativa | Interface web e console virtual |
| Alteração pontual em scripts | RACADM, quando suportado |
| Provisionamento em escala | Redfish, PXE e sistema de configuração |

A automação deve validar o identificador do servidor, registrar a ação e tratar a indisponibilidade do BMC. Comandos de energia precisam de confirmação adicional.

## Segurança e diagnóstico

Troque a credencial padrão, atualize firmware, limite a rede de origem e desabilite mídia virtual quando não houver necessidade. Revise usuários locais e privilégios. O BMC deve ser monitorado como um ativo separado do sistema operacional.

Quando o iDRAC não responde, verifique energia de standby, cabo e VLAN de gerenciamento, endereço, certificado, licença, firmware e limite de sessões. Um reset do iDRAC pode interromper console e monitoramento; use-o somente depois de preservar evidências e confirmar o impacto.

## Relações

- [IPMI](ipmi.md) explica o modelo de gerenciamento de plataforma.
- [FreeIPMI](freeipmi.md) acessa implementações compatíveis por CLI.
- [Instalação pela rede](../boot/network-install.md) reduz a dependência de mídia virtual.
- [netboot.xyz](../boot/netboot-xyz.md) oferece um menu de boot pela rede.

## Fontes primárias

- [Dell iDRAC virtual console](https://www.dell.com/support/kbdoc/en-us/000179797/dell-poweredge-idrac-virtual-console)
- [Dell iDRAC user guide](https://dl.dell.com/topicspdf/idrac9-lifecycle-controller-v30-series_users-guide_en-us.pdf)
