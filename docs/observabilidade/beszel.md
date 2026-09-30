# Beszel

Beszel é uma plataforma leve de monitoramento de servidores, especialmente adequada a homelabs e hosts que executam containers. Ela separa um hub, que apresenta e retém dados, de agentes instalados nos hosts monitorados.

## Quando usar

Beszel faz sentido quando a prioridade é uma visão simples de CPU, memória, disco, rede e containers sem implantar uma stack grande. Para inventário corporativo, correlação de traces ou regras complexas, outras plataformas podem ser mais apropriadas.

## Operação

Proteja o hub e os tokens de agente, limite a exposição da interface e configure retenção compatível com o disco disponível. Monitore o próprio hub e defina o que acontece quando um agente fica offline, para não confundir ausência de dados com saúde.

## Relações

- [Glances](glances.md) oferece inspeção local imediata.
- [Netdata](netdata.md) oferece dashboards de agente com outro modelo de retenção e integração.
- [Zabbix](zabbix.md) é uma alternativa mais abrangente para monitoramento centralizado.

## Fonte primária

- [Beszel](https://github.com/henrygd/beszel)
