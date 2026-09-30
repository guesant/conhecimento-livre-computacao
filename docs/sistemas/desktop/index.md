# Desktop Linux

Um desktop Linux é uma composição, não uma propriedade única da distribuição. A sessão combina um ambiente de desktop, um window manager ou compositor, um toolkit, serviços de sessão, portais, um display manager e aplicações. A distribuição fornece os pacotes e defaults, mas o comportamento percebido depende da combinação instalada.

## Vocabulário

| Termo | Responsabilidade |
| --- | --- |
| Desktop environment, DE | Conjunto integrado de shell, configurações, aplicações e serviços de sessão. |
| Window manager, WM | Organiza janelas e decide foco, posição, tamanho e regras de layout. |
| Compositor | Combina superfícies e produz a imagem final; em Wayland costuma integrar a função de WM. |
| Display manager | Apresenta login e inicia uma sessão gráfica. |
| Toolkit | Biblioteca usada pelas aplicações para widgets e interação visual. |
| Portal | Interface mediada para recursos como arquivos, abertura de URLs e screencast. |

## Ambientes

[Ambientes de desktop](desktop-environments.md) explica a fronteira entre distribuição, DE e sessão. [GNOME](gnome.md) e [KDE Plasma](kde-plasma.md) possuem páginas próprias porque são implementações com arquiteturas, componentes e ciclos distintos.

## Window managers

[Window managers](window-managers.md) compara gerenciadores flutuantes e tiling, além da diferença entre X11 e Wayland. [Tiling](tiling.md) detalha o modelo de organização automática e suas variantes.

## Protocolos e interoperabilidade

[freedesktop.org](freedesktop.md) reúne projetos e especificações de interoperabilidade. [XDG](xdg.md) cobre diretórios de base, arquivos `.desktop` e portais. [Wayland](wayland.md) documenta o protocolo de compositor e clientes. [X11](x11.md) explica o modelo cliente-servidor histórico. [X.Org](xorg.md) descreve a implementação do servidor X11.

## Governança e distribuição

[Fundações e governança](fundacoes-e-governanca.md) explica a diferença entre projeto upstream, entidade legal, patrocinador, mantenedor de distribuição e fornecedor de suporte. Essa distinção é necessária para entender quem decide o código, quem empacota o desktop e quem responde pela instalação usada.

## Relação com systemd e D-Bus

Uma sessão gráfica moderna usa serviços de usuário, sockets, timers, portals e mensagens [D-Bus](../systemd/dbus.md). Isso não significa que o ambiente de desktop seja um conjunto de daemons do systemd: o systemd user manager coordena parte do lifecycle, enquanto o desktop e o compositor continuam sendo componentes separados.

## Fontes primárias

- [GNOME](https://www.gnome.org/about/)
- [KDE Plasma](https://kde.org/plasma-desktop/)
- [freedesktop.org](https://www.freedesktop.org/)
