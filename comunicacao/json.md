# JSON

JSON, JavaScript Object Notation, é um formato textual, independente de
linguagem, para representar dados estruturados. Ele define objetos, arrays,
strings, números, booleanos e `null`. JSON não define transporte, autenticação,
schema de negócio, paginação, versionamento ou semântica de uma API.

Essa distinção é importante: uma resposta HTTP pode usar JSON, mas HTTP e JSON
resolvem problemas diferentes. Um RPC pode transportar JSON, e GraphQL pode
usar JSON nas respostas, sem que JSON se torne RPC ou GraphQL.

## Modelo de dados

JSON possui dois tipos estruturados:

- objeto, coleção de pares nome e valor;
- array, sequência ordenada de valores.

Os valores podem ser strings, números, booleanos, `null`, objetos ou arrays.
JSON não possui tipos nativos para data, hora, decimal exato, bytes, UUID ou
referência. Projetos precisam definir representação e validação para esses
valores.

```json
{
  "id": "item-42",
  "title": "Exemplo",
  "published": true,
  "tags": ["rede", "api"],
  "metadata": null
}
```

## Interoperabilidade

O formato é simples e tem bibliotecas em praticamente todas as linguagens,
mas detalhes de interoperabilidade ainda importam:

- números podem perder precisão em linguagens que usam apenas double;
- objetos JSON não devem depender de ordem de chaves;
- nomes duplicados em um objeto produzem comportamento inconsistente entre parsers;
- caracteres precisam seguir as regras de strings e escapes;
- `NaN`, `Infinity`, comentários e trailing commas não são JSON padrão;
- texto recebido deve ser validado antes de ser usado como comando ou query.

Para contratos públicos, documente limites numéricos, timezone, codificação,
campos ausentes, `null`, arrays vazios e representação de erros.

## JSON como contrato de API

JSON é frequentemente usado com HTTP usando `application/json`. Nesse caso,
além de validar a sintaxe, a API precisa definir:

- campos obrigatórios e opcionais;
- tipos e invariantes;
- semântica de `null` e de campo ausente;
- erros e códigos HTTP;
- paginação, filtros e ordenação;
- limites de tamanho e profundidade;
- evolução e compatibilidade;
- autenticação, autorização e rate limiting.

JSON Schema pode validar estrutura e tipos, mas não substitui regras de
negócio, autorização ou consistência entre registros.

## Serialização e desserialização

Serializar transforma valores locais em texto. Desserializar transforma texto
em valores de uma linguagem. O resultado pode variar se o parser converte
números para tipos com precisão diferente, aceita valores não padrão ou
materializa objetos com comportamento especial.

Use parsers mantidos, limite o tamanho da entrada, limite profundidade e não
interprete JSON como código. Evite construir JSON concatenando strings, porque
escapes, caracteres Unicode e valores inesperados podem quebrar a estrutura.

## JSON e segurança

JSON não é uma fronteira de segurança. Um campo `role`, `isAdmin` ou `tenant`
recebido do cliente só deve influenciar autorização depois de validado contra
a identidade e o estado confiável do servidor.

Proteja-se contra payloads grandes, estruturas profundamente aninhadas,
recursos recursivos, números extremos, consumo excessivo de CPU e exposição de
segredos em logs. Redija tokens, cookies, credenciais, dados pessoais e
parâmetros sensíveis antes de registrar documentos.

Ao usar JSONP, `eval`, templates ou inserção direta no HTML, o problema deixa
de ser apenas serialização e passa a envolver execução de código e XSS. Prefira
JSON comum, cabeçalhos corretos e escaping feito pela camada de saída.

## JSON para configuração, logs e documentos

JSON é útil para configurações pequenas, payloads de API e relatórios
estruturados. Para configuração editada por pessoas, YAML, TOML ou outro
formato podem oferecer comentários ou ergonomia melhor, mas introduzem suas
próprias regras e riscos.

Para logs, emita objetos com schema estável, timestamp, nível, evento e
identificadores de correlação. Não trate cada linha JSON como um evento seguro
sem definir rotação, retenção e política de dados.

Para documentos persistidos em banco, defina índices, migrações e regras de
versão. JSON não elimina a necessidade de modelar relações ou de escolher
quando um atributo deve virar coluna.

## JSON e formatos binários

JSON é legível e fácil de integrar, mas costuma ocupar mais espaço e exigir
mais CPU para parsear que formatos binários como Protocol Buffers. Em APIs
externas, legibilidade, tooling e compatibilidade podem valer mais que
eficiência de transporte. Em comunicação interna de alto volume, o custo deve
ser medido.

Compressão pode reduzir o tamanho de JSON, mas não muda seu custo de parse nem
resolve ambiguidades de contrato. Compactar também aumenta CPU e pode esconder
payloads muito grandes até que sejam descompactados.

## GraphQL e JSON

GraphQL define a consulta e o schema; a implementação normalmente serializa o
resultado em JSON. O cliente escolhe campos dentro do schema, mas o servidor
continua responsável por autenticar, autorizar, limitar custo e resolver os
dados.

GraphQL não transforma JSON em uma linguagem tipada. Os tipos vêm do schema e
o JSON é apenas a representação transportada do resultado e dos erros.

## Boas práticas

- publique um schema ou contrato validável;
- use `application/json` e uma codificação explicitamente documentada;
- trate números, data, hora, bytes e identificadores com convenções claras;
- limite tamanho, profundidade e tempo de processamento;
- valide entradas antes de persistir ou autorizar;
- mantenha compatibilidade e não reutilize campos removidos;
- não dependa da ordem das chaves;
- use uma biblioteca de serialização confiável;
- remova segredos e dados pessoais dos logs.

## Fontes

- [RFC 8259, JSON](https://www.rfc-editor.org/rfc/rfc8259)
- [ECMA-404, The JSON Data Interchange Syntax](https://ecma-international.org/publications-and-standards/standards/ecma-404/)
- [JSON Schema specification](https://json-schema.org/specification)
- [IANA media type application/json](https://www.iana.org/assignments/media-types/application/json)

## Continue por aqui

[gRPC](grpc.md) usa normalmente Protocol Buffers, embora possa suportar outros
formatos. [GraphQL](graphql.md) costuma serializar respostas em JSON.
[jq](../ferramentas/dados-estruturados/jq.md) consulta e transforma JSON sem
substituir a validação de um contrato.
