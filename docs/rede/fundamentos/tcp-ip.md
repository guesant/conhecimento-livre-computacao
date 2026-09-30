# Modelo TCP/IP

TCP/IP é a família de protocolos e o modelo prático associado à Internet. Ao
contrário do OSI, ele nasceu de protocolos operacionais e de sua experiência
de implementação. Por isso, suas camadas não precisam ter a simetria das sete
camadas OSI.

Existem duas formas didáticas muito usadas. O modelo de quatro camadas agrupa
o enlace e o meio físico em acesso à rede. O modelo de cinco camadas separa
física e enlace para facilitar o ensino e o diagnóstico. O segundo não é uma
nova pilha de protocolos, apenas uma decomposição mais detalhada da primeira
camada.

## Modelo de quatro camadas

| Camada | Responsabilidade | Exemplos |
| --- | --- | --- |
| Aplicação | protocolos e formatos consumidos por aplicações | HTTP, DNS, SSH, SMTP, TLS e formatos de dados |
| Transporte | comunicação entre processos identificados por portas | TCP, UDP, QUIC e SCTP |
| Internet | endereçamento e encaminhamento entre redes | IPv4, IPv6, ICMP e protocolos de roteamento |
| Acesso à rede | transmissão no enlace e no meio local | Ethernet, Wi-Fi, VLAN, ARP, fibra e rádio |

"Acesso à rede" é um agrupamento. Ele inclui o que o modelo de cinco camadas
separa em enlace e física, mas não significa que Ethernet, Wi-Fi e fibra
tenham a mesma implementação.

## Modelo de cinco camadas

| Camada | Responsabilidade | Exemplos |
| --- | --- | --- |
| Aplicação | significado das operações e representação usada pelo serviço | HTTP, DNS, SSH, JSON, Protobuf e TLS |
| Transporte | multiplexação, entrega, ordem, fluxo e congestionamento | TCP, UDP, QUIC e portas |
| Rede | endereçamento e roteamento entre redes | IPv4, IPv6 e ICMP |
| Enlace | quadros, endereços locais e acesso ao meio | Ethernet, Wi-Fi, VLAN e ARP |
| Física | sinais, símbolos, conectores e propagação | cobre, fibra, rádio e modulação |

O modelo de cinco camadas é útil em aulas e troubleshooting porque permite
separar uma falha de cabo de uma falha de quadros. Em documentos técnicos,
deve-se dizer qual versão do modelo está sendo usada quando "camada 1" ou
"camada 2" puder causar ambiguidade.

## Encapsulamento

Quando uma aplicação envia dados por HTTP sobre TCP e IPv4 em Ethernet, uma
sequência simplificada é:

1. HTTP produz uma mensagem;
2. TCP adiciona portas, números de sequência e controle de transporte;
3. IPv4 adiciona endereços de origem, destino e informações de roteamento;
4. Ethernet adiciona endereços locais e verificação do quadro;
5. a camada física transmite sinais pelo meio.

No receptor, cada camada valida e remove o cabeçalho que lhe pertence antes de
entregar o conteúdo à camada superior. Um roteador normalmente remove o
quadro recebido e cria outro quadro para o próximo enlace, enquanto preserva o
pacote IP, sujeito a alterações como TTL ou Hop Limit. O endereço MAC muda a
cada salto; os endereços IP normalmente identificam os endpoints do caminho.

## Exemplos de pilhas reais

### HTTP/1.1 ou HTTP/2 sobre TLS e TCP

Uma requisição pode usar HTTP sobre TLS, TLS sobre TCP, TCP sobre IPv6 e IPv6
sobre Ethernet ou Wi-Fi. HTTP e TLS são classificados na camada de aplicação
no modelo TCP/IP, embora TLS também exerça uma função de transformação e
proteção associada à apresentação no modelo OSI.

### HTTP/3 sobre QUIC e UDP

HTTP/3 usa QUIC, que é executado sobre UDP. Isso não significa que a aplicação
perdeu confiabilidade: QUIC implementa confiabilidade, multiplexação,
handshake e criptografia em seu próprio protocolo. A separação rígida "UDP é
sempre não confiável" é insuficiente para descrever essa pilha.

### DNS

DNS é um protocolo de aplicação. Consultas podem usar UDP ou TCP e, em
variantes modernas, HTTPS ou TLS. A escolha do transporte não muda a
responsabilidade semântica de DNS.

## Diagnóstico

Separe resolução de nome, rota, vizinhança, conexão de transporte, negociação
criptográfica e protocolo de aplicação. Uma sequência possível é:

1. `dig` ou `resolvectl` para nome;
2. `ip address`, `ip route` e `ip neigh` para endereços, rotas e vizinhança;
3. `ping`, `tracepath` ou `traceroute` para alcance e MTU, reconhecendo que
   ICMP pode ser filtrado;
4. `ss` e `nc` para sockets e portas;
5. `openssl s_client` para uma negociação TLS;
6. `curl -v` ou o cliente específico para o protocolo de aplicação;
7. `tcpdump` para confrontar a hipótese com os pacotes observados.

Uma falha em uma camada superior pode ser consequência de uma inferior, mas
uma resposta de aplicação também pode provar que várias camadas anteriores
funcionaram naquele instante. O diagnóstico deve registrar destino, endereço
resolvido, interface, rota, horário, protocolo e estado da conexão.

## O que o modelo não diz

TCP/IP não determina que toda aplicação use TCP, nem que todo tráfego IP passe
por Ethernet. IPv6 pode usar Wi-Fi, fibra, túnel, enlace celular ou uma
interface virtual. Uma aplicação pode usar UDP, QUIC, SCTP ou um transporte
próprio. Da mesma forma, um protocolo pode combinar funções que o modelo
didático coloca em camadas diferentes.

O modelo também não descreve sozinho autenticação, autorização, observabilidade
ou confiabilidade do serviço. Essas propriedades podem aparecer em TLS, no
protocolo de aplicação, no sistema operacional, no proxy ou no próprio
serviço.

## Relações

- [Modelo OSI](osi.md) fornece o vocabulário de sete camadas.
- [Comparação entre OSI e TCP/IP](comparativo-osi-tcp-ip.md) organiza o
  mapeamento e as diferenças.
- [IPv4](ipv4.md) e [IPv6](ipv6.md) aprofundam a camada Internet.
- [TCP e UDP](../tcp-udp.md) aprofundam a camada de transporte.
- [VLAN](vlan.md) aprofunda uma tecnologia de acesso à rede.

## Fontes primárias

- [RFC 1122, Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122)
- [RFC 8200, IPv6 Specification](https://www.rfc-editor.org/rfc/rfc8200)
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768, User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)
