# GitOps

GitOps usa um sistema versionado como fonte declarativa do estado desejado e
um agente que reconcilia esse estado no ambiente. A revisão do Git se torna a
revisão da mudança, enquanto o cluster aplica o resultado por um caminho
controlado.

## Propriedades

O modelo reduz credenciais de escrita em pipelines externas quando o agente
pull-based já está dentro do ambiente. Também cria uma trilha de auditoria,
repetibilidade e uma forma explícita de recuperar estado após reconstrução.

GitOps não significa que todo dado deve ser colocado no Git. Segredos podem
ser referenciados ou cifrados, e estado dinâmico deve permanecer sob o sistema
que o administra.

## Limites

Uma mudança manual pode ser revertida por self-heal. Uma configuração que
aplica automaticamente qualquer commit amplia o raio de dano de uma revisão
errada. O fluxo precisa de revisão, validação, promoção e observabilidade.

## Relações

- [Reconciliação](reconciliation.md) converge desejado e observado.
- [Entrega pull-based](pull-based-delivery.md) explica a direção de acesso.
- [Argo CD](../argocd.md) é uma implementação para Kubernetes.
- [Argo CD e Flux](../comparacoes/entrega/argocd-flux.md) compara implementações.

## Fonte primária

- [OpenGitOps principles](https://opengitops.dev/)
