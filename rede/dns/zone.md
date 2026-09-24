# Zona DNS

Uma zona é a porção do namespace DNS administrada por um conjunto de servidores
autoritativos. Ela pode corresponder a um domínio inteiro ou a uma parte
delegada separadamente.

## Conteúdo

O SOA descreve a zona e seu serial. NS identifica os servidores autoritativos.
Registros como A, AAAA, CNAME, MX, TXT, SRV e CAA expressam dados diferentes.
O serial participa da sincronização entre autoridade primária e secundária.

Delegação cria uma fronteira: a zona pai aponta para os nameservers da zona
filha, e o servidor da zona filha passa a responder por seus nomes. Um glue
record resolve a dependência quando o endereço do nameserver está dentro do
domínio delegado.

## Operação

Alterar um registro não altera imediatamente todos os clientes. Resolvers
podem manter a resposta até o TTL. Antes de uma migração, reduzir TTL com
antecedência diminui a janela de cache antigo, mas aumenta consultas durante a
mudança.

## Relações

- [Servidor autoritativo](authoritative.md) serve a zona.
- [Registros DNS](records.md) compõem o conteúdo.
- [DNSSEC](dnssec.md) acrescenta autenticidade à zona.

## Fontes primárias

- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
