# Proxies

Proxy é um intermediário de comunicação. A posição e a responsabilidade do intermediário definem categorias diferentes.

[Forward proxy](forward-proxy.md) atua em nome de clientes. [Reverse proxy](reverse-proxy.md) atua na frente de servidores. Reverse proxies podem aplicar [host-based routing](host-routing.md), [path-based routing](path-routing.md) e, em determinados desenhos TLS, decisões relacionadas a [SNI](../../seguranca/tls/sni.md).

Produtos como Nginx, HAProxy e Traefik implementam subconjuntos e modelos operacionais diferentes e devem ser estudados em páginas próprias quando aprofundados.
