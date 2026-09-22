# Retenção de telemetria

Retenção define por quanto tempo sinais permanecem disponíveis.

A duração correta depende de uso: diagnóstico recente, comparação sazonal, auditoria, capacity planning e requisitos regulatórios possuem horizontes diferentes.

## Trade-off

Mais retenção aumenta armazenamento e, em algumas arquiteturas, custo de índice e consulta. Menos retenção pode apagar evidência necessária para incidentes descobertos tardiamente.

## Boa prática

Defina retenção por sinal e finalidade. Métricas agregadas podem merecer horizonte diferente de logs detalhados.

## Má prática

"Guardar tudo para sempre" sem consumidor ou requisito transfere uma decisão de engenharia para a fatura e para o risco de dados acumulados.

## Continue por aqui

[Pipeline de observabilidade](../composicoes/observabilidade/pipeline.md) situa retenção na camada de armazenamento.