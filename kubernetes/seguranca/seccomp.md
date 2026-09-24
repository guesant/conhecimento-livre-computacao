# seccomp em containers

seccomp restringe syscalls que um processo pode invocar segundo um perfil.

No Kubernetes, SecurityContext pode selecionar perfis compatíveis. Restringir syscalls reduz superfície do kernel disponível ao workload.

Um perfil excessivamente restrito quebra aplicações; um perfil permissivo demais oferece pouco ganho. Compatibilidade deve ser testada.
