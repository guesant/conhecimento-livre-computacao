# Bun

Bun é um runtime e toolkit para JavaScript e TypeScript que reúne execução,
package manager, bundler e test runner. Ele busca inicialização rápida e
integração compacta, mas não deve ser tratado como uma substituição automática
de qualquer aplicação Node.

## Compatibilidade

Bun implementa APIs JavaScript e fornece APIs próprias. A compatibilidade com
Node, Web APIs, módulos, loaders nativos e pacotes que dependem de detalhes de
Node precisa ser testada. Uma aplicação que usa `fs`, native addons, streams,
timers, subprocessos ou comportamento específico de CommonJS pode exigir
adapters.

O runtime usado em desenvolvimento deve ser o mesmo usado no build e no
deploy, ou a diferença deve ser uma parte explícita da matriz de testes. Não
use a velocidade de instalação do Bun como evidência de compatibilidade de
produção.

## Toolchain integrada

O package manager, o bundler e o test runner podem simplificar projetos
pequenos e reduzir configuração. Lockfiles e scripts ainda precisam ser
revisados. Scripts de instalação têm acesso ao ambiente de build e devem ser
tratados como código de supply chain.

## Desempenho e operação

Meça startup, throughput, latência de cauda, memória, compatibilidade e tempo
de build no workload real. Um runtime mais rápido em um benchmark isolado pode
perder a vantagem se o gargalo estiver no banco, no proxy, na serialização ou
em uma dependência externa.

Configure graceful shutdown, timeouts, limites de concorrência e observabilidade
como faria em qualquer servidor JavaScript. Diferencie APIs suportadas pelo
runtime de APIs providas por um framework instalado por cima dele.

## Fonte primária

- [Bun documentation](https://bun.sh/docs)
- [Bun runtime APIs](https://bun.sh/docs/runtime)
- [Bun package manager](https://bun.sh/docs/pm/cli)
