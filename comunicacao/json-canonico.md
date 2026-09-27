# JSON Canônico

JSON Canônico é uma representação determinística de um documento JSON. O
objetivo é fazer com que valores estruturados equivalentes produzam exatamente
os mesmos bytes antes de uma assinatura, um HMAC, um digest ou uma comparação
de conteúdo.

JSON comum define a estrutura dos valores, mas não transforma todas as escolhas
de serialização em um contrato de bytes. Espaços, quebras de linha e a ordem
das propriedades podem variar sem mudar o significado do objeto. Essa
flexibilidade é boa para interoperabilidade, mas impede que duas partes
calculem diretamente a mesma assinatura sobre textos diferentes.

A especificação [JSON Canonicalization Scheme, RFC 8785](https://www.rfc-editor.org/rfc/rfc8785),
conhecida como JCS, define uma forma interoperável de resolver esse problema.

## Exemplo mínimo

Estas duas representações descrevem o mesmo objeto JSON para a maioria dos
consumidores:

```json
{ "b": 2, "a": 1 }
```

```json
{"a":1,"b":2}
```

Na forma canônica JCS, o resultado é:

```json
{"a":1,"b":2}
```

O resultado remove espaços insignificantes e ordena as propriedades segundo as
regras da especificação. A ordem dos elementos de um array continua sendo
significativa e não pode ser reordenada como se fosse a ordem de propriedades
de um objeto.

## Regras relevantes

Uma implementação compatível precisa seguir o conjunto completo de regras do
RFC 8785, não apenas aplicar `sort_keys` e remover espaços:

- objetos são serializados sem espaços desnecessários;
- nomes de propriedades são ordenados por unidades de código UTF-16;
- strings usam a serialização JSON definida pelo algoritmo ECMAScript adotado
  pelo JCS;
- números precisam seguir a representação determinística especificada, sem
  `NaN` ou `Infinity`;
- nomes duplicados não são aceitos;
- a saída canônica é uma sequência UTF-8;
- não há normalização Unicode implícita, portanto normalização de texto deve
  ser uma decisão do contrato antes da canonicalização.

Essas regras tornam importante usar uma biblioteca que declare conformidade
com o RFC 8785. Uma implementação local que só ordena chaves pode divergir em
caracteres fora de ASCII, números, escapes ou valores especiais.

## JSON Canônico e HMAC

A canonicalização é especialmente útil quando um serviço precisa autenticar
um documento JSON. O emissor e o receptor devem canonicalizar o mesmo valor e
calcular o HMAC sobre os mesmos bytes:

```python
import hashlib
import hmac

import rfc8785

document = {
    "amount": 10,
    "currency": "BRL",
}
secret = b"segredo-compartilhado"
canonical = rfc8785.dumps(document)
signature = hmac.new(secret, canonical, hashlib.sha256).hexdigest()
```

Nesse exemplo, `rfc8785.dumps` representa uma biblioteca compatível com JCS.
O contrato real deve fixar a biblioteca ou uma implementação equivalente,
além do algoritmo HMAC, da codificação e do formato da assinatura.

O HMAC autentica a representação canônica, não transforma JSON em um formato
confidencial. Quem tiver acesso ao documento pode lê-lo. Quem não possuir o
segredo não pode gerar um MAC válido para uma alteração, desde que a chave e o
protocolo estejam protegidos.

## Assinaturas e documentos externos

Em um fluxo de assinatura digital, o documento pode ser recebido como JSON,
canonicalizado e assinado com a chave privada do emissor. O verificador repete
a canonicalização, calcula ou verifica a assinatura e consulta a chave pública
confiável.

Um sistema de produção ainda precisa definir:

- qual schema valida o documento antes da assinatura;
- quais campos pertencem ao envelope e quais pertencem ao conteúdo;
- como o identificador da chave e o algoritmo são selecionados;
- como versões e extensões são representadas;
- como expiração, replay e revogação são tratados;
- como valores ausentes, `null`, datas, decimais e bytes são modelados.

Não é seguro assinar um objeto que contenha campos controlados pelo transporte
e depois interpretar esses campos com outra regra. A validação semântica e a
autorização devem ocorrer antes de confiar no conteúdo autenticado.

## Limitações

Canonicalização não resolve equivalência semântica geral. Duas strings podem
representar o mesmo texto para uma regra de negócio e continuar sendo bytes
diferentes. Datas em formatos diferentes, identificadores com maiúsculas e
minúsculas, números decimais e valores opcionais precisam de uma política
explícita.

Ela também não substitui JSON Schema, autenticação, autorização, criptografia,
controle de replay ou versionamento. Seu papel é estabilizar a representação
dos dados para que outra operação, como HMAC ou assinatura, receba uma entrada
determinística.

## Quando usar

Use JCS quando diferentes implementações precisam assinar ou gerar digest de
um mesmo documento JSON e o contrato precisa ser interoperável. Para uma API
que apenas transporta dados, JSON normal com schema e validação costuma ser
suficiente.

Antes de adotar JCS, confirme se o ecossistema de consumidores possui suporte
compatível. Se todos os participantes controlam o formato, um protocolo
binário ou uma serialização determinística própria pode ser mais apropriado,
mas essa escolha precisa ser especificada e testada da mesma forma.

## Relações

- [JSON](json.md) explica o formato de dados e suas limitações gerais.
- [HMAC](../seguranca/criptografia/hmac.md) autentica bytes usando um segredo compartilhado.
- [Hash](../seguranca/criptografia/hash.md) produz um digest, mas não autentica a origem sozinho.
- [Criptografia assimétrica](../seguranca/criptografia/criptografia-assimetrica.md) trata chaves públicas, privadas e assinaturas.

## Fontes

- [RFC 8785, JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785)
- [RFC 8259, The JavaScript Object Notation, JSON Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)
- [ECMA-262, JSON.stringify](https://tc39.es/ecma262/multipage/structured-data.html#sec-json.stringify)
- [JSON Schema specification](https://json-schema.org/specification)
