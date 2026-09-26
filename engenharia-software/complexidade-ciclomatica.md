# Complexidade ciclomática

Complexidade ciclomática é uma métrica de estrutura de controle associada a Thomas McCabe. Ela estima a quantidade de caminhos linearmente independentes em um grafo de fluxo de controle. O valor ajuda a pensar em testes e pontos de decisão, mas não mede sozinho legibilidade, tamanho, acoplamento ou dificuldade do domínio.

## Grafo de fluxo

Um grafo de fluxo representa blocos de execução como nós e transferências de controle como arestas. Para um grafo conectado, a forma clássica é:

```text
M = E - N + 2P
```

`E` é o número de arestas, `N` é o número de nós e `P` é o número de componentes conectados. Em uma função estruturada simples, a contagem pode ser aproximada por um caminho inicial mais uma unidade para cada decisão que cria uma bifurcação. A ferramenta concreta deve declarar como trata `if`, `else`, `switch`, loops, operadores booleanos, exceções e retornos.

Uma função com complexidade 1 tem um caminho básico sem decisões. Uma função com complexidade 5 possui mais caminhos independentes para considerar, não necessariamente cinco testes suficientes para cobrir todas as combinações de dados e efeitos externos.

## Para que serve

A métrica ajuda a identificar funções que concentram decisões, orientar testes de caminhos, priorizar revisão e encontrar pontos onde uma mudança pode produzir muitos comportamentos. Ela é particularmente útil quando combinada com cobertura, análise de risco, tamanho da função e histórico de defeitos.

Ela não deve ser usada como prova de correção. Uma função com `switch` sobre estados válidos pode ter complexidade maior e ser mais clara que uma cadeia de abstrações indiretas. Uma função com baixa complexidade pode chamar várias dependências perigosas, fazer parsing inseguro ou aplicar uma regra de negócio errada.

## Melhor e pior uso

É útil medir por função, registrar a versão da ferramenta e usar o resultado para iniciar uma conversa de refatoração. Também é útil acompanhar tendência: uma função que cresce a cada mudança merece atenção mesmo antes de ultrapassar o limite.

É ruim reduzir a métrica apenas extraindo cada ramo para uma função que mantém a mesma responsabilidade, criando wrappers ou substituindo uma decisão explícita por uma tabela difícil de entender. A complexidade foi deslocada, não reduzida. A refatoração deve melhorar coesão, testabilidade, nomeação, separação de responsabilidades ou previsibilidade.

## Limites

Um limite como 5 ou 10 é uma política de triagem, não uma lei universal. Código de parsing, compiladores, protocolos e máquinas de estado pode precisar de mais decisões, desde que possua testes e uma estrutura clara. Um limite baixo pode ser adequado para handlers, controllers e componentes de UI, onde decisões demais misturam responsabilidades.

Quando uma função excede o limite, pergunte se há estados que podem ser modelados por tipos, guard clauses, polimorfismo, tabelas de decisão, funções puras ou componentes delegados. Não esconda o fluxo só para agradar o linter. Registre exceções estreitas quando a complexidade for essencial e houver testes que expliquem o contrato.

## Relação com testes

Complexidade ciclomática sugere uma quantidade mínima de caminhos independentes para uma estratégia de cobertura estrutural. Isso não substitui testes de fronteira, propriedades, contratos, concorrência, segurança e falha de dependências. Uma entrada pode atravessar o mesmo caminho de controle e ainda revelar um erro de valor, estado ou integração.

## Relações

- [Análise de complexidade](analise-de-complexidade.md) trata crescimento assintótico de algoritmos.
- [Complexidade cognitiva](complexidade-cognitiva.md) trata esforço de compreensão humana.
- [Clean Code](clean-code.md) trata coesão, nomes e refatoração.
- [Qualidade e governança](../qualidade/repositorio/index.md) reúne ferramentas e gates
  usados para manter métricas verificáveis no repositório.

## Fontes

- [NIST, Structured Testing e complexidade ciclomática](https://www.nist.gov/publications/structured-testing-software-testing-methodology-using-cyclomatic-complexity-metric)
- [NIST, Structured Testing, publicação](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-235.pdf)
- [Definições de métricas do SonarQube](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/code-metrics/metrics-definition)
