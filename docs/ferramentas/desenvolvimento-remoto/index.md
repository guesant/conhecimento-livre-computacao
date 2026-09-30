# Desenvolvimento remoto

Desenvolvimento remoto separa a interface do editor, que roda na máquina local, da execução do projeto, que ocorre em outro host, container, VM ou workspace. O editor pode enviar um backend, conectar por SSH, usar um túnel e manter extensões ou índices próximos do código.

## Componentes

Uma sessão remota precisa de identidade, transporte, agente ou servidor remoto, filesystem, toolchain, terminal, debugger e caminho para encaminhar portas. O editor não elimina as necessidades do ambiente: compilador, SDK, dependências e credenciais continuam no host que executa o código.

## Segurança

Use contas nominativas, chaves protegidas, bastion ou VPN, forwarding mínimo, host key verification e um diretório de projeto com permissões adequadas. Não copie secrets para o workspace apenas porque a IDE não consegue acessar um serviço remoto. Separe o ambiente de desenvolvimento de produção e registre quem pode criar ou destruir workspaces.

## Ferramentas

- [VS Code Remote Development](vscode.md) oferece SSH, containers, WSL e tunnels.
- [IntelliJ e JetBrains Gateway](intellij.md) executam o backend da IDE no host remoto e usam um cliente leve local.
- [Zed](zed.md) usa um servidor remoto sobre SSH mantendo a interface local.

## Como escolher

Escolha SSH quando o host já existe e o projeto precisa de uma conexão direta. Use um workspace efêmero ou uma VM quando isolamento e reprodutibilidade forem mais importantes. Use containers remotos quando o ambiente deve ser declarado e recriado. O melhor editor é o que mantém indexação, debugging, terminal e deploy próximos do código sem ampliar desnecessariamente a superfície de acesso.
