# Policy routing no Linux

Policy routing permite escolher uma tabela de rotas com base em critérios
além do destino, como endereço de origem, interface de entrada, protocolo ou
porta. Ele combina tabelas adicionais com a Routing Policy Database, RPDB.

## Tabelas e regras

`ip route show` lista a tabela principal. O kernel mantém as tabelas `local`,
`main` e `default` por padrão, com prioridades 0, 32766 e 32767. Tabelas
adicionais podem ser nomeadas em `/etc/iproute2/rt_tables` ou referenciadas
por número.

`ip rule` mostra a RPDB. Cada regra seleciona um conjunto de pacotes e indica
qual tabela consultar. O kernel avalia as regras por prioridade e usa a rota
mais específica da tabela escolhida.

## Múltiplas saídas

Um host com uma interface para a rede interna e outra para um segundo
provedor pode receber uma conexão por uma interface e responder pela rota
default da outra. Esse caminho assimétrico quebra estados de firewall e
protocolos que dependem de retorno pelo mesmo enlace.

Uma tabela por interface, com sua própria rota default, e uma regra como
`ip rule add from <endereço-da-interface> table <tabela>` fazem a resposta
retornar pelo enlace de origem. A configuração deve incluir gateway, prefixos
locais, métricas e regras de firewall correspondentes.

## Diagnóstico

Consulte `ip rule list`, `ip route show table all` e `ip route get <destino>`
com a origem explícita. Validar somente `ip route show` não revela tabelas
adicionais nem a regra que selecionou o caminho final.

## Continue por aqui

[Rota](../route.md) explica a tabela de roteamento básica. [Interfaces, rotas e
camada 2](../../interfaces-rotas-e-l2-no-linux.md) mostra como a decisão se
relaciona a interfaces e vizinhança.
