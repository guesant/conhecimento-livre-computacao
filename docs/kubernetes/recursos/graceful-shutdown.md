# Graceful shutdown de Pods

Graceful shutdown é o processo de retirar um workload de serviço e permitir que ele encerre trabalho antes de terminar.

Kubernetes envia sinal de término e respeita um grace period antes de forçar encerramento. Hooks e comportamento da aplicação podem participar.

O desenho precisa coordenar remoção de tráfego, duração de requisições e tempo real de encerramento. Aumentar o grace period sem tornar a aplicação capaz de encerrar corretamente apenas posterga o kill.
