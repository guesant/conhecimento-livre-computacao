# X.Org

X.Org é uma implementação e um conjunto de projetos do ecossistema X Window System. O servidor X.Org, conhecido como Xorg, fornece uma implementação do servidor X11 para sistemas Unix-like. Ele não é sinônimo de X11: X11 é o protocolo e o modelo; Xorg é uma implementação concreta.

## Componentes

Uma sessão X.Org pode incluir:

- servidor Xorg;
- drivers ou módulos de vídeo e input;
- Mesa, DRI, GLX e outras partes da pilha gráfica;
- window manager;
- compositor opcional;
- display manager;
- desktop environment;
- aplicações e toolkits X11.

O servidor coordena display e input, mas o ambiente de desktop define shell, painel, configurações e aplicações. Instalar Xorg não instala automaticamente GNOME ou KDE Plasma.

## Xorg e Wayland

Xorg é usado em uma sessão X11. Em uma sessão Wayland, aplicações X11 podem usar Xwayland, uma camada de compatibilidade executada como cliente Wayland. Xorg e Xwayland têm papéis diferentes: o primeiro é o servidor de uma sessão X11 completa; o segundo atende aplicações X11 dentro de uma sessão Wayland.

## Operação e diagnóstico

Ao investigar uma sessão gráfica, identifique o display manager, o tipo de sessão, o compositor, o servidor, o toolkit e o driver gráfico. Ver apenas que uma aplicação abriu não prova que ela está usando Xorg diretamente. Variáveis como `XDG_SESSION_TYPE`, `DISPLAY` e `WAYLAND_DISPLAY`, logs do servidor e informações do compositor ajudam a distinguir os caminhos.

## Fontes primárias

- [X.Org documentation](https://www.x.org/Documentation/)
- [X.Org developer guide](https://www.x.org/guide/)
- [X.Org releases and documentation](https://www.x.org/releases/current/doc/)
- [Wayland Xwayland](https://wayland.freedesktop.org/xserver.html)
