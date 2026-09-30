# Window managers

Um window manager, WM, administra a posição, o tamanho, o foco e as regras das janelas. Ele pode usar um modelo flutuante, em que o usuário move e redimensiona livremente, ou um modelo tiling, em que o espaço é organizado por regras e árvores de layout.

## X11 e Wayland

No X11, o window manager é um cliente especial do servidor X e o compositor pode ser um processo separado. Em Wayland, o compositor é o servidor da sessão e normalmente acumula as responsabilidades de composição, input e organização das superfícies. Por isso, nomes como `sway` e `KWin` podem representar mais do que um WM tradicional.

## Famílias

| Família | Exemplos | Característica |
| --- | --- | --- |
| Floating | KWin, Mutter, Openbox, Fluxbox | Janelas livres e sobreposição. |
| Manual tiling | i3, sway, herbstluftwm | O usuário escolhe a árvore ou o destino do tile. |
| Dynamic tiling | dwm, awesome, xmonad | O WM aplica layouts e regras programáveis. |
| Compositor Wayland | sway, Hyprland, niri | Integra composição, input e gerenciamento de superfícies. |

## Seleção

Avalie suporte ao protocolo gráfico, input, aceleração, acessibilidade, integração com portais, regras de foco, multi-monitor e custo de configuração. Um WM pequeno pode exigir que o usuário componha manualmente serviços que um DE já fornece.

## Relações

- [Tiling](tiling.md) explica o layout automático.
- [Ambientes de desktop](desktop-environments.md) diferencia WM de DE.
- [KDE Plasma](kde-plasma.md) e [GNOME](gnome.md) apresentam WMs integrados a DEs.

## Fontes primárias

- [Wayland architecture](https://wayland.freedesktop.org/docs/html/)
- [X Window System](https://www.x.org/wiki/)
