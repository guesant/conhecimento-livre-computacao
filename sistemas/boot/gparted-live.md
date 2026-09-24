# GParted Live

GParted Live é uma distribuição Linux inicializável que carrega o editor de partições GParted fora do sistema operacional instalado. Ela pode ser usada por CD, USB, PXE ou disco e permite redimensionar, mover, copiar e verificar partições compatíveis.

## Quando usar

GParted Live é adequado quando o volume não pode ser desmontado pelo sistema em execução, quando o sistema instalado não inicia ou quando é necessário examinar o disco a partir de um ambiente neutro.

Ele é uma ferramenta de particionamento, não um backup. Redimensionar ou mover uma partição pode causar perda de dados. Faça e valide uma cópia antes de aplicar a operação.

## Fluxo seguro

1. Identifique o disco e a partição por tamanho, modelo e layout.
2. Confirme que o volume correto não está montado ou em uso.
3. Verifique backup e possibilidade de restauração.
4. Leia a operação planejada no painel de mudanças pendentes.
5. Execute uma operação por vez quando o impacto for alto.
6. Aguarde a conclusão sem desligar a máquina.
7. Reinicie e valide sistema de arquivos, bootloader e dados.

O programa permite acumular operações antes de aplicá-las. Essa conveniência pode esconder um conjunto destrutivo grande; revise a fila inteira antes de confirmar.

## Capacidades e limites

GParted entende diversos sistemas de arquivos por meio das ferramentas disponíveis na imagem, mas não deve ser usado para alterar um volume cuja implementação ou criptografia não seja reconhecida. Em volumes LUKS, LVM, RAID ou filesystems especiais, a sequência correta pode exigir ativar a camada inferior antes de editar a camada superior.

A ferramenta não corrige qualquer falha de hardware. Erros de leitura, setores instáveis e falhas de controladora devem ser tratados antes ou durante a cópia de recuperação.

## Boot

A imagem pode ser gravada em USB ou CD e também publicada em PXE. Em máquinas UEFI, confirme compatibilidade de Secure Boot e arquitetura. Uma mídia que inicia em um computador não necessariamente inicia em outro por causa de firmware, vídeo, armazenamento ou modo de boot.

Use uma imagem baixada de fonte confiável e valide o checksum ou assinatura disponibilizado pelo projeto.

## Diagnóstico

Se a partição não aparece, verifique cabo, controlador, modo SATA, criptografia, RAID, tabela de partições e mensagens do kernel. Se a operação falhar, preserve os logs e não repita uma alteração destrutiva automaticamente.

Se o sistema não iniciar depois, diferencie tabela de partições danificada, filesystem inconsistente, partição de boot ausente, bootloader não atualizado, modo UEFI e Legacy incompatível e disco ou memória com falha.

## Relações

- [Instalação pela rede](network-install.md) explica como iniciar GParted por PXE.
- [Hiren's BootCD PE](hirens-bootcd-pe.md) oferece ferramentas em Windows PE.
- [MemTest86 e Memtest86+](memtest.md) ajudam a descartar RAM instável antes de editar discos.
- [Backup e recuperação](../../confiabilidade/backup/index.md) define a proteção necessária antes da operação.

## Fontes primárias

- [GParted Live](https://gparted.org/livecd.php)
- [GParted download and checksums](https://gparted.org/download.php)
- [GParted Live manual](https://gparted.org/display-doc.php?name=gparted-live-manual)
