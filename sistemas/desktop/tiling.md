# Tiling

Tiling é um modelo de organização no qual as janelas ocupam regiões calculadas pelo gerenciador, normalmente sem sobreposição. O objetivo é manter o espaço previsível e reduzir operações repetitivas de mover e redimensionar.

## Variantes

No tiling manual, o usuário decide para qual contêiner a nova janela vai e pode alterar a árvore. No tiling dinâmico, regras e layouts escolhem automaticamente a distribuição. Alguns compositores oferecem modos híbridos, permitindo alternar entre tiling e janelas flutuantes.

O layout pode ser uma árvore binária, uma grade, colunas, monocle ou uma composição definida por scripts. O modelo escolhido afeta navegação, atalhos e comportamento em múltiplos monitores.

## Benefícios e custos

Tiling favorece teclado, repetibilidade e uso eficiente de telas grandes. Pode ser menos adequado para diálogos irregulares, ferramentas gráficas que esperam sobreposição, apresentações ou usuários que dependem de interação apontar e arrastar. A acessibilidade também precisa ser validada: foco visual e navegação por teclado devem permanecer previsíveis.

## Wayland

Em Wayland, o tiling costuma ser implementado dentro de um compositor, como sway, Hyprland ou niri. Isso reduz algumas ambiguidades do modelo X11, mas vincula o comportamento a protocolos, extensões e recursos suportados pelo compositor.

## Fontes primárias

- [i3 user guide](https://i3wm.org/docs/userguide.html)
- [sway](https://swaywm.org/)
- [Wayland](https://wayland.freedesktop.org/)
