# Mapa de CIDR e subnetting

Classless Inter-Domain Routing, CIDR, representa uma rede por um endereço e um
prefixo, como `192.168.10.0/24`. O número depois da barra informa quantos bits
identificam a rede. Os bits restantes identificam endereços dentro daquele
prefixo. O mesmo modelo funciona em IPv4 e IPv6, embora o tamanho do endereço e
as regras de uso dos hosts sejam diferentes.

## Máscara e tamanho

Em IPv4, `/24` corresponde à máscara `255.255.255.0`: 24 bits são um e oito
bits são zero. A quantidade total de endereços é `2^(32 - prefixo)`. Em uma
sub-rede tradicional, o endereço de rede e o broadcast não são atribuídos a
hosts, então a quantidade usual de hosts é dois a menos que o total. Prefixos
`/31` e `/32` possuem regras especiais e não devem receber essa subtração
automaticamente.

| Prefixo IPv4 | Máscara | Endereços totais | Hosts usuais |
| --- | --- | ---: | ---: |
| `/24` | `255.255.255.0` | 256 | 254 |
| `/25` | `255.255.255.128` | 128 | 126 |
| `/26` | `255.255.255.192` | 64 | 62 |
| `/27` | `255.255.255.224` | 32 | 30 |
| `/28` | `255.255.255.240` | 16 | 14 |
| `/30` | `255.255.255.252` | 4 | 2 |

Em IPv6, a fórmula de tamanho continua sendo baseada em 128 bits, mas uma
sub-rede comum `/64` tem espaço suficiente para o modelo de autoconfiguração.
Não se deve aplicar a regra de reservar o primeiro e o último endereço como se
IPv6 tivesse broadcast e a mesma convenção de hosts do IPv4.

## Calcular a rede e o broadcast

Para `192.168.10.77/26`, a máscara é `255.255.255.192`. O tamanho do bloco no
último octeto é `256 - 192 = 64`. Os blocos possíveis nesse octeto começam em
0, 64, 128 e 192. O valor 77 está no bloco 64 a 127, então:

| Elemento | Valor |
| --- | --- |
| Endereço informado | `192.168.10.77` |
| Prefixo | `/26` |
| Máscara | `255.255.255.192` |
| Endereço de rede | `192.168.10.64` |
| Primeiro host usual | `192.168.10.65` |
| Último host usual | `192.168.10.126` |
| Broadcast direcionado | `192.168.10.127` |

O cálculo bit a bit faz a mesma coisa: aplica AND entre o endereço e a máscara
para obter a rede e define todos os bits de host como um para obter o
broadcast. O método por tamanho de bloco é mais rápido à mão quando o prefixo
termina no meio de um octeto.

## Dividir uma rede

Dividir `192.168.10.0/24` em quatro redes `/26` empresta dois bits da parte de
hosts. Os intervalos são:

| Sub-rede | Rede | Hosts usuais | Broadcast |
| --- | --- | --- | --- |
| 1 | `192.168.10.0/26` | `.1` a `.62` | `.63` |
| 2 | `192.168.10.64/26` | `.65` a `.126` | `.127` |
| 3 | `192.168.10.128/26` | `.129` a `.190` | `.191` |
| 4 | `192.168.10.192/26` | `.193` a `.254` | `.255` |

Essa divisão pode separar usuários, servidores, gerenciamento e convidados,
mas o prefixo sozinho não cria segurança. É preciso configurar interfaces,
VLANs, gateways, rotas e políticas de firewall. Uma sub-rede pequena também
pode ser usada para um enlace ponto a ponto, mas o prefixo escolhido depende da
tecnologia e da convenção do equipamento.

## Planejamento

Escolha o tamanho pela quantidade atual, crescimento, reservas, sumarização e
domínios de falha. Use prefixos agregáveis quando possível: quatro redes
contíguas `/26` podem ser resumidas no anúncio externo como um `/24`, desde que
as fronteiras administrativas e o roteamento realmente permitam essa
agregação. Evite sobreposição entre redes locais, VPNs, clusters e redes de
provedores, porque a sobreposição torna o roteamento ambíguo.

Para IPv6, planeje primeiro o prefixo delegado, depois atribua um `/64` por
VLAN ou segmento e reserve prefixos maiores para sites, zonas ou ambientes.
Não use endereços globais como se fossem permanentes quando o provedor não
garante delegação estável. ULA pode complementar, mas não substitui um plano
de conectividade IPv6 global.

## Ferramentas e conferência

Ferramentas como `ipcalc` e `sipcalc` podem verificar uma conta, mas não
substituem a documentação do plano de endereçamento. No Linux, confirme o
resultado com `ip address`, `ip route` e `ip -6 route`. Em automação, valide
prefixos, sobreposições e gateways antes de aplicar mudanças.

## Relações

- [IPv4](ipv4.md) explica endereços de 32 bits e classes históricas.
- [IPv6](ipv6.md) explica prefixos de 128 bits e tipos de endereço.
- [Broadcast e multicast](broadcast-multicast.md) explica destinos especiais.
- [Rota](../route.md) explica como o host escolhe o próximo salto.
- [Alocação de endereços IP](../governanca/alocacao-de-enderecos-ip.md) explica
  como obter espaço público.

## Fontes primárias

- [RFC 4632, CIDR](https://www.rfc-editor.org/rfc/rfc4632)
- [RFC 791, IPv4](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 4291, IPv6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291)
- [RFC 6177, IPv6 address assignment to end sites](https://www.rfc-editor.org/rfc/rfc6177)
