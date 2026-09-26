# CentOS

CentOS exige distinguir duas fases. O CentOS Linux, que reconstruía releases do RHEL depois que elas eram publicadas, foi encerrado. O CentOS Stream é a linha mantida atualmente e funciona como distribuição contínua situada entre o desenvolvimento Fedora e a próxima atualização menor do RHEL.

## CentOS Stream

Stream não é uma LTS tradicional nem uma cópia binária congelada de RHEL. Pacotes entram na linha antes da release menor correspondente do RHEL, permitindo que colaboradores e parceiros validem mudanças com antecedência.

Isso faz do Stream uma opção útil para desenvolvimento, testes de compatibilidade e participação no ecossistema RHEL. Para um servidor que exige o contrato e as certificações de RHEL, a escolha correta continua sendo RHEL.

## Flavors e SIGs

CentOS Stream não possui um catálogo de flavors de desktop comparável ao Ubuntu. Os Special Interest Groups, SIGs, mantêm áreas e composições específicas, mas não devem ser tratados automaticamente como releases com o mesmo suporte do sistema principal.

## Bugs e CVEs

O modelo de Stream faz com que bugs e correções sejam tratados durante a promoção da mudança para a próxima versão menor do RHEL. A comunidade usa listas, fóruns, rastreadores e os canais do projeto CentOS. A política de segurança deve considerar a posição intermediária do Stream e a ausência de um ciclo congelado equivalente ao RHEL.

## Segurança e defaults

CentOS Stream segue a família de segurança do RHEL, incluindo SELinux, systemd e o modelo de serviços RPM. O modo do SELinux, os perfis e a configuração do firewall precisam ser verificados na imagem real.

As imagens normalmente orientam o uso de usuários administrativos, `sudo` ou `wheel` e autenticação SSH por chave, mas cloud images e instalações manuais podem divergir. Não presuma que root, senha, `umask` ou `openssh-server` têm o mesmo estado em todas as imagens Stream.

## Empacotamento

CentOS Stream usa RPM, `dnf` e `rpm`. A linha recebe pacotes e correções que serão validados para futuras atualizações menores do RHEL, com build, testes e promoção no ecossistema CentOS e Red Hat. Os repositórios são assinados e organizados por versão e arquitetura.

CentOS Linux antigo seguia um fluxo de rebuild posterior do RHEL. Esse modelo não deve ser aplicado ao Stream, que é uma linha de desenvolvimento contínuo entre Fedora e RHEL.

## Fontes primárias

- [CentOS Stream](https://www.centos.org/stream/)
- [CentOS Linux end of life](https://www.centos.org/centos-linux-eol/)
- [CentOS](https://www.centos.org/)
