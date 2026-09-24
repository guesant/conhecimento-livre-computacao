# Podman Compose

`podman compose` é um wrapper que executa um provedor externo de Compose e prepara o ambiente para que esse provedor converse com o socket do Podman. O comando não é, sozinho, uma implementação completa e independente da Compose Specification.

## Provedor externo

O provedor efetivo pode ser `docker-compose`, `podman-compose` ou outro executável configurado no `containers.conf` ou em `PODMAN_COMPOSE_PROVIDER`. As opções e os comandos disponíveis dependem desse provedor. Duas máquinas com o mesmo comando `podman compose` podem ter comportamentos diferentes se resolverem provedores ou versões diferentes.

Essa camada de indireção é útil para preservar uma interface familiar, mas precisa ser observada em diagnósticos e CI. Quando um campo da spec não funciona, a pergunta correta é qual provedor interpretou o arquivo e qual parte da spec ele suporta, não apenas qual versão do Podman está instalada.

## Rootless e permissões

O Podman pode operar sem daemon privilegiado e como usuário comum, mas a composição ainda precisa lidar com permissões de volumes, rede, mapeamento de UID/GID e acesso a sockets. Um arquivo pensado para um daemon rootful pode não funcionar sem ajustes em um ambiente rootless.

## Quando usar

Podman Compose é útil quando a equipe já usa a Compose Specification e quer executar a composição através do Podman. Ele é menos adequado como abstração de compatibilidade cega entre Docker e Podman quando a aplicação depende de extensões específicas do engine ou de comportamento não padronizado pelo arquivo.

Para workloads de um único host com requisitos de lifecycle mais explícitos, [Quadlets](../../podman-quadlets.md) podem oferecer uma composição mais integrada ao systemd. Para scheduling e reconciliação entre nós, Compose não substitui Kubernetes.

## Relações

- [Compose Specification](specification.md) define o contrato compartilhado.
- [Docker Compose](docker-compose.md) é outra implementação do mesmo modelo.
- [Podman](../engines/podman.md) fornece o engine e o socket consumido pelo provedor.
- [GitOps para Podman](../../gitops-para-podman-orches-e-materia.md) descreve um cenário de host único.

## Fonte primária

- [podman compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html)
