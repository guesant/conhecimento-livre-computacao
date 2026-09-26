# Conectividade WAN

Toda resolução DNS pressupõe que o host já alcança a internet. Antes de
configurar o DNS, o roteador de borda precisa obter um endereço público e
manter uma forma estável de ser alcançado.

## Como o endereço é obtido

PPPoE, definido na RFC 2516, autentica o assinante com credenciais do
provedor antes de entregar o endereço. DHCP, definido na RFC 2131, entrega
endereço, máscara, gateway e DNS sem exigir credencial na camada de enlace do
cliente. O terceiro modelo é um endereço estático, atribuído
contratualmente ou reservado pelo provedor.

PPPoE e DHCP podem mudar o endereço após reconexões. Sempre que um serviço
precisa ser alcançado diretamente de fora, essa instabilidade exige DDNS ou
alguma camada de exposição que não dependa do endereço público. Um prefixo
IPv6 delegado por DHCPv6-PD produz o mesmo problema em escala de bloco.

Um ULA IPv6, um registro DNS atualizado dinamicamente ou um túnel pode
remover a dependência do endereço público estável. Um túnel de exposição
continua funcionando mesmo quando o endereço do lado exposto muda.

## Camada física

SFP+ é um padrão de transceptor usado em uplinks de 10 Gigabit Ethernet. Ele
aparece em roteadores e switches de borda quando a velocidade do provedor
excede o que uma porta Gigabit comum suporta. O transceptor não escolhe o
método de endereçamento, PPPoE, DHCP ou endereço estático; ele apenas fornece
o meio físico.

## Continue por aqui

[Roteadores de borda](borda.md) trata os appliances e [túneis](tunel.md)
trata a exposição que não depende do IP público.
