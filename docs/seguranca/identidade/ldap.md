# LDAP

Lightweight Directory Access Protocol, LDAP, é um protocolo para consultar e
alterar diretórios de dados hierárquicos. LDAP não é o nome de um banco único
nem de um produto específico. OpenLDAP e 389 Directory Server são
implementações. FreeIPA pode usar um servidor LDAP como parte de uma
composição maior.

## Modelo de diretório

### Directory Information Tree

A Directory Information Tree, DIT, organiza entradas em uma árvore. Cada
entrada possui um distinguished name, DN, formado pelo relative distinguished
name, RDN, da entrada e pela cadeia de seus ancestrais.

Um exemplo conceitual é:

```text
uid=alice,ou=people,dc=example,dc=org
```

O DN identifica a entrada. Ele não deve ser confundido com um login curto,
um nome de exibição ou um identificador que permaneça igual para sempre.

### Entry, attribute e objectClass

Uma entry contém atributos, como `uid`, `cn`, `mail`, `uidNumber` e `member`.
`objectClass` declara quais atributos são obrigatórios e permitidos. O schema
define sintaxe, matching rules, cardinalidade e herança dessas classes.

O diretório costuma armazenar dados de identidade relativamente estáveis e
consultados por filtros. Relações complexas, transações de negócio e grandes
agregações podem exigir outro modelo de persistência.

## Operações LDAP

| Operação | Função |
| --- | --- |
| Bind | Inicia uma sessão e autentica ou estabelece identidade anônima. |
| Search | Consulta entradas por base, escopo e filtro. |
| Compare | Verifica se um atributo possui determinado valor. |
| Add | Cria uma entrada. |
| Modify | Adiciona, substitui ou remove atributos. |
| Modify DN | Move ou renomeia uma entrada. |
| Delete | Remove uma entrada. |
| Unbind | Encerra a sessão. |
| Abandon | Solicita que uma operação em andamento seja abandonada. |

Search usa base DN, `scope`, filtro e atributos solicitados. O escopo pode ser
apenas a entrada base, seus filhos imediatos ou toda a subárvore. Filtros
precisam ser construídos por uma biblioteca que faça escaping correto, nunca
por concatenação de entrada do usuário.

## Bind e autenticação

Simple bind associa uma identidade a uma senha, mas essa senha só deve ser
enviada por uma conexão protegida. SASL permite mecanismos de autenticação e
proteção negociados. Kerberos pode participar de SASL ou de uma composição
FreeIPA, enquanto o diretório continua fornecendo atributos.

Anonymous bind pode ser útil para descoberta limitada, mas deve ser proibido
quando permitir enumeração ou consulta de dados sensíveis. Bind administrativo
deve usar identidade e permissões separadas do serviço que apenas lê atributos.

## TLS

LDAP pode ser protegido com LDAPS, usando TLS desde a abertura da conexão, ou
com StartTLS, negociando TLS sobre uma conexão LDAP existente. A escolha deve
ser suportada por clientes e servidores e acompanhada de validação de
certificado, hostname, autoridade confiável e política de versões.

Criptografar o transporte não concede autorização. ACLs do diretório continuam
determinando quais entradas e atributos o bind pode ler ou modificar.

## Paginação, limites e índices

Diretórios precisam de limites para tamanho de resposta, tempo de busca,
profundidade, número de resultados e concorrência. Simple Paged Results permite
dividir respostas grandes, mas não transforma a consulta em um snapshot
transacional universal.

Índices devem refletir filtros reais, como `uid`, `mail`, DN e membership. Um
filtro não indexado pode consumir CPU e I/O, especialmente quando clientes
tentam enumerar a árvore. Monitore filtros lentos e limite atributos retornados
ao necessário.

## ACL e autorização

ACLs podem controlar operações, entradas e atributos para usuários, grupos,
serviços, redes ou identidades autenticadas. Uma conta de leitura não deve
possuir direito de alterar schema, ACL, grupos privilegiados ou credenciais.

O fato de uma busca retornar um atributo não significa que a aplicação possa
usar esse atributo como autorização. O serviço consumidor deve combinar
identidade, contexto e sua própria política.

## Replicação e referrals

Implementações LDAP podem oferecer replicação, referrals e topologias com
fornecedores múltiplos. Replicação melhora continuidade, mas pode introduzir
conflitos, atraso, divergência de schema e problemas de reconexão.

Uma réplica não substitui backup. Exclusão, corrupção lógica ou alteração de
ACL pode ser propagada para todas as cópias. Teste restauração de dados,
configuração, schema e certificados.

## LDAP como fonte de identidade

LDAP pode ser consumido por aplicações, SSSD, PAM, NSS, servidores de e-mail,
VPNs e provedores de identidade. Cada consumidor define seu bind, filtro,
atributos, cache, política de grupos e tratamento de indisponibilidade.

Não existe um login LDAP universal. Uma aplicação pode usar bind da própria
conta de serviço e comparar a senha do usuário, enquanto outra delega a
autenticação a Kerberos ou a um IdP que consulta LDAP. O modelo de segurança
e o risco de exposição de credenciais são diferentes.

## OpenLDAP, 389 Directory Server e FreeIPA

[OpenLDAP](openldap.md) é uma implementação generalista e exige que a
organização componha autenticação, PKI, DNS e gestão de hosts separadamente.
[389 Directory Server](389-directory-server.md) é outra implementação LDAP,
usada como backend de [FreeIPA](freeipa.md). FreeIPA adiciona Kerberos,
Dogtag, DNS, ferramentas administrativas e integração de clientes.

## Segurança

- Use TLS e valide certificados.
- Evite simple bind sem proteção.
- Desabilite anonymous bind quando não for necessário.
- Use contas de serviço com escopos mínimos.
- Escape filtros, DNs e valores recebidos do usuário.
- Limite buscas e paginação.
- Não permita leitura ampla de hashes, keytabs ou atributos sensíveis.
- Monitore falhas de bind, buscas lentas e alterações administrativas.
- Faça backup e restauração testada, não apenas replicação.

## Fontes

- [RFC 4510, LDAP Technical Specification Road Map](https://www.rfc-editor.org/rfc/rfc4510)
- [RFC 4511, LDAP Protocol](https://www.rfc-editor.org/rfc/rfc4511)
- [RFC 4512, LDAP Models](https://www.rfc-editor.org/rfc/rfc4512)
- [RFC 4513, LDAP Authentication Methods](https://www.rfc-editor.org/rfc/rfc4513)
- [RFC 4515, LDAP Search Filters](https://www.rfc-editor.org/rfc/rfc4515)
- [RFC 4516, LDAP URL](https://www.rfc-editor.org/rfc/rfc4516)

## Continue por aqui

[Autenticação e autorização](fundamentos/index.md) explica a fronteira entre identidade e
permissão. [SSSD](sssd.md) explica o cliente Linux. [MIT Kerberos](kerberos.md)
explica autenticação por tickets.
