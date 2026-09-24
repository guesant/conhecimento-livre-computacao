# Kubernetes API server

O API server é a porta de entrada do control plane. Ele autentica e autoriza
requisições, aplica admission control, valida objetos, persiste o estado no
datastore e expõe a API que kubectl, controllers, kubelets e operadores
consomem.

## Request path

Uma requisição passa por autenticação, autorização, admission e validação antes
de ser persistida. Ler o estado do API server não significa ler diretamente o
datastore. O servidor aplica regras de versão, conversão, watch e controle de
concorrência que fazem parte do contrato da API.

Watch permite que controllers recebam mudanças sem polling completo. Se o
cliente perde o histórico disponível, precisa relistar e retomar a partir de
um resource version compatível. Clientes robustos tratam encerramento de watch,
throttling e conflitos como estados normais do sistema distribuído.

## Disponibilidade e segurança

O API server é stateless em relação ao conteúdo persistido, mas depende do
datastore e da rede do cluster. TLS, autenticação forte, RBAC, admission policy
e exposição mínima determinam o risco real. Abrir a API para uma rede ampla sem
limitar identidades transforma todo bug de cliente em uma possível alteração
de cluster.

## Relações

- [etcd](etcd.md) persiste o estado da API.
- [Admission control](../extensibility/admission-control.md) intercepta
  requisições antes da persistência.
- [Controller](controller.md) observa recursos e reconcilia o estado.

## Fonte primária

- [Kubernetes API overview](https://kubernetes.io/docs/reference/using-api/)
