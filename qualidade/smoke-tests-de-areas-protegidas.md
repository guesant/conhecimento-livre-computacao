# Smoke tests de áreas protegidas

Smoke test é uma verificação rápida e deliberadamente rasa. Em uma área protegida, ele responde se um usuário autorizado consegue abrir as páginas essenciais e se o servidor consegue montar os componentes sem uma falha imediata. O objetivo não é provar que o recurso está correto em todos os detalhes. É impedir que uma exceção básica, uma migration ausente, uma relação inválida ou uma configuração de autorização quebre toda a área antes que testes mais profundos comecem.

## Escopo

O teste deve cobrir o primeiro carregamento de:

- dashboard ou página inicial protegida;
- listagens;
- páginas de criação;
- páginas de edição com registro existente;
- configurações, perfil, currículo e outras páginas customizadas;
- páginas com relações, uploads ou campos condicionais quando forem críticas.

Para cada rota, verifique o método, o status, o redirecionamento esperado e a identidade usada. Um redirecionamento para login pode ser correto em um teste de acesso anônimo, mas é falha em um smoke test autenticado. O usuário de teste deve possuir somente as permissões necessárias, para que o teste também valide a integração com autorização.

## Descoberta das rotas

Quando o framework oferece um registro de rotas confiável, o teste pode descobrir automaticamente as páginas do painel. Separe rotas estáticas de rotas com identificadores. Para rotas de edição, crie registros com factories ou builders de fixture. Não dependa de dados que alguém inseriu manualmente no banco de desenvolvimento.

Quando a descoberta automática não for segura, mantenha uma matriz de rotas críticas. A matriz deve indicar a rota, o método, a permissão, o fixture necessário e a pergunta respondida. Uma matriz explícita é preferível a uma descoberta que inclua páginas irrelevantes, rotas de login ou endpoints internos.

## O que o teste detecta

Um smoke test de área protegida pode detectar:

- exceção durante mount ou renderização;
- consulta a tabela ou coluna inexistente;
- relação que não está disponível;
- binding de registro inválido;
- migration que não foi aplicada;
- formulário que quebra com coleção vazia;
- erro de configuração do painel;
- middleware de autenticação ou autorização incompatível;
- falha de template, componente ou serialização.

O erro deve incluir nome da rota, método, identificador, identidade e status recebido. Isso reduz o tempo de diagnóstico e transforma uma falha genérica em uma evidência localizada.

## Smoke test não é teste de comportamento

Abrir uma página não prova que salvar, cancelar, excluir, ordenar, fazer upload ou alterar um campo condicional funciona. Interfaces reativas podem responder ao GET e falhar na requisição seguinte. Para essas operações, complemente o smoke test com testes de componente, integração ou navegador que executem a ação e verifiquem o resultado.

O teste de escrita deve verificar validação, autorização, transação, eventos, cache e persistência conforme o risco. O teste de cancelamento deve confirmar a navegação e a ausência de mutação. O teste de upload deve usar arquivo controlado, storage isolado e verificação de limpeza. O teste de relações deve incluir coleção vazia, registro existente e referência inválida.

## Banco e fixtures

O banco de teste deve ser criado pelas migrations do projeto. A suíte não deve compartilhar o banco de desenvolvimento nem depender de um estado produzido por uma sessão manual. Factories devem produzir registros mínimos, válidos e previsíveis. Quando uma entidade não tem factory, crie um builder explícito ou adicione uma factory reutilizável.

Se a página consulta catálogos, traduções ou relacionamentos, esses dados precisam ser preparados no cenário. Um teste que passa somente porque o banco local contém uma plataforma, um idioma ou uma categoria não é reproduzível.

## CI e operação

Execute o smoke test depois de preparar o schema de teste e antes dos testes de navegador mais caros. No pipeline de deploy, pode existir uma versão menor que verifica a aplicação implantada, sem criar ou alterar dados reais. Essa verificação deve usar identidade e fixtures próprias do ambiente, limites de tempo e limpeza.

Um smoke test não substitui health checks, probes, métricas, alertas ou testes completos. Ele é um filtro inicial para evitar investir em diagnósticos quando a área nem sequer consegue ser aberta.

## Exemplo

No Laravel com Filament, a mesma estratégia pode descobrir as rotas do painel, autenticar um usuário permitido, abrir listagem e criação, criar registros pelas factories e abrir todas as rotas de edição. Em Livewire, ações de salvar e cancelar precisam de testes separados. Em React, Vue ou Blazor, o equivalente pode ser um teste de rota autenticada, um teste de componente e uma jornada de navegador. A regra é independente de framework.
