# D

D é uma linguagem compilada de sistemas que combina controle de baixo nível,
templates, metaprogramação, orientação a objetos, programação funcional e
recursos de segurança selecionáveis. Ela pode interoperar com C e C++ e
produzir binários nativos, mas também oferece um garbage collector e
abstrações de alto nível.

## Memória e segurança

O garbage collector simplifica parte da gestão de memória, mas não elimina a
necessidade de entender alocações, latência, ownership lógico e recursos
externos. `@safe`, `@trusted` e `@system` permitem separar código com regras de
segurança diferentes. Um bloco `@trusted` deve ser pequeno, revisado e testado,
pois ele concentra a ponte para operações que o compilador não consegue
verificar.

`@nogc` pode ser usado quando um caminho não deve provocar coleta, mas não é um
atalho universal para performance. O código precisa controlar alocações e
interfaces manualmente, incluindo erros e cleanup.

## Metaprogramação e build

Templates, mixins e compile-time function evaluation permitem gerar código e
validar propriedades durante a compilação. Essas técnicas podem reduzir
repetição, mas também aumentam tempo de build e dificultam diagnósticos quando
usadas sem limites.

O ecossistema inclui compiladores, DUB, bibliotecas e bindings para C. Registre
compilador, runtime, flags e dependências para que o binário possa ser
reproduzido. Avalie ABI, libc, threads e suporte do sistema alvo.

## Casos de uso

D pode servir a ferramentas nativas, serviços de alto desempenho, aplicações
de sistemas e código que precisa de expressividade sem abrir mão de controle.
É menos adequado quando o projeto depende de um ecossistema corporativo muito
específico ou de uma oferta de bibliotecas que a equipe não consegue manter.

## Fonte primária

- [D Programming Language](https://dlang.org/)
- [D language specification](https://dlang.org/spec/spec.html)
