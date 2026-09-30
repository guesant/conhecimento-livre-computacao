# CustomResourceDefinition

CustomResourceDefinition, CRD, estende a API Kubernetes com um novo tipo de
recurso. O CRD define schema, nomes, versões e escopo. Instâncias desse tipo
passam a ser objetos consultáveis pela API, mas o CRD sozinho não implementa
comportamento operacional.

## CRD e controller

O CRD declara dados e validação. Um [controller](../control-plane/controller.md)
observa as instâncias e reconcilia o efeito desejado. Sem controller, o objeto
pode ser armazenado e lido, mas não cria Pods, volumes, certificados ou outros
efeitos por conta própria.

Status deve representar observações do controller e spec deve representar a
intenção do usuário. Misturar os dois dificulta ownership, automação e
diagnóstico. Schemas estruturais também protegem a API contra dados que o
controller não consegue interpretar.

## Lifecycle e versões

Alterar o schema ou remover uma versão pode exigir conversão e migração de
instâncias existentes. Excluir um CRD pode remover suas instâncias, conforme o
comportamento do cluster e dos recursos dependentes. CRDs de operadores
terceiros precisam ser tratados como parte da superfície de upgrade do cluster.

## Relações

- [Operator](../../kubernetes-operators.md) combina CRD e controller.
- [Admission control](admission-control.md) valida ou muta requisições.
- [API server](../control-plane/api-server.md) expõe o novo tipo.

## Fonte primária

- [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
