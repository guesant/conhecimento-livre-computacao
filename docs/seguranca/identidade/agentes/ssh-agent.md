# SSH agent

ssh-agent é um processo que responde a pedidos de assinatura para
autenticação SSH. A chave privada pode ser carregada depois de uma passphrase e
usada em várias conexões sem que o cliente precise ler o arquivo privado a
cada tentativa.

O cliente encontra o agente pelo socket Unix indicado por SSH_AUTH_SOCK.
Qualquer processo que consiga acessar esse socket pode pedir operações
autorizadas. O agente não deve ser tratado como um cofre que resolve sozinho a
separação entre processos do mesmo usuário ou host.

## Chaves em arquivo ou hardware

O agente pode carregar chaves privadas de arquivo, mas o material pode existir
em memória enquanto estiver carregado. Ele também pode encaminhar pedidos para
uma chave em smartcard ou token, mantendo a chave dentro do dispositivo.
Hardware reduz a possibilidade de cópia, mas não impede que um processo
autorizado peça uma assinatura durante a sessão.

## Forwarding

ForwardAgent ou ssh -A disponibiliza um socket que encaminha pedidos para o
agente da máquina de origem. O servidor remoto não recebe a chave privada, mas
um processo com acesso suficiente ao socket pode usar a chave para autenticar
em outro destino enquanto o encaminhamento estiver ativo.

Prefira ProxyJump quando o objetivo é apenas alcançar um servidor através de
um bastion. O cliente local mantém a operação de autenticação e o bastion
transporta a conexão sem receber o socket do agente.

## Operação

Carregue somente as chaves necessárias, defina expiração quando a ferramenta
suportar e remova identidades ao encerrar o trabalho. Restrinja permissões do
socket, não habilite forwarding globalmente e use IdentitiesOnly para evitar
oferecer chaves irrelevantes a um servidor.

## Relações

- [SSH](../../../ssh.md) explica chaves, known_hosts e forwarding.
- [Tunelamento de portas SSH](../../../ssh-port-forwarding.md) trata transporte.
- [Agentes de chave](index.md) compara os papéis.

## Fonte

- [OpenBSD, ssh-agent](https://man.openbsd.org/ssh-agent)
