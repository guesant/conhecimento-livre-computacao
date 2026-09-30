# Acesso remoto do Windows

O Windows possui mais de um recurso de acesso remoto. Remote Desktop usa RDP para abrir uma sessão no host. Remote Assistance e ferramentas de suporte colaborativo permitem que um usuário convide outro para observar ou controlar uma sessão existente, com fluxos e permissões diferentes.

## Remote Desktop

No host, habilite o recurso somente quando necessário, limite usuários e origem de rede e valide a edição do Windows. Em uma rede corporativa, prefira VPN, RD Gateway, bastion ou outro ponto de controle, em vez de encaminhar a porta diretamente do roteador para o host.

No cliente, o aplicativo pode guardar perfis, credenciais e redirecionamentos. Proteja o dispositivo cliente porque uma credencial salva pode equivaler ao acesso ao host.

## Administração

Use Group Policy, Windows Firewall, certificados, NLA, logs de Remote Desktop Services e políticas de conta. Desabilitar NLA, permitir login de contas administrativas genéricas ou deixar redirecionamento de disco aberto amplia o impacto de uma credencial comprometida.

## Relações

[RDP](rdp.md) descreve o protocolo. Esta página descreve o recurso do Windows, sua edição, configuração e fronteira de segurança. Ferramentas como RustDesk, AnyDesk e TeamViewer são produtos de suporte remoto com modelos de relay, conta e implantação diferentes.

## Fonte primária

- [Use Remote Desktop](https://support.microsoft.com/en-us/windows/experience/connectivity-networking/how-to-use-remote-desktop)
- [Remote Desktop Services](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/)
