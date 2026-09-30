# Hermit

Hermit é um gerenciador de ferramentas de desenvolvimento que instala versões em um diretório do projeto e expõe um ambiente controlado por meio de um shell. O objetivo é reduzir a diferença entre máquinas e evitar dependência de instalações globais.

## Modelo

O projeto declara ferramentas e versões. O ambiente ativado ajusta o caminho de execução para que comandos como `node`, `go` ou `terraform` usem os binários escolhidos pelo repositório. O lock da versão continua sendo responsabilidade do projeto.

## Quando usar

Hermit é útil quando o projeto precisa de um conjunto pequeno e conhecido de CLIs, especialmente em desenvolvimento local e em jobs de CI. Ele não substitui um gerenciador completo de dependências de runtime nem resolve sozinho a reprodução do sistema operacional.

## Limitações

É preciso revisar downloads, checksums, origem dos arquivos e política de atualização. A instalação deve ocorrer em um ambiente com rede e permissões controladas, e o cache local precisa ser tratado como descartável.

## Relações

- [Build e toolchains](index.md) situa o problema.
- [Bazel](bazel.md) usa toolchains próprias para builds herméticos.
- [Nix](nix.md) oferece uma abordagem mais ampla de ambientes e dependências.

## Fonte primária

- [Hermit](https://cashapp.github.io/hermit/)
