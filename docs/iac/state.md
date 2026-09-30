# State de infraestrutura

O state associa recursos declarados à identidade e aos atributos observados na
infraestrutura. Ele permite que a ferramenta saiba se um recurso existente
corresponde ao bloco declarado e calcule o próximo plano.

## Responsabilidade

State não é simplesmente um cache descartável. Ele pode conter IDs, atributos
sensíveis e metadados necessários para atualizar ou remover recursos. Perder o
state pode separar a configuração do que já existe; restaurar uma cópia
incorreta pode fazer o plano propor criação, alteração ou destruição indevida.

Use backend com controle de acesso, versionamento, backup e lock quando houver
mais de uma execução ou quando o recurso for importante.

## Drift e importação

Uma alteração fora da ferramenta pode aparecer como drift se o provider
conseguir observá-la. Um recurso criado antes do código pode precisar de
importação, que associa a identidade real a uma declaração sem necessariamente
alterar o recurso no primeiro passo.

## Relações

- [State locking](state-locking.md) protege concorrência.
- [Drift](drift.md) trata diferença entre state, configuração e realidade.
- [Provider](provider.md) consulta e altera a API do recurso.

## Fonte primária

- [OpenTofu state](https://opentofu.org/docs/language/state/)
