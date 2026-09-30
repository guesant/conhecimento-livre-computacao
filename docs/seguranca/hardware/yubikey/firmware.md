# Firmware da YubiKey

Modelo comercial e versão de firmware são eixos diferentes. Duas chaves com
o mesmo nome podem expor capacidades diferentes quando pertencem a famílias
distintas ou executam versões distintas. O firmware também pode limitar a
quantidade de credenciais FIDO2 e OATH, a versão de OpenPGP, recursos CTAP e
interfaces de smart card.

## Matriz oficial

A matriz técnica da Yubico relaciona capacidades a versões. Para a linha
YubiKey 5 comum, a documentação registra tabelas para 5.8.x e 5.7.4. Para a
linha FIPS, a página consultada registra 5.7.4, 5.4.3 e 5.4.2. Security Key,
Bio e outras séries têm matrizes próprias.

Entre os campos que podem variar estão:

- FIDO2 CTAP e recursos como PRF;
- AlwaysUV e gerenciamento de PIN;
- quantidade de credenciais FIDO2 e OATH;
- versão do OpenPGP;
- PIV, OTP e OATH;
- SCP03, SCP11 e FIDO2 sobre CCID;
- serial e attestation para uso empresarial.

Não se deve fazer downgrade ou escolher uma chave apenas pela versão mais
alta. O procedimento precisa considerar compatibilidade com o serviço, a
política de atualização, a certificação da família e a impossibilidade de
alterar o firmware em muitos modelos depois da fabricação.

## Diagnóstico

Registre modelo, identificador, firmware, AAGUID quando relevante e os
protocolos habilitados. Use as ferramentas oficiais para confirmar o estado
real em vez de inferir a capacidade pelo conector ou pela aparência.

## Fontes

- [Yubico, visão geral do firmware](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-firmware-overview.html)
- [Yubico, manual técnico](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
