# GitLab

GitLab é uma plataforma de desenvolvimento que combina forge Git, issues,
merge requests, CI/CD, registry, segurança, deploy, observabilidade e gestão
de ambientes. Pode ser consumido como serviço hospedado ou instalado como
GitLab Self-Managed, com pacote Linux, containers e Kubernetes entre as formas
de implantação disponíveis.

## Modelo de ciclo de vida

Um projeto contém o repositório e os objetos associados ao desenvolvimento.
Grupos organizam projetos e herdam configurações, membros e políticas. A
merge request reúne mudança, discussão, validações e evidências antes da
integração. Pipelines executam jobs em runners e podem produzir pacotes,
imagens, relatórios de segurança e ambientes temporários.

Essa integração permite relacionar código, revisão, pipeline, vulnerabilidade,
release e ambiente. O custo é maior acoplamento à plataforma: uma decisão sobre
permissões, runners, registry ou modelo de CI pode afetar várias etapas ao
mesmo tempo.

## CI/CD e runners

O pipeline é uma descrição versionada da execução, mas os runners são a
fronteira operacional. Runners compartilhados precisam ser isolados de jobs que
aceitam código não confiável. Runners privilegiados, acesso ao Docker socket,
tokens amplos e secrets disponíveis em jobs de merge request são riscos
independentes da proteção do branch.

Para workloads Kubernetes, o executor pode criar pods por job, mas isso não
elimina a necessidade de quotas, NetworkPolicies, service accounts mínimas,
limites de concorrência e limpeza de volumes. O pipeline deve produzir artefatos
identificados por digest ou checksum, não depender apenas de tags móveis.

## Self-Managed

Operar GitLab exige planejar PostgreSQL, Redis, armazenamento de objetos,
registry, runners, busca, e-mail, backups, upgrades e recuperação. A alta
disponibilidade do frontend não recupera dados se o banco ou o storage de
artefatos não tiver restauração testada. O plano de backup deve distinguir
repositórios Git, banco, uploads, registry, secrets e configuração da instância.

## Quando usar

GitLab é adequado quando a organização quer uma plataforma integrada para
planejamento, código, pipeline, segurança e entrega, ou quando precisa de uma
instância autogerenciada com fronteiras administrativas próprias. Pode ser
excessivo para apenas hospedar um repositório e revisar pull requests; nesse
caso, Gitea, Codeberg ou Bitbucket podem ter menor custo operacional, conforme
as demais necessidades.

## Relações

- [Forjas de código](index.md) compara as responsabilidades comuns.
- [Gitea](gitea.md) enfatiza leveza e autogerenciamento.
- [Bitbucket](bitbucket.md) integra código ao ecossistema Atlassian.
- [GitLab Runner para Docker](../../../ci/gitlab-runner/docker-executor.md) e
  [GitLab Runner para Kubernetes](../../../ci/gitlab-runner/kubernetes-executor.md)
  detalham executores.

## Fontes

- [GitLab Docs](https://docs.gitlab.com/)
- [Use GitLab](https://docs.gitlab.com/user/)
- [Install GitLab Self-Managed](https://docs.gitlab.com/install/)
