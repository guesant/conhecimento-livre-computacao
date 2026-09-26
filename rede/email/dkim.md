# DKIM

DKIM, DomainKeys Identified Mail, permite que uma organização assine uma mensagem
com uma chave privada e publique a chave pública no DNS. O receptor valida a assinatura
e obtém evidência de que o domínio indicado no campo d= participou do envio ou de um
relay que preservou as partes assinadas.

DKIM autentica a responsabilidade do domínio assinante. Ele não prova que o nome
visível no campo From é o mesmo domínio, não confirma que o remetente é uma pessoa
legítima e não impede que uma mensagem assinada seja maliciosa.

## Seletor e DNS

O assinante escolhe um seletor. A chave pública é publicada em:

selector._domainkey.example.com

O registro costuma ser TXT, embora a interpretação seja a de uma chave DKIM. A chave
privada deve permanecer no sistema que assina. Use seletores diferentes para rotação,
provedores ou fluxos distintos e remova chaves antigas somente depois que mensagens
legítimas deixarem de depender delas.

## Assinatura e validação

A assinatura indica quais cabeçalhos e qual parte do corpo foram incluídos. O corpo pode
ser normalizado por uma canonicalization, e relays que alteram conteúdo assinado podem
invalidar o resultado. O receptor recupera a chave pública, verifica a assinatura e
registra pass, fail, temperror ou permerror conforme a implementação.

DKIM precisa ser combinado com SPF e DMARC. DMARC usa o domínio autenticado por DKIM e
verifica se ele está alinhado ao domínio visível no From.

## Operação

Monitore falhas causadas por truncamento, alteração de assunto, gateways, listas de
distribuição, limite de tamanho de DNS, rotação de chave e múltiplos assinantes. A
chave pública é pública, mas a privada exige controle de acesso, rotação e proteção
contra cópia não autorizada.

## Relações

- [SPF](spf.md) autentica o servidor de envio por outro sinal.
- [DMARC](dmarc.md) define alinhamento e política.
- [Registros DNS](../dns/records.md) explica TXT e nomes de serviço.

## Fontes

- [RFC 6376, DKIM Signatures](https://www.rfc-editor.org/rfc/rfc6376)
- [RFC 8301, DKIM cryptographic algorithm requirements](https://www.rfc-editor.org/rfc/rfc8301)
- [RFC 8463, DKIM elliptic curve signature](https://www.rfc-editor.org/rfc/rfc8463)
