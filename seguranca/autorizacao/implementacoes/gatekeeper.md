# OPA Gatekeeper

OPA Gatekeeper integra Open Policy Agent ao admission control do Kubernetes.
Ele usa recursos customizados para declarar constraints e templates que
validam objetos antes de serem persistidos no cluster.

## Modelo

Um template define a lógica de validação e uma constraint escolhe onde e como
ela se aplica. O webhook recebe o objeto, avalia a política e pode rejeitar a
operação.

## Limites

Gatekeeper controla admission, não substitui autorização de runtime nem
NetworkPolicy. Mudanças em constraints podem impedir deploys existentes, então
devem ser testadas em modo de auditoria antes de bloquear.

## Fonte

- [Documentação do Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/)
