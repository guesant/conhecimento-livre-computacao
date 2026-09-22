# Sink em taint analysis

Um sink é uma operação na qual a chegada de determinado dado pode produzir o efeito que a análise procura detectar.

Execução de SQL, comandos do sistema, construção de HTML ou acesso a filesystem podem ser sinks para classes diferentes de vulnerabilidade.

Um sink não é universalmente inseguro. O risco depende do dado que chega, da API usada e da propriedade analisada.

## Continue por aqui

[Taint analysis](taint-analysis.md), [source](source.md) e [sanitizer](sanitizer.md) completam o modelo.