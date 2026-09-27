# Modelos legados da YubiKey

Produtos antigos continuam aparecendo em inventários, tutoriais e mercados de
revenda. Eles devem ser classificados antes de serem usados em uma política
de autenticação nova.

## Famílias descontinuadas

A página de identificação da Yubico registra, entre outros:

- FIDO U2F Security Key, de 2013 a 2018;
- Security Key by Yubico, de 2018 a 2020;
- Security Key NFC e Security Key C NFC anteriores, de 2019 a 2023 e de 2021
  a 2023;
- YubiKey 5A, de 2018 a 2023;
- variantes YubiKey 5 CSPN, de 2021 a 2024;
- variantes YubiKey 5 FIPS anteriores, de 2021 a 2026.

Também existem gerações históricas como YubiKey 4, YubiKey 4C, YubiKey NEO e
modelos anteriores. A disponibilidade de software, suporte de protocolo,
certificação e correções varia por geração.

## Risco operacional

Não basta verificar que uma chave antiga ainda acende ou responde a um
comando. Confirme se ela suporta o protocolo exigido, se o serviço ainda
aceita a credencial, se o firmware tem suporte, se a origem FIDO é compatível
e se há procedimento de substituição. Uma chave antiga pode continuar útil
para uma conta pessoal, mas ser inadequada para uma política corporativa ou
regulada.

Não compre uma chave usada sem considerar a custódia anterior. Credenciais
FIDO, OATH, PIV e OpenPGP podem permanecer registradas no dispositivo, e o
estado não deve ser tratado como conhecido apenas porque o invólucro parece
intacto.

## Fontes

- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
- [Yubico, documentação de suporte](https://support.yubico.com/)
- [Yubico, manual técnico](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
