# Reverse DNS

Reverse DNS, ou rDNS, resolve um endereço IP para um nome usando registros
PTR. A resolução direta normalmente parte de um nome e procura um registro A
ou AAAA. A resolução reversa parte do endereço e procura uma zona especial
que representa o endereço em ordem reversa.

## Zonas reversas

Para IPv4, um endereço como `192.0.2.10` é consultado como
`10.2.0.192.in-addr.arpa`. Para IPv6, cada nibble hexadecimal aparece em ordem
reversa sob `ip6.arpa`. A autoridade da zona é delegada pelo responsável pelo
bloco de endereços, normalmente um provedor, operador de rede ou organização
que recebeu a delegação.

O proprietário do domínio direto não pode necessariamente criar o PTR. Quem
controla a zona reversa é que precisa publicar o registro ou oferecer uma
interface para o cliente solicitá-lo. Em redes privadas, a organização pode
administrar as zonas reversas internas, como parte do DNS interno.

## Forward-confirmed reverse DNS

Um padrão operacional comum é fazer o PTR apontar para um nome e fazer esse
nome retornar ao mesmo endereço por A ou AAAA. Essa correspondência é chamada
de forward-confirmed reverse DNS. Ela ajuda diagnóstico, logs e políticas que
consultam nomes, mas não transforma DNS em um mecanismo de autenticação.

O nome reverso pode ser inexistente, genérico ou diferente do nome usado por
uma aplicação. Um serviço não deve conceder acesso apenas porque um PTR parece
confiável. Para identidade, use autenticação e autorização apropriadas.

## Usos

- logs de servidores, firewalls, mail relays e ferramentas de diagnóstico;
- identificação operacional de endereços em uma rede;
- validações de reputação e configuração de servidores de e-mail;
- mensagens de erro mais compreensíveis para operadores;
- inventário e correlação de ativos quando o DNS interno é mantido com rigor.

Consultas reversas podem adicionar latência a uma aplicação e podem falhar,
ser bloqueadas ou retornar resultados desatualizados. Logs de alto volume
devem considerar cache, timeout e a possibilidade de registrar o endereço sem
esperar pelo rDNS.

## Diagnóstico

Use `dig -x 192.0.2.10` para consultar IPv4 ou informe diretamente um nome sob
`ip6.arpa` para IPv6. Compare o resolver usado pelo host com o servidor
autoritativo e observe TTL, autoridade, NXDOMAIN, timeout e resposta vazia.
Em e-mail, verifique PTR, A, AAAA, HELO, SPF, DKIM, DMARC e a reputação do
endereço como propriedades separadas.

## Relações

- [Registros DNS](records.md) explica o tipo PTR.
- [Servidor autoritativo](authoritative.md) publica a zona reversa.
- [Resolver](resolver.md) responde consultas e mantém cache.
- [DNSSEC](dnssec.md) pode autenticar dados DNS quando a cadeia está validada.

## Fontes primárias

- [RFC 1034, Domain Names](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035, Domain Names implementation](https://www.rfc-editor.org/rfc/rfc1035)
- [RFC 1912, Common DNS operational errors](https://www.rfc-editor.org/rfc/rfc1912)
- [RFC 6303, Locally served DNS zones](https://www.rfc-editor.org/rfc/rfc6303)
