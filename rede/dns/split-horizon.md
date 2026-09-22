# Split-horizon DNS

Split-horizon DNS fornece respostas diferentes para o mesmo nome conforme a visão ou origem da consulta.

## Caso de uso

Um nome administrativo pode resolver para endereço interno para clientes conectados à rede privada e não existir, ou resolver diferentemente, para a Internet pública.

## Trade-off

O padrão reduz exposição e mantém nomes estáveis, mas cria múltiplas visões de DNS que precisam ser diagnosticadas e documentadas.

Split-horizon não é reverse proxy. DNS escolhe resolução de nome; [reverse proxy](../proxy/reverse-proxy.md) escolhe backend depois que a conexão chega ao intermediário.