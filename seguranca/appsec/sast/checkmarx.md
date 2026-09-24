# Checkmarx SAST

Checkmarx SAST é uma implementação comercial de SAST que analisa código-fonte por meio de um grafo lógico e de consultas de segurança. A análise não depende de compilar a aplicação nem de executá-la, portanto pode ser integrada antes de um ambiente funcional existir.

## Fronteira

O objeto principal é o código próprio. O produto pode encontrar fluxos, chamadas perigosas, problemas de lógica e violações de regras definidas pelos seus conjuntos de consultas. Isso o diferencia de DAST, que observa uma aplicação em execução, e de SCA, que correlaciona componentes de terceiros com vulnerabilidades e licenças.

## Modos de uso

Uma varredura completa estabelece a cobertura da branch. Uma varredura incremental reduz o tempo de feedback em mudanças menores, mas depende de uma base completa recente para preservar contexto. Presets, filtros de arquivos e exclusões alteram a pergunta respondida pelo scanner, por isso devem ser versionados ou registrados como parte da configuração do projeto.

## Limitações

O resultado depende das linguagens, frameworks, regras e exclusões habilitadas. Um finding ausente não prova que a aplicação está segura, e um finding não deve ser tratado como risco confirmado sem validação de contexto, reachability e impacto. SAST também não observa exposição de rede, configuração efetiva ou comportamento emergente em runtime.

## Relações

- [SAST](index.md) define a categoria e suas técnicas.
- [Data-flow analysis](data-flow-analysis.md) descreve a propagação de valores.
- [CodeQL](codeql.md) é uma implementação baseada em consultas com outro modelo de extensibilidade.
- [SCA](../sca/index.md) trata componentes de terceiros.

## Fonte primária

- [Checkmarx SAST Overview](https://docs.checkmarx.com/en/34965-46311-checkmarx-sast-overview.html)
