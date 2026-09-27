# Rust

Rust é uma linguagem de sistemas compilada que busca segurança de memória sem
garbage collector obrigatório. Ownership, borrowing, lifetimes e o borrow
checker verificam relações entre valores durante a compilação. O objetivo não
é tornar qualquer código automaticamente correto: concorrência, lógica de
negócio, FFI, `unsafe` e recursos externos continuam exigindo projeto e
testes.

## Ownership

Cada valor possui um owner. Mover, emprestar por referência imutável ou
mutável e controlar o tempo de vida tornam explícito quem pode acessar e
alterar dados. O compilador rejeita muitas combinações de use-after-free,
double free e data race antes da execução.

O modelo pode exigir reorganização do design. Clonar dados resolve uma
restrição de ownership, mas pode aumentar memória e custo. `Arc`, `Mutex`,
channels e outras estruturas introduzem sincronização que ainda pode gerar
contenção, deadlock ou starvation.

## Unsafe e interoperabilidade

`unsafe` permite operações que o compilador não prova, como dereferenciar
ponteiros crus, implementar traits específicas ou chamar FFI. Ele deve ser
confinado a uma abstração pequena com invariantes documentadas e testes. Código
seguro que chama uma função insegura depende das garantias dessa fronteira.

Bindings C e bibliotecas nativas exigem atenção a layout, ownership, threads,
erros e lifetime. Um tipo Rust não torna uma biblioteca externa segura por
conversão automática.

## Async e build

Rust não define um único runtime async. Crates como Tokio e async-std oferecem
executors, timers e I/O com modelos diferentes. Uma future só executa quando é
pollada por um executor, e cancelar uma future não desfaz automaticamente um
efeito externo já aceito.

Cargo resolve dependências, compila crates, executa testes e produz lockfiles.
Verifique o supply chain, use `cargo audit` ou controles equivalentes e fixe
toolchain quando reprodutibilidade for requisito.

## Casos de uso

Rust é adequado para serviços, ferramentas, sistemas embarcados, componentes
de infraestrutura e bibliotecas que precisam de desempenho e invariantes de
memória fortes. O custo aparece no tempo de aprendizado, no design explícito
de ownership e na integração com bibliotecas que não compartilham o mesmo
modelo.

## Fontes primárias

- [Rust Learn](https://www.rust-lang.org/learn)
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust Reference](https://doc.rust-lang.org/reference/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
