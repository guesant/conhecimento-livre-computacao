# Windows Subsystem for Linux

WSL permite instalar e executar distribuições Linux integradas ao Windows. A distribuição tem seu próprio userland, filesystem e ferramentas, mas o grau de compatibilidade depende de estar usando WSL 1 ou WSL 2.

## Integração

O Windows pode iniciar processos Linux e Windows de forma integrada, montar drives Windows, expor variáveis e oferecer integração de rede e arquivos. Essa conveniência não elimina as diferenças entre os modelos de permissões, path, line endings, sockets e processos.

WSL é adequado para desenvolvimento, automação e ferramentas Linux. Não é automaticamente equivalente a uma VM Linux genérica ou a um host de produção: recursos de kernel, systemd, dispositivos, networking e storage precisam ser verificados para o caso concreto.

## WSL 1 e WSL 2

[WSL 1 e WSL 2](wsl1-e-wsl2.md) detalha a diferença arquitetural. WSL 1 traduz syscalls Linux para o kernel Windows. WSL 2 usa um kernel Linux dentro de uma máquina virtual leve gerenciada pelo Windows. Uma distribuição pode ser convertida entre os modos e ambas podem coexistir.

## Segurança e operação

A distribuição WSL herda parte do contexto de segurança do usuário Windows, mas não deve ser tratada como um processo Windows comum. Arquivos em `/mnt/c` têm semântica de permissões e desempenho diferentes dos arquivos no filesystem virtual Linux. Para builds Linux, mantenha o repositório no filesystem Linux quando o desempenho de I/O for relevante.

## Fonte primária

- [What is WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
- [WSL documentation](https://learn.microsoft.com/en-us/windows/wsl/)
