# ValidatingAdmissionPolicy

ValidatingAdmissionPolicy é o recurso nativo do Kubernetes para validar objetos
no admission usando Common Expression Language. A política é associada a um
binding que define recursos, escopo e modo de enforcement.

## Vantagem

A validação ocorre sem instalar um webhook externo para regras que cabem no
modelo expressivo do CEL. Isso reduz componentes operacionais e pontos de
falha no caminho de criação de recursos.

## Limites

Ela não substitui webhooks quando a regra exige chamadas externas, estado
complexo ou efeitos de mutação. Políticas precisam ser testadas antes de usar
efeito bloqueante.

## Fonte

- [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
