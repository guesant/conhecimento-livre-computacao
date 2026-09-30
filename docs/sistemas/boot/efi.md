# EFI

EFI, Extensible Firmware Interface, foi a especificação original que definiu uma interface moderna entre firmware e sistema operacional. A especificação foi desenvolvida inicialmente pela Intel e posteriormente evoluiu para UEFI, Unified Extensible Firmware Interface, mantida pelo UEFI Forum.

Na prática, os termos EFI e UEFI aparecem misturados. EFI pode significar a especificação histórica, o modo de boot não legado ou o diretório `EFI` usado na ESP. UEFI é o nome da especificação atual. A distinção é importante quando se lê documentação antiga, analisa um instalador ou interpreta uma opção de firmware.

## O que EFI introduziu

O modelo EFI separa o firmware da aplicação de boot por meio de protocolos e serviços definidos. Em vez de limitar o firmware a executar um pequeno trecho de código em um setor inicial, o modelo permite localizar e executar aplicações em um filesystem conhecido. Essas aplicações podem acessar dispositivos por protocolos de firmware e carregar o próximo estágio de inicialização.

Esse desenho também permite que a plataforma tenha um gerenciador de boot persistente, entradas nomeadas e aplicações de diagnóstico. UEFI preservou e ampliou essas ideias, acrescentando serviços, formatos, variáveis autenticadas e mecanismos como Secure Boot.

## A diretoria EFI

O diretório `EFI` na ESP é uma convenção de organização de arquivos, não uma prova de que o firmware usa exatamente a especificação EFI histórica. Uma estrutura comum é:

```text
EFI/
  BOOT/
    BOOTX64.EFI
  Linux/
  Microsoft/
```

O nome e a capitalização podem variar conforme o filesystem e o firmware. O caminho `EFI/BOOT/BOOTX64.EFI` é o caminho removível padrão para plataformas x86-64. Arquiteturas diferentes usam nomes correspondentes, e uma mídia não deve assumir que todo equipamento é x86-64.

## EFI, BIOS e modo de boot

EFI e UEFI não são sinônimos de BIOS. Um sistema UEFI pode oferecer CSM para compatibilidade com boot legado, enquanto um sistema em modo legado usa as convenções de BIOS mesmo que o firmware físico seja chamado informalmente de BIOS. O modo efetivo usado para iniciar o instalador ou o sistema é o que determina a estrutura esperada.

Essa diferença explica casos em que a mesma mídia aparece na lista de boot duas vezes, uma entrada identificada como UEFI e outra sem esse prefixo. A primeira executa uma aplicação EFI/UEFI na ESP; a segunda tenta usar o fluxo legado. A escolha do modo deve ser consistente com o particionamento, o carregador instalado e o estado de Secure Boot.

## Onde o termo ainda aparece

Distribuições Linux e ferramentas de sistema usam EFI em nomes de diretórios, variáveis e interfaces, mesmo quando a máquina implementa UEFI. Exemplos incluem `/sys/firmware/efi`, `efibootmgr`, `efivarfs` e a montagem da ESP em `/boot/efi`. Esses nomes indicam a compatibilidade histórica da interface, não necessariamente uma versão antiga do firmware.

## Fontes primárias

- [UEFI Forum, especificações](https://uefi.org/specifications)
- [UEFI Forum, perguntas frequentes](https://uefi.org/faq)
- [Documentação do kernel Linux sobre variáveis EFI](https://docs.kernel.org/filesystems/efivarfs.html)
