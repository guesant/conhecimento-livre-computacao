# OPAL

OPAL é uma camada de distribuição de políticas e dados para OPA. Ela ajuda a
propagar mudanças para agentes que precisam tomar decisões localmente.

## Problema

Um PDP local tem baixa latência, mas precisa receber políticas e dados novos.
OPAL coordena essa distribuição e pode emitir eventos quando uma fonte de
política ou de dados muda.

## Trade-offs

Distribuição assíncrona cria uma janela em que agentes possuem versões
diferentes. A arquitetura deve definir revisão, observabilidade, reprocessamento
e comportamento quando o agente está desatualizado.

## Fonte

- [OPAL](https://www.opal.ac/)
