# Organização de diretórios

Linux e Windows organizam arquivos em árvores, mas usam convenções diferentes para alcançar a raiz, montar volumes, expressar permissões e nomear caminhos.

## Linux

Linux começa na raiz `/`. Não existe uma letra de unidade como parte obrigatória do caminho. Volumes são montados em diretórios, e a hierarquia tradicional separa responsabilidades:

| Diretório | Função comum |
| --- | --- |
| `/etc` | Configuração do sistema e serviços. |
| `/usr` | Programas, bibliotecas e dados compartilhados da distribuição. |
| `/var` | Estado variável, cache, filas, logs e bancos locais. |
| `/home` | Dados dos usuários. |
| `/run` | Estado runtime, geralmente temporário. |
| `/tmp` | Arquivos temporários. |
| `/dev`, `/proc`, `/sys` | Interfaces virtuais para dispositivos e kernel. |

## Windows

Windows usa uma raiz por volume, como `C:\\` ou `D:\\`, além de caminhos UNC. Diretórios comuns incluem `C:\\Windows`, `C:\\Program Files`, `C:\\ProgramData`, `C:\\Users` e `C:\\Users\\<usuário>\\AppData`. Esses nomes não substituem a política de cada aplicação, que pode armazenar configuração no Registro, em `%ProgramData%` ou no perfil do usuário.

## Compatibilidade

Camadas como Cygwin, MSYS2 e WSL projetam uma visão POSIX sobre ou ao lado da árvore Windows. `/c/Users` em MSYS2, `/mnt/c` em WSL e uma montagem Cygwin não têm exatamente a mesma semântica de permissões, links, case sensitivity, locks ou desempenho.

Não mova automaticamente um repositório entre essas árvores esperando o mesmo comportamento. Builds com muitos arquivos e ferramentas Linux tendem a se comportar melhor dentro do filesystem Linux do WSL; aplicações Windows tendem a integrar melhor com volumes NTFS.

## Fontes primárias

- [Windows path naming](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)
- [Filesystem hierarchy standard](https://refspecs.linuxfoundation.org/fhs.shtml)
