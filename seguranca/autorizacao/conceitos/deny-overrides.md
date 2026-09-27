# Deny-overrides

Deny-overrides é um algoritmo de combinação em que uma negação explícita
prevalece sobre qualquer permissão encontrada.

## Uso

É apropriado quando uma exceção de bloqueio deve sempre vencer uma regra geral
de allow. A ordem dos documentos deixa de ser suficiente para explicar a
decisão, pois a precedência faz parte do algoritmo.

## Cuidado

Negação ampla pode bloquear operações legítimas sem mensagem clara. A policy
deve informar a razão e permitir auditoria da regra que venceu.
