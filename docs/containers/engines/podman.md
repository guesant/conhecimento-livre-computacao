# Podman

Podman é um container engine com operação local daemonless. Ele administra containers e Pods e pode operar rootless usando user namespaces.

## Casos de uso

É adequado para hosts Linux em que integração com systemd, operação rootless e ausência de daemon central são propriedades desejadas.

## Rootless

Rootless reduz privilégios do engine e dos containers no host, mas possui implicações de UID/GID, portas, filesystem e networking que precisam ser compreendidas.

## Integração

[Quadlet](../../podman-quadlets.md) integra declarações de containers com systemd.

## Continue por aqui

[Docker Engine](docker-engine.md) representa um modelo alternativo de engine.
