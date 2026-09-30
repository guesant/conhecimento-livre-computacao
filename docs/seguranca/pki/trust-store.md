# Trust store

Um trust store contém âncoras que um sistema aceita para determinados processos de validação.

Sistemas operacionais, runtimes, browsers e aplicações podem usar stores diferentes. Instalar uma CA no sistema não garante que toda aplicação use automaticamente esse store.

## Operação

Distribuir confiança é uma responsabilidade distinta de emitir certificados. Rotação pode exigir período de sobreposição em que clientes confiam simultaneamente na cadeia antiga e na nova.

## Continue por aqui

[trust-manager](trust-manager.md) automatiza distribuição em Kubernetes. [Cadeia de certificados](certificate-chain.md) explica como a âncora participa da validação.
