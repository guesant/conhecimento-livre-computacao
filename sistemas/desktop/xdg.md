# XDG

XDG é uma família de convenções associadas ao Cross-Desktop Group e ao ecossistema freedesktop.org. O termo aparece em variáveis de ambiente, especificações de arquivos, diretórios, portais e convenções de sessão gráfica.

## Diretórios de base

A XDG Base Directory Specification define locais para que aplicações não espalhem arquivos diretamente em `$HOME`:

| Variável | Finalidade padrão |
| --- | --- |
| `XDG_CONFIG_HOME` | Configuração do usuário, normalmente `$HOME/.config` |
| `XDG_DATA_HOME` | Dados persistentes do usuário, normalmente `$HOME/.local/share` |
| `XDG_STATE_HOME` | Estado persistente, como histórico e layout, normalmente `$HOME/.local/state` |
| `XDG_CACHE_HOME` | Cache não essencial, normalmente `$HOME/.cache` |
| `XDG_RUNTIME_DIR` | Sockets e arquivos temporários da sessão do usuário |
| `XDG_CONFIG_DIRS` | Diretórios de configuração compartilhada |
| `XDG_DATA_DIRS` | Diretórios de dados compartilhados |

Os caminhos definidos pelas variáveis precisam ser absolutos. `XDG_RUNTIME_DIR` possui requisitos mais fortes: deve ser privado do usuário, local, temporário e associado ao ciclo de login. Sockets de sessão, arquivos de lock e outros objetos de runtime costumam viver ali.

## Desktop Entry

Arquivos `.desktop` descrevem aplicações, links ou diretórios. Eles podem informar nome, ícone, comando de execução, MIME types, ações e se a aplicação suporta ativação via D-Bus. Menus e launchers usam esses arquivos para montar a interface de aplicações disponíveis.

Um arquivo `.desktop` não é um executável nem uma autorização. O ambiente pode validar o arquivo, aplicar regras de segurança e decidir como apresentar ou iniciar a aplicação. O comando de execução ainda precisa ser tratado com cuidado, especialmente quando recebe caminhos ou URLs externos.

## Portais

XDG Desktop Portals fornecem APIs mediadas para aplicações, especialmente aplicações sandboxed. Um portal pode solicitar ao usuário a seleção de arquivo, abertura de URL, captura de tela, screencast, impressão ou acesso a localização sem entregar à aplicação acesso irrestrito ao desktop.

O portal é uma fronteira entre aplicação e sessão. Ele não elimina a necessidade de autorização dentro da própria aplicação, nem transforma qualquer aplicação em confiável.

## XDG e containers

Containers e pacotes sandboxed podem receber valores XDG diferentes da sessão do host. Isso afeta localização de configurações, cache, sockets e dados. Ao depurar uma aplicação, compare o ambiente real do processo com o ambiente do usuário interativo, em vez de assumir que ambos usam os mesmos diretórios.

## Fontes primárias

- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/)
- [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry/latest-single/)
- [XDG Desktop Portals](https://flatpak.github.io/xdg-desktop-portal/)
- [freedesktop.org Specifications](https://specifications.freedesktop.org/)
