# Recursos de workload no Kubernetes

Workloads combinam objetos e propriedades independentes. Esta categoria separa recursos de scheduling, execução, saúde e disponibilidade para que cada um tenha semântica própria.

[Resource requests](requests.md) influenciam scheduling. [Resource limits](limits.md) impõem limites em runtime. [QoS](qos.md) classifica Pods conforme configuração de recursos. [Liveness](liveness-probe.md), [readiness](readiness-probe.md) e [startup probes](startup-probe.md) respondem perguntas diferentes. [PodDisruptionBudget](pdb.md) limita disrupções voluntárias. [Graceful shutdown](graceful-shutdown.md) trata encerramento coordenado.