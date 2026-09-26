# Netlify

Netlify é uma plataforma gerenciada de entrega de aplicações web, especialmente adequada para sites estáticos, aplicações Jamstack e frontends que precisam de build, pré-visualização, domínio e CDN integrados. O projeto pode ser conectado a um repositório Git, ter o comando de build executado pela plataforma e publicar uma implantação imutável associada a uma revisão.

O valor principal está na integração entre repositório, build e entrega. Pull requests podem receber deploy previews, e a implantação de produção pode ser promovida ou revertida sem que a equipe mantenha diretamente um servidor web. A conveniência não elimina a necessidade de definir como dependências, segredos, cache, dados privados e falhas de build serão tratados.

## Arquitetura de publicação

O pipeline normalmente instala dependências, executa o build e publica o diretório de saída. Headers, redirects, funções e regras de cache fazem parte da configuração do projeto. O resultado é distribuído por uma camada de edge, enquanto dados persistentes e integrações de negócio normalmente ficam em serviços externos.

Deploy previews são úteis para revisar uma mudança com a mesma forma de entrega do site, mas uma pré-visualização precisa receber apenas dados e segredos compatíveis com esse ambiente. Não se deve apontar automaticamente um preview para credenciais de produção ou para operações destrutivas.

## Funções e edge functions

Netlify Functions permitem expor endpoints sem manter um processo de aplicação tradicional. Edge Functions executam lógica em pontos de presença compatíveis com o modelo da plataforma. Esses recursos são adequados para webhooks simples, autenticação, middleware, transformação de respostas e integrações pequenas.

Eles não devem ser tratados como servidores long-running, banco de dados ou fila. Tarefas demoradas, conexões persistentes, processamento pesado e workflows com estado exigem uma arquitetura que inclua serviços próprios para essas responsabilidades. Timeouts, concorrência, retries e idempotência precisam ser definidos explicitamente.

## Quando usar

Netlify é uma opção natural para documentação, marketing, portfólios, sites gerados por frameworks e frontends com ciclo de revisão baseado em pull requests. Também pode ser adequado quando a equipe quer um fluxo de publicação gerenciado e não precisa operar Kubernetes, proxy, certificados e servidores de build.

Para uma aplicação com banco, workers, sessões complexas ou requisitos de rede privada, avalie se Netlify será apenas a camada de frontend ou se outra plataforma deve executar o backend. Separar frontend e backend pode ser saudável, desde que CORS, autenticação, observabilidade e deploy coordenado sejam projetados como uma única arquitetura.

## Segurança e operação

Variáveis de ambiente devem ser separadas por contexto e escopo. O bundle enviado ao navegador é público, portanto nenhuma chave secreta pode ser usada em código client-side. Restrinja funções administrativas, valide entrada, registre falhas e proteja webhooks contra replay e chamadas não autorizadas.

Cache e invalidação devem ser tratados como parte do contrato de conteúdo. Uma publicação bem-sucedida não garante que todos os consumidores verão a mesma versão imediatamente se existirem caches, APIs externas ou dados gerados em momentos diferentes.

## Relação com outras plataformas

Netlify disputa parte do espaço de Cloudflare Pages, Vercel, GitHub Pages e Surge.sh. GitHub Pages é mais restrito a hosting estático integrado ao GitHub. Surge.sh privilegia uma publicação estática simples por CLI. Cloudflare Pages e Workers combinam publicação e edge dentro do ecossistema Cloudflare. A escolha deve considerar runtime, previews, funções, portabilidade, dados e operação, não apenas a velocidade do primeiro deploy.

## Fontes primárias

- [Documentação do Netlify](https://docs.netlify.com/)
- [Builds](https://docs.netlify.com/build/get-started/)
- [Deploy previews](https://docs.netlify.com/deploy/deploy-previews/)
- [Netlify Functions](https://docs.netlify.com/build/functions/overview/)
- [Edge Functions](https://docs.netlify.com/build/edge-functions/overview/)
