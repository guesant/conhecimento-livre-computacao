# Resource requests

Resource request declara a quantidade de um recurso que o scheduler considera ao posicionar um Pod.

Request não é consumo atual nem teto. Ele representa a demanda usada para decidir se há capacidade alocável suficiente no nó.

Requests subestimados favorecem overcommit e podem aumentar contenção. Requests superestimados desperdiçam capacidade de scheduling.

Veja [limits](limits.md) e [QoS](qos.md).
