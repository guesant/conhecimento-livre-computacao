# Source em taint analysis

Uma source é um ponto em que um dado recebe a marca acompanhada pela análise.

Em segurança, exemplos comuns são parâmetros HTTP, corpo de requisição, dados vindos de arquivos ou mensagens externas. O fato de uma entrada ser source não significa que ela seja maliciosa; significa que o modelo decidiu tratá-la como não confiável ou relevante.

Uma mesma API pode ser source para uma regra e irrelevante para outra. O conceito só faz sentido em relação à propriedade que a análise acompanha.

## Continue por aqui

[Taint analysis](taint-analysis.md), [sink](sink.md) e [sanitizer](sanitizer.md) completam o modelo.