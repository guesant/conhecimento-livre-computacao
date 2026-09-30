# SourceForge

SourceForge é uma plataforma pública de descoberta, distribuição e colaboração
em torno de software. Sua identidade histórica está ligada a projetos de
software livre, downloads de releases, mirrors e ferramentas de colaboração,
mas a plataforma também mantém um diretório e comparativos de software.

## Modelo de distribuição

Além do repositório, um projeto pode publicar binários e releases em uma rede
de mirrors. Estatísticas de download ajudam a entender plataforma e região dos
usuários. Esse modelo é diferente de uma forge centrada apenas em pull requests:
o artefato distribuído e a descoberta do projeto são partes explícitas do
produto.

O projeto deve tratar arquivos publicados como releases imutáveis. Gere
checksums, assine artefatos quando possível, documente a origem do build e
mantenha um canal alternativo de distribuição. Estatística de download não é
prova de integridade nem substitui observabilidade da aplicação.

## Colaboração

SourceForge oferece recursos como repositórios, controle de versão, bug
tracking, fóruns, listas de e-mail, discussões e estatísticas. A profundidade e
o fluxo não são necessariamente equivalentes aos de uma plataforma moderna de
CI/CD. Avalie se o projeto precisa de revisão integrada, pipelines, registry,
gestão de vulnerabilidades ou apenas de uma superfície pública para releases.

## Quando usar

SourceForge pode ser útil para distribuir software livre com histórico de
releases, mirrors e descoberta pública. Para desenvolvimento interno, revisão
de código e pipelines com políticas sofisticadas, uma forge especializada como
GitLab, Bitbucket ou Gitea pode ser mais adequada. O projeto pode manter o Git
em outra forge e usar SourceForge como canal adicional de distribuição, desde
que a publicação seja reproduzível.

## Relações

- [Forjas de código](index.md) apresenta o modelo geral.
- [Codeberg](codeberg.md) prioriza comunidade e software livre.
- [GitLab](gitlab.md) concentra CI/CD e segurança no ciclo de desenvolvimento.

## Fontes

- [About SourceForge](https://sourceforge.net/about)
- [Why Use SourceForge?](https://sourceforge.net/create/)
