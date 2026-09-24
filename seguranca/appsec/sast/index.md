# SAST

Static Application Security Testing analisa código ou representações derivadas dele sem precisar exercitar a aplicação como um atacante externo. A categoria inclui implementações com profundidades e modelos diferentes.

## Mapa conceitual

Regras estruturais podem trabalhar sobre sintaxe e AST. [Data-flow analysis](data-flow-analysis.md) modela propagação de valores. [Taint analysis](taint-analysis.md) especializa esse modelo com [sources](source.md), [sinks](sink.md) e [sanitizers](sanitizer.md).

Essas técnicas são independentes da ferramenta que as implementa. Uma implementação pode oferecer apenas parte delas.

## Estratégias de execução

[Análise incremental](analise-incremental.md) prioriza mudanças recentes e reduz feedback em pull requests. [Baseline](baseline.md) separa dívida conhecida de novas violações. Varreduras completas continuam úteis para novas regras, novos modelos e relações que ultrapassam o diff.

## Casos de uso

SAST funciona bem para propriedades expressáveis a partir do código: fluxos de entrada não confiável, uso de APIs perigosas, validações ausentes e outras classes modeláveis estaticamente.

Ele não observa sozinho configuração real de proxy, exposição de rede ou comportamento emergente do ambiente implantado. [DAST](../dast.md) examina outra superfície. [SCA](../sca/index.md) trata componentes de terceiros.

## Seleção de implementação

Compare linguagens suportadas, profundidade semântica, autoria de regras, integração com revisão, tempo de execução, qualidade dos modelos de frameworks e custo.

[CodeQL](codeql.md) é uma implementação orientada a consultas sobre uma representação semântica do código. [SonarQube](sonarqube.md) combina análise de código com qualidade e manutenção. Outras ferramentas ocupam pontos diferentes entre regras estruturais, data flow e plataformas integradas de qualidade.

## Boas práticas

Comece por regras de alta confiança; execute cedo; preserve contexto do finding; modele frameworks internos quando necessário; revise suppressions; combine severidade com reachability e contexto.

## Más práticas

"Zero findings" não prova segurança. Bloquear toda regra no primeiro dia pode inviabilizar adoção. Contar findings como produtividade incentiva comportamento ruim. SAST não substitui threat modeling, revisão de arquitetura ou testes em runtime.

## Fontes

- OWASP Source Code Analysis Tools: <https://owasp.org/www-community/Source_Code_Analysis_Tools>
- CodeQL documentation: <https://codeql.github.com/docs/>

## Continue por aqui

Escolha a técnica que precisa entender, como [taint analysis](taint-analysis.md), ou siga para uma implementação como [CodeQL](codeql.md) ou [SonarQube](sonarqube.md).
