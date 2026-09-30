# Golden signals

Golden signals são quatro dimensões popularizadas pela prática de Site Reliability Engineering: latency, traffic, errors e saturation.

Elas ajudam a começar uma visão operacional cobrindo demanda, experiência, falha e capacidade.

## Relação com RED e USE

Há sobreposição: RED cobre rate/traffic, errors e duration/latency; USE enfatiza utilization, saturation e errors. Golden signals não tornam as outras heurísticas incorretas.

## Má prática

Criar exatamente quatro painéis por serviço sem perguntar quais operações representam tráfego ou erro transforma uma heurística em checklist.

## Continue por aqui

[RED](red.md) e [USE](use.md) são modelos relacionados.
