# MemTest86 e Memtest86+

MemTest86 e MemTest86+ são ambientes inicializáveis que exercitam a memória sem depender do sistema operacional instalado. Eles ajudam a investigar travamentos, corrupção de dados, reinicializações e instabilidade aparentemente aleatória.

## Duas linhas de projeto

| Projeto | Característica |
| --- | --- |
| MemTest86 | Projeto da PassMark, com edição gratuita e edições pagas para relatórios e automação |
| Memtest86+ | Projeto livre e open source sob GPLv2, com suporte a IA-32, x86-64 e LoongArch64 |

As capacidades de CPU, Secure Boot, relatórios, automação e boot pela rede não são iguais. Escolha o projeto de acordo com arquitetura e automação necessária, não somente pelo nome parecido.

## Como testar

Grave a imagem em USB ou use CD ou PXE quando suportado. Reinicie e deixe o teste executar pelo menos uma passagem completa. Para maior confiança, execute várias passagens e teste em condições próximas às do problema.

Um erro é significativo mesmo quando aparece em apenas um endereço. Antes de atribuir a culpa a um módulo, remova overclock, restaure configurações padrão, teste módulos individualmente e altere os slots conforme o manual da placa. O controlador de memória, o slot, a placa e a temperatura também podem causar erros.

## Interpretação

Memória defeituosa pode corromper arquivos, provocar crashes e produzir sintomas que parecem falhas de aplicação. Um teste sem erro reduz a probabilidade de um problema de RAM, mas não prova que todo o sistema está saudável.

Se um erro aparece:

1. registre endereço, padrão, CPU e configuração;
2. repita em frequência e tensão padrão;
3. remova módulos conforme o manual;
4. teste cada módulo e slot separadamente;
5. atualize firmware somente depois de preservar evidência;
6. substitua a peça ou ajuste a configuração conforme o resultado.

ECC pode corrigir ou registrar alguns erros sem apresentar exatamente a mesma saída que uma memória não ECC. Consulte o log do firmware e do sistema junto do MemTest.

## Boot pela rede e Secure Boot

Memtest86+ pode ser carregado por PXE com payloads distintos para BIOS e UEFI, mas Secure Boot pode bloquear um binário não assinado. MemTest86 oferece suporte a UEFI, Secure Boot e boot PXE conforme a edição e a documentação do produto.

Quando um teste não inicia, confirme arquitetura, modo de firmware, assinatura, ordem de boot e payload. Não interprete a ausência do menu como ausência de erro de memória.

## Limitações

O teste precisa de acesso suficiente à memória e pode não reproduzir falhas que dependem de carga de I/O, temperatura ou combinação de dispositivos. Um teste de RAM não substitui teste de disco, fonte, CPU, placa ou sistema.

Não use uma única passagem sem erro para justificar a entrada imediata de um servidor em produção quando já existem sintomas. Combine o teste com logs, monitoramento, stress controlado e substituição cruzada de componentes.

## Relações

- [Instalação pela rede](network-install.md) explica PXE e iPXE.
- [netboot.xyz](netboot-xyz.md) pode disponibilizar utilitários em um menu.
- [GParted Live](gparted-live.md) trata armazenamento e partições.
- [IPMI](../hardware/ipmi.md) pode expor sensores e eventos de plataforma.

## Fontes primárias

- [MemTest86](https://www.memtest86.com/)
- [MemTest86 user guide](https://www.memtest86.com/userguide.html)
- [Memtest86+](https://memtest.org/)
