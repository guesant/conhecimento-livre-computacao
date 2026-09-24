# MIT Kerberos

Kerberos é um protocolo de autenticação de rede baseado em criptografia de chave simétrica. MIT Kerberos é uma implementação do protocolo e também o conjunto de ferramentas usado para operar realms, clientes e serviços. A autenticação produz tickets de duração limitada para evitar que a senha seja enviada a cada serviço.

## Modelo mental

O cliente obtém do Key Distribution Center um Ticket-Granting Ticket, conhecido como TGT, após autenticar sua identidade. Depois usa o TGT para obter service tickets destinados a serviços específicos. O serviço valida o ticket e usa as chaves correspondentes para autenticar a comunicação.

Um principal identifica um usuário, host ou serviço dentro de um realm. Um serviço normalmente possui uma identidade própria, frequentemente associada ao nome completo do host. Um keytab guarda chaves de serviço para que um processo se autentique sem solicitar uma senha interativa.

## Dependências

Kerberos depende de DNS coerente para localizar KDCs e serviços, e de relógios próximos para validar o período de cada ticket. Falhas de tempo frequentemente aparecem como erro de autenticação, embora o diretório e a senha estejam corretos.

O protocolo fornece autenticação mútua e pode proteger a comunicação, mas não é um diretório de atributos. Grupos, nomes POSIX, políticas sudo e regras de acesso podem vir de LDAP, FreeIPA, Active Directory ou outra fonte integrada.

## Ciclo de vida

Tickets expiram e podem ser renovados conforme as políticas do realm. O cliente deve proteger o credential cache, destruir tickets quando a sessão terminar e tratar keytabs como credenciais de serviço de alto impacto. Revogar uma conta ou serviço exige considerar tickets já emitidos, chaves persistentes e caches locais.

## Quando usar

Kerberos é apropriado quando vários serviços precisam de autenticação forte, SSO e validação mútua sem repetir senhas. Ele é especialmente útil em domínios centralizados, mas exige operação de KDC, políticas de criptografia, DNS, tempo e distribuição segura de keytabs.

Não use Kerberos como substituto automático para autorização. O fato de um principal ser autenticado não define quais operações ele pode executar no serviço.

## Relações

- [FreeIPA](freeipa.md) integra MIT Kerberos ao diretório, à CA e à gestão de hosts.
- [OpenLDAP](openldap.md) pode fornecer atributos complementares, mas não é o KDC.
- [SSSD](sssd.md) integra Kerberos com PAM, NSS e caches no cliente Linux.
- [NTP e sincronização de tempo](../../sistemas/linux/ntp.md) explica uma dependência operacional crítica.

## Fontes primárias

- [MIT Kerberos](https://web.mit.edu/kerberos/index.html)
- [MIT Kerberos, gerenciamento de tickets](https://web.mit.edu/kerberos/www/krb5-1.22/doc/user/tkt_mgmt.html)
- [RFC 4120](https://www.rfc-editor.org/rfc/rfc4120)
