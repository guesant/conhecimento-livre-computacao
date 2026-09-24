# runc

runc é um low-level runtime que implementa OCI Runtime Specification.

Ele recebe um bundle OCI, configura os mecanismos de isolamento solicitados e inicia o processo do container.

## Fronteira

runc não é um engine, registry ou scheduler. Ferramentas de camadas superiores normalmente o invocam.

## Continue por aqui

[Low-level runtime](low-level-runtime.md) explica a categoria e [crun](crun.md) é uma implementação alternativa.
