# Mapa de chaves e bancos do Secure Boot

Secure Boot usa variáveis UEFI autenticadas para estabelecer quem pode alterar a política e quais imagens podem ou não ser executadas. As quatro estruturas mais conhecidas são PK, KEK, db e dbx. Elas formam uma hierarquia de autorização, mas não são quatro cópias da mesma chave.

## PK, Platform Key

A Platform Key, ou PK, estabelece a autoridade principal da plataforma. Em user mode, a PK autoriza alterações nas chaves de troca e em parte da configuração autenticada do firmware. Uma plataforma normalmente possui uma PK ativa, embora a representação interna seja definida pela especificação e pelo firmware.

O proprietário pode ser o fabricante, a organização que administra o equipamento ou o usuário. Substituir a PK muda a autoridade de administração da plataforma. Remover a PK normalmente coloca o firmware em setup mode, mas o efeito exato deve ser confirmado na documentação do fabricante.

## KEK, Key Exchange Key

As Key Exchange Keys, ou KEK, autorizam atualizações de bases de assinatura como db e dbx. Pode haver mais de uma KEK, porque fabricantes, sistema operacional e organização administradora podem precisar de autoridades distintas.

Uma KEK não é a lista de programas permitidos. Ela é uma autoridade de atualização. Se uma KEK for comprometida, um atacante pode tentar alterar a política de confiança, sujeito às proteções e validações do firmware.

## db, allowed signature database

db é a base de assinaturas, certificados e hashes permitidos. Quando o firmware valida uma imagem UEFI, ele procura uma correspondência nessa base ou em uma cadeia de certificados autorizada. A base pode conter certificados do fabricante, do sistema operacional, de uma distribuição Linux ou da organização que administra a máquina.

Adicionar uma autoridade à db amplia o conjunto de imagens que podem ser executadas. Por isso, a base deve ser pequena, documentada e atualizada somente por um processo controlado. Uma entrada aparentemente conveniente pode autorizar mais código do que o necessário.

## dbx, forbidden signature database

dbx é a base de assinaturas, certificados e hashes revogados. Ela bloqueia imagens que antes poderiam ter sido aceitas, normalmente porque uma vulnerabilidade foi descoberta ou uma autoridade deixou de ser confiável.

Na decisão de boot, uma revogação em dbx deve impedir a execução mesmo que a imagem também corresponda a uma entrada permitida em db. Isso é essencial para retirar da cadeia um carregador vulnerável que ainda possui uma assinatura válida.

Uma atualização de dbx pode afetar mídia de recuperação e sistemas antigos. A aplicação deve ser acompanhada de teste de boot, plano de recuperação e confirmação de que os carregadores usados pelo ambiente não dependem de certificados ou hashes revogados.

## Relação entre as estruturas

O fluxo conceitual é:

1. PK define a autoridade de plataforma.
2. KEK autoriza mudanças nas bases de política.
3. db lista o que pode ser executado.
4. dbx lista o que não pode ser executado.

Essa sequência é uma simplificação operacional. O firmware pode ter políticas adicionais, certificados intermediários, variáveis específicas do fabricante e regras para drivers ou Option ROMs. A especificação UEFI e a documentação da plataforma devem prevalecer sobre qualquer diagrama simplificado.

## Administração e diagnóstico

No Linux, `efi-vars` e `efibootmgr` ajudam a observar partes do estado UEFI, mas não substituem as ferramentas de gerenciamento de chaves do firmware. No Windows, o cmdlet `Get-SecureBootUEFI` expõe variáveis como PK, KEK, db e dbx. Leitura e alteração exigem privilégios e podem depender de modo de boot e suporte do firmware.

Não altere PK, KEK, db ou dbx em produção sem backup da configuração, teste em hardware equivalente e uma mídia de recuperação compatível. A perda da autoridade correta ou a inclusão de uma revogação inadequada pode deixar a máquina sem um caminho de boot aceito.

## Fontes primárias

- [UEFI Forum, Secure Boot e assinatura de drivers](https://uefi.org/specs/UEFI/2.10/32_Secure_Boot_and_Driver_Signing.html)
- [Microsoft, chaves e bancos recomendados](https://learn.microsoft.com/en-gb/windows-hardware/manufacture/desktop/windows-secure-boot-key-creation-and-management-guidance?view=windows-11)
- [Microsoft, consulta das variáveis Secure Boot](https://learn.microsoft.com/en-us/powershell/module/secureboot/get-securebootuefi)
