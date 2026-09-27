# Default deny

Default deny significa negar uma operação quando nenhuma policy aplicável
concede explicitamente o acesso. É uma base para evitar que novos recursos ou
ações sejam expostos por omissão.

## Aplicação

O padrão deve valer para rotas, roles, policies, buckets, filas e operações de
banco. Exceções precisam ser explícitas, revisadas e cobertas por testes.

## Falhas

Default deny não corrige uma policy que autoriza o sujeito errado ou um PEP que
não aplica a decisão. Ele apenas define o comportamento quando não existe uma
concessão.
