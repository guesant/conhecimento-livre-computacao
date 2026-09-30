# Vercel

Vercel é uma plataforma de aplicações orientada à web, com integração a Git, previews, deploy contínuo, CDN, funções e execução próxima do usuário. O fluxo reduz a quantidade de infraestrutura que a equipe administra e é particularmente conveniente para frontends, aplicações full-stack com limites bem definidos e endpoints orientados a requisições.

## Modelo de execução

O código é construído e publicado pela plataforma. Funções, rotas e assets são distribuídos conforme o runtime e a configuração do projeto. O modelo favorece operações curtas e stateless. Estado durável, filas, processamento longo e bancos devem ser tratados como serviços separados ou como recursos explicitamente suportados pela plataforma.

## Quando faz sentido

Vercel é adequada para sites estáticos, frameworks web, aplicações com previews por pull request e times que valorizam feedback rápido entre Git e produção. A CDN e a integração com deploy podem simplificar bastante o caminho até o usuário.

## Limitações

Não é uma substituta geral para VM, Kubernetes ou banco relacional. Runtimes têm limites de tempo, memória, região e acesso ao filesystem. O desenho precisa considerar cold start, observabilidade, autenticação, cache, invalidação, egress e o custo de chamadas a serviços externos.

Antes de adotar, confirme como exportar o build, executar localmente, migrar funções, obter logs e manter o estado fora da plataforma. O ganho de simplicidade é real, mas vem com acoplamento ao modelo de deploy e ao runtime.

## Fontes primárias

- [Vercel documentation](https://vercel.com/docs)
- [Vercel Functions](https://vercel.com/docs/functions)
- [Vercel platform](https://vercel.com/platform)
