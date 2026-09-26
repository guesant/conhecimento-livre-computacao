# Frontend

Frontend é a parte da aplicação que apresenta uma interface ao usuário e transforma ações em solicitações ao sistema. Em uma aplicação web, ele pode incluir HTML renderizado no servidor, CSS, JavaScript executado no navegador, componentes, estado de interface, acessibilidade e integração com APIs.

Frontend não é sinônimo de SPA. Uma página server-rendered possui frontend mesmo quando quase todo o HTML é produzido no servidor. Uma SPA é uma estratégia de navegação e atualização no cliente, com benefícios e custos próprios.

## Responsabilidades

Uma camada frontend normalmente cuida de:

- composição visual e responsividade;
- acessibilidade e interação;
- navegação e URL;
- validações imediatas de formato;
- estado local e estado de servidor em cache;
- renderização de loading, erro e vazio;
- chamadas a endpoints e tratamento de respostas;
- adaptação da representação para a interface.

Ela não deve ser a autoridade final para autenticação, autorização, integridade de dados ou regras que protegem um recurso. Esconder um botão não impede uma chamada direta à API.

## Modelos de renderização

### Server-side rendering

SSR produz HTML no servidor antes da resposta. Ele pode melhorar tempo até o conteúdo, indexação e compartilhamento, mas exige que dados críticos estejam disponíveis no caminho de renderização e que hidratação seja compatível com o HTML recebido.

### Client-side rendering

CSR entrega uma aplicação que busca e renderiza o conteúdo no navegador. Pode reduzir trabalho por navegação depois do primeiro carregamento, mas tende a mostrar loading inicial e depende mais do JavaScript, da rede e do cache local.

### Static generation

Geração estática produz HTML em build ou revalidação. É eficiente para conteúdo estável, mas requer estratégia para invalidação e para dados personalizados ou protegidos.

### Híbrido

Uma aplicação pode combinar SSR para shell e conteúdo crítico, cache para dados estáveis e busca no cliente para trechos secundários. A decisão deve evitar substituir conteúdo já visível por um loading global quando apenas uma seção está atualizando.

## Estado

Separe estado de interface, como menu aberto, de estado de servidor, como uma lista carregada da API. Estado de servidor precisa de política de cache, stale time, invalidação, deduplicação, retry e fallback. Estado local não deve ser usado como fonte concorrente da verdade editorial.

O frontend também deve preservar o dado anterior durante uma revalidação quando isso for melhor para a experiência. Loading de página inteira é apropriado quando não há shell nem conteúdo anterior; não é apropriado para cada mudança de filtro ou atualização em background.

## Contratos com o backend

O frontend deve consumir contratos estáveis, validar o formato recebido e tratar erros diferenciando indisponibilidade, autenticação, autorização, validação e ausência de recurso. Não deve reconstruir filtros, ordenação ou agregações que pertencem ao backend quando a API já oferece uma consulta paginada.

Tipos compartilhados, clientes gerados e schemas reduzem divergência, mas não substituem testes de compatibilidade. Uma alteração de campo pode afetar SSR, hidratação, cache do cliente e deep links.

## Performance

Meça HTML inicial, JavaScript crítico, fontes, imagens, hidratação, chamadas duplicadas e interação. Code splitting e lazy loading ajudam quando não atrasam o conteúdo crítico. Prefetch deve considerar rede e custo de CPU, não ser aplicado a todas as rotas sem evidência.

Componentes devem ter limites claros. Um card que aparece em listagem e detalhe pode ser reutilizado com composição e variantes, enquanto regras de negócio e acesso a dados devem permanecer fora da camada visual.

## Segurança

Não coloque segredos em bundles. Escape conteúdo recebido de fontes externas, trate URLs e HTML rico com sanitização adequada e considere que todo código do navegador é observável e modificável. A autenticação da sessão e a autorização da operação permanecem no backend.

## Fontes

- [MDN, web application architecture](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps)
- [web.dev, rendering on the web](https://web.dev/articles/rendering-on-the-web)
- [W3C, Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG22/)
