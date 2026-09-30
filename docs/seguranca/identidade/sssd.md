# SSSD

SSSD, System Security Services Daemon, é um componente cliente que integra um host Linux a provedores centralizados de identidade e autenticação. Ele pode consumir FreeIPA, Active Directory, 389 Directory Server, OpenLDAP e outros provedores por meio de backends apropriados.

## O que o cliente fornece

Os responders do SSSD atendem consultas locais de NSS e PAM e podem fornecer regras sudo, mapas automount, chaves SSH e decisões de acesso. Os backends consultam os serviços remotos, atualizam o cache e aplicam o provider configurado para identidade, autenticação e autorização.

O SSSD não é um diretório, um KDC ou uma CA. Ele é a camada no host que transforma fontes remotas em serviços locais com uma política de cache e integração com o sistema operacional.

## Cache e modo offline

O cache local pode responder rapidamente a dados já conhecidos. Quando uma entrada está ausente ou expirada, o backend tenta atualizar os dados no provedor remoto. Dependendo da configuração, informações e credenciais de usuários que já autenticaram podem permitir login offline.

Esse comportamento melhora disponibilidade, mas cria uma janela em que uma remoção ou alteração remota ainda não alcançou o host. A política deve considerar tempo de validade, revogação, limpeza do cache e o risco de manter acesso quando o provedor está indisponível.

## Integração

PAM delega autenticação e mudança de senha. NSS permite que aplicações consultem usuários, grupos e outros dados como se fossem fontes locais. A integração Kerberos fornece tickets e SSO; a integração LDAP fornece atributos e regras; a integração IPA combina os dois com descoberta e políticas específicas.

TLS, validação de certificados, descoberta DNS e sincronização de tempo continuam sendo responsabilidades da composição. Instalar SSSD sem testar esses caminhos apenas desloca a falha para o login do host.

## Diagnóstico

Separe falhas de resolução local, consulta ao diretório, obtenção de ticket, autorização PAM e estado do cache. Logs do responder e do backend ajudam a distinguir um usuário inexistente de um provedor indisponível. Limpar o cache pode alterar o comportamento de login e deve ser uma ação deliberada, não um primeiro diagnóstico automático.

## Relações

- [FreeIPA](freeipa.md) é uma solução integrada que usa SSSD nos clientes.
- [OpenLDAP](openldap.md) pode ser consumido pelo provider LDAP.
- [MIT Kerberos](kerberos.md) fornece autenticação baseada em tickets.
- [389 Directory Server](389-directory-server.md) é um provedor LDAP comum em ambientes Linux.

## Fontes primárias

- [Introdução ao SSSD](https://sssd.io/docs/introduction.html)
- [Arquitetura do SSSD](https://sssd.io/docs/architecture.html)
