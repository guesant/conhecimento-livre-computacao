# commitlint

commitlint valida mensagens de commit contra uma convenção configurada. Ele
transforma o histórico em uma interface previsível para changelog,
versionamento, automações e revisão humana.

## Contrato da mensagem

Uma convenção pode exigir tipo, escopo, descrição, tamanho e regras para
breaking changes. O contrato precisa ser menor que o conjunto de metadados que
os consumidores realmente usam. Quanto mais regras sem consumidor, maior a
chance de mensagens artificiais e de exceções recorrentes.

O lint deve executar no ponto mais próximo da criação da mensagem e novamente
na CI quando o histórico for uma entrada de automação. Hooks locais melhoram o
feedback, mas não substituem a validação em um ambiente confiável.

## Integração

Configure a mesma convenção no repositório, nos hooks e no workflow. Quando o
projeto usa squash merge, defina se o gate valida a mensagem do commit final,
os commits individuais ou ambos. Essa decisão evita que a política verifique
um artefato que não chega ao histórico principal.

## Failure modes

Falhas frequentes vêm de tipos não previstos, descrições vazias, escopos que
não existem ou diferenças entre a configuração local e a instalada na CI.
Diagnostique imprimindo a configuração efetiva, a mensagem exata e a versão
do parser. Não corrija o problema com uma regra permissiva global sem verificar
qual consumidor depende da convenção.

## Relações

- [Manutenção de repositório](index.md) agrupa as práticas de qualidade do
  histórico e dos links.
- [CI](../../../arquitetura/ci.md) explica como os gates deste repositório são
  encadeados.

## Fonte primária

- [commitlint](https://commitlint.js.org/)
