# Linux namespaces

Linux namespaces particionam visões de recursos globais do kernel. Um processo
pode pertencer a um namespace de cada tipo e compartilhar outros com o host ou
com processos irmãos.

## Tipos

| Tipo | Visão isolada |
| --- | --- |
| PID | árvore de processos e seus identificadores |
| Network | interfaces, rotas, portas e regras de rede |
| Mount | pontos de montagem visíveis |
| UTS | hostname e domainname |
| IPC | mecanismos System V e filas POSIX |
| User | UIDs, GIDs e capabilities |
| Cgroup | hierarquia de cgroups observada pelo processo |
| Time | relógios monotônico e de boot |

Um container costuma combinar vários tipos, mas não existe exigência de criar
todos. Uma opção como `--network host` reutiliza a rede do host e abre mão
desse isolamento para aquele recurso.

## Criação e inspeção

`unshare` cria um processo em namespaces novos. `nsenter` executa uma
ferramenta dentro dos namespaces de um processo existente. `lsns` lista
namespaces observáveis no host. Em um diagnóstico de container, descubra o PID
do processo principal no host e compare os links em `/proc/<pid>/ns/` com os
processos que deveriam compartilhar a mesma visão.

Namespaces não são limites de CPU ou memória. Para isso, consulte cgroups.
Também não são uma política de autorização de API; no Kubernetes, RBAC possui
essa responsabilidade.

## Failure modes

Um processo pode estar no namespace esperado e ainda não alcançar o destino
porque a rota, o firewall, o DNS ou a policy estão errados. Um mount namespace
pode ocultar um arquivo sem impedir que o processo continue executando um
descritor já aberto. Um user namespace pode remapear UID 0 sem tornar o
processo root no host.

## Relações

- [Processo Linux](process.md) explica o ciclo de vida da unidade isolada.
- [User namespaces](user-namespaces.md) detalham a tradução de identidade.
- [Cgroups](cgroups.md) cobrem limites e contabilização.
- [Rede de containers](../../containers/index.md) relaciona namespaces à
  execução de workloads.

## Fontes primárias

- [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- [namespaces do kernel](https://docs.kernel.org/namespaces/index.html)
