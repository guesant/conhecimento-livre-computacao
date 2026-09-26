# Composição: secret stores externos

Um secret store externo mantém o valor sensível fora do repositório e fora do
cluster consumidor. Um operator ou controlador busca o valor e materializa o
resultado como um `Secret` Kubernetes, preservando uma interface local para o
workload.

## Componentes

- [External Secrets Operator](seguranca/secrets/external-secrets.md) fornece
  uma API declarativa comum para múltiplos backends.
- [Vault](seguranca/secrets/vault.md) e [OpenBao](seguranca/secrets/openbao.md)
  fornecem armazenamento centralizado, políticas e auditoria.
- [Infisical](seguranca/secrets/infisical.md) combina backend, interface de
  equipes e operator específico.
- [Auto-unseal e KMS](seguranca/secrets/auto-unseal.md) trata o destravamento
  de backends que protegem a chave interna com um serviço externo.

## Fluxo de entrega

O backend autentica o operator ou o workload, o recurso declarativo informa
qual caminho consultar e o controlador cria ou atualiza o `Secret` local. A
identidade deve usar menor privilégio, e o ciclo de rotação precisa considerar
tanto o backend quanto o Secret materializado.

## Trade-offs

Essa composição reduz a exposição de valores no Git e centraliza auditoria,
mas acrescenta uma dependência de disponibilidade, autenticação e rede. Um
backend externo não elimina bootstrap, backup ou recuperação. Em ambientes
pequenos, [SOPS e age](criptografia-de-segredos-no-git.md) podem oferecer uma
cadeia operacional menor.

O cluster deste repositório usa SOPS com age. As alternativas desta página
documentam conhecimento geral e não representam uma dependência da
arquitetura atual.
