# PodDisruptionBudget

PodDisruptionBudget limita indisponibilidade causada por disrupções voluntárias que usam a API de eviction.

Ele não impede queda física de nó, perda de rede ou outras disrupções involuntárias e não cria réplicas.

Um PDB restritivo sem capacidade suficiente pode impedir manutenção planejada. Disponibilidade depende também de réplicas, placement e failure domains.
