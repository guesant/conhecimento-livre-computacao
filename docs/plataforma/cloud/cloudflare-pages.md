# Cloudflare Pages

Cloudflare Pages é uma plataforma de publicação para sites estáticos e aplicações web que transforma um diretório de artefatos em uma implantação distribuída na rede da Cloudflare. O projeto pode receber o código por integração com Git, por upload direto ou pela CLI C3. Cada implantação pode ter uma URL própria, e o projeto pode associar domínios personalizados, configurar redirecionamentos, cabeçalhos e regras de construção.

Pages atende principalmente ao problema de publicar o resultado de um build. Ele não é uma máquina virtual, não fornece um processo persistente para a aplicação e não transforma automaticamente um site estático em um sistema com banco de dados. Quando a aplicação precisa de comportamento dinâmico, Pages Functions executa código no runtime de Workers e pode acessar bindings e serviços da plataforma.

## Modelo de publicação

O fluxo típico começa com uma revisão no Git ou com um conjunto de arquivos gerado por um pipeline. O provedor executa o comando de build, publica os artefatos e associa a implantação a uma URL. O projeto pode ter implantações de pré-visualização para branches ou pull requests e uma implantação de produção separada. Essa distinção permite validar o resultado antes de mudar o domínio principal.

A integração com Git é conveniente quando o repositório é a fonte de verdade do site. O upload direto é útil quando outro sistema já executa o build e deve entregar apenas os artefatos. Em ambos os casos, o pipeline precisa fixar a versão das ferramentas, controlar variáveis de ambiente e preservar os mapas de origem quando eles forem necessários para diagnóstico.

## Pages Functions

Pages Functions adiciona rotas de servidor sem exigir que o operador mantenha uma VM. A execução usa o modelo de Workers, portanto o código deve ser escrito para o ciclo de vida de uma requisição e para as APIs disponíveis no runtime. É adequado para autenticação simples, formulários, middleware, transformação de respostas e pequenas APIs próximas do conteúdo publicado.

Uma Function não deve ser tratada como um worker de longa duração ou como um substituto automático para um backend stateful. Filas, bancos, sessões, arquivos e tarefas demoradas precisam de serviços compatíveis com o modelo escolhido e de uma política clara de timeout, retry, observabilidade e consistência.

## Quando usar

Pages é uma boa escolha para documentação, landing pages, portfólios, sites gerados por Hugo, MkDocs, Astro ou frameworks com saída estática, além de frontends que consomem uma API externa. Pré-visualizações e rollback de implantações também são úteis quando o fluxo de revisão é parte importante da publicação.

Para projetos novos que dependem intensamente de lógica server-side, a própria documentação da Cloudflare recomenda avaliar Workers, que possui uma superfície mais ampla. Pages continua fazendo sentido quando o centro do sistema é a publicação de artefatos estáticos e a parte dinâmica é pequena ou bem delimitada.

## Limitações e cuidados

O build precisa ser reprodutível, e o conteúdo gerado não deve depender de arquivos presentes apenas no ambiente de construção do provedor. Verifique limites de builds, tamanho de artefatos, cache, invalidação, headers, redirects e comportamento de rotas de fallback.

Conteúdo publicado em Pages é público por padrão quando o domínio é público. Segredos não devem ser enviados ao diretório de saída, incluídos no JavaScript do navegador ou armazenados em arquivos gerados. Dados privados devem permanecer atrás de autenticação e ser obtidos por uma API autorizada.

## Relação com outras opções

Pages se aproxima de GitHub Pages, Netlify, Vercel e Surge.sh na publicação de conteúdo web, mas difere no grau de integração com o restante da rede Cloudflare e na possibilidade de usar Pages Functions. Workers é o runtime adjacente para a lógica dinâmica. Cloudflare Tunnel resolve conectividade com origens privadas, não a publicação de artefatos.

## Fontes primárias

- [Cloudflare Pages](https://developers.cloudflare.com/pages/)
- [Pages Functions](https://developers.cloudflare.com/pages/functions/)
- [Integração com Git](https://developers.cloudflare.com/pages/configuration/git-integration/)
- [Implantações de pré-visualização](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
