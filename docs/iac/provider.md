# Provider

Um provider traduz recursos declarativos em chamadas para uma API externa. Ele
define schemas, autenticação, leitura, criação, atualização e remoção de
recursos.

## Contrato

O schema do provider determina quais atributos são configuráveis, calculados,
sensíveis ou substituíveis. A versão do provider é parte da reprodutibilidade;
uma mudança pode alterar defaults, validação ou comportamento de leitura.

Credenciais pertencem ao ambiente de execução e não à configuração versionada.
A autenticação precisa ter menor privilégio e escopo compatível com o recurso.

## Failure modes

Um provider pode falhar por credencial, rate limit, recurso ausente, mudança de
API, diferença regional ou leitura incompleta. Antes de alterar a configuração,
separe erro de acesso de erro de plano.

## Relações

- [Resource](resource.md) declara um objeto administrado.
- [Data source](data-source.md) lê sem administrar.
- [State](state.md) conserva o vínculo com a API.

## Fonte primária

- [OpenTofu providers](https://opentofu.org/docs/language/providers/)
