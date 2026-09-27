# YubiKey 5

YubiKey 5 é a família multi-protocolo para uso geral. A página de produtos da
Yubico lista atualmente seis modelos padrão: YubiKey 5 NFC, YubiKey 5C NFC,
YubiKey 5C, YubiKey 5 Nano, YubiKey 5C Nano e YubiKey 5Ci. A matriz pode
mudar, portanto o nome comercial não deve ser usado como substituto da versão
do firmware.

## Capacidades

Os modelos da família foram projetados para combinar FIDO2 e U2F com
Yubico OTP, OATH HOTP e TOTP, PIV, OpenPGP e senha estática segura. Nem toda
capacidade está disponível em todos os transportes, e a matriz de firmware
deve ser consultada antes de uma implantação que dependa de uma função
específica.

## Modelos

| Modelo | Transporte | Formato | Destaque |
| --- | --- | --- | --- |
| [YubiKey 5 NFC](yubikey-5-nfc.md) | USB-A, NFC | Chaveiro | NFC e multi-protocolo |
| [YubiKey 5C NFC](yubikey-5c-nfc.md) | USB-C, NFC | Chaveiro | USB-C e NFC |
| [YubiKey 5C](yubikey-5c.md) | USB-C | Chaveiro | USB-C multi-protocolo |
| [YubiKey 5 Nano](yubikey-5-nano.md) | USB-A | Nano | Fica na porta USB |
| [YubiKey 5C Nano](yubikey-5c-nano.md) | USB-C | Nano | Fica na porta USB-C |
| [YubiKey 5Ci](yubikey-5ci.md) | USB-C, Lightning | Chaveiro | Compatibilidade com Apple e USB-C |

## Escolha física

Escolha USB-A quando o parque de computadores ainda depender desse conector.
Escolha USB-C quando o conector for predominante. Escolha NFC quando o fluxo
precisar funcionar em um telefone ou em outro leitor sem inserir a chave.
Escolha Nano somente quando deixar o dispositivo conectado fizer sentido, pois
o formato é menos conveniente para transportar e remover.

O 5Ci resolve a combinação USB-C e Lightning, mas não substitui NFC. A
compatibilidade depende do sistema operacional, do navegador e da aplicação
que usa o protocolo.

## Configuração e gestão

Yubico Authenticator gerencia credenciais OATH e pode interagir com recursos
de outros protocolos. PIV e OpenPGP usam ferramentas próprias do sistema ou
integrações específicas. Não misture a credencial FIDO de uma conta com o
segredo OATH de outra sem um inventário que identifique o serviço, o usuário e
o procedimento de recuperação.

## Fontes

- [Yubico, YubiKey 5 Series](https://www.yubico.com/store/yubikey-5-series/)
- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
- [Yubico, manual técnico da YubiKey 5](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [Yubico, visão geral do firmware](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-firmware-overview.html)
