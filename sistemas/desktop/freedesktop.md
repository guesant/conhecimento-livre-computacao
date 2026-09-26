# freedesktop.org

freedesktop.org é um projeto de interoperabilidade e tecnologias de base para desktops livres em Linux e outros sistemas Unix-like. Ele não é uma distribuição, um ambiente de desktop único ou um órgão formal de padronização. Publica especificações, mantém projetos e oferece convenções que GNOME, KDE Plasma e outras implementações podem adotar para compartilhar comportamento.

## O problema que resolve

Sem convenções comuns, cada ambiente de desktop precisaria definir sozinho como localizar configurações, descrever aplicações, abrir URLs, montar dispositivos, expor portais, registrar serviços e integrar sessões. Uma aplicação funcionaria em GNOME, mas poderia não aparecer no menu do KDE ou não encontrar o diretório de configuração esperado.

As especificações do freedesktop.org reduzem esse acoplamento. Elas são implementadas por diferentes projetos, com níveis variados de adoção. Uma especificação amplamente usada é uma convenção de interoperabilidade, não uma garantia de que todo ambiente implementa todas as extensões.

## Especificações e projetos relacionados

Entre os componentes associados estão:

- XDG Base Directory, para dados, configuração, estado, cache e runtime;
- Desktop Entry, para arquivos `.desktop` de aplicações, links e diretórios;
- menus, temas de ícones, MIME types e autostart;
- XDG Desktop Portals, para acesso mediado a arquivos, URLs, screencast e outros recursos;
- D-Bus, para IPC orientado a mensagens entre serviços e aplicações;
- Wayland, protocolo entre clientes e compositores;
- projetos de áudio, vídeo, gráficos, input e infraestrutura compartilhada.

Nem tudo possui o mesmo status. Algumas especificações são estáveis e amplamente adotadas; outras são propostas, experimentais ou implementadas apenas por determinados ambientes.

## Relação com GNOME e KDE

GNOME e KDE Plasma possuem identidades, toolkits e arquiteturas próprias, mas compartilham várias convenções do ecossistema freedesktop.org. Isso permite que um arquivo `.desktop`, um portal ou um diretório XDG seja reconhecido por mais de um ambiente.

Interoperabilidade não significa identidade visual. Dois ambientes podem interpretar a mesma especificação com interfaces diferentes e adicionar extensões próprias.

## Fontes primárias

- [freedesktop.org Specifications](https://specifications.freedesktop.org/)
- [Lista de especificações freedesktop.org](https://wiki.freedesktop.org/www/Specifications/)
- [XDG Desktop Portals](https://flatpak.github.io/xdg-desktop-portal/)
