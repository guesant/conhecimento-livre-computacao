# RustDesk

RustDesk é uma ferramenta de controle remoto multiplataforma com cliente open source e opções de servidor self-hosted. O modelo usa identificação, conexão direta quando possível e servidores de rendezvous ou relay quando a rede impede a conexão direta.

## OSS e Pro

O servidor OSS oferece a base self-hosted. O servidor Pro acrescenta console web, SSO e controles empresariais conforme a licença. A escolha deve considerar inventário, grupos, auditoria, atualização, suporte e política de identidade, não apenas o fato de o cliente ser open source.

## Segurança

Configure servidor próprio, chave pública esperada, ACLs, autenticação forte e rede administrativa quando soberania de dados for requisito. Controle permissões locais para teclado, mouse, clipboard, arquivos, terminal e elevação. Acesso unattended deve ter inventário, expiração, logs e processo de revogação.

A criptografia da sessão não elimina o risco do endpoint: um operador autorizado pode observar e controlar a tela. Proteja o servidor de rendezvous, os clientes, os tokens e o canal de distribuição do instalador.

## Quando usar

RustDesk é adequado para suporte remoto e administração de endpoints quando self-hosting ou controle de relay são importantes. Para console de VM, SPICE pode ser mais apropriado; para administração de servidor, SSH, RDP ou Cockpit podem fornecer uma superfície menor.

## Fontes primárias

- [RustDesk documentation](https://rustdesk.com/docs/en/)
- [RustDesk client](https://rustdesk.com/docs/en/client/)
