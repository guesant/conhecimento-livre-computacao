# Modelo OSI

O modelo OSI é uma referência conceitual de sete camadas para discutir
responsabilidades de comunicação. Ele não é uma implementação única da
internet, mas fornece vocabulário para localizar uma decisão ou falha.

## Camadas

| Camada | Pergunta |
| --- | --- |
| Física | como bits atravessam o meio |
| Enlace | como quadros chegam ao próximo salto local |
| Rede | como pacotes chegam a outras redes |
| Transporte | como aplicações multiplexam e controlam fluxos |
| Sessão | como uma conversa é estabelecida e mantida |
| Apresentação | como dados são representados ou transformados |
| Aplicação | qual protocolo a aplicação entende |

TCP/IP agrupa as três camadas superiores na aplicação e normalmente combina
física e enlace em acesso à rede. O mapeamento é útil, mas não é uma regra de
que cada protocolo precisa caber perfeitamente em uma camada.

## Diagnóstico

Um problema de camada física pode aparecer como interface sem portadora. Um
problema de enlace pode aparecer como vizinhança ou VLAN. Um problema de rede
pode aparecer como rota. Um problema de transporte pode aparecer como porta
fechada. Um problema de aplicação pode aparecer como resposta HTTP inválida.

Comece pela camada mais baixa que explica o sintoma e avance sem saltar
diretamente para a aplicação. Um timeout não prova que o problema é HTTP.

## Relações

- [TCP/IP](tcp-ip.md) descreve a pilha usada na internet.
- [Interfaces e rotas](../../interfaces-rotas-e-l2-no-linux.md) aplica o modelo no
  Linux.
- [Reverse proxy](../proxy/reverse-proxy.md) opera com informações de aplicação.

## Fontes primárias

- [ISO/IEC 7498-1](https://www.iso.org/standard/14256.html)
- [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)
