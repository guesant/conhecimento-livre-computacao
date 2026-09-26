# Distribuição de aplicações

AppImage, Snap, Flatpak, WinGet e Chocolatey resolvem problemas relacionados, mas não são o mesmo tipo de sistema. Alguns empacotam uma aplicação com suas dependências; outros são clientes que localizam instaladores; alguns oferecem sandbox e runtime; outros apenas automatizam a execução de um instalador.

## Comparação

| Ecossistema | Plataforma | Artefato ou entrada | Isolamento | Origem e publicação |
| --- | --- | --- | --- | --- |
| AppImage | Linux | Arquivo executável único | Não há sandbox obrigatório. | O upstream ou um distribuidor constrói e hospeda o arquivo. |
| Snap | Linux | Snap squashfs e metadados | Confinement, interfaces e `snapd`. | Snapcraft constrói e a Snap Store distribui canais e revisões. |
| Flatpak | Linux | App, runtime e repositório OSTree | Sandbox com portals e permissões. | `flatpak-builder` produz commits; Flathub ou outro remote publica. |
| WinGet | Windows | Manifesto YAML e instalador externo | Depende do instalador. | Microsoft Store ou repositórios WinGet fornecem catálogo e URLs. |
| Chocolatey | Windows | Pacote NuGet `.nupkg` com scripts PowerShell | Não é sandbox por si só. | Feed público, feed privado ou repositório interno distribui pacotes. |

## O que realmente é confiável

O catálogo não é a mesma coisa que o software executado. É necessário verificar:

- quem mantém o manifesto ou pacote;
- de onde vem o binário;
- se o build é reproduzível ou apenas um download de um instalador;
- quem assina o artefato e o índice;
- quais scripts executam com privilégio;
- como versões, rollback e CVEs são comunicados;
- se o sandbox pode ser substituído por permissões amplas ou modo clássico.

Um AppImage pode ser uma distribuição legítima e assinada, mas não ganha isolamento só por ser um arquivo único. Um pacote Chocolatey pode ter uma revisão útil e ainda executar um script de instalação com privilégios administrativos. Snap e Flatpak oferecem confinamento, mas permissões, interfaces, portals e modos de exceção precisam ser revisados.

## Escolha por cenário

Use o gerenciador nativo da distribuição quando integração com bibliotecas, serviços, logs, usuários e atualizações do sistema for mais importante que a versão mais nova. Use Flatpak ou Snap quando a aplicação desktop precisa de um ciclo independente e a política de sandbox for aceitável. Use AppImage quando a portabilidade de um arquivo e a distribuição direta forem requisitos, desde que assinatura e atualização sejam tratadas explicitamente.

No Windows, WinGet é adequado quando o catálogo, os manifestos e a integração ao Windows Package Manager atendem ao software desejado. Chocolatey é flexível para scripts e feeds privados, mas a organização precisa controlar fontes, pacotes e scripts permitidos.

## Páginas

- [AppImage](appimage.md)
- [Snap](snap.md)
- [Flatpak](flatpak.md)
- [WinGet](winget.md)
- [Chocolatey](chocolatey.md)
