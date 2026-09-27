# Desenvolvimento remoto com IntelliJ

JetBrains Remote Development executa o backend da IDE no ambiente remoto e abre um JetBrains Client local. JetBrains Gateway inicia ou encontra esse backend e pode conectar por SSH ou por plataformas de workspace compatíveis.

## Modelo

O backend remoto mantém projeto, indexação, compilação, execução e debugging perto do código. O cliente local renderiza a interface e encaminha a interação. Isso reduz o custo de sincronizar grandes repositórios, mas o host remoto precisa ter SDK, dependências, ferramentas de build e recursos suficientes para indexação.

## Rede e proxy

A conexão pode usar SSH, proxy HTTP/SOCKS e os túneis necessários ao backend. Não basta liberar a porta da aplicação: valide o canal de controle, os port forwards, o acesso ao package manager e a resolução de nomes do host remoto.

## Segurança

Use uma conta remota restrita, chaves individuais, host key verification e um workspace sem secrets desnecessários. O backend da IDE executa código do projeto com as permissões do usuário, portanto abrir um projeto não confiável no host de desenvolvimento pode ser uma ação privilegiada.

## Fonte primária

- [JetBrains Gateway](https://www.jetbrains.com/help/idea/remote-development-a.html)
- [IntelliJ remote development](https://www.jetbrains.com/help/idea/remote-development-starting-page.html)
