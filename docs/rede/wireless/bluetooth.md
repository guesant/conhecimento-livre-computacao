# Bluetooth

Bluetooth é uma família de tecnologias de comunicação sem fio de curto alcance
definida pela Bluetooth SIG. Bluetooth Classic e Bluetooth Low Energy, BLE,
compartilham o ecossistema, mas têm modelos de rádio, descoberta, conexão e
perfis diferentes. Um dispositivo pode suportar uma ou as duas famílias.

## Classic e BLE

Bluetooth Classic é usado em perfis como áudio e portas seriais legadas. BLE
foi desenhado para dispositivos de baixo consumo, sensores e interações curtas.
No BLE, um dispositivo anuncia dados, outro descobre serviços e características
GATT e as operações podem ler, escrever, notificar ou indicar valores.

GATT organiza serviços e características, mas não é uma política de autorização.
Uma característica que aceita escrita precisa validar pareamento, identidade,
permissão e conteúdo no firmware. Ocultar um UUID não protege um dispositivo.

## Segurança

Pareamento negocia chaves segundo um método que depende de capacidade de entrada,
display e política do dispositivo. Just Works reduz atrito, mas oferece proteção
limitada contra homem no meio durante o pareamento. Métodos com confirmação ou
autenticação fora de banda melhoram a garantia quando a interface permite.

Bonding guarda chaves para reconexões futuras. Isso exige um procedimento para
apagar bonds, trocar proprietário e responder a um dispositivo perdido. Uma
chave vazada pode permanecer válida até ser removida em todos os lados.

## Rádio e operação

Bluetooth usa a banda de 2,4 GHz e convive com Wi-Fi, micro-ondas e outras fontes
de interferência. O canal, potência, advertising interval, conexão e tamanho de
pacote afetam consumo, latência e alcance. Um teste feito em uma bancada não
representa necessariamente o comportamento em metal, corpo humano, paredes ou
ambiente congestionado.

BLE foi projetado para baixo consumo, mas um intervalo de anúncio curto, scans
contínuos ou notificações frequentes podem esgotar uma bateria. Defina timeout,
backoff, limite de conexões e comportamento quando o dispositivo não encontra
seu central.

## Relações

- [Wi-Fi](wifi-generations.md) compartilha a banda, mas possui outro modelo de rede.
- [FIDO2](../../seguranca/identidade/fido2.md) pode usar Bluetooth como transporte em alguns autenticadores.
- [Arduino e microcontroladores](../../embarcados/index.md) usam BLE em cenários embarcados.

## Fontes primárias

- [Bluetooth Core Specification](https://www.bluetooth.com/specifications/specs/core-specification/)
- [Bluetooth SIG, GATT](https://www.bluetooth.com/specifications/specs/generic-attribute-profile-1-1/)
- [NIST Bluetooth security](https://csrc.nist.gov/publications/detail/sp/800-121/rev-2/final)
