# Distribuições Linux

Uma distribuição Linux combina o kernel Linux com um userland, um sistema de empacotamento, políticas de atualização, instaladores, documentação e uma comunidade. O nome da distribuição não descreve apenas o desktop. Ele também indica como o projeto publica versões, corrige vulnerabilidades e assume responsabilidades de suporte.

## Como comparar distribuições

Há três modelos principais.

| Modelo | Característica | Exemplos |
| --- | --- | --- |
| Versão estável | Um conjunto de pacotes recebe correções durante um ciclo definido. | Debian Stable, Ubuntu LTS, RHEL, Linux Mint |
| Rolling release | O sistema é atualizado continuamente, sem uma grande migração de versão. | Arch, Manjaro, openSUSE Tumbleweed |
| Base estável com componentes móveis | A base muda em ciclos mais longos, enquanto uma camada específica recebe atualizações mais rápidas. | KDE neon, CentOS Stream, openSUSE Leap |

Uma distribuição pode oferecer vários produtos, edições ou ambientes de desktop sem que cada combinação constitua uma distribuição independente. `Kubuntu`, por exemplo, é uma flavor oficial do Ubuntu; `KDE neon` é um projeto separado que usa uma base Ubuntu LTS para entregar o KDE Plasma com maior rapidez.

## Suporte e segurança

Suporte comercial significa que existe uma organização que vende manutenção, consultoria, atualizações estendidas ou um acordo de nível de serviço. Suporte comunitário significa que usuários, mantenedores e voluntários ajudam por fóruns, listas, chats, rastreadores e documentação. Os dois modelos podem coexistir, mas não oferecem a mesma garantia operacional.

Uma correção de CVE também não implica necessariamente uma nova versão do pacote. Distribuições estáveis costumam fazer backport: aplicam a correção a uma versão antiga preservando a interface e o comportamento esperados da release. Distribuições rolling tendem a publicar a versão corrigida do upstream mais rapidamente, mas transferem ao usuário uma parte maior do risco de mudança.

Compare sempre:

- duração do suporte da release;
- quais repositórios recebem correções de segurança;
- quem publica avisos e pacotes corrigidos;
- se há backports ou apenas upgrades completos;
- se a edição escolhida tem suporte comercial;
- como bugs são priorizados e onde devem ser reportados.

## Distribuições e páginas canônicas

- [Ubuntu](ubuntu.md), incluindo flavors oficiais e variantes de desktop.
- [Debian](debian.md), com Stable, Testing, Unstable e o modelo de LTS.
- [openSUSE](opensuse.md), com Leap, Tumbleweed e MicroOS.
- [Red Hat Enterprise Linux](rhel.md), com o ciclo empresarial e seus errata.
- [Fedora](fedora.md), incluindo Workstation, Server, IoT, CoreOS e Atomic Desktops.
- [CentOS](centos.md), distinguindo o CentOS Linux encerrado do CentOS Stream.
- [Manjaro](manjaro.md), com branches Stable, Testing e Unstable.
- [Linux Mint](linux-mint.md), com Cinnamon, MATE, Xfce e LMDE.
- [Alpine Linux](alpine.md), com branches estáveis, Edge e imagens por finalidade.
- [Arch Linux](arch.md), uma distribuição rolling sem flavor oficial de desktop.
- [KDE neon](kde-neon.md), focado em entregar o KDE Plasma atualizado.
- [Kubuntu](kubuntu.md), flavor Ubuntu com KDE Plasma.
- [Governança e distribuição](governanca-e-distribuicao.md), responsabilidades de projetos, empresas, fundações, builders, arquivos e mirrors.
- [Segurança e empacotamento](seguranca-e-empacotamento.md), baseline, MAC, SSH, sudo, umask e supply chain de pacotes.

## Fonte primária

- [The Linux Kernel Archives](https://www.kernel.org/)
- [Ubuntu releases](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)
- [Debian releases](https://www.debian.org/releases)
- [Fedora documentation](https://docs.fedoraproject.org/en-US/releases/)
- [Red Hat errata policy](https://access.redhat.com/support/policy/updates/errata)
