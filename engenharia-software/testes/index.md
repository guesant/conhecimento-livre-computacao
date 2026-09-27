# Testes de software

Testes de software são atividades para produzir evidência sobre o
comportamento, os contratos e as propriedades de um sistema. Eles não são
sinônimo de verificar apenas se uma função retorna o valor esperado. Uma
estratégia de testes pode incluir unidades, componentes, integração, contratos,
segurança, desempenho, acessibilidade e jornadas completas.

O tipo de teste deve acompanhar a pergunta que precisa ser respondida. Um teste
unitário pergunta se uma regra pequena se comporta corretamente. Um teste de
integração pergunta se duas fronteiras funcionam juntas. Um teste end-to-end
pergunta se um usuário ou consumidor consegue concluir um fluxo através do
sistema real o bastante para o risco avaliado.

## Camadas

Testes unitários tendem a ser rápidos e numerosos. Eles isolam uma unidade
coerente e ajudam a localizar a causa de uma falha. Testes de componente
verificam uma unidade visual ou de aplicação com suas dependências imediatas.
Testes de integração exercitam banco, filas, filesystem, rede ou outros
contratos reais. Testes end-to-end atravessam a aplicação como um consumidor,
incluindo navegador, API, autenticação e persistência quando o cenário exigir.

Essa divisão não é uma lei de quantidade. Um teste de integração pode ser mais
valioso que muitos mocks, e um fluxo end-to-end pode ser necessário para um
risco que não aparece em uma unidade isolada. O ponto é conhecer o custo e a
evidência de cada camada.

## TDD e testes exploratórios

[TDD](tdd.md) é uma abordagem de desenvolvimento em que o teste orienta o
design de uma pequena mudança. Testes exploratórios e testes manuais continuam
importantes para comportamento emergente, usabilidade, acessibilidade visual e
cenários difíceis de codificar. Automação não elimina investigação humana.

## Ferramentas de navegador

[Cypress](cypress.md) e [Playwright](playwright.md) automatizam browsers e
podem executar testes end-to-end. Eles oferecem capacidades diferentes de
isolamento, execução, depuração, browsers suportados e controle de rede. A
ferramenta não substitui a decisão sobre quais fluxos são críticos nem a
preparação de dados determinísticos.

Os testes de capacidade ficam documentados em
[Confiabilidade -> Testes](../../confiabilidade/testes/index.md). Eles
respondem a perguntas diferentes das verificações funcionais de uma jornada.

## Princípios

Uma suíte útil deve:

- produzir falhas reproduzíveis;
- verificar comportamento observável e contratos relevantes;
- controlar tempo, aleatoriedade, rede e dados externos;
- limpar ou isolar estado entre cenários;
- registrar evidência suficiente para diagnosticar;
- rodar com frequência compatível com o ciclo de mudança;
- distinguir falha do produto de falha da infraestrutura de teste.

Cobertura de linhas pode revelar áreas sem execução, mas não demonstra que os
casos de negócio, limites, permissões e falhas foram considerados. O valor do
teste está na hipótese que ele protege.
