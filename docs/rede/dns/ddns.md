# DNS dinâmico

DNS dinâmico, ou DDNS, é a associação de um nome DNS a um endereço IP que
pode mudar. O problema aparece quando um serviço está em uma conexão residencial
ou em outro ambiente sem endereço público estático. Em vez de descobrir o
endereço atual manualmente, um cliente de atualização informa a mudança ao
provedor DNS.

## Como funciona

O fluxo típico é:

1. O roteador ou um agente em um host descobre o endereço público atual.
2. O agente compara esse endereço com o último valor publicado.
3. Quando há mudança, ele autentica uma atualização no serviço DDNS.
4. O servidor autoritativo altera o registro, normalmente um registro `A` ou
   `AAAA`.
5. Resolvers continuam servindo valores antigos até o TTL e os caches
   permitirem a nova resposta.

DDNS não é um protocolo único. Um ambiente pode usar uma API HTTPS do
provedor, um cliente específico, um recurso do roteador ou o mecanismo de
atualização dinâmica definido no DNS. A identidade usada para atualizar o
registro deve ser limitada ao nome e à operação necessários.

## O que o DDNS resolve

O DDNS resolve a descoberta do endereço atual. Ele é adequado para publicar um
nome estável para uma VPN, um laboratório, um servidor doméstico ou um serviço
que já possui uma estratégia segura de exposição.

Ele não resolve automaticamente:

- NAT ou port forwarding;
- CGNAT do provedor de Internet;
- bloqueio de portas de entrada;
- autenticação da aplicação;
- certificado TLS;
- disponibilidade do host;
- propagação imediata em todos os caches;
- mudança de rede sem conectividade com o provedor de atualização.

Quando a conexão está atrás de CGNAT, o cliente pode saber seu endereço
externo, mas não receber conexões de entrada nesse endereço. Nesse caso, é
necessário usar um túnel, uma VPN com ponto público, um relay ou outro desenho
de conectividade.

## TTL e consistência

O registro autoritativo pode ser atualizado rapidamente, mas resolvers
recursivos e clientes podem manter a resposta anterior pelo TTL. Um TTL
menor reduz o tempo de convergência e aumenta consultas ao autoritativo. Um TTL
maior reduz consultas e torna mudanças mais lentas.

Por isso, DDNS não deve ser tratado como um mecanismo de failover instantâneo.
Para alta disponibilidade, considere health checks, múltiplos destinos,
balanceamento, retirada controlada de endpoints e uma política de recuperação.
O DNS pode participar da composição, mas não substitui esses mecanismos.

## Segurança operacional

O cliente de atualização deve usar TLS, armazenar a credencial com permissões
restritas e registrar sucessos e falhas sem vazar o segredo. Prefira uma
credencial com escopo limitado, rotação e revogação. O host não deve aceitar
administração apenas porque seu nome passou a apontar para o endereço correto.

O serviço publicado ainda precisa de firewall, autenticação, autorização,
atualizações, certificados e observabilidade. Se somente uma VPN ou um proxy
de acesso deve alcançar o host, não exponha o serviço diretamente na Internet
apenas para aproveitar o DDNS.

## Relação com certificados

O certificado TLS normalmente é emitido para o nome DNS, não para o endereço
IP que muda. A aplicação precisa responder com esse nome e o cliente precisa
validar a cadeia de confiança. A atualização do registro não renova o
certificado automaticamente, embora ACME e automações de DNS possam ser
combinados com DDNS.

## Fontes

- [RFC 2136, Dynamic Updates in the Domain Name System](https://www.rfc-editor.org/rfc/rfc2136)
- [No-IP, conceito de Dynamic DNS](https://www.noip.com/support/knowledgebase/what-is-dynamic-dns)
- [DNS e registro de domínio](registro-de-dominio.md)
- [Reverse DNS](reverse-dns.md)
- [VPN](../conectividade/vpn.md)
