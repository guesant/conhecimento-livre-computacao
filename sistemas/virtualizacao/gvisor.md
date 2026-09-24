# gVisor

gVisor é uma sandbox que implementa uma camada de kernel em espaço de usuário
para interceptar syscalls da aplicação. O objetivo é reduzir a superfície que
o workload expõe diretamente ao kernel do host sem exigir uma VM convidada
completa para cada instância.

## Modelo

O componente Sentry implementa a maior parte da interface de sistema esperada
pelo processo. O Gofer medeia acesso a arquivos e outros recursos. O runtime
`runsc` integra o modelo com interfaces de containers e pode ser usado em
ambientes que esperam um runtime OCI.

A compatibilidade é uma decisão técnica. Syscalls incomuns, comportamento de
filesystem, debug e acesso direto a dispositivos podem não se comportar como
num runtime baseado apenas no kernel do host.

## Trade-offs

gVisor adiciona isolamento e uma implementação intermediária, mas pode
introduzir overhead e incompatibilidades. Ele é atraente quando a carga é
compatível com a sandbox e o risco de expor o kernel do host é maior que o
custo de compatibilidade e diagnóstico.

## Relações

- [MicroVM](microvm.md) usa um kernel convidado como fronteira.
- [Containers](../../containers/index.md) descreve o modelo OCI usual.
- [Hypervisor](hypervisor.md) explica a alternativa de virtualização.

## Fonte primária

- [gVisor architecture](https://gvisor.dev/docs/architecture_guide/architecture/)
