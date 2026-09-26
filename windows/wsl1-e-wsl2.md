# WSL 1 e WSL 2

WSL 1 e WSL 2 oferecem a mesma intenção de integrar Linux ao Windows, mas usam modelos internos diferentes.

| Aspecto | WSL 1 | WSL 2 |
| --- | --- | --- |
| Kernel | Tradução de syscalls para o kernel Windows. | Kernel Linux real em uma VM leve gerenciada. |
| Compatibilidade Linux | Boa para muitas ferramentas, com diferenças em syscalls. | Maior compatibilidade de syscalls e comportamento Linux. |
| Filesystem Linux | Armazenado na árvore Windows. | Filesystem virtual Linux dentro da VM gerenciada. |
| I/O em `/mnt/c` | Frequentemente mais integrado ao Windows. | Pode ser mais lento para workloads Linux com muitos arquivos. |
| Rede | Mais próxima da rede Windows. | Possui uma camada virtual e integração própria. |
| Containers Linux | Limitados pelo modelo de compatibilidade. | Melhor alinhamento com ferramentas que esperam kernel Linux. |
| Uso de memória | Não mantém uma VM Linux completa. | A VM usa memória e recursos conforme a demanda. |

## Escolha

Escolha WSL 1 quando a integração direta com o filesystem e a rede Windows for mais importante e a aplicação funcionar com a tradução de syscalls. Escolha WSL 2 quando compatibilidade Linux, containers, systemd ou comportamento de kernel forem requisitos. Teste o workload: I/O em milhares de arquivos, acesso a `/mnt/c`, sockets e ferramentas de rede podem inverter a escolha.

## Migração

Uma distribuição pode ser convertida entre versões. Antes de mudar, faça backup ou exporte a distribuição, confirme o espaço disponível e valide mounts, serviços, chaves e ferramentas que dependem do modo atual.

## Fontes primárias

- [Comparar WSL 1 e WSL 2](https://learn.microsoft.com/en-us/windows/wsl/compare-versions)
- [What is WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
