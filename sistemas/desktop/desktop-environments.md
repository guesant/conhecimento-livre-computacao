# Ambientes de desktop

Um desktop environment, DE, é uma composição de componentes que torna uma sessão gráfica coerente. Ele normalmente inclui shell, painel, menu ou launcher, gerenciador de configurações, integrações de rede e energia, aplicações padrão, notificações, acessibilidade e um conjunto de convenções visuais.

## O que um DE não é

Um DE não é sinônimo de distribuição, window manager ou tema. A mesma distribuição pode iniciar GNOME, KDE Plasma, Xfce ou uma sessão tiling. Um window manager pode ser substituído sem trocar todo o DE, embora a integração visual e os serviços disponíveis possam mudar.

## Componentes da sessão

Em X11, o window manager e o compositor podem ser processos separados. Em Wayland, o compositor costuma controlar também a composição e a organização das superfícies. O display manager autentica o usuário e inicia a sessão; ele não é o ambiente de desktop.

Portais, como os definidos pelo projeto XDG, permitem que aplicações usem recursos mediados pela sessão. Isso é importante para sandboxing, seleção de arquivos, abertura de URLs, impressão, localização e captura de tela.

## GNOME e KDE Plasma

[GNOME](gnome.md) prioriza uma shell integrada e um fluxo de trabalho deliberadamente simples. [KDE Plasma](kde-plasma.md) oferece uma superfície altamente configurável e um conjunto amplo de componentes KDE. Ambos podem usar Wayland ou X11 conforme a versão, hardware e sessão disponível.

## Escolha

Escolha pelo fluxo de trabalho, suporte ao hardware, acessibilidade, integração com aplicações e capacidade de manutenção. Consumo de memória isolado não descreve a experiência inteira: serviços de indexação, aplicações abertas, extensões, aceleração gráfica e configuração do usuário frequentemente pesam mais.

## Fontes primárias

- [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/)
- [KDE Human Interface Guidelines](https://develop.kde.org/hig/)
- [XDG desktop portals](https://flatpak.github.io/xdg-desktop-portal/)
