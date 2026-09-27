# RDAP

Registration Data Access Protocol, RDAP, é um conjunto de serviços HTTP para
consultar dados estruturados de registros de nomes de domínio, endereços IP e
autonomous systems. Ele moderniza o modelo textual do WHOIS com JSON, HTTPS,
redirecionamento e mecanismos de descoberta adequados para automação.

## O que pode ser consultado

Um servidor RDAP pode responder informações sobre domínio, entidade, nameserver,
rede IP e ASN. O resultado possui eventos, status, links, entidades e contatos
conforme a política do registry. Nem todo campo estará disponível: privacidade,
legislação, contratos e regras do registry podem ocultar ou redigir dados.

A resposta também informa referências para outros servidores. Uma consulta pode
começar em um bootstrap service, descobrir o registry responsável e seguir o
link correto. O cliente não deve assumir que um endpoint fixo é autoridade para
todo o espaço de nomes.

## Segurança e uso responsável

RDAP transporta dados de registro, não uma autorização para enumerar pessoas ou
realizar abuso. Clientes devem respeitar rate limits, cachear respostas conforme
as regras do serviço e não expor contatos pessoais em logs ou relatórios. HTTPS
protege a transmissão até o servidor, mas não transforma dados públicos em
dados confiáveis sem validar a autoridade e a data do evento.

Erros de rede, limitação e ausência legítima de dados precisam ser diferenciados.
Um domínio inexistente, um resultado redigido e uma falha do servidor não têm a
mesma consequência operacional. Em automações de segurança, guarde o endpoint
consultado, o momento e a autoridade responsável para que o resultado possa ser
reproduzido.

## WHOIS e RDAP

WHOIS costuma retornar texto com formato variável e parsing frágil. RDAP possui
objetos JSON, nomes de campos e links definidos por especificações, o que facilita
clientes programáticos. Isso não significa que todas as respostas tenham a mesma
semântica: registries podem divergir em extensões, políticas de exposição e
qualidade dos dados.

## Relações

- [Alocação de endereços IP](alocacao-de-enderecos-ip.md) explica registros e blocos.
- [Registros DNS](../dns/records.md) trata resolução, mas não substitui dados de registro.
- [Governança da Internet](index.md) apresenta as organizações responsáveis.

## Fontes primárias

- [RFC 9082, RDAP query format](https://www.rfc-editor.org/rfc/rfc9082)
- [RFC 9083, RDAP JSON responses](https://www.rfc-editor.org/rfc/rfc9083)
- [IANA RDAP bootstrap registry](https://data.iana.org/rdap/)
- [ICANN RDAP](https://www.icann.org/rdap)
