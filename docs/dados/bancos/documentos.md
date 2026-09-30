# Bancos de documentos

Document databases armazenam registros como documentos estruturados, frequentemente semelhantes a JSON, e normalmente permitem consultar campos internos e criar índices sobre eles.

## Casos de uso

São adequados quando agregados de dados possuem estrutura flexível e são frequentemente lidos e atualizados como documentos, sem exigir o mesmo modelo relacional de joins e constraints.

## Boa prática

Projete documentos a partir dos padrões de acesso e compreenda limites de tamanho, atomicidade e índices da implementação escolhida.

## Má prática

"Schema flexible" não significa "sem schema". Deixar toda validação implícita na aplicação pode produzir documentos incompatíveis ao longo do tempo.

## Continue por aqui

[Key-value](key-value.md) representa um modelo mais simples de acesso por chave.
