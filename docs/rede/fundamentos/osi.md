# Modelo OSI

O modelo OSI, definido pela ISO/IEC 7498-1, é uma referência conceitual de
sete camadas para discutir sistemas de comunicação. Ele separa
responsabilidades, interfaces e tipos de falha. Não é uma implementação única
da Internet e não exige que cada protocolo real pertença a uma camada isolada.

## Por que existe um modelo em camadas

Uma rede precisa transportar sinais, entregar quadros no enlace local,
encaminhar pacotes entre redes, multiplexar aplicações e interpretar dados.
Se todas essas responsabilidades fossem implementadas como uma única unidade,
uma mudança no meio físico exigiria alterar aplicações e uma mudança no
protocolo de aplicação poderia afetar drivers de rede.

Em um modelo em camadas, cada camada usa serviços da camada inferior e oferece
serviços à camada superior. O emissor encapsula os dados adicionando
informações de controle. O receptor remove essas informações na ordem inversa.
Na prática, as fronteiras podem ser atravessadas por desempenho, segurança,
offload, tunelamento ou evolução do protocolo.

## As sete camadas

| Camada | Responsabilidade | Exemplos e unidade aproximada |
| --- | --- | --- |
| 7. Aplicação | define operações compreendidas por uma aplicação | HTTP, DNS, SMTP, SSH e mensagens de aplicação |
| 6. Apresentação | representa, transforma, comprime ou cifra dados | codificação, serialização, compressão e TLS em uma classificação conceitual |
| 5. Sessão | organiza uma conversa, seus pontos de controle e sua retomada | sessões RPC, diálogo e checkpoints, sem um protocolo universal único |
| 4. Transporte | multiplexa por portas e controla entrega, ordem, fluxo ou congestionamento | TCP, UDP, QUIC e segmentos ou datagramas |
| 3. Rede | endereça e encaminha pacotes entre redes | IPv4, IPv6, ICMP e pacotes |
| 2. Enlace | entrega quadros no enlace local e usa endereços locais | Ethernet, Wi-Fi, VLAN, ARP e quadros |
| 1. Física | transporta sinais, símbolos ou bits pelo meio | cobre, fibra, rádio, modulação e bits |

As camadas 5 e 6 são úteis para raciocínio, mas muitas pilhas da Internet não
possuem componentes separados com esses nomes. TLS pode ser descrito como
apresentação por sua função de transformação e proteção, mas normalmente é
configurado junto da aplicação ou do transporte. Uma biblioteca de sessão pode
ser implementada sobre HTTP, RPC ou um protocolo próprio.

## O que cada camada resolve

### Física

A camada física trata do meio e do sinal: conectores, frequência, voltagem,
potência, modulação, sincronização, largura de banda e taxa de símbolos. Ela
não sabe que um endereço IP existe. Um cabo desconectado, um transceptor
incompatível, interferência de rádio ou perda de sincronização são problemas
que começam aqui.

### Enlace

A camada de enlace organiza a transmissão no domínio local. Ethernet e Wi-Fi
definem quadros, endereços MAC, controle de acesso ao meio e detecção de
erros. VLAN 802.1Q acrescenta identificação lógica a quadros Ethernet. Switches
tomam decisões de encaminhamento principalmente usando informações dessa
camada.

### Rede

A camada de rede permite que um pacote atravesse múltiplos enlaces. IPv4 e
IPv6 fornecem endereçamento e encaminhamento, enquanto roteadores escolhem o
próximo salto. IP é um serviço de melhor esforço: ele não garante entrega,
ordem, ausência de duplicação ou confidencialidade.

### Transporte

A camada de transporte diferencia aplicações por portas e pode oferecer
propriedades adicionais. TCP fornece conexão, ordem, retransmissão, controle
de fluxo e controle de congestionamento. UDP fornece um datagrama simples sem
essas garantias. QUIC implementa transporte confiável e multiplexado sobre
UDP, por isso seu mapeamento escolar para as camadas não é perfeito.

### Sessão

A camada de sessão representa a continuidade de uma conversa: abertura,
manutenção, sincronização, retomada e encerramento. Em algumas arquiteturas
isso é implementado por uma biblioteca ou pelo protocolo de aplicação, e não
por um cabeçalho de rede independente. A ausência de um protocolo chamado
"sessão" não significa que aplicações não mantenham sessões.

### Apresentação

A camada de apresentação trata da forma dos dados. JSON, XML, Protobuf,
UTF-8, compressão e criptografia podem ser discutidos aqui. Na Internet real,
essas funções frequentemente aparecem dentro da aplicação ou de uma biblioteca
como TLS, e uma mesma conexão pode carregar diversas representações.

### Aplicação

A camada de aplicação define o significado das operações. HTTP define
requisições e respostas, DNS define consultas e respostas de nomes, SSH define
um protocolo de acesso remoto e SMTP define transporte de mensagens. A camada
não significa necessariamente o processo final: um proxy, gateway ou
balanceador também pode falar o protocolo de aplicação.

## Diagnóstico orientado pelo modelo

O modelo ajuda a formular perguntas, mas não autoriza conclusões automáticas.
Uma sequência prática pode verificar:

1. sinal, link, interface e erros físicos;
2. vizinhança, VLAN, MAC e entrega no enlace;
3. endereço, rota, MTU e ICMP;
4. socket, porta, handshake, retransmissões e congestionamento;
5. TLS, sessão e autenticação;
6. método, cabeçalhos, payload e resposta da aplicação.

Um timeout pode ser causado por cabo, rota, firewall, transporte, TLS ou
aplicação. Ele não prova que o problema está no HTTP. Ferramentas como
`ethtool`, `ip link`, `ip neigh`, `ip route`, `ss`, `tcpdump` e `curl -v`
respondem a perguntas diferentes.

## Confusões comuns

- MAC é um endereço local do enlace; IP é usado para encaminhamento entre
  redes. Um endereço MAC não substitui uma rota.
- Porta TCP ou UDP identifica um endpoint de transporte; porta de switch é uma
  interface física ou lógica. São conceitos diferentes.
- Switch e roteador não são apenas versões rápidas um do outro. O primeiro
  encaminha principalmente no domínio local; o segundo conecta redes.
- DNS é um protocolo de aplicação, mesmo quando usa UDP. UDP é o transporte.
- HTTPS é HTTP protegido por TLS, não uma oitava camada.
- VLAN separa domínios de camada 2, mas não substitui firewall ou autorização.
- TCP garante propriedades de transporte, não garante que a aplicação aceitou
  ou persistiu os dados.
- TLS protege uma sessão criptográfica, mas não corrige autorização incorreta
  ou um endpoint comprometido.

## Relações

- [TCP/IP](tcp-ip.md) descreve a organização prática mais usada na Internet.
- [Comparação entre OSI e TCP/IP](comparativo-osi-tcp-ip.md) mostra os
  mapeamentos e as diferenças.
- [Interfaces, rotas e camada 2](../../interfaces-rotas-e-l2-no-linux.md)
  aplica parte do modelo no Linux.
- [VLAN](vlan.md) aprofunda uma tecnologia de enlace.

## Fontes primárias

- [ISO/IEC 7498-1](https://www.iso.org/standard/14256.html)
- [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)
