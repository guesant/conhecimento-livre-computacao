# WinGet

WinGet é o cliente Windows Package Manager para descobrir, instalar, atualizar e remover aplicações no Windows. Ele não é um formato único de executável: o catálogo aponta para instaladores como MSI, MSIX, EXE, Inno, WiX, Nullsoft e outros tipos suportados pelo manifesto.

## Fontes e manifestos

As fontes padrão incluem Microsoft Store e o repositório comunitário WinGet. Uma fonte fornece os dados de descoberta e instalação; pode ser adicionada, removida, atualizada ou marcada como explícita. Em ambientes corporativos, fontes confiáveis devem ser controladas por política e, quando possível, substituídas por uma fonte interna.

O repositório comunitário usa manifestos YAML. Eles descrevem identificador, versão, locale, publisher, instaladores, URLs, arquitetura e SHA-256. O manifesto não é o binário: ele aponta para o instalador e registra o hash que o cliente deve validar.

## Segurança

WinGet normalmente entrega o instalador do fornecedor ou da fonte. O instalador pode executar lógica com privilégios, alterar serviços, escrever no registro e instalar componentes fora do controle do cliente. O operador deve revisar fonte, publisher, URL, hash, escopo de instalação e opções silenciosas.

Não trate a presença no catálogo como uma auditoria completa do fornecedor. Para frotas, fixe o identificador e a versão quando necessário, restrinja fontes, valide manifestos em pull requests e mantenha logs da instalação.

## Build e atualização

WinGet não precisa compilar o software. O publisher constrói o instalador e o mantenedor do manifesto registra como encontrá-lo. A atualização compara versões no catálogo e executa o instalador correspondente. A segurança da cadeia depende do publisher, do HTTPS, do hash, da assinatura do instalador e do processo de revisão do manifesto.

## Fontes primárias

- [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [WinGet sources](https://learn.microsoft.com/en-us/windows/package-manager/winget/source)
- [WinGet package manifests](https://learn.microsoft.com/en-us/windows/package-manager/package/manifest)
- [WinGet community repository](https://github.com/microsoft/winget-pkgs)
