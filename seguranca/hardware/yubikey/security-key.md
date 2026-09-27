# Security Key

Security Key é a família FIDO da Yubico. Diferentemente da YubiKey 5, ela
tem escopo deliberadamente menor: suporta FIDO2 e FIDO U2F, sem os módulos de
OATH, OTP, PIV ou OpenPGP da linha multi-protocolo.

## Modelos atuais

- [Security Key NFC](security-key-nfc.md), com USB-A e NFC;
- [Security Key C NFC](security-key-c-nfc.md), com USB-C e NFC;
- [Security Key NFC Enterprise](security-key-nfc-enterprise.md), com USB-A,
  NFC e serial para inventário;
- [Security Key C NFC Enterprise](security-key-c-nfc-enterprise.md), com
  USB-C, NFC e serial para inventário.

## Quando escolher

É uma boa escolha quando a política exige apenas passkeys, FIDO2 ou U2F e a
organização quer reduzir a superfície de configuração. Ela não é adequada
quando a mesma chave precisa gerar TOTP, atuar como smart card PIV ou guardar
uma chave OpenPGP.

## Enterprise

A edição Enterprise acrescenta serial para controle de inventário e recursos
de gestão previstos pelo programa da Yubico. A serial não substitui o cadastro
da credencial no serviço e não deve ser usada como segredo.

## Fontes

- [Yubico, Security Key Series](https://www.yubico.com/products/security-key/)
- [Yubico, manual técnico da Security Key](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [FIDO2](../../identidade/fido2.md)
