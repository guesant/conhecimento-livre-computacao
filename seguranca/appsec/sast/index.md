# SAST

Static Application Security Testing analisa código ou representações derivadas dele sem precisar exercitar a aplicação como um atacante externo. A família vai de regras sintáticas simples a análise semântica interprocedural e rastreamento de fluxo de dados.

## O problema

Muitas vulnerabilidades surgem da relação entre uma entrada controlável e uma operação sensível. Revisão humana encontra parte delas, mas software grande possui caminhos demais para inspecionar manualmente a cada mudança.

SAST automatiza hipóteses sobre código. Ele não prova ausência de vulnerabilidades; procura classes de padrões dentro do modelo que a ferramenta consegue representar.

## Níveis de análise

Regras textuais procuram sequências de texto e são baratas, mas ignoram estrutura. AST entende construções da linguagem. Control-flow graphs representam caminhos de execução. Data-flow acompanha valores. Taint analysis modela sources, propagação, sanitizers e sinks.

Quanto mais semântica a análise incorpora, maior pode ser sua capacidade de encontrar relações não locais, e também maior o custo de modelagem e execução.

## Exemplo conceitual

Uma entrada HTTP é uma source. Uma função que monta e executa SQL pode ser sink. A análise procura um caminho em que dado não confiável chega ao sink sem passar por um sanitizer ou API segura reconhecida.

Se a aplicação usa uma abstração interna desconhecida pela ferramenta, o fluxo pode ser perdido até que o modelo seja ensinado.

## Casos de uso

SAST funciona bem para vulnerabilidades expressáveis como propriedades do código: injection, uso de APIs perigosas, validações ausentes e fluxos sensíveis. É especialmente útil cedo no desenvolvimento porque não depende de ambiente implantado.

## Quando não basta

Configuração do proxy em produção, autenticação realmente exposta na rede, comportamento de WAF e vulnerabilidades que só emergem da composição em runtime podem exigir DAST, testes manuais ou análise de infraestrutura.

Dependências vulneráveis são responsabilidade primária de SCA, embora algumas plataformas apresentem ambos os resultados na mesma UI.

## Estratégia de adoção

Comece com regras de alta confiança e superfícies críticas. Meça ruído. Modele frameworks internos quando necessário. Expanda cobertura sem transformar suppressions em rotina automática.

Para código legado, um baseline pode impedir novas violações sem exigir corrigir todo histórico antes de adotar o gate. O baseline deve ser dívida visível, não lixeira permanente.

## Pull request versus varredura completa

Análise incremental em PR reduz feedback e foca mudanças. Varreduras completas periódicas encontram efeitos de novas regras, novas versões do engine e fluxos que atravessam código não alterado.

Os dois modos respondem riscos diferentes e podem coexistir.

## Boas práticas

Execute perto do desenvolvedor e novamente em CI quando o risco justificar. Fixe versão da ferramenta/regras. Preserve localização e caminho de dados no finding. Revise suppressions. Trate severidade junto com reachability e contexto.

## Más práticas

Bloquear todo finding desde o primeiro dia; desabilitar a ferramenta depois do primeiro lote de falsos positivos; contar findings como métrica de produtividade; usar SAST como substituto de revisão de design; considerar "zero findings" prova de segurança.

## Ferramentas e modos

[CodeQL](codeql.md) modela código como uma base consultável e oferece análise semântica/dataflow profunda. Semgrep oferece regras estruturais e capacidades de dataflow com uma experiência diferente de autoria. SonarQube/SonarCloud combinam qualidade e segurança numa plataforma de análise.

A escolha depende de linguagens, profundidade necessária, facilidade de criar regras, integração com revisão, custo e tolerância a tempo de análise.

## Fontes

- OWASP Static Application Security Testing: https://owasp.org/www-community/Source_Code_Analysis_Tools
- CodeQL documentation: https://codeql.github.com/docs/

## Continue por aqui

[CodeQL](codeql.md) aprofunda uma implementação. [Segurança de aplicações](../index.md) situa SAST junto de SCA, DAST e secret scanning.