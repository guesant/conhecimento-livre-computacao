# Rego

Rego é a linguagem de políticas do Open Policy Agent. Ela consulta documentos
estruturados e produz decisões ou dados derivados a partir de regras
declarativas.

## Modelo mental

Rego trabalha com conjuntos, objetos, regras e compreensões. A política não
deve depender de efeitos colaterais nem de uma ordem imperativa de execução.
Entradas devem ser estáveis, pequenas e documentadas para evitar decisões
inconsistentes entre consumidores.

## Qualidade

Teste políticas com casos permitidos, negados, campos ausentes, tipos
inesperados e combinações de contexto. Valide também o custo de avaliação e a
forma como políticas são empacotadas e distribuídas.

## Fonte

- [Linguagem Rego](https://www.openpolicyagent.org/docs/latest/policy-language/)
