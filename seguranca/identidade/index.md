# Identidade e diretórios

Gerenciamento de identidade combina um diretório de informações, um protocolo de autenticação, políticas de autorização, nomes de serviço, tempo confiável e, em alguns ambientes, uma autoridade certificadora. Esses papéis se relacionam, mas não são a mesma coisa.

Um servidor LDAP organiza entradas hierárquicas e atributos. Kerberos autentica usuários, hosts e serviços por meio de tickets. Uma CA emite identidades criptográficas. DNS permite localizar serviços e o tempo sincronizado mantém válidas as janelas de expiração dos tickets. No cliente Linux, o SSSD integra essas fontes ao NSS, PAM e outros consumidores locais.

## Escolha da composição

[FreeIPA](freeipa.md) oferece uma composição integrada para identidade e administração de hosts Linux. [OpenLDAP](openldap.md) é uma opção de diretório LDAP generalista que exige a composição dos mecanismos restantes. [389 Directory Server](389-directory-server.md) é uma implementação de servidor LDAP, usada também como armazenamento principal pelo FreeIPA. [MIT Kerberos](kerberos.md) implementa o protocolo de autenticação e SSO. [SSSD](sssd.md) é o componente cliente que conecta o host a essas fontes.

Quando uma instalação precisa apenas publicar atributos consultáveis, um diretório LDAP pode ser suficiente. Quando precisa de login centralizado, SSO, regras de acesso a hosts, certificados e descoberta de serviços, a decisão deve considerar a composição inteira e não apenas o produto que armazena os usuários.

## Dependências e domínios de falha

O diretório não substitui o KDC, e o KDC não substitui o diretório. DNS incorreto pode impedir descoberta de serviços mesmo quando o diretório está saudável. Relógios divergentes podem invalidar tickets ainda que usuário e senha estejam corretos. Uma CA indisponível pode impedir novas emissões sem necessariamente impedir autenticações já baseadas em tickets válidos.

SSSD reduz a dependência de disponibilidade imediata com caches locais, mas não transforma dados antigos em política atualizada. A duração do cache, o comportamento offline e a revogação precisam ser tratados como decisões de segurança.

## Relações

- [DNS autoritativo](../../rede/dns/authoritative.md) explica a função do serviço de nomes.
- [BIND](../../rede/dns/bind.md) documenta uma implementação de DNS usada em várias composições.
- [NTP e sincronização de tempo](../../sistemas/linux/ntp.md) explica a dependência temporal.
- [Dogtag](../pki/dogtag.md) documenta a CA integrada ao FreeIPA.
- [SOPS keyservice](../secrets/sops-keyservice.md) trata distribuição de operações de chave para outro contexto, que não é um diretório de usuários.

## Fontes primárias

- [FreeIPA, About](https://www.freeipa.org/About.html)
- [RFC 4120, Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120)
