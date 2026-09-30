# VNC

VNC é uma família de implementações que usa o protocolo RFB, Remote Framebuffer, para transportar a imagem de uma sessão e eventos de input. O servidor captura ou fornece um framebuffer; o cliente renderiza a tela e envia teclado e mouse.

## Sessão

Um servidor VNC pode compartilhar uma sessão gráfica existente ou criar uma sessão virtual separada. Essa diferença é operacionalmente importante: `x0vncserver` e ferramentas semelhantes podem espelhar uma sessão, enquanto outros servidores criam um desktop novo com seu próprio display.

## Segurança

VNC não deve ser exposto diretamente à internet apenas porque a senha funciona. A proteção varia por implementação, versão e configuração. Use VPN, túnel SSH, rede administrativa ou um gateway; valide criptografia, autenticação, autorização e logs do servidor específico.

VNC pode transportar uma tela inteira e input, mas não oferece por si só a identidade ou o modelo de autorização de uma sessão SSH. Separe contas, limite origem, desabilite compartilhamento quando não for necessário e evite senhas reutilizadas.

## Implementações

TigerVNC é uma implementação comum para clientes e servidores. `x11vnc` pode compartilhar uma sessão X11 existente. Em Wayland, o modelo de captura e controle depende do compositor e de portais, por isso uma configuração X11 não pode ser transportada automaticamente para qualquer sessão Wayland.

## Fontes primárias

- [TigerVNC](https://tigervnc.org/)
- [TigerVNC viewer](https://tigervnc.org/doc/vncviewer.html)
- [RFB protocol specification](https://www.rfc-editor.org/rfc/rfc6143)
