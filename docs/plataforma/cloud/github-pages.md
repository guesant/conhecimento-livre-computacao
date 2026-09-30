# GitHub Pages

GitHub Pages é um serviço de hospedagem para sites estáticos publicados a partir de um repositório GitHub. Ele pode servir um site de usuário ou organização, um site de projeto associado a um repositório ou um resultado de build gerado por GitHub Actions. O serviço é adequado quando o conteúdo pode ser entregue como HTML, CSS, JavaScript, imagens e outros arquivos estáticos.

## Modelos de site

Um site de usuário ou organização normalmente usa um repositório com nome específico e fica associado ao domínio principal configurado. Um site de projeto fica sob um caminho relacionado ao repositório, o que afeta URLs absolutas, base paths e links gerados pelo framework. Essa diferença precisa ser considerada antes de publicar um site que assume estar na raiz do domínio.

O build pode ser feito pelo fluxo padrão do Pages, por Jekyll ou por um workflow personalizado. Com GitHub Actions, o repositório controla as versões do gerador, dependências, validações e o artefato enviado ao Pages. Essa opção é mais previsível para MkDocs, Hugo, Astro e outros geradores que exigem uma etapa de build própria.

## O que Pages não fornece

GitHub Pages não executa um backend persistente, não oferece um banco de dados para o site e não transforma arquivos públicos em dados privados. Formulários, autenticação, busca dinâmica, comentários e operações de escrita precisam ser implementados por serviços externos ou substituídos por uma solução compatível com conteúdo estático.

O JavaScript do navegador pode consumir uma API, mas essa API precisa tratar CORS, autenticação, rate limiting, cache e disponibilidade. Colocar uma chave privada no bundle não é uma forma de autenticação, porque qualquer visitante pode inspecionar os arquivos publicados.

## Domínios e segurança

É possível usar o domínio padrão do GitHub Pages ou um domínio personalizado, desde que DNS, verificação e HTTPS sejam configurados corretamente. O repositório e o workflow devem ser tratados como parte da cadeia de publicação: proteja branches, revise mudanças em workflows, fixe actions quando necessário e não permita que conteúdo não confiável controle comandos de build.

Como o site é público, artefatos, histórico publicado e arquivos gerados devem ser revisados antes do deploy. Segredos devem permanecer em secrets do GitHub ou em um provedor externo e não podem aparecer no HTML, no JavaScript ou nos logs do workflow.

## Quando usar

Pages funciona bem para documentação, projetos open source, portfólios, páginas pessoais e sites cuja publicação deve acompanhar commits. A integração com pull requests torna a revisão simples e o custo operacional é baixo quando não há backend próprio.

Se o projeto precisa de funções server-side, previews sofisticadas, regras de edge ou integração profunda com uma CDN, compare Pages com Netlify, Cloudflare Pages, Workers e Vercel. Se precisa apenas expor temporariamente um serviço local, o problema é de túnel e ngrok ou Cloudflare Tunnel são categorias diferentes.

## Fontes primárias

- [O que é GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Configurar uma fonte de publicação](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Usar GitHub Actions para publicar](https://docs.github.com/en/pages/using-github-actions-with-github-pages)
- [Segurança do GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
