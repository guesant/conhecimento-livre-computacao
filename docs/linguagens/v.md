# V

V é uma linguagem compilada de tipagem estática, com sintaxe concisa, builds
rápidos e foco em produzir binários nativos. O compilador e a biblioteca
padrão fazem parte de uma toolchain que também inclui módulos, testes,
formatação e ferramentas de documentação.

O nome da linguagem não deve ser confundido com uma versão ou com a letra usada
para representar variáveis em outros contextos. Em documentação e scripts,
registre a versão do compilador e a revisão dos módulos para que o build possa
ser reproduzido.

## Modelo da linguagem

V combina tipos estáticos, structs, enums, interfaces, funções de primeira
classe e composição. O compilador verifica boa parte dos erros de tipo antes da
execução. Inferência de tipos pode reduzir repetição, mas não elimina a
necessidade de declarar contratos estáveis nas fronteiras de módulos e APIs.

A linguagem oferece recursos de mutabilidade, option e result para representar
ausência e falhas de forma explícita. A aplicação ainda precisa classificar
erros, definir retries e liberar recursos externos, pois um tipo de erro não
substitui uma política operacional.

## Build e dependências

O fluxo de desenvolvimento normalmente passa pelo compilador V, pelos módulos,
testes e pelo formatador. A velocidade de compilação é uma vantagem quando o
ciclo de edição e validação é frequente, mas um build reproduzível também exige
fixar versão do compilador, dependências, flags, ambiente e imagem base.

Não trate um executável nativo como prova de independência total do sistema.
Verifique libc, loader, certificados, timezone, arquivos de configuração e
arquitetura alvo. Um binário pode ser estaticamente vinculado em um cenário e
ainda depender de recursos externos em produção.

## Concorrência e sistemas

V oferece mecanismos para escrever aplicações concorrentes e pode ser usado em
ferramentas de sistema, serviços e aplicações nativas. Antes de criar uma
thread ou tarefa por requisição, estabeleça limites de concorrência, filas,
cancelamento e timeouts. O desempenho final depende do scheduler do runtime,
do sistema operacional, do I/O e do padrão de alocação.

Para um serviço, documente o modelo de supervisão, o comportamento em caso de
panic ou erro fatal, a política de encerramento e a forma de coletar logs e
métricas. A linguagem não remove os problemas de backpressure, starvation,
deadlock ou vazamento de recursos.

## Interoperabilidade e adoção

V pode ser interessante para ferramentas de linha de comando e serviços que
precisam de binários simples e uma linguagem compilada com ciclo curto. Avalie
com cuidado a maturidade das bibliotecas necessárias, a estabilidade dos
contratos, o suporte a plataformas e a capacidade da equipe de manter módulos
de terceiros.

Quando o ecossistema e a disponibilidade de profissionais forem requisitos
dominantes, Go, Rust, C#, Java ou outra linguagem consolidada podem reduzir
risco. Quando o objetivo for experimentar V, isole o componente e defina uma
fronteira de integração que permita substituí-lo.

## Relações

- [Go](go.md) privilegia simplicidade, toolchain integrada e serviços nativos.
- [Rust](rust.md) oferece verificações de ownership e borrowing mais fortes.
- [D](d.md) combina recursos de alto nível com integração de sistemas.
- [Sistemas de build](../build/sistemas-de-build/index.md) explica como
  compilação, toolchain e artefatos entram no ciclo de entrega.

## Fontes primárias

- [V Language](https://vlang.io/)
- [V documentation](https://docs.vlang.io/)
- [V source repository](https://github.com/vlang/v)
