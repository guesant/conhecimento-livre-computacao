# Secret como credencial

Secret é um valor que precisa de confidencialidade, integridade ou controle de
acesso mais forte que configuração comum. Exemplos incluem chaves privadas,
tokens, senhas, credenciais de banco e material de bootstrap.

## Propriedades

Classifique segredo por consumidor, duração, privilégio, impacto de exposição e
necessidade de rotação. Um valor público ou apenas operacional não deve ser
tratado como segredo por hábito, pois isso obscurece os casos de alto risco.

Cifrar em repouso protege armazenamento, não uso. O valor pode aparecer no
processo, no ambiente, no arquivo montado, no log ou numa ferramenta que o
imprima.

## Kubernetes

Secret do Kubernetes é um objeto de API. Base64 é codificação, não
confidencialidade. Controle de acesso, cifragem do etcd, auditoria e política
de distribuição definem a proteção real.

## Relações

- [Gerenciamento de segredos](index.md) cobre o lifecycle.
- [Bootstrap](bootstrap.md) entrega a primeira credencial.
- [RBAC Kubernetes](../../kubernetes/access/rbac.md) limita acesso à API.

## Fonte primária

- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
