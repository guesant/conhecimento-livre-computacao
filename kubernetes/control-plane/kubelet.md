# Kubelet

Kubelet é o agente que roda em cada nó e garante que os Pods atribuídos a ele
sejam executados. Ele lê a especificação pelo API server, conversa com o
container runtime, monta volumes, configura rede por meio do runtime de rede e
reporta status, condições e eventos.

## Reconciliação local

O kubelet compara a configuração desejada com containers, volumes e probes
existentes no nó. Ele reinicia containers segundo a restart policy, executa
liveness, readiness e startup probes e atualiza o status do Pod. Essa
reconciliação local não substitui o controller que cria um novo Pod quando o
Pod atual deixa de existir.

## Limites

Kubelet não é scheduler, API server ou controller de workload. Ele não decide
em qual nó um Pod deve ser colocado e não mantém réplicas. Problemas no
kubelet, no runtime, no CNI ou no filesystem podem fazer um Pod parecer
correto no API server enquanto não consegue iniciar no nó.

## Segurança e diagnóstico

O endpoint local do kubelet deve ter autenticação e autorização adequadas. Logs
do serviço, eventos do Pod, estado do runtime e capacidade do nó precisam ser
correlacionados. Disk pressure, falta de inode, erro de mount e falha de image
pull são failure domains diferentes.

## Fonte primária

- [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
