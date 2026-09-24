# Modelo TCP/IP

O modelo TCP/IP descreve a pilha prática da internet em camadas de acesso à
rede, internet, transporte e aplicação. Seus protocolos definem interfaces
operacionais entre hosts, redes e aplicações.

## Responsabilidades

A camada de acesso à rede entrega quadros no meio local. A camada internet
endereça e roteia pacotes, principalmente com IPv4 ou IPv6. A camada de
transporte multiplexa aplicações por portas e pode fornecer confiabilidade,
como TCP, ou transporte simples, como UDP. A camada de aplicação define o
protocolo entendido pelo consumidor, como DNS, HTTP ou SSH.

Uma camada pode usar várias tecnologias abaixo dela. HTTP pode operar sobre
TCP ou QUIC, enquanto uma aplicação pode usar UDP diretamente quando prefere
controlar confiabilidade e latência.

## Diagnóstico

Separe falha de resolução de nome, rota, conexão de transporte, negociação
criptográfica e protocolo de aplicação. `dig`, `ip route`, `ss`,
`tcpdump` e `curl -v` respondem perguntas diferentes e devem ser usados
nessa ordem quando o sintoma ainda é ambíguo.

## Relações

- [Modelo OSI](osi.md) fornece o vocabulário de camadas.
- [IPv4](ipv4.md) e [IPv6](ipv6.md) definem endereçamento e entrega.
- [TCP e UDP](../tcp-udp.md) tratam transporte e portas.

## Fontes primárias

- [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)
- [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200)
