# MicroVMs e sandboxes de processo

MicroVMs e sandboxes ocupam o espaço entre um container comum e uma máquina
virtual completa. Cada alternativa adiciona uma fronteira de isolamento e um
custo operacional diferente.

## MicroVMs

Firecracker é um monitor de máquina virtual baseado em KVM, criado para
workloads como Lambda e Fargate. Ele reduz dispositivos emulados e mantém um
kernel convidado próprio, buscando combinar inicialização rápida com uma
fronteira mais forte que namespaces compartilhados.

Kata Containers aplica uma ideia semelhante a containers e Pods: cada unidade
roda dentro de uma VM leve, usando QEMU ou Firecracker por trás de um runtime
compatível com OCI. O custo aparece em tempo de inicialização e memória por
instância, mas o workload deixa de compartilhar o kernel do host.

## Sandboxes

gVisor intercepta chamadas de sistema por meio do componente Sentry e media o
acesso ao filesystem com o Gofer. O runtime `runsc` o integra a Docker e
Kubernetes. Essa abordagem reduz a superfície exposta ao kernel real sem
exigir uma VM completa, mas pode ter incompatibilidades com chamadas de
sistema menos comuns.

`bubblewrap` fica mais próximo de um container tradicional: usa namespaces do
Linux, não possui daemon nem formato próprio de imagem e declara o sandbox por
linha de comando.

## Critérios

MicroVMs fazem sentido quando o isolamento do kernel é requisito e o overhead
de uma VM tradicional é alto. Sandboxes de processo são adequados quando o
runtime precisa continuar leve e a aplicação é compatível com uma superfície
de chamadas de sistema mediada. Nenhuma dessas opções substitui a análise de
capabilities, filesystem, rede e ciclo de vida do workload.

## Continue por aqui

[Máquinas virtuais](../../vms-e-hipervisores.md) explica o isolamento
completo. [Containers de sistema](system-containers.md) trata a alternativa
que continua compartilhando o kernel do host.
