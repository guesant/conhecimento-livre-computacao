# Read-only root filesystem

readOnlyRootFilesystem impede escrita no filesystem raiz do container.

Aplicações que precisam escrever devem receber locais explícitos, como volumes para dados temporários ou persistentes.

Isso reduz persistência e modificação do ambiente após comprometimento, mas não impede escrita nos volumes que continuam montados como graváveis.
