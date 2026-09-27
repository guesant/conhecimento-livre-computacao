# YubiKey

YubiKey é uma família de autenticadores físicos da Yubico. O dispositivo pode
proteger autenticação FIDO2 e U2F, gerar OTP, armazenar credenciais OATH,
expor uma interface de smart card PIV, participar de operações OpenPGP ou
digitar uma senha estática configurada pelo usuário. A disponibilidade exata
depende da família, do modelo, do firmware e do transporte utilizado.

Uma YubiKey não é uma senha portátil. Em FIDO2, por exemplo, o serviço
registra uma chave pública e a chave privada permanece no autenticador. O
servidor recebe uma assinatura vinculada ao desafio e à origem. Esse modelo é
descrito em [FIDO2](../../identidade/fido2.md) e [WebAuthn](../../identidade/webauthn.md).

## Como escolher

- [YubiKey 5](series-5.md) é a família geral multi-protocolo.
- [YubiKey 5 FIPS](series-5-fips.md) é a família voltada a ambientes que
  exigem certificação e processo de validação específico.
- [YubiKey Bio](bio.md) acrescenta verificação por impressão digital para
  credenciais FIDO.
- [Security Key](security-key.md) reduz o escopo ao FIDO2 e ao U2F.
- [Modelos legados](legado.md) documenta produtos descontinuados e os riscos
  de escolhê-los para uma implantação nova.
- [Firmware e recursos](firmware.md) separa a versão do produto da versão do
  firmware e registra a matriz oficial de capacidades.

## Dimensões que não devem ser confundidas

O conector indica como o computador ou o telefone conversa com a chave. USB-A,
USB-C e Lightning são diferenças físicas. NFC é outro transporte, usado sem
inserir a chave em uma porta. O transporte não cria um protocolo novo e não
significa que todos os protocolos do dispositivo estarão disponíveis por NFC.

O formato também muda a operação. Um modelo Nano pode ficar permanentemente
conectado, enquanto um modelo de chaveiro é mais adequado para ser removido e
transportado. A presença de NFC não implica biometria, e a presença de USB-C
não implica suporte a FIPS.

## NFC

NFC é útil para autenticar em telefones e computadores que tenham leitor
compatível. A aplicação, o sistema operacional e o protocolo precisam suportar
o transporte. Antes de comprar um modelo para uso móvel, valide o fluxo real
de FIDO2, o navegador, a política de PIN e o leitor NFC do telefone.

Para uma política portátil e resistente a phishing, FIDO2 normalmente é a
função principal. OTP, OATH, PIV e OpenPGP resolvem problemas diferentes e
devem ser habilitados somente quando houver um caso de uso e uma política de
recuperação definidos.

## Segurança operacional

Registre pelo menos duas chaves por conta ou por operador, mantenha uma chave
de recuperação em custódia separada e não trate uma segunda chave como cópia
automática das credenciais da primeira. Cada autenticador precisa ser
registrado individualmente no serviço.

O administrador deve decidir como revogar uma chave perdida, como substituir
uma chave danificada, quem pode registrar novas credenciais e como auditar o
uso. O dispositivo reduz o risco de phishing e exportação de chaves, mas não
resolve recuperação de conta fraca, sessão já comprometida ou malware no
endpoint.

## Limites de comparação

YubiKey 5, YubiKey 5 FIPS, YubiKey Bio e Security Key não são apenas tamanhos
ou cores diferentes. Eles podem ter firmware, protocolos, certificações,
capacidades de gestão e ciclos de suporte distintos. A documentação técnica
oficial deve prevalecer sobre uma tabela antiga de revendedor.

## Fontes

- [Yubico, produtos](https://www.yubico.com/products/)
- [Yubico, identificação de modelos](https://www.yubico.com/products/identifying-your-yubikey/)
- [Yubico, documentação técnica da YubiKey 5](https://docs.yubico.com/hardware/yubikey/yk-tech-manual/yk5-intro.html)
- [FIDO Alliance, FIDO2](https://fidoalliance.org/fido2/)
