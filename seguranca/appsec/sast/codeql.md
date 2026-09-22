# CodeQL

CodeQL é uma plataforma de análise semântica em que código é extraído para uma base de dados e consultado por meio da linguagem QL. Em vez de procurar apenas texto, uma consulta pode raciocinar sobre elementos do programa e relações entre eles, incluindo fluxo de dados.

## Modelo mental

A etapa de criação da base transforma propriedades do programa em fatos consultáveis. Bibliotecas da linguagem fornecem abstrações sobre AST, tipos, chamadas, control flow e data flow. Uma consulta seleciona relações que representam o comportamento procurado.

Para segurança, um padrão importante é taint tracking: definir de onde dados potencialmente não confiáveis entram, por onde podem se propagar e quais operações são sensíveis. Isso permite procurar caminhos que atravessam múltiplas funções em vez de depender de uma única linha suspeita.

## Casos de uso

CodeQL é adequado para code scanning contínuo, investigação de uma classe de vulnerabilidade em uma base grande, criação de consultas específicas de um framework interno e variant analysis depois que uma vulnerabilidade revela um padrão que pode existir em outros pontos.

Um caso realista é descobrir uma injeção de comando e transformar o padrão em consulta: fontes são parâmetros de requisição, sinks são APIs de execução de processo e sanitizers são as validações reconhecidas pelo sistema. A consulta pode então procurar variantes em todo o código.

## Boas práticas

Comece pelas suites mantidas para a linguagem antes de escrever consultas próprias. Ao customizar, modele bibliotecas e frameworks que alteram o fluxo real dos dados. Mantenha testes de consulta com casos positivos e negativos. Diferencie resultado de consulta de confirmação de explorabilidade e preserve contexto suficiente para triagem.

## Más práticas

Evite escrever consultas excessivamente genéricas que geram ruído, considerar ausência de findings como prova de ausência de vulnerabilidades ou criar modelos customizados sem testes. Outra má prática é misturar a segurança do workflow que executa CodeQL com a segurança do código analisado: são superfícies diferentes.

## Limites e alternativas

A profundidade semântica tem custo de extração, execução e manutenção de modelos. Ferramentas baseadas em padrões estruturais podem ser mais simples e rápidas para políticas locais. DAST e testes manuais continuam necessários para comportamentos dependentes do ambiente.

## Fontes

- CodeQL documentation: <https://codeql.github.com/docs/>
- GitHub, About code scanning with CodeQL: <https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql>
- CodeQL data flow analysis: <https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/>

## Continue por aqui

[SAST](index.md) explica a abordagem da qual CodeQL é uma implementação. [zizmor](../../cicd/zizmor.md) analisa outra superfície: a definição do CI/CD.
