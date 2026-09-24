# FreeIPA

FreeIPA é uma solução integrada de gerenciamento de identidade e autenticação para ambientes Linux e Unix. Ela combina diretório, autenticação, certificados, DNS, administração e componentes de cliente em uma composição coerente. Não é apenas um banco LDAP nem apenas um servidor Kerberos.

## Composição

| Componente | Responsabilidade | Limite do papel |
| --- | --- | --- |
| 389 Directory Server | Armazenar identidades, políticas, configuração e certificados em LDAP | Não fornece sozinho o SSO Kerberos |
| MIT Kerberos | Emitir tickets para autenticação e acesso a serviços | Não é o diretório de atributos da solução |
| Dogtag | Operar a CA e o ciclo de vida de certificados | Não substitui políticas de acesso ou o KDC |
| BIND | Publicar ou resolver nomes relacionados ao domínio, quando habilitado | DNS não autentica usuários |
| NTP ou chrony | Manter relógios próximos entre clientes e servidores | Sincronização não é autenticação |
| SSSD | Integrar clientes Linux ao provedor de identidade | É um componente de cliente, não o servidor central |

O servidor FreeIPA também oferece ferramentas web e de linha de comando para provisionar hosts, usuários, grupos, regras de acesso e credenciais de serviços. O armazenamento principal é o 389 Directory Server; a autenticação de rede usa o KDC Kerberos; a emissão de certificados pode usar Dogtag.

## Modelo mental

Um usuário ou serviço possui uma identidade no diretório e um principal no realm Kerberos. Um host ingressado recebe configuração e credenciais que permitem localizar os serviços do domínio. O cliente usa SSSD para transformar essas fontes remotas em identidades locais, autenticação PAM, resolução NSS, regras sudo e outras decisões de acesso.

O fluxo de login não deve ser confundido com uma consulta LDAP simples. O LDAP pode fornecer atributos e grupos, enquanto Kerberos prova a posse de uma credencial e emite tickets. O serviço acessado valida o ticket com sua própria chave ou com o KDC, conforme o protocolo integrado.

## DNS e tempo

Descoberta de serviços depende de nomes e registros coerentes. O domínio também precisa de relógios suficientemente próximos para que os tickets não sejam rejeitados por diferença de tempo. Por isso, DNS e sincronização de tempo são dependências operacionais da composição, mesmo quando os administradores percebem apenas uma falha de login.

## Quando usar

FreeIPA é apropriado quando a organização precisa administrar identidades, hosts Linux, SSO, delegação, regras de acesso e certificados de forma integrada. Ele reduz o trabalho de montar manualmente LDAP, Kerberos, CA, DNS e clientes, mas aumenta a responsabilidade de operar a composição e suas dependências.

OpenLDAP com componentes separados pode ser melhor quando o diretório precisa atender aplicações heterogêneas e a organização já possui mecanismos independentes de autenticação, PKI e DNS. FreeIPA também não é uma substituição automática para Active Directory em qualquer cenário; integração, trusts e requisitos de clientes precisam ser avaliados.

## Failure modes

- Diretório indisponível pode impedir consultas novas e alterações administrativas.
- KDC indisponível pode impedir obtenção ou renovação de tickets.
- DNS incorreto pode impedir descoberta dos serviços mesmo com portas abertas.
- Relógio fora da tolerância pode invalidar tickets recém-obtidos.
- CA indisponível pode bloquear novos certificados sem invalidar automaticamente todos os tickets existentes.
- Cache do SSSD pode manter logins anteriores disponíveis e também prolongar a visibilidade de informações desatualizadas, conforme a política configurada.

## Relações

- [Diretório LDAP](openldap.md) separa o protocolo e o modelo de dados da solução integrada.
- [389 Directory Server](389-directory-server.md) é a implementação de diretório usada como backend pelo FreeIPA.
- [MIT Kerberos](kerberos.md) explica tickets, realms e o KDC.
- [Dogtag](../pki/dogtag.md) explica a CA integrada.
- [SSSD](sssd.md) explica o componente que opera nos hosts clientes.

## Fonte primária

- [FreeIPA, About](https://www.freeipa.org/About.html)
