# malloc

`malloc` é a interface C para solicitar memória dinâmica ao processo. O
alocador mantém metadados, arenas, caches e regiões obtidas do kernel por
interfaces como `brk` ou `mmap`. A implementação pode variar entre libc e
versões; o contrato da função não garante um algoritmo ou uma latência fixa.

## Contrato

`malloc(0)` possui comportamento permitido que não deve ser tratado como uma
alocação comum. `free(NULL)` é seguro; liberar duas vezes, usar depois de
liberar, escrever além do bloco ou misturar allocators é erro de memória. O
tamanho retornado inclui alinhamento necessário para os tipos suportados.

`calloc` também verifica multiplicação e inicializa bytes; `realloc` pode mover
o bloco e deixa o ponteiro antigo inválido quando tem sucesso. Use um temporário
ao atribuir o resultado de `realloc`, para não perder a referência quando a
operação falhar.

## Fragmentação e desempenho

Fragmentação interna desperdiça espaço por alinhamento e classes de tamanho.
Fragmentação externa impede uma reutilização simples apesar de haver memória
livre. Alocações de tamanhos variados, ciclos de vida diferentes e threads
podem criar contenção ou muitos mapeamentos. Medir RSS, heap, page faults e
perfil de alocações é mais útil que escolher um alocador por reputação.

Um processo pode ter memória virtual disponível e falhar em uma alocação por
limite de address space, cgroup, overcommit, quota ou pressão física. O retorno
`NULL` precisa ser tratado em caminhos nos quais recuperação é possível.

## Segurança

Erros de heap são uma fonte importante de vulnerabilidades. Sanitizers, hardening
da libc, allocator debugging e fuzzing ajudam a encontrar corrupção, mas não
substituem ownership, limites e lifetime corretos. Dados secretos devem ser
apagados conscientemente, lembrando que cópias podem existir em buffers,
registers, swap ou dumps.

## Relações

- [libc](libc.md) fornece a API e escolhe a implementação.
- [Pthread](pthread.md) compartilha o heap entre threads.
- [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) detecta vários erros de memória.

## Fontes primárias

- [malloc(3)](https://man7.org/linux/man-pages/man3/malloc.3.html)
- [The GNU C Library malloc](https://sourceware.org/glibc/wiki/MallocInternals)
- [C standard memory management](https://en.cppreference.com/w/c/memory)
