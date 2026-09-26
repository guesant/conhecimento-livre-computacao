# SOCKS5

SOCKS5 é um protocolo de proxy definido pela RFC 1928. Ele transporta conexões TCP e pode negociar resolução de nomes e UDP conforme o método e a implementação. SOCKS5 não é uma sessão remota nem um protocolo de desktop: ele apenas fornece um caminho de proxy para aplicações que sabem usá-lo.

## SSH dynamic forwarding

O OpenSSH pode criar um proxy SOCKS5 local com `ssh -D`. A aplicação aponta para o endereço e a porta locais, e o cliente SSH abre os destinos através do host remoto. Isso é útil para alcançar uma rede privada, validar serviços internos e evitar publicar uma porta.

O túnel não transforma uma aplicação que não entende proxy em uma aplicação compatível. Para uma ferramenta sem suporte SOCKS, use port forwarding explícito, proxy HTTP, VPN ou um gateway apropriado.

## Segurança

O proxy conhece os destinos e pode observar metadados. SOCKS5 não cifra o tráfego até o destino por si só. SSH protege o trecho entre cliente e bastion, mas a aplicação precisa usar TLS ou outro protocolo seguro de ponta a ponta quando o conteúdo exigir confidencialidade.

Restrinja bind local, usuário SSH, destino, duração, forwarding permitido e logs. Um proxy aberto pode virar um relay para abuso ou permitir acesso lateral à rede interna.

## Fonte primária

- [RFC 1928, SOCKS Protocol Version 5](https://www.rfc-editor.org/rfc/rfc1928)
- [OpenSSH manual](https://man.openbsd.org/ssh)
