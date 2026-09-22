# VPN

Uma Virtual Private Network cria conectividade lógica protegida sobre uma rede subjacente que não precisa ser confiável. Dependendo da tecnologia, ela pode conectar hosts individuais, redes inteiras ou ambos.

## Casos de uso

Acesso remoto de operadores, conexão site-to-site e exposição de serviços apenas a participantes autorizados são casos comuns. WireGuard, IPsec, OpenVPN e redes overlay oferecem modelos diferentes.

## Boa prática

Defina claramente quais prefixes devem atravessar a VPN, como identidade é estabelecida, como chaves são rotacionadas e qual DNS será usado. Prefira least privilege também na camada de rede.

## Má prática

Enviar todo tráfego por um exit node sem necessidade aumenta dependência e superfície operacional. Também é inadequado usar "estar na VPN" como única autorização para aplicações sensíveis quando identidade e autorização de aplicação são necessárias.

## Continue por aqui

[Túneis](tunel.md) são um mecanismo mais geral. [Borda de rede](borda.md) explica onde políticas e conectividade externa se encontram.