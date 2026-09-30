# Zed Remote Development

Zed Remote Development usa a interface local do Zed e conecta a um servidor remoto por SSH. O código, o terminal e as operações do projeto ficam no host remoto, enquanto o cliente local fornece a experiência de edição.

## Modelo

O cliente inicia ou usa um servidor Zed no host remoto e mantém a comunicação pelo transporte SSH. A versão do servidor precisa ser compatível com o cliente. O host remoto deve ter arquitetura, libc, permissões, shell e dependências compatíveis com o servidor distribuído pelo Zed.

## Segurança

Use chaves individuais, valide host keys e limite forwarding ao necessário. O servidor remoto acessa o workspace com as permissões do usuário e pode executar comandos, extensões e ferramentas do projeto. Não trate o editor como sandbox de código não confiável.

## Comparação

Zed tem um modelo mais direto e leve que uma IDE completa com backend grande. VS Code oferece mais modalidades de ambiente remoto e extensões; IntelliJ oferece um backend profundo para linguagens e frameworks JetBrains. A escolha depende de indexação, debugging, plugins, custo de recursos e integração com o host.

## Fonte primária

- [Zed remote development](https://zed.dev/docs/remote-development)
