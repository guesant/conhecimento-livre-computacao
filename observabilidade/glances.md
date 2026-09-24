# Glances

Glances é um monitor de sistema escrito em Python, com visão em tempo real de CPU, memória, disco, rede, processos e sensores. Ele pode ser usado no terminal e oferece modos de acesso remoto e web.

## Quando usar

Glances é apropriado para inspeção rápida de um host, diagnóstico pontual e ambientes em que uma stack completa seria desproporcional. Ele não substitui retenção histórica, correlação entre hosts ou alertas duráveis.

## Operação

Execute com permissões mínimas e publique a interface remota somente atrás de autenticação e rede administrativa. Controle o intervalo de coleta e o número de plugins para não transformar o monitor em uma fonte relevante de carga no host pequeno.

## Relações

- [Netdata](netdata.md) oferece uma experiência de agente e dashboard mais contínua.
- [Zabbix](zabbix.md) oferece inventário, histórico e alertas centralizados.
- [Observabilidade](index.md) explica o que um monitor local não cobre.

## Fonte primária

- [Glances documentation](https://glances.readthedocs.io/en/latest/)
