# Cgroups

Control groups agrupam processos para contabilizar, priorizar e limitar recursos como CPU, memória, PIDs e I/O. Em Linux moderno, cgroups v2 organiza controllers numa hierarquia unificada.

## Casos de uso

Containers usam cgroups para aplicar limites de recursos. Serviços systemd também são organizados em cgroups. O mecanismo é útil para impedir que uma carga monopolize recursos compartilhados e para observar consumo por grupo.

## Exemplo

Em cgroups v2, arquivos como `memory.max`, `cpu.max` e `pids.max` representam controles aplicados pelo kernel. Um runtime de container traduz opções de alto nível para esses mecanismos.

## Boas práticas

Defina limites com base no comportamento real da carga e observe throttling, OOM e pressão de recursos. Diferencie limite rígido de peso/prioridade. Em Kubernetes, relacione o mecanismo com requests, limits e QoS sem tratá-los como a mesma abstração.

## Más práticas

Não configure limites arbitrariamente baixos apenas para "ter limites". Isso transforma proteção em instabilidade. O oposto, deixar toda carga sem limite em ambiente compartilhado, permite que uma falha local degrade o host inteiro.

## Falhas comuns

Ao atingir limite de memória, processos podem ser encerrados pelo OOM killer no contexto do cgroup. Código de saída 137 é um sintoma possível de SIGKILL, mas deve ser confirmado com evidência do kernel em vez de assumir automaticamente OOM.

## Fontes

- Linux kernel, cgroup v2: <https://docs.kernel.org/admin-guide/cgroup-v2.html>
- systemd, Control Group APIs and Delegation: <https://systemd.io/CGROUP_DELEGATION/>

## Continue por aqui

[Capabilities](capabilities.md) restringem privilégio, não consumo. [Requests](../../kubernetes/recursos/requests.md), [limits](../../kubernetes/recursos/limits.md) e [QoS](../../kubernetes/recursos/qos.md) mostram as abstrações correspondentes no Kubernetes.
