# BSD

BSD é uma família de sistemas Unix-like cujo kernel, userland, sistema de base e documentação são desenvolvidos e lançados como uma unidade coordenada. Essa propriedade diferencia um sistema BSD de uma distribuição Linux, na qual o kernel, o userland e o empacotamento vêm de projetos que precisam ser integrados por uma distribuição. O padrão POSIX fornece uma base comum, mas não elimina as diferenças de administração, inicialização, empacotamento e segurança.

## O que pertence ao sistema de base

O sistema de base normalmente inclui kernel, bibliotecas essenciais, shell, utilitários, ferramentas de administração e documentação. O projeto controla a combinação dessas peças e testa a atualização como um conjunto, em vez de tratar cada componente como um pacote independente do sistema. Isso não significa que todo software instalado no host faça parte da base, pois aplicações de terceiros continuam sendo distribuídas separadamente.

Essa fronteira torna a atualização mais previsível, mas também torna o projeto responsável por uma superfície ampla. Uma correção no kernel, no `libc`, no `init` ou num utilitário básico pode exigir coordenação entre várias partes do mesmo ciclo de release. O operador precisa distinguir a atualização da base do sistema de pacotes adicionais instalados pelos repositórios ou pela árvore de ports.

## Principais projetos

FreeBSD é a variante generalista mais associada a servidores, rede, armazenamento e appliances. OpenBSD prioriza correção, redução da superfície de ataque e revisão contínua do código, além de manter projetos amplamente reutilizados como OpenSSH e PF. NetBSD prioriza portabilidade entre arquiteturas, enquanto DragonFly BSD segue uma linha própria de desenvolvimento de multiprocessamento e armazenamento.

Esses projetos compartilham ancestrais e ideias, mas não são intercambiáveis. Cada um possui ciclo de release, suporte de hardware, sistema de empacotamento, documentação, ferramentas de segurança e decisões de compatibilidade próprias. Quando uma aplicação diz ser compatível com BSD, confirme qual implementação, libc, shell e conjunto de utilitários foram realmente testados.

## Ports e pacotes binários

A árvore de ports descreve como obter o código-fonte, aplicar patches, selecionar opções e construir um pacote para o sistema. Ela oferece controle detalhado sobre versões e recursos, mas exige tempo de compilação, ferramentas de build, espaço temporário e uma política para reproduzir o resultado. Um port não é apenas um download de código, pois também contém metadados, dependências e instruções específicas do sistema.

Pacotes binários são construídos a partir de uma árvore de ports e publicados por repositórios do projeto ou por terceiros. Eles reduzem o custo operacional da instalação, mas transferem para o fornecedor a escolha das opções de build e a frequência de atualização. Misturar repositórios incompatíveis ou compilar uma parte crítica fora da política de atualização pode produzir uma base difícil de manter.

## Licença e consequências

As licenças BSD são permissivas e permitem redistribuição de versões modificadas, inclusive em produtos proprietários, respeitando as condições da licença. Essa característica facilitou o uso de código BSD em produtos comerciais e em outros sistemas operacionais. A licença não elimina obrigações de atribuição nem transforma todo componente de um sistema BSD em domínio público.

A licença do sistema também não determina sozinha sua segurança. A confiança depende do processo de revisão, da resposta a vulnerabilidades, da atualização da base, da configuração do host e do software adicional instalado. Compare o modelo de governança e o ciclo de suporte, não apenas o texto da licença.

## Quando considerar BSD

BSD é uma opção coerente quando a integração entre kernel e userland, o modelo de rede e armazenamento, a licença, a documentação e a previsibilidade do sistema de base atendem ao cenário. Ele aparece com frequência em firewalls, appliances, servidores de rede, sistemas de armazenamento e ambientes que valorizam uma base integrada. A escolha exige verificar drivers, aplicações necessárias, suporte comercial e conhecimento disponível na equipe.

Uma distribuição Linux pode ser melhor quando o workload depende de drivers ou ferramentas disponíveis primeiro no ecossistema Linux, de imagens OCI específicas ou de uma integração estreita com um orquestrador. O BSD também não substitui uma política de backup, hardening, monitoramento e atualização. A família fornece um modelo de sistema, não uma garantia automática de disponibilidade ou segurança.

## Relações

- [Mapa de famílias Unix](../../unix-familias-e-padroes.md) compara o modelo BSD com o das distribuições Linux e explica o papel do POSIX.
- [BSD Jail](../virtualizacao/bsd-jail.md) descreve o mecanismo de isolamento de processos do FreeBSD.
- [Solaris Zones](../virtualizacao/solaris-zones.md) apresenta outro modelo histórico de isolamento no nível do sistema.
- [Comparação entre Solaris Zones e BSD Jails](../virtualizacao/zones-jails.md) contrasta as duas abordagens.

## Fontes primárias

- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)
- [OpenBSD FAQ](https://www.openbsd.org/faq/)
- [NetBSD Guide](https://netbsd.org/docs/guide/en/)
- [DragonFly BSD Handbook](https://www.dragonflybsd.org/docs/handbook/)
- [The Open Group, POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/)
