# Admission control

Admission control intercepta requisições depois de autenticação e autorização
e antes de persistir o objeto. Admissão pode rejeitar, mutar ou validar um
recurso conforme policy, defaults, segurança e dependências externas.

## Mutating e validating

Mutating admission altera a requisição, por exemplo adicionando defaults ou
injeções. Validating admission decide se o resultado é aceito. A ordem e o
comportamento dos webhooks fazem parte da disponibilidade da API, porque um
webhook lento ou indisponível pode atrasar ou bloquear operações.

## Segurança

Admission é um ponto de enforcement, não uma substituição de autorização.
Policies precisam limitar escopo e evitar mutações surpreendentes. Webhooks
devem ter timeout, failure policy e observabilidade coerentes com o risco da
regra. Se a policy é crítica para segurança, aceitar falha silenciosamente pode
ser pior que rejeitar temporariamente uma requisição.

## Relações

- [API server](../control-plane/api-server.md) executa a cadeia de request.
- [CRD](crd.md) pode definir schemas e tipos próprios.
- [Pod Security](../seguranca/security-context.md) é uma família de controles
  que pode ser aplicada por admission.

## Fonte primária

- [Admission Control in Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
