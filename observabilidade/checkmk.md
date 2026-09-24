# Checkmk

Checkmk é uma plataforma de monitoramento baseada em descoberta, regras, checks e uma interface central de operação. Ela combina um núcleo de monitoramento com agentes e integrações para hosts, serviços, containers e dispositivos de rede.

## Quando usar

Checkmk é adequado quando descoberta e configuração guiada por interface reduzem o esforço de inventário, mas ainda são necessários checks detalhados, histórico e alertas. Existem edições e modelos de distribuição diferentes, que devem ser avaliados conforme licença e operação.

## Modelo

O servidor centraliza configuração e estado, enquanto agentes e métodos de coleta fornecem dados. Regras determinam thresholds, períodos, notificações e dependências. A descoberta automática precisa ser revisada antes de transformar novos serviços em itens monitorados.

## Limitações

A conveniência da interface não remove a necessidade de versionar configurações, controlar acesso e dimensionar retenção. Integrações que executam checks remotos devem ter autenticação, timeouts e escopo mínimo.

## Fonte primária

- [Checkmk documentation](https://docs.checkmk.com/latest/en/)
