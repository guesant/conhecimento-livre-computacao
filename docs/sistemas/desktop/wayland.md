# Wayland

Wayland é um protocolo para comunicação entre clientes gráficos e um compositor. Também existe uma biblioteca de referência do protocolo, mas Wayland não é um desktop environment, um window manager completo ou um servidor monolítico equivalente ao Xorg.

## Modelo

Um cliente Wayland cria surfaces e fornece buffers com o conteúdo que deseja exibir. O compositor recebe esses buffers, trata entrada, composição, posição, foco, saída e apresentação final. O cliente não conhece necessariamente a posição global de sua surface nem acessa diretamente as surfaces de outros clientes.

O compositor normalmente integra funções que no X11 podiam estar separadas, como window manager, composição, controle de telas, input, lock screen e integração com o desktop. Exemplos de compositores são Mutter, KWin, Sway e Weston, mas o protocolo não exige um compositor específico.

## Segurança e isolamento

O modelo restringe o acesso direto de um cliente às janelas e entradas de outros clientes. Isso facilita uma fronteira de segurança mais clara para captura de tela, injeção de teclado, clipboard e screencast, normalmente complementada por portais e políticas da sessão.

Isso não torna toda sessão automaticamente segura. O compositor, extensões, portais, permissões, aplicações e componentes privilegiados continuam fazendo parte do domínio de confiança.

## Renderização

Wayland não define sozinho toda a pilha gráfica. O compositor pode usar kernel modesetting, DRM, evdev, EGL, OpenGL, Vulkan, Mesa, aceleração de hardware e protocolos auxiliares. Clientes podem renderizar com toolkit, shared memory ou buffers gráficos apropriados.

## Compatibilidade com X11

Aplicações X11 podem rodar em Wayland por meio de Xwayland, que implementa um servidor X11 como cliente Wayland. Isso permite migração gradual, mas não transforma APIs X11 em APIs nativas Wayland. Uma aplicação pode comportar-se de forma diferente dependendo de estar em Xwayland ou em uma sessão Xorg.

## O que Wayland não resolve sozinho

Wayland não define ambiente de desktop, menu de aplicações, tema, gerenciamento de arquivos, configuração, áudio, serviços de sessão ou descoberta de aplicações. Esses elementos vêm de GNOME, KDE, toolkits, D-Bus, XDG, portais, systemd user e outros componentes.

## Fontes primárias

- [Wayland protocol](https://wayland.freedesktop.org/docs/html/)
- [Wayland architecture](https://wayland.freedesktop.org/architecture.html)
- [Wayland book, protocol](https://wayland.freedesktop.org/docs/book/Protocol.html)
- [Xwayland](https://wayland.freedesktop.org/xserver.html)
