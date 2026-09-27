# Proxies

Proxy é um intermediário de comunicação. A posição e a responsabilidade do intermediário definem categorias diferentes.

[Forward proxy](forward-proxy.md) atua em nome de clientes. [Reverse proxy](reverse-proxy.md) atua na frente de servidores. Reverse proxies podem aplicar [host-based routing](host-routing.md), [path-based routing](path-routing.md) e, em determinados desenhos TLS, decisões relacionadas a [SNI](../../seguranca/tls/sni.md).

Produtos como Nginx, HAProxy e Traefik implementam subconjuntos e modelos operacionais
diferentes. [HAProxy](haproxy.md) detalha seus frontends, backends, health checks,
balanceamento e modos TCP e HTTP.

[PROXY protocol](proxy-protocol.md) preserva metadados de uma conexão TCP entre
intermediários. [Nginx com PROXY protocol](nginx-proxy-protocol.md) mostra como
receber essa informação, restringir as origens e encaminhar o tráfego sem aceitar
endereços forjados.

## Escolha por posição no fluxo

A primeira pergunta não é qual produto instalar, mas onde o intermediário fica e
qual protocolo ele realmente enxerga. Um forward proxy representa clientes para
destinos externos. Um reverse proxy representa servidores para clientes. Um
balanceador pode distribuir conexões sem entender HTTP ou tomar decisões por
host e caminho. Um gateway de aplicação pode acrescentar autenticação, rate
limit e transformação, mas passa a ser parte do domínio de segurança.

Terminar TLS muda a fronteira. O componente que termina o handshake pode validar
certificados, ler SNI e HTTP e produzir headers para o upstream. Um proxy em
pass-through preserva o TLS até o próximo salto, mas não consegue aplicar regras
de aplicação sem outra camada. PROXY protocol resolve a preservação do endereço
de conexão entre os saltos, mas não transforma o intermediário em uma autoridade
de identidade.

## Contrato mínimo entre saltos

Para cada rota, documente:

1. protocolo recebido e protocolo enviado;
2. onde TLS termina e qual trust store é usado;
3. como o endereço original é preservado;
4. quais headers ou TLVs são reescritos;
5. quais redes podem alcançar o próximo salto;
6. como health checks e drenagem usam o mesmo contrato;
7. qual componente autoriza a identidade do cliente.

Sem esse contrato, uma configuração aparentemente pequena pode produzir IPs
forjáveis nos logs, um health check incompatível ou um backend que recebe TLS
onde esperava HTTP.
