# Wake-on-LAN

Wake-on-LAN, normalmente abreviado como WoL, é um mecanismo para acordar um computador que está desligado em um estado no qual a placa de rede continua energizada. O mecanismo depende da placa de rede, do firmware, da alimentação elétrica e do caminho de rede. Ele não inicializa um sistema que está mecanicamente sem energia e não substitui uma interface de gerenciamento fora de banda, como IPMI ou Redfish.

## Modelo de funcionamento

Durante o estado de baixo consumo, a interface de rede mantém uma parte mínima do circuito ativa e observa os quadros recebidos. Quando reconhece um padrão de ativação, sinaliza a placa-mãe para sair do estado de energia suportado pela plataforma. A sequência exata depende da implementação do firmware, da NIC, da configuração ACPI e do sistema operacional.

O padrão mais comum é o magic packet. Ele contém seis bytes `FF` seguidos por dezesseis repetições do endereço MAC da interface que deve acordar. O pacote costuma ser enviado por UDP para as portas 7 ou 9, mas essas portas são uma convenção de ferramentas. O requisito essencial é que o quadro ou pacote alcance a interface no domínio de rede esperado.

O WoL pode funcionar com um endereço unicast conhecido, com broadcast dirigido ou com uma retransmissão feita por um equipamento na rede local. Roteadores normalmente não encaminham broadcasts entre sub-redes por padrão. Por isso, acordar um host a partir de outra VLAN exige um relay controlado, uma regra específica ou um agente dentro da rede de destino.

## Pré-requisitos

O diagnóstico deve separar quatro camadas que frequentemente são confundidas:

1. A fonte e a placa-mãe precisam fornecer energia em um estado compatível com WoL.
2. O BIOS ou UEFI precisa permitir acordar pela rede, PCIe ou pela interface correspondente.
3. O driver precisa manter o recurso habilitado quando o sistema desliga ou suspende.
4. O switch, a VLAN e o caminho entre emissor e receptor precisam entregar o pacote.

No Linux, `ethtool` permite consultar e alterar capacidades do driver quando o hardware oferece suporte. Uma saída com `Wake-on: g` indica que o modo de magic packet está habilitado; uma saída com `Wake-on: d` indica que está desabilitado. A configuração pode ser perdida durante o desligamento ou a atualização do driver, portanto a persistência deve ser configurada pelo mecanismo de rede adotado pelo sistema.

Antes de testar, registre o MAC correto da interface, confirme que a máquina ainda recebe energia em estado desligado e verifique se o switch mantém a associação necessária. Em notebooks, estados modernos de suspensão, docking stations, economia de energia e políticas do fabricante podem restringir o comportamento.

## Operação e diagnóstico

Uma sequência mínima de diagnóstico é:

1. confirmar no sistema ligado a interface e o MAC com `ip link`;
2. consultar a capacidade com `ethtool <interface>`;
3. habilitar o modo suportado, se necessário, com `ethtool -s <interface> wol g`;
4. desligar a máquina pelo estado que será testado;
5. enviar o magic packet a partir da mesma rede local;
6. observar a tabela MAC do switch e capturar tráfego no segmento quando o teste falhar.

Ferramentas como `wakeonlan` e `etherwake` geram o pacote. O teste deve ser feito primeiro no mesmo domínio de broadcast, porque isso elimina roteamento, ACLs e relay como variáveis. Depois, cada VLAN ou rede remota deve ser testada com o mecanismo de retransmissão escolhido.

Uma falha antes de o pacote chegar ao segmento aponta para roteamento, firewall, broadcast ou switch. Um pacote observado no segmento sem despertar o host aponta para alimentação, firmware, driver, estado ACPI ou MAC incorreto. A captura precisa ser feita em um ponto que realmente veja o tráfego, pois o host desligado não poderá confirmar o recebimento por logs comuns.

## Segurança

O magic packet não é uma credencial forte. Em sua forma comum, qualquer pessoa que conheça o MAC e tenha alcance ao segmento pode tentar acordar a máquina. Não exponha UDP de WoL diretamente à Internet. Prefira VPN, bastion, relay autenticado ou um agente dentro da rede de gerenciamento.

Separe a capacidade de acordar da capacidade de administrar o host. O WoL pode ser liberado para uma automação com escopo restrito, enquanto IPMI, Redfish, SSH ou o painel de virtualização exigem autenticação, autorização, registro e uma rede de gerenciamento isolada. Registre quem solicitou a ativação e limite tentativas para evitar abuso ou acionamento repetitivo.

## WoL, IPMI e Redfish

WoL resolve uma única transição: pedir que um host energizado parcialmente inicie. Ele não informa de forma confiável o estado do sistema, não monta uma mídia, não altera a sequência de boot e não oferece console. IPMI e Redfish operam em um controlador de gerenciamento separado e podem fornecer energia, sensores, console e boot remoto, conforme o hardware.

Em um servidor com BMC, WoL costuma ser útil como mecanismo simples ou redundante, mas não deve ser tratado como substituto do BMC. Em um computador de uso geral, ele pode ser suficiente quando o objetivo é iniciar um agente, acessar arquivos ou reduzir o consumo fora do horário de uso.

## Fontes

- [Documentação do kernel Linux sobre Wake-on-LAN](https://docs.kernel.org/networking/device_drivers/ethernet/wol.html)
- [Manual do ethtool](https://man7.org/linux/man-pages/man8/ethtool.8.html)
- [Wake-on-LAN, visão geral](https://en.wikipedia.org/wiki/Wake-on-LAN)
- [IPMI](ipmi.md)
- [iDRAC](idrac.md)
