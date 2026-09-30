# VS Code Remote Development

VS Code Remote Development mantém a interface do editor no cliente e executa parte da experiência no ambiente remoto. A família inclui Remote SSH, Dev Containers, WSL e tunnels. O workspace, o terminal, ferramentas e muitas extensões podem rodar perto do código, reduzindo a necessidade de sincronizar arquivos para a máquina local.

## Remote SSH

O cliente conecta por SSH, instala ou inicia um VS Code Server no host remoto e encaminha a comunicação pelo canal autenticado. O código e os comandos permanecem no host remoto. Port forwarding permite abrir uma aplicação que escuta no host sem publicá-la diretamente.

## Extensões

Algumas extensões executam localmente, outras no host remoto e algumas dividem seus componentes. Uma extensão que acessa o filesystem, executa um compilador ou analisa o projeto precisa estar no lado correto. Isso explica por que uma extensão pode aparecer instalada e ainda não enxergar o workspace remoto.

## Segurança

Proteja a instalação do servidor remoto, o socket SSH, as chaves, o forwarding e a conta usada pela IDE. Não aceite automaticamente hosts desconhecidos, não encaminhe portas administrativas sem necessidade e não abra o VS Code Server diretamente na internet.

## Fonte primária

- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
- [Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
