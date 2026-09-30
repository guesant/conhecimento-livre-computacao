# BSD Jail

BSD Jail é um mecanismo de isolamento do FreeBSD que limita o escopo de processos, filesystem, identidade e rede dentro de um host que compartilha o kernel. Ele nasceu como uma extensão do modelo de `chroot`, mas a fronteira não se resume a trocar o diretório raiz. Um jail pode representar um ambiente de serviço com filesystem próprio, usuários e interfaces de rede controlados pelo host.

## Modelo de isolamento

O host mantém a autoridade administrativa sobre os jails e decide quais recursos podem ser vistos ou alterados. Processos dentro de um jail não devem enxergar livremente processos, dispositivos, interfaces ou configurações pertencentes ao host. O grau exato de isolamento depende das permissões, das opções do jail, do modo de rede, do acesso a `devfs` e do código que roda dentro dele.

O mecanismo compartilha o kernel do host. Isso reduz o custo em relação a uma máquina virtual, mas também significa que uma vulnerabilidade no kernel ou uma configuração privilegiada pode afetar a fronteira de todos os jails. Um jail não deve ser descrito como uma VM, e a decisão de usá-lo precisa considerar o nível de isolamento exigido pelo adversário e pelo workload.

## Rede e filesystem

Um jail pode usar uma pilha de rede compartilhada com endereços controlados ou o modelo VNET, que fornece uma pilha e interfaces de rede virtualizadas com maior separação. A escolha afeta roteamento, firewall, observabilidade, binding de portas e integração com bridges. O host precisa continuar sendo a autoridade para endereços, rotas e exposição externa.

O filesystem do jail deve ser preparado com uma política clara de leitura, escrita, montagem e persistência. Expor dispositivos, sockets administrativos ou diretórios do host pode desfazer a separação que o jail pretendia criar. Dados persistentes devem ter backup e lifecycle próprios, em vez de depender de uma cópia implícita da árvore do sistema.

## Administração e ciclo de vida

O host cria, inicia, interrompe, atualiza e destrói o jail. O sistema de base e as ferramentas de gerenciamento devem registrar a configuração, o caminho do filesystem, o modo de rede, os limites e os serviços iniciados. Uma atualização segura precisa ser reproduzível e permitir validar o serviço antes de remover a versão anterior.

Jails podem ser usados para consolidar serviços, separar aplicações legadas e criar ambientes de teste com baixo overhead. Eles não resolvem sozinhos dependências de versão, identidade, armazenamento, observabilidade ou atualização. O serviço dentro do jail continua precisando de autenticação, autorização, logging, limites e gestão de vulnerabilidades.

## Relação com outros mecanismos

Linux namespaces e cgroups decompõem o isolamento em dimensões configuráveis, enquanto um jail oferece uma abstração integrada ao sistema FreeBSD. Solaris Zones também apresenta uma unidade de isolamento no nível do sistema, mas possui modelo, ferramentas e ciclo de vida próprios. Containers de sistema Linux, como LXC e Incus, ocupam espaço semelhante sem serem implementações do jail.

Quando a fronteira do kernel precisa ser independente, uma microVM ou uma VM tradicional é mais apropriada. Quando o objetivo é apenas limitar uma aplicação e sua imagem, um container de aplicação pode ter um ciclo de vida mais simples. A escolha deve considerar isolamento, compatibilidade, persistência, operação e failure domains.

## Relações

- [BSD](../unix/bsd.md) explica a família de sistemas que fornece o mecanismo.
- [Solaris Zones](solaris-zones.md) descreve a alternativa histórica de isolamento.
- [Comparação entre Solaris Zones e BSD Jails](zones-jails.md) compara as duas abordagens.
- [Containers de sistema](system-containers.md) apresenta a alternativa baseada em Linux.
- [Namespaces](../linux/namespaces.md) explica as primitivas de isolamento do Linux.

## Fontes primárias

- [FreeBSD Handbook, jails](https://docs.freebsd.org/en/books/handbook/jails/)
- [FreeBSD jail manual](https://man.freebsd.org/cgi/man.cgi?query=jail)
- [FreeBSD VNET](https://docs.freebsd.org/en/books/handbook/jails/#jails-vnet)
