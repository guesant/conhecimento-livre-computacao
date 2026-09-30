# Liveness probe

Liveness probe responde se o container deve ser considerado vivo. Falhas repetidas podem provocar restart conforme a política do Pod.

Ela não deve ser usada para indicar se o workload está pronto para receber tráfego. Essa responsabilidade pertence à [readiness probe](readiness-probe.md).

Uma liveness dependente de serviço externo pode reiniciar processos saudáveis durante uma falha da dependência e amplificar o incidente.
