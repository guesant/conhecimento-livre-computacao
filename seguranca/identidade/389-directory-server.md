# 389 Directory Server

389 Directory Server é um servidor LDAP de alto desempenho para armazenar e consultar diretórios hierárquicos. Ele possui frontend de protocolo, plugins de funções do servidor, controle de acesso, replicação e um backend persistente indexado e transacional. No FreeIPA, ele atua como o armazenamento principal de identidades, políticas, configuração e certificados.

## Arquitetura

O frontend recebe operações LDAP por TCP/IP e pode protegê-las com TLS. O backend organiza os dados da árvore do diretório, executa buscas usando índices, mantém caches e trata persistência, recuperação e locking. Plugins implementam funções como controle de acesso, replicação e políticas específicas.

A Directory Information Tree possui sufixos e entradas de configuração. O conteúdo de usuários e grupos não deve ser confundido com a configuração interna do servidor. A separação é importante para backup, replicação, autorização e diagnóstico.

## Replicação

O projeto suporta topologias com múltiplos fornecedores e consumidores. A escolha entre uma réplica gravável, uma cópia somente leitura e uma topologia intermediária afeta resolução de conflitos, failover e operação de escrita. Replicação não substitui backup: ela pode propagar exclusões ou corrupção lógica.

## Segurança

O acesso deve ser fechado por padrão e liberado por ACIs coerentes com a árvore. TLS protege credenciais e atributos durante o transporte. Limites de busca, índices, limites de recursos e monitoramento de logs reduzem o risco de consultas abusivas e de degradação do serviço.

## Relação com FreeIPA

389 Directory Server é uma implementação de diretório e não, isoladamente, um sistema completo de gerenciamento de identidade. FreeIPA acrescenta Kerberos, Dogtag, DNS, administração e integração por SSSD. Em uma instalação independente, os mecanismos de autenticação, PKI, descoberta e política precisam ser especificados separadamente.

## Quando usar

Use 389 Directory Server quando LDAP for o modelo de integração adequado e houver necessidade de um servidor especializado com índices, plugins, ACLs e replicação. Use uma solução mais integrada quando o problema principal for administrar todo o ciclo de identidade Linux, e não apenas operar o diretório.

## Relações

- [FreeIPA](freeipa.md) usa o 389 Directory Server como backend de identidade.
- [OpenLDAP](openldap.md) implementa o mesmo protocolo com arquitetura e operação diferentes.
- [SSSD](sssd.md) fornece a integração do host cliente.
- [LDAP autoritativo e resolução DNS](../../rede/dns/authoritative.md) e [BIND](../../rede/dns/bind.md) cobrem serviços de nomes que podem acompanhar uma composição de identidade.

## Fontes primárias

- [Arquitetura do 389 Directory Server](https://www.port389.org/docs/389ds/design/architecture)
- [Introdução ao 389 Directory Server](https://www.port389.org/docs/389ds/FAQ/getting-started.html)
