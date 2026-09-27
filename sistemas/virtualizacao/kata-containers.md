# Kata Containers

Kata Containers é um runtime que combina a interface operacional de containers com uma máquina virtual leve por workload. Em vez de executar o processo diretamente no kernel do host, ele inicia um ambiente convidado e conecta o workload a esse ambiente por uma integração compatível com o ecossistema OCI e Kubernetes. A finalidade é aumentar a separação do kernel sem exigir uma VM administrada como um host completo.

## Modelo de execução

O runtime recebe uma especificação de container, prepara uma sandbox virtualizada e inicia um guest kernel com os recursos necessários. A camada de integração precisa traduzir operações de rede, filesystem, dispositivos, sinais e ciclo de vida para o ambiente convidado. O detalhe da implementação varia conforme o hypervisor, o kernel guest e a configuração do runtime.

Essa arquitetura cria mais componentes do que um runtime baseado apenas em namespaces. O host, o runtime, o hypervisor, o kernel guest e a aplicação possuem logs, métricas, falhas e atualizações próprias. A equipe deve observar todas essas camadas, porque um Pod pode estar saudável no Kubernetes enquanto o guest ou o caminho de I/O enfrenta problemas.

## Isolamento e compatibilidade

O kernel convidado reduz a exposição direta ao kernel do host e pode ser uma escolha adequada para workloads com código não confiável, multi-tenancy ou requisitos de isolamento mais fortes. Isso não elimina vulnerabilidades no hypervisor, no runtime, na imagem ou no guest kernel. A proteção ainda depende de políticas de identidade, filesystem, rede, capabilities, seccomp e origem das imagens.

O custo inclui memória adicional, tempo de boot, complexidade de debugging, integração de dispositivos e possíveis diferenças de compatibilidade. Workloads que dependem de acesso direto ao host, de módulos específicos ou de latência muito baixa podem não se adaptar bem. Faça testes representativos antes de trocar o runtime por uma expectativa abstrata de segurança.

## Uso no Kubernetes

No Kubernetes, Kata Containers pode ser selecionado por uma RuntimeClass para que apenas workloads compatíveis usem o runtime virtualizado. A escolha deve ser explícita e observável, com limites de recursos, política de scheduling, imagens suportadas e um procedimento de rollback. O cluster precisa ter os componentes e permissões necessários em cada nó elegível.

A RuntimeClass não altera o contrato da aplicação nem transforma todo o cluster em uma VM. Ela define qual runtime executa o Pod e, portanto, qual fronteira e qual custo aquele workload recebe. Avalie o efeito sobre autoscaling, probes, volumes, rede, GPU e coleta de logs antes de aplicar a classe por padrão.

## Relações

- [MicroVM](microvm.md) explica o modelo de virtualização leve.
- [Firecracker](firecracker.md) é uma implementação de microVM usada em algumas composições.
- [Containers de sistema](system-containers.md) compartilham o kernel do host.
- [Mapa de MicroVMs e sandboxes](microvms-e-sandboxes.md) compara famílias de isolamento.

## Fontes primárias

- [Kata Containers documentation](https://katacontainers.io/docs/)
- [Kata Containers architecture](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture.md)
- [Kubernetes RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/)
