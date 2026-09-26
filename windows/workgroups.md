# Workgroups no Windows

Um workgroup é um modelo de organização peer-to-peer em que cada computador mantém suas próprias contas e políticas. Não há um diretório central que autentique os usuários de todos os dispositivos. Para acessar um compartilhamento, a máquina de destino precisa reconhecer uma conta local ou uma credencial compatível.

## Workgroup e domínio

| Aspecto | Workgroup | Domínio |
| --- | --- | --- |
| Identidade | Contas locais por computador. | Diretório central, normalmente Active Directory. |
| Administração | Repetida em cada máquina. | Políticas e grupos podem ser centralizados. |
| Escala | Pequenas redes e laboratórios. | Organizações com muitos usuários e dispositivos. |
| Dependência | Não exige controlador de domínio. | Depende de serviços de identidade e DNS adequados. |
| Isolamento | Cada host é uma autoridade separada. | Uma conta ou política pode afetar muitos hosts. |

Um workgroup não é uma fronteira de segurança forte nem uma senha compartilhada. Ele apenas define a ausência de uma autoridade central de domínio. Compartilhamentos, firewall, SMB, UAC e permissões NTFS continuam precisando de configuração própria.

## Políticas

Workgroup pode usar políticas locais, Local Security Policy, Windows Defender Firewall, UAC, usuários e grupos locais. Em uma frota, a repetição manual aumenta drift e dificulta auditoria. Quando políticas, identidade e inventário precisam ser centralizados, avalie domínio, MDM ou outra camada de gerenciamento.

## Fonte primária

- [Microsoft, configurar uma pequena rede e workgroup](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/set-up-your-small-business-network)
- [Microsoft, ingressar em um domínio](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain)
