# Playwright

Playwright é uma biblioteca e um conjunto de ferramentas para automação de
browsers e testes web. O projeto mantém automação para Chromium, Firefox e
WebKit, além de um test runner com fixtures, isolamento de contexto, execução
paralela, asserções e traces.

## Modelo de isolamento

Um `BrowserContext` representa uma sessão isolada, com cookies, storage e
permissões próprios. Criar contextos separados reduz interferência entre
testes e permite executar cenários com usuários ou papéis diferentes no mesmo
processo do browser.

O isolamento não substitui a separação dos dados no backend. Tenants,
entidades, filas e banco também precisam de estratégia determinística.
Credenciais de teste devem ter escopo restrito e não podem ser copiadas para
logs, traces ou artefatos públicos.

## Sincronização e locators

Locators expressam como encontrar um elemento e permitem que a ferramenta
aguarde condições de ação e asserção. Prefira role, label, texto semântico,
test id estável ou contrato de acessibilidade. Seletores baseados em classes de
layout e posições físicas tendem a quebrar quando a interface é refatorada.

O auto-waiting não significa que qualquer fluxo assíncrono será correto.
Espere a condição de negócio ou de interface que demonstra o resultado e
verifique estados de erro. Não use `sleep` para mascarar uma corrida.

## Recursos úteis

Fixtures encapsulam preparação e limpeza. Projetos permitem separar browsers,
ambientes e configurações. Retries podem coletar evidência em falhas
intermitentes, mas uma execução que só passa no retry deve ser investigada.
Trace, screenshot, vídeo e logs ajudam a localizar falhas de navegação,
console, rede e asserções.

A execução paralela exige cuidado com portas, banco, dados e serviços
compartilhados. Se duas workers usam o mesmo usuário ou alteram o mesmo
registro, o teste pode ficar instável sem que exista um defeito no produto.

## Quando escolher

Playwright é uma opção forte quando a suíte precisa cobrir mais de um engine,
usar contextos isolados, executar em paralelo ou coletar traces detalhados.
Cypress pode oferecer uma experiência mais integrada para equipes que preferem
um modelo de execução próximo da aplicação. A comparação deve considerar
requisitos concretos, não somente a sintaxe dos testes.

## Fontes

- [Playwright, introdução](https://playwright.dev/docs/intro)
- [Playwright, browsers](https://playwright.dev/docs/browsers)
- [Playwright, isolamento](https://playwright.dev/docs/browser-contexts)
- [Testes end-to-end](testes-end-to-end.md)
