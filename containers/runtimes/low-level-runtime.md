# Low-level container runtime

Um low-level runtime recebe uma descrição de execução e cria o processo confinado usando mecanismos do sistema operacional.

Ele tende a ser de vida curta: configura namespaces, mounts, capabilities e cgroups, inicia o processo e pode sair, enquanto outro supervisor mantém o ciclo de vida.

## Implementações

[runc](runc.md) e [crun](crun.md) implementam OCI Runtime Specification.