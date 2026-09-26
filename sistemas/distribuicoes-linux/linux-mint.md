# Linux Mint

Linux Mint é uma distribuição orientada a desktop, baseada principalmente no Ubuntu LTS. Ela também mantém LMDE, Linux Mint Debian Edition, que usa Debian como base para reduzir a dependência do Ubuntu e preservar uma alternativa dentro do projeto.

## Flavors

| Flavor | Característica |
| --- | --- |
| Cinnamon | Desktop principal do projeto, integrado ao ecossistema Mint. |
| MATE | Interface tradicional e leve. |
| Xfce | Interface mais leve para hardware modesto. |
| LMDE | Edição baseada diretamente no Debian, normalmente com Cinnamon. |

As flavors Cinnamon, MATE e Xfce compartilham a orientação de desktop, mas diferem em consumo, componentes e defaults. LMDE não é apenas outro tema: tem uma distribuição base diferente e acompanha as políticas do Debian.

## Lançamento e suporte

As releases principais seguem a base Ubuntu LTS e tradicionalmente recebem cinco anos de suporte. O ciclo exato, a base e o estado de cada release devem ser conferidos na página de versões do projeto. O suporte é comunitário, financiado por doações e serviços associados ao projeto, sem um SLA empresarial padrão equivalente ao de uma subscrição RHEL.

## Bugs e CVEs

Falhas podem estar no Mint, na base Ubuntu, na base Debian ou no desktop upstream. O diagnóstico deve identificar a camada antes do reporte. Atualizações de segurança são distribuídas pelos repositórios correspondentes e podem incluir backports. Pacotes de terceiros e PPAs ficam fora da mesma política de validação.

## Segurança e defaults

Nas edições baseadas em Ubuntu, Linux Mint aproveita AppArmor e os mecanismos de segurança da base. LMDE segue a base Debian e pode ter diferenças de pacote, perfil e ativação. SELinux não é o mecanismo MAC padrão do Mint.

O desktop cria um usuário normal e normalmente oferece `sudo` para tarefas administrativas. SSH server não faz parte da experiência desktop mínima por obrigação. Login de root, autenticação SSH e `umask` variam com a imagem e devem ser conferidos antes de transformar uma estação em servidor.

## Empacotamento

Mint usa `apt` e `dpkg` para a base e distribui pacotes `.deb` pelos repositórios Ubuntu, Debian e Mint correspondentes. Pacotes próprios são construídos pela infraestrutura do projeto e publicados em seus repositórios; pacotes da base são construídos e assinados pelas equipes Ubuntu ou Debian.

PPAs, Flatpak e repositórios externos ampliam as opções, mas criam ciclos de atualização e confiança separados. A política deve registrar quem constrói cada artefato e quem assina o repositório consumido.

## Fontes primárias

- [Linux Mint FAQ](https://www.linuxmint.com/faq.php)
- [Linux Mint all versions](https://linuxmint.com/download_all.php)
- [Linux Mint downloads](https://www.linuxmint.com/download.php)
- [LMDE](https://www.linuxmint.com/lmde.php)
