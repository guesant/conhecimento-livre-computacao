# IPMI

IPMI, Intelligent Platform Management Interface, define interfaces para monitorar e controlar a plataforma por meio de um controlador de gerenciamento separado, normalmente chamado BMC. A especificação cobre sensores, inventário, eventos, energia, console serial e comunicação local ou pela rede.

IPMI gerencia a plataforma, não o sistema operacional. Ele pode indicar que uma ventoinha falhou mesmo quando o Linux não iniciou, mas não conhece a saúde de uma aplicação nem substitui métricas do sistema.

## Modelo de componentes

A plataforma tem um BMC conectado a sensores e controladores internos. O operador acessa esse BMC por um canal local ou remoto:

| Caminho | Nome | Exemplo |
| --- | --- | --- |
| Pelo sistema operacional | In-band | Linux usa um driver e um dispositivo IPMI |
| Pela rede de gerenciamento | Out-of-band | Operador consulta o BMC com o host desligado |
| Pelo console serial | Serial over LAN | Terminal remoto acompanha boot e kernel |

O BMC mantém dados como o Sensor Data Record, que descreve sensores disponíveis, e o System Event Log, que registra eventos de plataforma. Os nomes e a qualidade dos sensores dependem do firmware do fabricante.

## Operações comuns

As operações mais úteis são consultar temperatura, tensão, ventiladores e energia, ler eventos, controlar energia, obter inventário, abrir console serial e escolher o dispositivo de boot seguinte. Atualização de firmware é uma operação do fabricante, não uma consequência automática de usar IPMI.

Comandos de energia têm impacto imediato. Antes de usar uma ação remota, confirme o host, a janela de mudança e a existência de acesso alternativo.

## In-band e out-of-band

O modo in-band depende do sistema operacional, do driver e de permissões locais. É útil para inventário e monitoramento dentro do host, mas deixa de funcionar quando o kernel não carrega ou o computador está desligado.

O modo out-of-band usa a interface de gerenciamento do BMC. Ele tem maior independência operacional, mas precisa de uma rede, credencial e firmware próprios. A perda da rede de gerenciamento não deve deixar o operador sem outra forma de recuperar o host crítico.

## IPMI sobre LAN

IPMI 2.0 introduziu RMCP+, autenticação e recursos de rede mais robustos que as versões anteriores, mas a implementação e a postura de segurança continuam variando. Não exponha UDP 623 publicamente. Restrinja clientes por rede e, quando possível, prefira Redfish para novas automações.

Alguns fabricantes oferecem extensões OEM. Um comando que funciona em um PowerEdge pode não existir em outra placa. Automação portátil deve detectar capacidade, validar resposta e tratar falhas sem assumir que todo sensor está disponível.

## Diagnóstico

Quando uma consulta falha, separe as camadas:

1. O host tem energia e o BMC responde?
2. A rede alcança o endereço de gerenciamento?
3. A conta possui o privilégio necessário?
4. O BMC aceita a versão de autenticação?
5. O sensor ou comando existe nesta plataforma?
6. O firmware possui um problema conhecido?

Teste conectividade sem repetir comandos de energia. Consulte o manual do fabricante para endereço inicial, reset do BMC e recuperação de firmware.

## Segurança operacional

Troque credenciais padrão, aplique atualizações assinadas e registre alterações de configuração. Separe administradores de leitura de sensores de administradores que podem desligar a máquina. Evite reutilizar a senha do sistema operacional no BMC.

O BMC é um domínio de confiança independente. Um comprometimento pode permitir console, mídia virtual, alteração de boot e interrupção física do serviço mesmo que o sistema operacional esteja atualizado.

## Relações

- [OpenIPMI](openipmi.md) explica a integração Linux.
- [FreeIPMI](freeipmi.md) apresenta ferramentas de operação.
- [iDRAC](idrac.md) é uma implementação de fabricante.

## Fontes primárias

- [Intel IPMI](https://www.intel.com/content/www/us/en/products/docs/servers/ipmi/ipmi-home.html)
- [IPMI specification update](https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/ipmi-intelligent-platform-mgt-interface-spec-2nd-gen-v2-0-spec-update.pdf)
- [OpenIPMI introduction](https://openipmi.sourceforge.io/IPMI.pdf)
