# Secure Boot

Secure Boot é um mecanismo opcional do ambiente UEFI que valida imagens de boot antes de executá-las. O firmware compara a assinatura ou o hash da imagem com bases de confiança e de revogação armazenadas em variáveis UEFI. Quando a imagem não é autorizada ou está revogada, a execução é interrompida ou a política definida pelo firmware é aplicada.

O objetivo é proteger a cadeia inicial contra código alterado ou não autorizado antes do carregamento do sistema operacional. Secure Boot não é antivírus, não garante que o sistema operacional esteja íntegro depois do boot e não substitui atualizações, controle de acesso ou proteção de runtime.

## Cadeia de confiança

O firmware é a primeira autoridade de execução. Ele valida o carregador de boot. O carregador pode validar ou carregar componentes adicionais, como kernels, drivers e módulos, conforme a política da plataforma. Cada etapa precisa confiar explicitamente na próxima; uma assinatura válida não torna o código automaticamente seguro.

As chaves e os bancos de assinatura são explicados em [Chaves e bancos do Secure Boot](secure-boot-keys.md). A política normalmente começa com uma chave de plataforma, autoriza chaves de troca e consulta uma lista de imagens permitidas e uma lista de revogações.

## Modos de operação

O firmware normalmente diferencia setup mode e user mode. No setup mode, a plataforma ainda não está vinculada a uma Platform Key e permite provisionar a autoridade inicial. No user mode, a PK e as políticas autenticadas controlam alterações nas variáveis protegidas. Os nomes e detalhes da interface podem variar por fabricante.

Desativar Secure Boot pode ser necessário para um sistema antigo, um driver não assinado ou uma ferramenta de recuperação, mas essa decisão reduz a proteção da etapa de boot. A mudança deve ser registrada e revertida depois do procedimento. Em ambientes administrados, a política precisa definir quem pode alterar o estado e como a mudança será auditada.

## Linux e outros sistemas

Distribuições Linux podem usar um carregador assinado por uma autoridade reconhecida pelo firmware e continuar a validação em etapas posteriores. Algumas usam um carregador intermediário, como shim, que carrega o bootloader e o kernel de acordo com a política da distribuição. O detalhe da cadeia varia por distribuição e hardware.

Uma mídia USB iniciada em UEFI também precisa satisfazer a política de assinatura. A existência do arquivo `EFI/BOOT/BOOTX64.EFI` não garante que ele será aceito quando Secure Boot está ativo. Em caso de falha, verifique o modo de boot, a assinatura, o certificado presente em db e as revogações em dbx.

## Atualizações e recuperação

Atualizações de dbx podem revogar carregadores vulneráveis. Isso melhora a segurança, mas pode impedir o boot de instalações antigas que ainda dependem de uma assinatura revogada. Antes de aplicar uma atualização, confirme que o carregador e a mídia de recuperação foram atualizados.

Se uma máquina deixar de iniciar depois de uma alteração de Secure Boot, use uma mídia confiável para examinar a ESP, o estado das variáveis e os eventos do firmware. Não apague as chaves como primeira reação. Limpar PK ou restaurar chaves de fábrica altera a autoridade da plataforma e pode afetar sistemas instalados.

## Fontes primárias

- [UEFI Forum, Secure Boot e assinatura de drivers](https://uefi.org/specs/UEFI/2.10/32_Secure_Boot_and_Driver_Signing.html)
- [UEFI Forum, especificação UEFI](https://uefi.org/specifications)
- [Microsoft, orientação para criação e gerenciamento de chaves](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-secure-boot-key-creation-and-management-guidance)
- [Microsoft, cmdlet para consultar variáveis Secure Boot](https://learn.microsoft.com/en-us/powershell/module/secureboot/get-securebootuefi)
