# YubiKey Bio

YubiKey Bio é a família de autenticadores FIDO com sensor de impressão
digital. A impressão é usada localmente para liberar a credencial no
dispositivo. O serviço não recebe a impressão digital como parte do protocolo
WebAuthn.

## Modelos

- [YubiKey Bio](yubikey-bio.md), com USB-A;
- [YubiKey C Bio](yubikey-c-bio.md), com USB-C.

Os dois modelos atuais são identificados pela Yubico como FIDO Edition. A
função principal é FIDO U2F e FIDO2, não OATH, PIV, OpenPGP ou Yubico OTP.

## Biometria local

O autenticador pode armazenar até cinco impressões digitais. A impressão
digital substitui ou complementa a verificação por PIN e presença, conforme o
fluxo FIDO e o firmware. A política deve prever um método alternativo quando
o sensor não reconhecer o dedo, quando o usuário estiver sem a chave ou quando
uma credencial precisar ser revogada.

Biometria não é sinônimo de recuperação. Uma impressão não pode ser trocada
como uma senha. Por isso, o cadastro deve ser acompanhado de uma segunda
credencial, de um processo de substituição e de contatos de recuperação.

## Edição multi-protocolo

A documentação técnica da Yubico também descreve uma edição Bio
multi-protocolo com interface semelhante a smart card e PIN compartilhado com
as credenciais biométricas. Essa edição tem disponibilidade e condições
comerciais próprias. Não confunda a edição FIDO comum com a edição
multi-protocolo.

## Fontes

- [YubiKey Bio Series](https://www.yubico.com/products/yubikey-bio-series/)
- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
- [Yubico, manual técnico da YubiKey Bio](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [WebAuthn](../../identidade/webauthn.md)
