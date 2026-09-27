# HMAC

HMAC, ou Hash-based Message Authentication Code, é um código de autenticação
de mensagem construído com uma função de hash e um segredo compartilhado. Ele
permite verificar que uma mensagem foi produzida por alguém que conhece o
segredo e que os bytes recebidos não foram alterados.

HMAC não cifra a mensagem, não esconde seu conteúdo e não oferece
não-repúdio. Como os dois lados conhecem a mesma chave, qualquer um deles pode
produzir uma mensagem válida. Para provar autoria perante terceiros, use uma
assinatura digital assimétrica.

## Construção

Para uma função de hash H, uma chave K e uma mensagem M, a construção definida
no RFC 2104 é, em termos conceituais:

```text
HMAC(K, M) = H((K' xor opad) || H((K' xor ipad) || M))
```

K' é a chave ajustada ao tamanho de bloco da função, `ipad` é o preenchimento
interno e `opad` é o preenchimento externo. A composição em duas camadas evita
usar a função de hash como se fosse uma simples concatenação de segredo e
mensagem, além de permitir a análise formal da construção.

Em aplicações novas, HMAC-SHA-256 é uma escolha comum quando o protocolo
precisa de interoperabilidade. O algoritmo exato, o tamanho da chave, o
formato da saída e a identificação da chave devem ser definidos pelo protocolo
ou pela biblioteca. Não troque o algoritmo apenas porque outro digest é mais
longo.

## Exemplo básico

Este exemplo calcula e verifica um HMAC em Python. A comparação usa
`compare_digest`, que evita uma comparação ingênua com saída dependente do
primeiro byte diferente.

```python
import hashlib
import hmac

secret = b"chave-secreta-do-exemplo"
message = b"body original"

mac = hmac.new(secret, message, hashlib.sha256).hexdigest()
received = "8a3d..."

valid = hmac.compare_digest(mac, received)
```

O valor `received` normalmente chega em um header ou em um campo separado. A
aplicação deve validar o formato e o tamanho antes de comparar, mas não deve
aceitar uma versão truncada sem que o protocolo tenha definido explicitamente
essa redução.

Em PHP, a mesma operação pode ser expressa com as primitivas da biblioteca
padrão:

```php
$mac = hash_hmac('sha256', $message, $secret);
$valid = hash_equals($mac, $received);
```

As duas pontas precisam usar exatamente os mesmos bytes. Um lado não pode
assinar o texto UTF-8 enquanto o outro normaliza Unicode, troca quebras de
linha, reordena campos ou serializa números de outra forma.

## Assinatura de uma requisição HTTP

Um protocolo de webhook pode definir uma entrada composta por método, caminho,
timestamp e corpo:

```text
POST\n/api/events\n1735689600\n{"id":"evt-42","type":"created"}
```

O emissor calcula `HMAC-SHA-256(secret, signing_input)` e envia, por exemplo,
o identificador da chave, o timestamp e a assinatura em headers. O receptor
reconstrói a mesma entrada usando o corpo bruto recebido, verifica a janela de
tempo e só então processa a mensagem.

O timestamp não autentica nada sozinho. Ele limita a reutilização de uma
assinatura capturada. Para operações sensíveis, associe também um nonce ou um
identificador de evento e guarde os identificadores já processados por uma
janela adequada. O processamento precisa ser idempotente porque a mesma
requisição pode ser reenviada legitimamente.

Não assine uma representação ambígua. Se o corpo for JSON, defina o formato de
serialização, ou use JSON Canônico, antes de calcular o HMAC.

## Chaves e rotação

O segredo precisa ser imprevisível e ter proteção equivalente à importância da
mensagem. Não use senha humana diretamente, não coloque o segredo no
repositório e não registre a chave ou a entrada completa em logs. O serviço
emissor e o receptor precisam receber a chave por um mecanismo de distribuição
confiável.

Uma rotação sem indisponibilidade pode usar um identificador de chave:

1. o emissor passa a assinar com a chave nova e informa seu identificador;
2. o receptor aceita a chave nova e a anterior durante a janela de transição;
3. mensagens antigas expiram ou são reprocessadas dentro de uma política
   definida;
4. a chave anterior é revogada e removida dos consumidores.

Não aceite qualquer `key_id` enviado pelo cliente. O identificador seleciona
apenas uma chave conhecida e autorizada para aquele emissor, tenant ou
endpoint.

## HMAC, hash e assinatura digital

| Mecanismo | Segredo compartilhado | Confidencialidade | Prova para terceiros | Uso típico |
| --- | --- | --- | --- | --- |
| Hash | Não | Não | Não | Digest e identificação de conteúdo |
| HMAC | Sim | Não | Não | Webhooks, APIs e mensagens entre serviços |
| Assinatura digital | Não, usa chave privada e pública | Não por si só | Sim | Documentos, artefatos e identidade verificável |
| Cifra autenticada | Chave simétrica ou esquema híbrido | Sim | Não necessariamente | Sessões e dados confidenciais |

Um hash publicado no mesmo canal do arquivo não impede que um atacante altere
os dois. O HMAC resolve esse problema quando o receptor possui um segredo que o
atacante não conhece. Uma assinatura resolve o problema de distribuição quando
o verificador precisa usar uma chave pública sem poder assinar.

## Erros frequentes

- concatenar campos sem delimitadores ou sem um formato definido;
- comparar assinaturas com `==` em vez de comparação em tempo constante;
- reutilizar uma chave em serviços e contextos sem relação;
- aceitar algoritmo escolhido pelo cliente sem uma allowlist;
- truncar a saída sem documentar tamanho e impacto;
- confiar em timestamp sem validar relógio, janela e replay;
- registrar segredo, assinatura ou corpo sensível em logs;
- usar HMAC como se fosse criptografia;
- calcular o MAC antes de validar limites de tamanho da mensagem.

## Fontes

- [RFC 2104, HMAC](https://www.rfc-editor.org/rfc/rfc2104)
- [FIPS 198-1, The Keyed-Hash Message Authentication Code](https://csrc.nist.gov/pubs/fips/198-1/final)
- [NIST SP 800-107 Rev. 1, Recommendation for Applications Using Approved Hash Algorithms](https://csrc.nist.gov/pubs/sp/800/107/r1/final)
- [OWASP, Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
