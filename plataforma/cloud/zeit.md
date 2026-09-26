# ZEIT

ZEIT foi o nome anterior da empresa que criou o Now e que depois adotou a marca Vercel. Não é um
provedor independente atual para ser comparado diretamente com Railway, Coolify ou CapRover. A
página é mantida porque o nome aparece em documentação antiga, pacotes, variáveis de ambiente,
repositórios, artigos e decisões de arquitetura registradas antes da mudança de marca.

## O que o nome representava

A empresa surgiu com uma proposta de simplificar a publicação de aplicações web. O produto Now
permitia fazer deploy por uma CLI e receber uma URL pública com HTTPS e roteamento. A evolução do
produto aproximou o fluxo de desenvolvimento, preview e publicação de sites Jamstack e aplicações
web, especialmente no ecossistema Next.js.

Em abril de 2020, a empresa anunciou oficialmente que ZEIT passaria a se chamar Vercel. A mudança
foi de identidade e posicionamento, não uma migração para uma empresa sem relação com os projetos
anteriores. Workflows, projetos e clientes foram tratados como parte da continuidade da
plataforma, com mudanças graduais de marca e domínios.

## Como interpretar referências antigas

Uma referência a `zeit.co`, `zeit/now`, ZEIT ou ao Now pode apontar para uma versão histórica da
plataforma. Para novos projetos, consulte a documentação e os produtos atuais da Vercel. Ao
migrar um repositório antigo, procure:

- pacotes e comandos `now` que devem ser substituídos pelo CLI `vercel`;
- variáveis e nomes de builder que ainda usam o prefixo ZEIT;
- URLs `now.sh` usadas em aliases, previews, callbacks ou documentação;
- integrações de GitHub, tokens e scripts de CI que dependem de comportamento antigo;
- suposições sobre containers, processos persistentes e execução serverful.

Não se deve concluir que todo código que contém ZEIT está quebrado. A compatibilidade histórica
pode continuar funcionando, mas deve ser diferenciada de uma configuração recomendada para novos
deploys.

## Relação com Vercel e now.sh

ZEIT é a marca anterior, Now foi o produto e `now.sh` foi um domínio associado aos deployments.
Vercel é a marca e a plataforma que sucederam esse conjunto. As páginas [now.sh](now-sh.md) e
[Vercel](vercel.md) explicam as duas pontas dessa transição sem tratar nomes históricos como
produtos atuais independentes.

## Fonte primária

- [Vercel, ZEIT is now Vercel](https://vercel.com/blog/zeit-is-now-vercel)
