# Cerbos

Cerbos é um policy decision point independente para autorização contextual.
Ele avalia políticas declarativas usando atributos do principal, do recurso e
da requisição.

## Modelo

Uma decisão pode combinar papéis, atributos, ações, recursos e contexto. As
políticas podem ser distribuídas como arquivos versionados e avaliadas por
instâncias do PDP próximas dos serviços.

## Operação

A implantação deve definir como políticas são carregadas, validadas,
atualizadas e revertidas. Logs de decisão precisam evitar segredos e permitir
correlacionar a versão da política com a resposta.

## Fonte

- [Documentação do Cerbos](https://www.cerbos.dev/docs/)
