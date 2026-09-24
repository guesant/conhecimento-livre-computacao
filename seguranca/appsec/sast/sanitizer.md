# Sanitizer em taint analysis

Um sanitizer é uma operação que torna um dado aceitável para uma classe específica de uso segundo o modelo da análise.

Sanitização é contextual. Escapar HTML não torna uma string segura para uma query SQL; validar um identificador numérico não resolve todos os contextos de shell.

Ferramentas de SAST precisam reconhecer sanitizers de frameworks e abstrações locais para modelar corretamente o fluxo.

## Continue por aqui

[Taint analysis](taint-analysis.md), [source](source.md) e [sink](sink.md) completam o modelo.
