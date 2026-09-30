# Quay

Quay é um registry de artefatos OCI voltado à publicação, distribuição e governança de imagens de container. Pode ser operado como serviço ou instalado de forma autogerenciada, conforme a edição e a plataforma escolhidas.

## O que ele oferece

O registry organiza repositórios, manifestos, tags e blobs, aplicando autenticação e autorização às operações de push e pull. A API pode ser usada para automatizar criação de repositórios, gestão de imagens e tarefas de integração. Recursos de retenção, replicação, scanning e interface administrativa dependem da configuração e da distribuição adotada.

## Identidade do artefato

Tags são ponteiros mutáveis e não devem ser a única identidade usada em uma promoção. O pipeline deve registrar o digest do manifesto publicado e transportar essa identidade entre ambientes. O registry controla distribuição e governança, mas não prova por si só a origem ou a integridade do processo de build.

## Relações

- [Registry OCI](registry.md) explica o protocolo e os objetos distribuídos.
- [Repositório de artefatos](artifact-repository.md) compara registry dedicado e repositório universal.
- [Digest](../digest.md) explica a identidade por conteúdo.
- [Skopeo](skopeo.md) copia e inspeciona imagens sem executá-las.

## Fonte primária

- [Project Quay documentation](https://docs.projectquay.io/)
