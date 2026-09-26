# Backbone

Backbone é a camada de transporte de alta capacidade que conecta redes menores, regiões, data centers ou pontos de interconexão. Ele não é sinônimo de Internet inteira, nem precisa pertencer a uma única empresa. A Internet é formada por vários backbones que trocam tráfego por peering e trânsito.

## Componentes

Um backbone costuma combinar fibra óptica, sistemas de transmissão, amplificadores, módulos ópticos, roteadores de núcleo, enlaces redundantes, fontes e sistemas de operação. Em trechos de longa distância, a camada óptica pode transportar muitos canais sobre a mesma fibra; os roteadores IP selecionam caminhos e encaminham pacotes.

## Protocolos e controle

BGP troca informações de alcançabilidade entre sistemas autônomos. Protocolos internos, engenharia de tráfego, RSVP-TE, Segment Routing, MPLS ou mecanismos específicos podem controlar caminhos dentro de uma rede. O protocolo utilizado depende da arquitetura, do fornecedor e dos requisitos operacionais.

O backbone não elimina a necessidade de roteamento e não transforma todos os participantes em uma única rede. Cada sistema autônomo mantém sua política, seus filtros, seus acordos de peering e seus requisitos de segurança.

## Disponibilidade

Alta capacidade não é o mesmo que alta disponibilidade. Um backbone precisa de caminhos alternativos, diversidade física, proteção óptica, redundância de roteadores, controle de congestionamento, telemetria, manutenção planejada e recuperação testada. Dois enlaces que passam pelo mesmo duto podem falhar juntos.

## Backbone e rede de acesso

A rede de acesso conecta clientes e dispositivos. A agregação concentra esses enlaces. O backbone transporta grandes volumes entre pontos de presença e regiões. Uma falha no acesso pode afetar um cliente; uma falha no backbone pode afetar muitas redes e serviços simultaneamente.

## Fontes primárias

- [RFC 4271, BGP-4](https://datatracker.ietf.org/doc/html/rfc4271)
- [RFC 1812, requisitos de roteadores IPv4](https://datatracker.ietf.org/doc/html/rfc1812)
- [IX.br](../conectividade/ixp.md)
