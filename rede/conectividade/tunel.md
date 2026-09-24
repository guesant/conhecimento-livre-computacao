# Túneis de rede

Tunneling encapsula tráfego de um protocolo dentro de outro caminho de transporte. Um túnel pode participar de uma VPN, de acesso reverso, de overlay networking ou de uma solução de administração remota, mas "túnel" e "VPN" não são sinônimos.

## Casos de uso

SSH port forwarding, GRE, encapsulamento de overlays e túneis reversos para publicar um serviço sem aceitar conexão diretamente na borda são exemplos de usos diferentes do mesmo princípio.

## Boa prática

Documente o que é encapsulado, onde o túnel termina e qual propriedade de segurança o transporte fornece. Monitore a dependência do endpoint remoto.

## Má prática

Tratar encapsulamento como criptografia é um erro. Alguns túneis apenas transportam pacotes; confidencialidade e autenticação dependem do protocolo concreto.

## Continue por aqui

[VPN](vpn.md) aplica conectividade privada como objetivo. [Borda](borda.md) contextualiza túneis reversos e gateways.
