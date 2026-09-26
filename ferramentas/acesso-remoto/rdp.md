# RDP

RDP, Remote Desktop Protocol, é o protocolo da Microsoft para transportar display, input e canais auxiliares entre um cliente e um serviço de desktop remoto. Ele suporta múltiplos canais para apresentação, clipboard, dispositivos e outros recursos conforme a versão e a implementação.

## Sessões

RDP pode conectar um usuário a uma sessão Windows existente ou criar uma sessão de Remote Desktop Services. A política do host define quem pode entrar, se múltiplas sessões são permitidas, quais dispositivos são redirecionados e quais recursos locais podem atravessar o canal.

## Segurança

Use Network Level Authentication, TLS, contas individuais, MFA quando disponível, firewall e gateway ou VPN. Não publique a porta RDP diretamente na internet sem uma arquitetura de acesso e monitoramento apropriada. Desabilite clipboard, disco, impressora, áudio ou USB quando não forem necessários.

O cliente RDP pode rodar em Windows, Linux, macOS e outras plataformas, mas o recurso de aceitar conexões depende da edição e da configuração do host Windows. A Microsoft informa que o PC remoto para o Remote Desktop integrado precisa de Windows Pro, enquanto o dispositivo cliente pode usar outras edições.

## Fonte primária

- [Microsoft RDP protocol](https://learn.microsoft.com/en-us/windows/win32/termserv/remote-desktop-protocol)
- [Microsoft Remote Desktop](https://support.microsoft.com/en-us/windows/experience/connectivity-networking/how-to-use-remote-desktop)
