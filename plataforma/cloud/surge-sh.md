# Surge.sh

Surge.sh é um serviço de publicação de sites estáticos orientado à linha de comando. Ele recebe
um diretório com HTML, CSS, JavaScript e outros arquivos públicos, publica o conteúdo em uma CDN
e permite associar um domínio próprio, HTTPS, previews, revisões e rollback.

## Modelo de publicação

O build acontece fora do Surge. Um gerador, bundler ou framework produz a pasta final, e a CLI
envia essa pasta para o serviço. Isso torna Surge adequado para HTML estático, sites gerados,
documentação, SPAs e assets de frontend. O serviço não é um runtime geral para PHP, Laravel,
workers persistentes, banco de dados ou processos que precisem executar no servidor.

Uma publicação cria uma revisão. A revisão pode receber uma URL de preview e ser promovida para
produção quando o upload terminar. A CLI também oferece rollback, o que reduz o custo de uma
publicação incorreta, mas não substitui testes do build nem uma estratégia de cache e invalidação.

## Roteamento e arquivos

Uma SPA precisa tratar o acesso direto a rotas internas. O servidor deve entregar o shell da
aplicação para os caminhos que o roteador do cliente reconhece, ou a configuração deve usar o
mecanismo de fallback documentado pelo projeto. Um arquivo `404.html` pode ter papel diferente de
um fallback de roteamento e não deve ser usado sem entender o comportamento desejado.

O domínio da publicação pode ser lembrado por um arquivo `CNAME`. Esse arquivo precisa sobreviver
ao processo de build; quando o bundler apaga a pasta de saída, coloque o `CNAME` em uma entrada
de origem que seja copiada para o resultado final.

## CI e segurança

O token da CLI deve existir somente como secret do pipeline. Nunca publique a pasta de trabalho
inteira sem revisar arquivos ocultos, mapas de origem, rascunhos e artefatos que possam conter
credenciais. Use uma pasta de saída limpa e faça o deploy somente depois do build e dos testes.

Surge é útil para previews e sites públicos de baixa complexidade operacional. Dados privados,
rotas que dependem de autorização no servidor e qualquer segredo precisam permanecer em um
backend apropriado. CDN e HTTPS não transformam arquivos públicos em dados protegidos.

## Comparação

Surge tem uma superfície menor que Vercel, Railway ou plataformas autohospedadas. Isso facilita
publicar um diretório, mas deixa build, backend, banco, jobs e observabilidade fora da plataforma.
Essa simplicidade é uma vantagem quando o workload é realmente estático e uma limitação quando a
aplicação precisa de execução no servidor.

## Fontes primárias

- [Surge, início](https://surge.sh/docs/getting-started)
- [Surge, CLI](https://surge.sh/docs/cli/)
- [Surge, deploys e revisões](https://surge.sh/docs/api/deploys)
- [Surge, guias](https://surge.sh/docs/guides/)
