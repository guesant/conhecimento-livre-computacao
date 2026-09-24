# Policy enforcement

Policy enforcement impede ou altera a admissão de recursos que violam regras
do ambiente. No Kubernetes, a validação pode ocorrer no admission control por
meio de Pod Security Admission, webhooks ou engines de policy as code.

Pod Security Admission é integrado ao Kubernetes e aplica os níveis das Pod
Security Standards por namespace. Kyverno e Gatekeeper ampliam esse modelo com
políticas próprias, validação de campos e, quando habilitado com cuidado,
mutação de recursos.

Uma política de admissão não substitui validação de schema, revisão de código,
scan de imagem ou observabilidade. Cada camada encontra uma classe diferente
de problema e deve ser colocada no ponto em que a informação necessária existe.

## Relações

- [Kubescape](kubescape.md) avalia postura e conformidade, mas não é por si só
  o admission controller.
- [Admission control](../../kubernetes/extensibility/admission-control.md)
  explica o ponto de extensão da API.
- [Policy as code](../../qualidade/validacao/policy-as-code.md) trata da
  validação declarativa fora ou antes do cluster.

## Fontes primárias

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Kyverno](https://kyverno.io/docs/)
- [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)
