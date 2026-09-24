# pkgx

pkgx é uma ferramenta para executar pacotes de linha de comando em ambientes macOS e Linux sem exigir uma instalação global tradicional. Ela facilita experimentar versões de ferramentas e compor comandos portáveis.

## Modelo

O comando resolve e executa pacotes a partir de uma especificação. A conveniência não elimina a necessidade de fixar versões em CI, revisar a origem dos binários e controlar o cache local.

## Quando usar

pkgx é útil para onboarding, uso ocasional e scripts que precisam de ferramentas auxiliares sem modificar permanentemente o host. Em builds de produção, prefira imagens ou toolchains versionadas de forma explícita e reproduzível.

## Segurança

Execução sob demanda envolve downloads e confiança em metadados de pacotes. Use rede e permissões mínimas, valide checksums quando o fluxo permitir e não passe segredos como argumentos de comandos que possam ser registrados.

## Relações

- [Build e toolchains](index.md) compara a função de gerenciadores de ferramentas.
- [Hermit](hermit.md) mantém versões declaradas dentro do projeto.
- [Nix](nix.md) descreve uma abordagem reprodutível de pacotes e ambientes.

## Fonte primária

- [pkgx](https://pkgx.sh/)
