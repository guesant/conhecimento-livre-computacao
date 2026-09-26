# KDE neon

KDE neon é um projeto do KDE que entrega o KDE Plasma e aplicações KDE atualizados sobre uma base Ubuntu LTS. A separação entre a base Ubuntu e os repositórios KDE é a característica central do projeto.

## Edições

| Edição | Papel |
| --- | --- |
| User | Usuários que querem a versão estável mais recente do software KDE. |
| Testing | Pacotes KDE pré-lançamento que ainda precisam de validação. |
| Unstable | Desenvolvimento mais recente, com maior risco de regressões. |
| Developer | Ambiente para desenvolvimento e contribuição ao KDE. |

Testing, Unstable e Developer não devem ser tratados como releases com o mesmo nível de QA da User. A base Ubuntu LTS continua sendo uma camada distinta do ciclo de atualização do KDE.

## Lançamento e suporte

O projeto acompanha a base Ubuntu LTS, mas atualiza o KDE conforme novos lançamentos são publicados. O suporte principal é comunitário e orientado ao KDE. Não há, por padrão, um contrato comercial e um SLA equivalente ao de uma distribuição empresarial; organizações podem contratar suporte externo no ecossistema KDE ou Ubuntu conforme sua necessidade.

## Bugs e CVEs

Bugs do desktop devem ser reportados no sistema de bugs do KDE quando o problema está no Plasma ou em uma aplicação KDE. Falhas da base Ubuntu devem seguir os canais Ubuntu. A separação é importante porque uma atualização do KDE e um aviso de segurança do Ubuntu têm responsáveis e ciclos diferentes.

## Segurança e defaults

A base Ubuntu fornece o baseline de segurança da edição User, incluindo AppArmor quando a imagem o carrega. O KDE Plasma não substitui AppArmor, SELinux, sudo, PAM ou as políticas SSH da base.

A edição desktop normalmente não precisa de SSH server para funcionar. Usuário administrativo, login de root, senha, chaves e `umask` dependem da instalação Ubuntu subjacente e devem ser auditados como em qualquer imagem derivada.

## Empacotamento

KDE neon usa `apt` e `dpkg` para a base Ubuntu e repositórios próprios para os pacotes KDE. O projeto constrói pacotes KDE a partir do código e dos metadados de packaging em sua infraestrutura, publica repositórios APT e atualiza os componentes Plasma com mais rapidez que uma flavor Ubuntu estável.

A confiança final depende de separar pacotes Ubuntu dos pacotes KDE neon, manter os repositórios corretos e validar assinaturas e origem. Misturar PPAs ou pacotes de uma release diferente pode quebrar exatamente a separação que o projeto tenta preservar.

## Fontes primárias

- [KDE neon FAQ](https://neon.kde.org/faq)
- [KDE neon editions](https://neon.kde.org/download/testing)
- [KDE neon development](https://neon.kde.org/develop)
