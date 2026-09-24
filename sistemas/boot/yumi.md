# YUMI

YUMI, Your Universal Multiboot Installer, cria uma unidade USB multiboot que pode conter sistemas operacionais, instaladores Windows, distribuições Linux, antivírus, ferramentas de diagnóstico e ambientes de recuperação.

## Variantes

A família YUMI possui variantes com objetivos diferentes. A documentação atual recomenda YUMI Py para uso multiplataforma e mantém YUMI exFAT como alternativa nativa do Windows. Edições antigas Legacy e UEFI podem estar arquivadas.

Escolha a variante pela documentação atual do projeto. Não misture instruções de uma versão antiga com o layout de outra.

## Fluxo

1. Faça backup do USB.
2. Instale ou abra a variante apropriada.
3. Selecione o dispositivo correto.
4. Escolha uma distribuição ou forneça uma ISO.
5. Instale a entrada no menu.
6. Repita para as outras imagens.
7. Teste cada entrada em firmware e hardware representativos.

O dispositivo pode continuar sendo atualizado com novas entradas. Isso é diferente de gravar novamente a unidade inteira a cada ISO, embora algumas variantes possam recriar partições ao mudar de modo.

## Recursos

Dependendo da variante e da imagem, YUMI pode oferecer downloads integrados, persistência, testes com QEMU ou VirtualBox e compartilhamento pela rede local. Esses recursos dependem da imagem e do backend de boot, portanto não são garantidos para toda distribuição.

Persistência deve ser tratada como estado operacional. Ela pode guardar arquivos, chaves ou configurações que não deveriam estar em uma mídia compartilhada.

## Comparação com Ventoy

YUMI e Ventoy resolvem o problema de carregar vários ambientes, mas a experiência e o modelo de compatibilidade diferem. Ventoy tende a tratar imagens como arquivos em uma partição de dados. YUMI pode usar uma integração específica por distribuição, com entradas e recursos próprios.

Para um kit simples de ISOs, compare o tempo de atualização e a compatibilidade do hardware. Para um fluxo que precisa de persistência ou integração de uma distribuição, valide a variante YUMI indicada pelo projeto.

## Segurança e diagnóstico

Baixe o programa e as imagens de fontes oficiais. Verifique que o menu aponta para arquivos conhecidos e remova imagens antigas. Se uma entrada falhar, valide a ISO fora do YUMI e teste outra imagem antes de alterar o bootloader.

## Relações

- [Ventoy](ventoy.md) é outra abordagem para multiboot.
- [Rufus](rufus.md) é mais apropriado para uma mídia única com opções detalhadas.
- [netboot.xyz](netboot-xyz.md) leva parte do catálogo para a rede.

## Fontes primárias

- [YUMI Multiboot USB Creator](https://pendrivelinux.com/yumi-multiboot-usb-creator/)
- [Pendrive Linux](https://pendrivelinux.com/)
