# YubiKey 5 FIPS

YubiKey 5 FIPS é a variante da família multi-protocolo destinada a ambientes
que precisam operar dentro de requisitos de validação FIPS. FIPS não é um
modo que o usuário ativa em qualquer YubiKey. É uma linha de hardware e
firmware com ciclo de certificação próprio.

## Modelos atuais

A página de identificação da Yubico lista estes modelos FIPS atuais:

- [YubiKey 5 NFC FIPS](yubikey-5-nfc-fips.md), USB-A e NFC;
- [YubiKey 5C NFC FIPS](yubikey-5c-nfc-fips.md), USB-C e NFC;
- [YubiKey 5C FIPS](yubikey-5c-fips.md), USB-C;
- [YubiKey 5 Nano FIPS](yubikey-5-nano-fips.md), USB-A;
- [YubiKey 5C Nano FIPS](yubikey-5c-nano-fips.md), USB-C;
- [YubiKey 5Ci FIPS](yubikey-5ci-fips.md), USB-C e Lightning.

## O que muda

O processo de certificação limita a velocidade com que recursos e versões de
firmware são introduzidos. A documentação técnica informa, por exemplo, que a
linha FIPS permanece na versão de firmware 5.7.4 enquanto a certificação de
firmware 5.8 é processada. Portanto, uma tabela de recursos da YubiKey 5
comum não pode ser copiada automaticamente para a linha FIPS.

As capacidades relevantes incluem FIDO2, U2F, OATH, OTP e PIV, mas o conjunto
exato deve ser conferido na matriz da versão instalada. A linha FIPS é uma
decisão de conformidade e aquisição, não uma justificativa para escolher o
modelo mais caro em uma conta pessoal que não tem esse requisito.

## Implantação

Antes da compra, identifique a validação exigida, os algoritmos permitidos, o
processo de inventário, a política de PIN, o procedimento de substituição e a
forma de comprovar que o modelo e o firmware ainda estão cobertos. Certificação
não elimina a necessidade de validar integração, transporte, recuperação e
controle de acesso.

## Fontes

- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
- [Yubico, manual técnico da YubiKey 5](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [Yubico, matriz de firmware](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-firmware-overview.html)
- [NIST, programa CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program)
