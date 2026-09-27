# Kyverno

Kyverno é um engine de políticas para Kubernetes que usa recursos nativos do
cluster para validar, mutar, gerar e verificar objetos. Suas políticas são
escritas em YAML e usam padrões próximos da estrutura dos manifests.

## Uso

Ele pode exigir labels, restringir imagens, aplicar defaults e gerar recursos
relacionados. A política deve declarar escopo, modo de aplicação e o efeito de
uma violação.

## Limites

Kyverno não protege uma aplicação contra toda alteração feita depois do
admission. Combine-o com RBAC, segurança de workload, auditoria e controles de
runtime.

## Fonte

- [Documentação do Kyverno](https://kyverno.io/docs/)
