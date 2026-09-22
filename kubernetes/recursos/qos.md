# QoS de Pods

Kubernetes deriva classes de QoS a partir da configuração de requests e limits dos containers.

Guaranteed, Burstable e BestEffort representam relações diferentes entre reserva e limites e influenciam comportamento sob pressão de recursos.

QoS não é prioridade de negócio. PriorityClass e preemption são mecanismos diferentes.

Veja [requests](requests.md) e [limits](limits.md).