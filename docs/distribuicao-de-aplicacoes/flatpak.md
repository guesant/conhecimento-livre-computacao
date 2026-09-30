# Flatpak

Flatpak distribui aplicações Linux por meio de um identificador, um runtime, extensões e repositórios. A aplicação é executada em um sandbox e acessa recursos do host por permissões e portals, em vez de depender diretamente de todas as bibliotecas instaladas na distribuição.

## Empacotamento

O mantenedor descreve a aplicação em um manifesto e usa `flatpak-builder` para compilar fontes, instalar módulos e produzir objetos no repositório. Runtimes fornecem a base compartilhada; SDKs fornecem ferramentas de build. O resultado é publicado em um remote que pode ser Flathub ou um repositório privado.

Flatpak usa OSTree para armazenar e transportar commits. O repositório contém referências, objetos e metadados; clientes baixam somente o que precisam e podem compartilhar runtimes entre aplicações. Assinatura do repositório, controle do remote e revisão do manifesto são parte da cadeia de confiança.

## Sandbox e portals

O sandbox restringe a aplicação, enquanto portals oferecem interfaces mediadas para arquivos, URLs, notificações, captura de tela e outros recursos. Permissões amplas, acesso ao filesystem, dispositivos ou modo de desenvolvimento podem reduzir o isolamento. O administrador deve revisar o manifesto e as permissões efetivas.

## Atualização e runtimes

A aplicação e o runtime possuem ciclos relacionados, mas não idênticos. Atualizar o runtime pode corrigir uma biblioteca compartilhada para várias aplicações; manter runtimes antigos aumenta consumo de disco. Uma política de retenção deve considerar rollback e suporte da aplicação.

## Quando usar

Flatpak é particularmente adequado para aplicações desktop que precisam de um ciclo independente da distribuição e de integração com portals. Ele é menos adequado para daemons de host, componentes de boot ou software que precisa controlar diretamente serviços e dispositivos sem a mediação do sandbox.

## Fontes primárias

- [Flatpak documentation](https://docs.flatpak.org/en/latest/)
- [Flatpak Builder](https://docs.flatpak.org/en/latest/flatpak-builder.html)
- [Flatpak sandbox permissions](https://docs.flatpak.org/en/latest/sandbox-permissions.html)
- [XDG desktop portals](https://flatpak.github.io/xdg-desktop-portal/)
