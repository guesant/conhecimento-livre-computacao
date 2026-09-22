# SAST

Static Application Security Testing analisa software sem executar a aplicação como um atacante externo. A análise pode variar de regras sintáticas simples até modelos semânticos capazes de acompanhar fluxo de dados entre funções e arquivos.

SAST não é sinônimo de grep. Ferramentas mais simples reconhecem padrões locais; analisadores baseados em AST entendem construções da linguagem; análises de control flow representam caminhos possíveis de execução; data flow acompanha como valores se propagam; taint tracking especializa esse modelo em valores não confiáveis, normalmente descrevendo sources, propagação, sanitizers e sinks.

## Caso de uso

Considere uma API que recebe um parâmetro HTTP e posteriormente o entrega a uma função de execução de comandos. Uma análise local pode não perceber a relação se o valor atravessa várias funções. Uma análise interprocedural de fluxo de dados pode procurar um caminho entre a entrada controlável e o sink perigoso e verificar se existe sanitização relevante no caminho.

SAST é especialmente útil em pull requests, revisão contínua de bases grandes, identificação de padrões repetitivos e políticas que precisam ser verificadas antes de existir um ambiente executável.

## Quando não basta

SAST não observa configuração real de proxy, WAF, IAM ou banco; não confirma que uma vulnerabilidade é explorável no ambiente implantado; não substitui SCA para vulnerabilidades conhecidas de componentes; e pode não representar corretamente comportamento criado dinamicamente em runtime.

## Exemplo conceitual

Uma regra de taint pode modelar entrada HTTP como source, uma API de shell como sink e uma função de validação específica como sanitizer. O finding não significa automaticamente exploração confirmada: significa que o modelo encontrou um caminho que satisfaz a consulta.

## Boas práticas

Rode a análise cedo e de forma incremental quando possível. Priorize regras relevantes às linguagens e frameworks usados. Faça triagem de falsos positivos em vez de simplesmente desligar categorias inteiras. Mantenha suppressions pequenas, justificadas e revisáveis. Para regras customizadas, teste tanto exemplos vulneráveis quanto exemplos seguros para evitar uma consulta que "funciona" apenas porque marca tudo.

## Más práticas

É má prática tratar qualquer finding como prova automática de vulnerabilidade, medir qualidade pela quantidade de alertas, habilitar milhares de regras sem estratégia de triagem ou criar suppressions globais para fazer a pipeline ficar verde. Também é inadequado usar SAST como substituto de revisão arquitetural: uma consulta encontra o que seu modelo sabe representar.

## Implementações

[CodeQL](codeql.md) representa código em uma base consultável e oferece análises semânticas e de fluxo de dados. Outras famílias de ferramenta podem privilegiar regras sobre AST, padrões estruturais ou análise compilada. A escolha depende de linguagem, profundidade desejada, extensibilidade, custo de execução e integração com o fluxo de desenvolvimento.

## Fontes

- OWASP, Static Application Security Testing: https://owasp.org/www-community/Source_Code_Analysis_Tools
- GitHub, CodeQL data flow analysis: https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/

## Continue por aqui

[CodeQL](codeql.md) mostra uma implementação concreta desse modelo. [DAST](../dast.md) observa a aplicação por outro ângulo, já em execução.