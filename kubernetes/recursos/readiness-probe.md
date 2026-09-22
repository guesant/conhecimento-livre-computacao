# Readiness probe

Readiness probe indica se o workload está pronto para receber tráfego por mecanismos que respeitam sua condição de readiness.

Falhar readiness normalmente remove o endpoint da seleção sem exigir restart do processo.

Use-a para condições transitórias que tornam atendimento inadequado. Não a confunda com [liveness](liveness-probe.md).