# Forjas de código

Uma forge de código é uma plataforma que coloca um repositório Git no centro
da colaboração. Ela normalmente acrescenta identidade, organizações, equipes,
branches, revisão, issues, releases, webhooks e algum mecanismo de automação.

O repositório continua sendo a fonte do histórico de código. A forge é a
camada que transforma esse histórico em um processo colaborativo observável.
Isso não significa que a forge seja a única fonte de verdade para tudo. Dados
de CI, artefatos, comentários e campos de planejamento podem ter ciclos de vida
e políticas de retenção diferentes do Git.

## Capacidades comuns

Uma forge madura costuma oferecer:

- repositórios públicos e privados;
- autenticação, organizações e permissões por equipe;
- revisão por pull request ou merge request;
- issues, labels, milestones e discussões;
- webhooks e APIs;
- releases e arquivos de distribuição;
- registro de pacotes ou imagens;
- pipelines e runners;
- busca, auditoria e notificações.

Essas capacidades não têm a mesma profundidade em todas as plataformas. Uma
forge leve pode delegar CI, registry ou gestão de projeto a serviços externos.
Uma plataforma integrada pode reduzir integrações, mas aumenta acoplamento,
complexidade de atualização e impacto de uma indisponibilidade.

## Source of truth

Defina quais dados precisam sobreviver à migração. Commits, tags e objetos Git
devem ter um backup independente da interface da forge. Issues, pull requests,
comentários, anexos, secrets, artefatos e configurações de pipeline exigem
estratégias específicas. Um clone do repositório não é backup completo da
plataforma.

## Segurança

Exija MFA para contas administrativas, reduza tokens a escopos mínimos, revise
webhooks e trate runners como execução de código não confiável quando o projeto
aceitar contribuições externas. Permissões de leitura no Git não devem conceder
acesso automático a secrets de CI. Proteções de branch e revisão obrigatória
precisam ser acompanhadas por verificação fora da interface quando o risco
justificar.

## Relações

- [Gitea](gitea.md) prioriza uma instalação leve e autogerenciada.
- [GitLab](gitlab.md) integra código, CI/CD, segurança e operação.
- [Codeberg](codeberg.md) oferece um serviço comunitário baseado em Forgejo.
- [SourceForge](sourceforge.md) dá ênfase a descoberta e distribuição pública.
- [Bitbucket](bitbucket.md) é integrado ao ecossistema Atlassian.
- [Ferramentas de colaboração](../index.md) explica a fronteira entre forge e
  workspace de conhecimento.
