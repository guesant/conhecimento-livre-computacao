# Tipos de clone

Um clone é um trecho repetido de código ou configuração. A classificação
indica quanto as duas cópias divergem e ajuda a escolher entre uma correção
automática, uma revisão arquitetural ou uma investigação manual.

| Tipo | Diferença entre cópias | Tratamento no jscpd |
| --- | --- | --- |
| Type-1 | Espaçamento, layout e comentários | Detecção padrão de clones exatos |
| Type-2 | Nomes de identificadores, literais e anotações | Opções como `--ignore-identifiers`, `--ignore-literals` e `--ignore-annotations` |
| Type-3 | Linhas adicionadas, removidas ou alteradas | `--max-gap-lines` e comparação sintática com `--similarity` |
| Type-4 | Mesmo comportamento com implementação diferente | Fora do alcance de um detector baseado em tokens |

Type-1 é o melhor candidato a um gate determinístico, porque o resultado é
estável e a repetição costuma ser inequívoca. Type-2 é útil para localizar
cópias parametrizadas durante uma refatoração, mas pode capturar padrões
legítimos. Type-3 deve ser tratado como investigação e não como prova
automática de duplicação arquitetural. Type-4 exige análise semântica,
testes ou revisão humana.

## Fonte primária

- [Tipos de clone no jscpd](https://jscpd.dev/guides/clone-types)
