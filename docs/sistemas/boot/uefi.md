# UEFI

UEFI, Unified Extensible Firmware Interface, é a especificação que define a interface entre o firmware da plataforma e o software executado antes do sistema operacional. Ela substituiu progressivamente o modelo de boot associado ao BIOS tradicional e fornece serviços padronizados para inicialização, descoberta de dispositivos, carregamento de drivers e execução de aplicações de firmware.

UEFI não é um sistema operacional nem um bootloader específico. O firmware implementa a especificação e o Boot Manager do firmware escolhe uma aplicação UEFI, normalmente o carregador do sistema operacional. Um carregador Linux, Windows Boot Manager ou utilitário de diagnóstico pode ser uma imagem UEFI no formato PE/COFF.

## Modelo de inicialização

Em uma inicialização UEFI, o firmware inicializa a plataforma, enumera dispositivos e procura uma entrada de boot persistida nas variáveis NVRAM. A entrada normalmente aponta para uma aplicação em uma EFI System Partition, conhecida como ESP. A ESP usa um filesystem compatível com a especificação, normalmente FAT32, e contém os carregadores e outros arquivos necessários ao boot.

Uma máquina pode ter várias entradas de boot, cada uma com um identificador, uma descrição e um caminho para a aplicação. O firmware também pode usar o caminho removível padronizado, como `EFI/BOOT/BOOTX64.EFI`, quando não existe uma entrada NVRAM adequada. Isso permite inicializar mídias removíveis e facilita a recuperação de sistemas.

O UEFI Boot Manager não precisa conhecer a lógica interna do sistema operacional. Ele entrega o controle à aplicação selecionada, e essa aplicação pode carregar um kernel, um segundo estágio ou outro componente de inicialização. Essa separação permite que a organização do boot varie entre sistemas sem alterar a interface básica do firmware.

## Relação com a ESP

A ESP é uma partição de boot, não o volume principal do sistema. Ela deve permanecer acessível ao firmware e não deve ser tratada como um diretório comum para arquivos arbitrários. Em uma instalação com múltiplos sistemas, os carregadores de cada sistema normalmente ocupam diretórios próprios dentro da ESP.

O sistema operacional pode criar ou alterar entradas UEFI por meio de interfaces específicas. No Linux, `efibootmgr` é uma ferramenta comum para consultar e modificar entradas NVRAM quando o sistema foi inicializado em modo UEFI. A disponibilidade e o comportamento dependem do firmware e das permissões expostas pela plataforma.

## UEFI e Secure Boot

UEFI fornece o ambiente no qual Secure Boot é implementado, mas os conceitos não são equivalentes. É possível ter uma máquina UEFI com Secure Boot desativado. Quando Secure Boot está ativo, o firmware valida as assinaturas das imagens UEFI de acordo com as bases de confiança da plataforma antes de executá-las.

A cadeia pode incluir firmware, carregador de boot, componentes intermediários e, em alguns sistemas, módulos ou drivers assinados. O objetivo é impedir a execução de imagens que não estejam autorizadas ou que tenham sido revogadas. A proteção depende da configuração das chaves, das atualizações de firmware e da integridade de cada elo da cadeia.

## Compatibilidade com boot legado

Alguns firmwares UEFI oferecem CSM, Compatibility Support Module, para inicializar sistemas que dependem do modelo legado. CSM não transforma UEFI em BIOS original; ele fornece uma camada de compatibilidade para código e mídias que esperam o fluxo antigo. Em máquinas modernas, CSM pode estar ausente ou desativado, especialmente quando Secure Boot é necessário.

Misturar os modos UEFI e legado dificulta o diagnóstico. Um instalador iniciado em modo legado pode instalar um sistema que espera boot legado, enquanto o firmware configurado para UEFI procurará uma ESP e entradas NVRAM. Antes de instalar ou reparar um sistema, confirme o modo usado pelo instalador e pelo sistema instalado.

## Diagnóstico

Ao investigar uma falha de boot UEFI, verifique o modo de inicialização atual, a existência da ESP, o conteúdo do diretório do carregador, as entradas NVRAM, o estado de Secure Boot e a ordem de boot. A ausência de uma entrada não prova que os arquivos desapareceram, porque o caminho removível pode ainda ser encontrado pelo firmware.

Uma alteração na ESP, na NVRAM ou nas variáveis autenticadas pode impedir o boot sem que o volume principal tenha sido danificado. Por isso, ferramentas de recuperação devem preservar uma cópia da ESP e registrar as entradas existentes antes de alterar a configuração.

## Fontes primárias

- [UEFI Forum, especificações](https://uefi.org/specifications)
- [UEFI Forum, visão geral da especificação](https://uefi.org/specs/UEFI/2.11/02_Overview.html)
- [Documentação do kernel Linux sobre UEFI](https://docs.kernel.org/arch/x86/uefi.html)
- [systemd-boot](https://www.freedesktop.org/software/systemd/man/latest/systemd-boot.html)
