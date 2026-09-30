# Microfrontend

Microfrontend é uma estratégia para dividir uma interface web em partes compostas por equipes ou aplicações independentes. Cada parte representa uma capacidade ou domínio de produto e pode possuir ciclo de desenvolvimento e deploy próprio.

Microfrontend não significa simplesmente dividir um bundle em chunks. Code splitting reduz o JavaScript carregado; microfrontend define ownership, contrato, composição e ciclo de vida entre partes da interface.

## Formas de composição

### Composição no servidor

Um servidor monta fragmentos HTML produzidos por aplicações diferentes. O navegador recebe uma resposta integrada. Essa forma pode preservar SSR e reduzir dependência de runtime compartilhado, mas exige contratos de fragmento, navegação e assets.

### Composição no cliente

Um shell carrega módulos remotos ou bundles de aplicações diferentes no navegador. Module Federation é uma técnica possível para expor e consumir módulos remotos. A composição passa a depender de carregamento assíncrono, compatibilidade de runtime e disponibilidade dos remotes.

### Web components

Componentes customizados podem representar um contrato baseado em elementos, atributos e eventos. Eles reduzem acoplamento ao framework, mas não resolvem sozinhos tema, estado, autenticação, observabilidade ou versionamento.

### Navegação por aplicações

Cada rota ou conjunto de rotas pode ser entregue por uma aplicação diferente. É a forma mais simples de isolar deploy, mas pode produzir transições inconsistentes, duplicação de shell e perda de estado se a navegação atravessar processos.

## Contratos

Um microfrontend precisa definir contrato de composição, navegação, eventos, identidade visual, acessibilidade e erro. O design system compartilhado deve ter ownership e política de compatibilidade. Dependências comuns, como React, podem ser compartilhadas, duplicadas ou isoladas, e cada escolha afeta tamanho, compatibilidade e independência.

O shell não deve conhecer detalhes internos de cada domínio. Um microfrontend também não deve alterar diretamente o DOM ou o estado privado de outro. Comunicação deve usar propriedades, eventos, APIs e contratos versionados.

## Estado e autenticação

Evite um estado global mutável compartilhado por todos os remotes. Prefira estado local e eventos pequenos. Estado de servidor deve ter uma política de cache por domínio e não deve ser duplicado sem resolver invalidação.

Autenticação pode ser responsabilidade do shell, mas cada backend continua responsável por autorização. Um microfrontend não pode transformar a presença de um menu em prova de permissão.

## Performance e falhas

Cada remote adiciona requests, JavaScript, parsing, hidratação e possíveis falhas. Exiba fallback por região, não substitua a aplicação inteira por loading quando um domínio secundário falhar. Prefetch precisa respeitar prioridade e capacidade da rede.

Defina timeout, fallback, observabilidade e compatibilidade para remote indisponível. Assets devem ser imutáveis e associados a versões. Carregar código remoto sem integridade, origem confiável e controle de publicação amplia a cadeia de supply chain do frontend.

## Quando usar

Microfrontend é justificável quando várias equipes precisam entregar partes da interface independentemente, quando domínios possuem ritmos diferentes e quando a organização consegue sustentar contratos e observabilidade. Para uma equipe única, um frontend modular com code splitting costuma oferecer a maior parte do benefício com menos complexidade.

## Relação com microsserviços

Microfrontends podem acompanhar microsserviços, mas não precisam. Um monólito backend pode servir várias partes independentes da interface. Da mesma forma, microsserviços podem ter um frontend único. Alinhar os dois lados por capacidade pode ajudar ownership, mas copiar cada fronteira de backend para o browser nem sempre é uma boa experiência.

## Fontes

- [micro-frontends.org](https://micro-frontends.org/)
- [Martin Fowler, micro frontends](https://martinfowler.com/articles/micro-frontends.html)
- [webpack, Module Federation](https://webpack.js.org/concepts/module-federation/)
