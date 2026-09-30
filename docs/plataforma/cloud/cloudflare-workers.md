# Cloudflare Workers

Cloudflare Workers é um runtime distribuído para executar código próximo dos usuários sem administrar servidores individuais. Um Worker recebe eventos, executa a lógica dentro do modelo de isolamento da plataforma e devolve uma resposta ou interage com serviços vinculados. A aplicação pode ser publicada com a CLI, por integração contínua ou pelo painel, e as versões implantadas podem ser acompanhadas e revertidas.

Workers não é apenas uma função HTTP. O mesmo runtime pode ser usado para APIs, middleware, proxies, tarefas agendadas, consumidores de filas e composição com produtos de armazenamento e coordenação da Cloudflare. Essa variedade não elimina a necessidade de desenhar limites de estado, consistência, custos e observabilidade.

## Modelo de execução

O código é carregado em um ambiente isolado e atende eventos de acordo com o tipo de Worker. A unidade de execução não deve depender de memória local para preservar estado entre requisições. Variáveis de ambiente e segredos são fornecidos por bindings, enquanto produtos como KV, R2, D1, Queues e Durable Objects oferecem formas diferentes de persistência, armazenamento e coordenação.

Essa separação é importante. KV é apropriado para leituras distribuídas e dados que toleram consistência eventual em determinados usos. R2 é armazenamento de objetos. D1 é um banco SQL gerenciado para casos compatíveis com seu modelo. Durable Objects fornecem identidade e coordenação por objeto. Nenhum desses serviços deve ser escolhido apenas porque está disponível no mesmo painel.

## Compatibilidade e ciclo de vida

O runtime possui APIs próprias e uma camada de compatibilidade parcial com APIs do ecossistema Node.js. O projeto deve fixar a compatibility date e as compatibility flags, testar a versão efetiva do runtime e evitar depender de comportamento implícito. Bibliotecas que esperam processos persistentes, acesso arbitrário ao filesystem ou módulos nativos precisam ser avaliadas antes da migração.

Implantações são versionadas. O fluxo pode usar ambientes, URLs de versão, gradual deployments e rollback. Para uma mudança que afeta dados ou contratos, versionar o código não basta: o esquema, os bindings, as filas e as dependências externas também precisam permanecer compatíveis durante a transição.

## Quando usar

Workers é adequado para autenticação na borda, roteamento, transformação de requisições, APIs pequenas, webhooks, personalização por região, cache controlado, integração entre serviços e tarefas que se beneficiam da proximidade com o usuário. Também é útil para adicionar uma camada de comportamento a uma aplicação cuja origem principal esteja em outro provedor.

Ele não é uma escolha automática para processamento pesado, conexões longas arbitrárias, jobs que exigem filesystem local, workloads com dependências nativas ou aplicações que pressupõem um servidor sempre ativo. Nesses casos, uma VM, container, serviço gerenciado ou fila especializada pode ser mais previsível.

## Segurança e operação

Bindings devem seguir o princípio do menor privilégio. Segredos não devem ser compilados no bundle nem expostos em respostas. Valide autenticação e autorização no próprio Worker quando ele for uma fronteira de segurança, aplique limites de tamanho e tempo, registre correlation IDs e trate falhas de serviços vinculados sem transformar indisponibilidade parcial em respostas ambíguas.

Métricas de invocação não substituem métricas de dependências. Uma função rápida pode esconder uma consulta lenta ao banco, uma fila acumulada ou uma falha intermitente de origem. O diagnóstico deve relacionar versão implantada, rota, região, serviço vinculado e erro observado.

## Relação com Pages

Pages é o fluxo orientado à publicação de sites e artefatos web. Pages Functions usa o runtime de Workers para adicionar lógica a um projeto Pages. Workers é a opção mais geral quando a aplicação é essencialmente um serviço de execução distribuída ou quando precisa das configurações e recursos próprios de Workers.

## Fontes primárias

- [Cloudflare Workers](https://developers.cloudflare.com/workers/)
- [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
- [Variáveis de ambiente e secrets](https://developers.cloudflare.com/workers/configuration/environment-variables/)
- [Compatibility dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates/)
- [Implantações e versões](https://developers.cloudflare.com/workers/versions-and-deployments/)
