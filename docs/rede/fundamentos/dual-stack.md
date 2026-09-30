# Dual stack

Dual stack é a operação simultânea de IPv4 e IPv6 no mesmo host, interface ou
serviço. Não é apenas instalar IPv6: a aplicação, o DNS, o roteamento, o
firewall e a observabilidade precisam operar com as duas famílias.

## Resolução e seleção

Um nome pode ter registros `A` e `AAAA`. O cliente escolhe entre os endereços
conforme sua implementação e a conectividade disponível. Um endereço IPv6
publicado sem rota funcional pode introduzir atrasos antes do fallback para
IPv4, por isso anunciar IPv6 exige testar o caminho completo.

## Operação

As regras de firewall devem cobrir IPv4 e IPv6 explicitamente. Rotas, MTU,
DNS, certificados, logs e métricas também precisam ser verificados nas duas
famílias. Desabilitar IPv6 em uma aplicação não equivale a desabilitá-lo no
host ou no balanceador.

## Transição

Dual stack reduz o risco de migração porque os clientes podem usar a família
que alcançam. O custo é manter duas pilhas e dois conjuntos de failure modes.
NAT64, DNS64 e túneis podem ser necessários quando apenas uma família existe
em parte do caminho, mas são estratégias diferentes de dual stack.

## Continue por aqui

[IPv4](ipv4.md), [IPv6](ipv6.md) e [TCP/IP](tcp-ip.md) explicam os
fundamentos das pilhas. [Modelo OSI](osi.md) fornece o vocabulário de camadas
usado para descrever os pontos da composição.
