# now.sh

`now.sh` foi o domínio e o nome associado ao produto Now, antecessor da plataforma Vercel. O
produto oferecia deploy pela linha de comando, URLs de preview, HTTPS e roteamento para sites e
aplicações web. A partir de 2020, o nome Now passou a ser Vercel e os novos domínios padrão foram
associados a `vercel.app`.

## Valor histórico

O Now ajudou a popularizar um fluxo em que um desenvolvedor executava um comando no repositório e
recebia uma implantação versionada. Esse modelo aproximou build, preview, colaboração e produção,
reduzindo a necessidade de configurar manualmente DNS, TLS e um servidor para cada projeto.

As referências a `now.sh` continuam importantes para manutenção de projetos antigos. Elas podem
aparecer em aliases, links de preview, scripts de CI, documentação, callbacks OAuth, regras de
origem e variáveis de ambiente. Uma migração precisa localizar essas referências antes de trocar
o domínio, porque mudar somente o texto visível não atualiza integrações externas.

## Migração para Vercel

O CLI e os exemplos atuais devem usar `vercel`, não iniciar um projeto novo com o pacote ou o
comando histórico `now`. O processo de migração deve confirmar:

- qual projeto e equipe recebem o deployment;
- quais domínios antigos continuam apontando para versões existentes;
- quais aliases precisam ser recriados em domínios atuais;
- se webhooks, callbacks e políticas de CORS aceitam o hostname novo;
- se o build e o runtime ainda obedecem aos limites atuais da plataforma;
- como retirar tokens e integrações antigas depois da validação.

As URLs históricas podem continuar acessíveis por compatibilidade, mas não devem ser usadas como
base para novos contratos, links de documentação ou configuração de produção sem verificar o
estado atual do serviço.

## O que o Now não era

Now não era uma VM geral nem uma plataforma para executar qualquer processo persistente. O modelo
era orientado a deploys web, funções e workloads compatíveis com o runtime da plataforma. Bancos,
filas, armazenamento durável e jobs longos precisavam de serviços próprios ou de outro modelo de
infraestrutura.

## Relação com ZEIT e Vercel

ZEIT era a empresa e a marca anterior. Now era o produto e `now.sh` o domínio associado a muitos
deployments. Vercel é o nome atual da plataforma e da empresa. Consulte [ZEIT](zeit.md) para a
história da marca e [Vercel](vercel.md) para a descrição do produto atual.

## Fontes primárias

- [Vercel, ZEIT is now Vercel](https://vercel.com/blog/zeit-is-now-vercel)
- [Vercel, discussão sobre a mudança do Now](https://github.com/vercel/vercel/discussions/4468)
- [Vercel, discussão sobre a transição do domínio](https://github.com/vercel/vercel/discussions/4176)
