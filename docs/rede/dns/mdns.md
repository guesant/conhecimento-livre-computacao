# mDNS

Multicast DNS resolve nomes em uma rede local usando multicast, sem exigir um servidor DNS convencional para aquela consulta. É comum em descoberta de dispositivos e serviços em redes locais.

## Casos de uso

mDNS é adequado para descoberta local e ambientes pequenos em que configuração centralizada seria desnecessária. Protocolos de service discovery como DNS-SD podem usar registros DNS sobre esse mecanismo.

## Limites

Multicast normalmente fica restrito ao domínio local de broadcast e não atravessa roteadores por padrão. Isso é propriedade importante, não um defeito a ser corrigido automaticamente.

## Boa prática

Use mDNS quando o escopo realmente é local e a descoberta automática é desejada. Para nomes estáveis de infraestrutura atravessando redes, prefira DNS administrado explicitamente.

## Má prática

Estender multicast indiscriminadamente entre VLANs para "fazer descoberta funcionar" pode aumentar ruído e apagar fronteiras de rede que existiam deliberadamente.

## Fontes

- RFC 6762, Multicast DNS: <https://www.rfc-editor.org/rfc/rfc6762>
- RFC 6763, DNS-Based Service Discovery: <https://www.rfc-editor.org/rfc/rfc6763>

## Continue por aqui

[DNSSEC](dnssec.md) trata autenticidade no DNS hierárquico. [Registro de domínio](registro-de-dominio.md) trata delegação pública.
