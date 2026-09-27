# Contextual authorization

Contextual authorization usa dados da requisição ou do ambiente para decidir
acesso. Exemplos são horário, local, dispositivo, nível de risco e estado do
recurso.

## Cuidados

O contexto precisa ter origem confiável, validade e semântica clara. Uma policy
que aceita headers enviados livremente pelo cliente cria uma aparência de
segurança sem proteção real.

## Trade-off

Contexto melhora precisão, mas aumenta dependências e dificulta cache. Registre
os atributos relevantes para explicar uma decisão sem armazenar dados excessivos.
