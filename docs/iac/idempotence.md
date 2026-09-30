# Idempotência

Uma operação idempotente pode ser executada novamente sem mudar o resultado
depois que o estado desejado já foi alcançado. Isso não significa que toda
execução é sem efeito: a primeira execução pode criar ou alterar recursos.

## Limites

Idempotência depende da ferramenta e do recurso. Um script que sempre gera uma
senha nova, um timestamp novo ou um nome aleatório pode produzir mudança em
toda execução. Um provider que não lê corretamente o estado real também pode
planejar alterações repetidas.

A propriedade não torna uma operação segura. Uma declaração idempotente pode
destruir e recriar um recurso quando a mudança exige isso. O plano precisa ser
revisado antes do apply.

## Diagnóstico

Execute duas vezes sobre o mesmo estado e compare plano, saída e mudanças
externas. Quando há diferença, identifique valor não determinístico, drift,
provider, dependência implícita ou recurso fora do escopo.

## Relações

- [Estado desejado](desired-state.md) define o resultado.
- [State](state.md) registra identidade e atributos conhecidos.
- [Ansible](../ansible.md) implementa idempotência em módulos.

## Fonte primária

- [OpenTofu resource behavior](https://opentofu.org/docs/language/resources/)
