# Fedora

Fedora é uma distribuição comunitária patrocinada pela Red Hat e organizada pelo Fedora Project. Ela serve como espaço de inovação para tecnologias que depois podem aparecer no ecossistema Red Hat, mas Fedora não é uma edição gratuita de RHEL com o mesmo ciclo ou contrato.

## Edições, spins e variantes

| Variante | Foco |
| --- | --- |
| Fedora Workstation | Estação de trabalho, normalmente com GNOME. |
| Fedora KDE Plasma Desktop | Estação de trabalho com KDE Plasma. |
| Fedora Server | Serviços de servidor e administração. |
| Fedora IoT | Dispositivos e edge com atualização controlada. |
| Fedora CoreOS | Hosts para containers com atualização automática e imutável. |
| Fedora Atomic Desktops | Desktops imutáveis, como Silverblue e Kinoite. |
| Spins | Imagens com outros ambientes, como Xfce, Cinnamon, MATE, LXQt e Budgie. |
| Labs | Imagens orientadas a casos de uso, como ciência, jogos e design. |

Workstation, Server e as imagens Atomic têm objetivos diferentes. Escolher KDE ou Xfce altera a sessão gráfica, mas não transforma a base em outro ciclo de suporte.

## Lançamento e suporte

Fedora publica aproximadamente duas releases por ano. Cada release é mantida até cerca de um mês depois da segunda release subsequente, o que produz uma janela aproximada de treze meses. O calendário exato e o estado de uma release devem ser conferidos na documentação do Fedora.

O suporte principal é comunitário. A Red Hat patrocina infraestrutura e trabalho do projeto, mas uma instalação Fedora não recebe automaticamente o contrato de suporte RHEL. Empresas podem contratar consultoria independente ou optar por RHEL quando precisam do ciclo empresarial e de certificações.

## Bugs e CVEs

O projeto usa Bugzilla, rastreadores e o ecossistema de build e atualização Fedora para testar e promover pacotes. Vulnerabilidades são coordenadas com os mantenedores e publicadas com atualizações de segurança. O ritmo mais rápido traz software recente e também exige acompanhamento mais frequente de regressões.

## Segurança e defaults

Fedora usa SELinux como mecanismo MAC principal e normalmente inicia em enforcing. A política, `firewalld`, systemd e os perfis da edição formam uma baseline, mas uma imagem Atomic ou CoreOS adiciona imutabilidade e atualização transacional.

O servidor SSH não precisa existir em uma Workstation recém-instalada e pode ser habilitado por função. O primeiro usuário administrativo costuma usar `sudo` pelo grupo apropriado. Chaves, login de root, senha e `umask` podem ser alterados por installer, cloud-init ou políticas locais; valide a configuração da imagem em uso.

## Empacotamento

Fedora usa RPM, `dnf` e `rpm`. O código de empacotamento vive em dist-git, builders como Koji produzem os RPMs e Bodhi coordena atualizações, testes e promoção para repositórios. Assinaturas, metadados e o fluxo de promoção permitem separar build experimental de pacote liberado.

O mesmo modelo aparece nas variantes, mas CoreOS e Atomic Desktops entregam uma camada de sistema que é atualizada como imagem ou deployment, não como uma coleção de mudanças manuais arbitrárias.

## Fontes primárias

- [Fedora releases](https://docs.fedoraproject.org/en-US/releases/)
- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Fedora Server](https://fedoraproject.org/server/)
- [Fedora Atomic Desktops](https://fedoraproject.org/atomic-desktops/)
- [Fedora CoreOS](https://fedoraproject.org/coreos/)
