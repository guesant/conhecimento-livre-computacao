# Ferramentas de acesso remoto

Ferramentas de acesso remoto podem oferecer um terminal SSH, transferência de arquivos, administração gráfica ou uma combinação desses recursos. Elas não substituem o modelo de autenticação, autorização e auditoria do sistema remoto; apenas fornecem uma interface diferente para os mesmos protocolos e APIs.

## Escolha por responsabilidade

[Cockpit](cockpit.md) é uma interface web para administrar um servidor Linux usando as credenciais e os serviços do próprio sistema. [Termius](termius.md) é um cliente multiplataforma voltado principalmente a SSH, SFTP e organização de conexões. [RustConn](rustconn.md) é um gerenciador de conexões para Linux que reúne SSH, RDP, VNC, serial, Telnet, Mosh e outros transportes.

Uma interface gráfica não elimina a necessidade de entender o caminho de rede, a identidade usada, o host key verification, o encaminhamento de agente e o escopo das permissões. Em ambientes sensíveis, a preferência deve ser por conexões auditáveis, chaves protegidas e exposição mínima dos serviços de administração.

## Relação com SSH

Cockpit pode usar SSH para acessar outros hosts. Termius e RustConn podem abrir sessões SSH e, conforme a plataforma e a edição, oferecer recursos como SFTP, jump host, proxy e port forwarding. O modelo nativo do protocolo está descrito em [SSH](../../ssh.md), e os quatro modos de encaminhamento estão em [tunelamento de portas SSH](../../ssh-port-forwarding.md).

## Fontes primárias

- [Cockpit](https://cockpit-project.org/)
- [Documentação do Cockpit](https://cockpit-project.org/documentation.html)
- [Termius](https://termius.com/)
- [RustConn](https://github.com/totoshko88/RustConn)
