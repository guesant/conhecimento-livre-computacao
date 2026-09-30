# OpenLDAP

OpenLDAP é uma implementação de serviços de diretório baseada no protocolo LDAP. O diretório organiza entradas em uma árvore, identificadas por distinguished names, e armazena atributos definidos por um schema. Ele é uma base para identidade e consulta, mas não é automaticamente uma plataforma completa de SSO, PKI, DNS ou administração de hosts.

## Modelo de dados

Uma entrada possui um DN, uma ou mais object classes e atributos. O DN combina o nome relativo da entrada com seus ancestrais na Directory Information Tree. O schema define quais atributos são obrigatórios, quais são permitidos e como os valores devem ser interpretados.

Essa estrutura favorece consultas frequentes, filtros e leitura de dados relativamente estáveis. Ela não deve ser escolhida como substituta direta de um banco relacional para transações complexas, agregações ou relações altamente mutáveis.

## Componentes e operação

O daemon `slapd` atende clientes LDAP e aplica schema, controle de acesso, índices, TLS e plugins. A configuração pode incluir bases locais, referrals e replicação baseada em mecanismos como syncrepl. O diretório precisa de índices coerentes com os filtros mais usados, limites de busca e políticas de tamanho para evitar que uma consulta consuma recursos sem controle.

TLS protege o transporte, mas não define por si só como o cliente autentica nem quais atributos pode ler. SASL e Kerberos podem participar da autenticação, enquanto PAM, NSS e SSSD integram o diretório ao sistema operacional.

## Quando usar

OpenLDAP é adequado quando se precisa de um diretório LDAP generalista, interoperável e controlado diretamente pela organização. É uma escolha natural para aplicações que já falam LDAP e para ambientes que querem montar separadamente diretório, autenticação, CA, DNS e políticas.

Ele é inadequado quando a expectativa é instalar apenas o diretório e obter automaticamente SSO Kerberos, emissão de certificados, descoberta DNS, ingresso de hosts e políticas de acesso. Nesse caso, uma solução integrada como FreeIPA ou uma composição explicitamente documentada pode reduzir lacunas operacionais.

## Segurança e disponibilidade

Desabilitar acesso anônimo quando ele não for necessário, limitar operações por ACL, configurar TLS, restringir buscas e monitorar replicação são responsabilidades do operador. Backups precisam preservar dados, schema, configuração e uma forma testada de restauração.

Replicação melhora disponibilidade de leitura e continuidade, mas introduz topologia, consistência e procedimentos de recuperação próprios. Uma réplica não elimina a necessidade de testar alterações de schema nem de garantir que clientes saibam para onde reconectar.

## Relações

- [FreeIPA](freeipa.md) compõe um diretório com Kerberos, CA, DNS e ferramentas de gestão.
- [389 Directory Server](389-directory-server.md) é outra implementação LDAP, com foco e integração diferentes.
- [SSSD](sssd.md) consome OpenLDAP no host Linux.
- [MIT Kerberos](kerberos.md) pode complementar LDAP com autenticação baseada em tickets.

## Fonte primária

- [OpenLDAP Administrator's Guide](https://www.openldap.org/doc/admin26/)
