# TOTP

Time-based One-Time Password, TOTP, é um mecanismo que calcula códigos curtos
a partir de um segredo compartilhado e do tempo atual. O servidor e o
autenticador dividem uma chave e aplicam o algoritmo HOTP a um contador derivado
do relógio. O código muda em intervalos definidos e é usado como um fator
adicional, não como substituto automático de uma senha forte ou de uma chave
de segurança resistente a phishing.

## Cálculo

O RFC 6238 define TOTP como HOTP com um contador de tempo. Em termos conceituais:

```text
contador = floor((tempo_utc - T0) / passo)
codigo = HOTP(segredo, contador)
```

O valor é truncado e reduzido ao número de dígitos configurado, normalmente seis
ou oito. O segredo precisa ser gerado com entropia suficiente, transmitido uma
vez por um canal protegido e armazenado de modo que o servidor possa validar o
código sem expô-lo em logs, URLs ou mensagens de suporte.

## Janela de tolerância

O relógio do cliente e o do servidor podem divergir. Uma janela de aceitação
permite códigos do intervalo anterior ou seguinte, mas amplia a superfície para
replay. O servidor deve registrar o uso, limitar tentativas e rejeitar um código
já aceito quando o fluxo exigir uso estritamente único. NTP melhora a
confiabilidade, mas não deve ser usado para aceitar uma janela ilimitada.

TOTP não prova presença do dispositivo, não liga automaticamente o código a uma
origem e não evita phishing em tempo real. Um atacante pode convencer o usuário
a informar o código a uma página falsa e usá-lo antes que expire. Para contas
de alto valor, combine TOTP com WebAuthn ou prefira um autenticador com
resistência a phishing.

## Provisionamento e recuperação

O QR code de provisionamento contém o segredo. Ele deve ser exibido uma única
vez, com confirmação de identidade e possibilidade de revogação. Códigos de
recuperação precisam ter entropia própria e não devem ser derivados do segredo
TOTP. Trocar o telefone sem um processo de recuperação pode deixar a conta
inacessível; permitir reset por suporte sem evidência suficiente torna o segundo
fator inútil.

## Relações

- [Autenticação](index.md) compara fatores e fronteiras de identidade.
- [FIDO2](fido2.md) e [WebAuthn](webauthn.md) oferecem autenticação com chave pública.
- [OTP e HOTP](https://www.rfc-editor.org/rfc/rfc4226) define a base de contador.

## Fontes primárias

- [RFC 6238, TOTP](https://www.rfc-editor.org/rfc/rfc6238)
- [RFC 4226, HOTP](https://www.rfc-editor.org/rfc/rfc4226)
- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)
