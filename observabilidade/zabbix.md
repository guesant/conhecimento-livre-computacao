# Zabbix

Zabbix é uma plataforma de monitoramento de redes, servidores, aplicações e dispositivos. Ela combina coleta, descoberta, templates, histórico, tendências, triggers e notificações em um modelo centralizado.

## Quando usar

Zabbix é adequado para ambientes tradicionais e corporativos que precisam de inventário, descoberta automática, dependências e regras de alerta detalhadas. O servidor, o banco de dados e os proxies formam uma arquitetura que precisa ser dimensionada conforme a cardinalidade e a retenção.

## Modelo

Agentes, SNMP, IPMI, checks HTTP e integrações fornecem itens de coleta. Triggers avaliam condições e ações encaminham eventos. Templates aceleram a padronização, mas devem ser ajustados para não transformar toda métrica disponível em alerta.

## Limitações

Retenção longa em um único banco e descoberta ampla podem gerar custo de armazenamento e consultas. Defina janelas, níveis de severidade, escalonamento e responsáveis antes de ativar notificações.

## Relações

- [Observabilidade](index.md) separa sinais, retenção e ação.
- [Prometheus](prometheus.md) usa um modelo diferente, orientado a séries temporais e scraping.
- [Alertas acionáveis](alertas-acionaveis.md) explica como evitar ruído.

## Fonte primária

- [Zabbix documentation](https://www.zabbix.com/documentation/current/en/manual)
