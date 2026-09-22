# OCI Runtime Specification

OCI Runtime Specification define como descrever e executar um container a partir de um filesystem e uma configuração.

O bundle inclui uma raiz de filesystem e um `config.json` que descreve processo, mounts, namespaces, capabilities e outros parâmetros.

## Implementação

[Low-level runtimes](../runtimes/low-level-runtime.md) como [runc](../runtimes/runc.md) e [crun](../runtimes/crun.md) implementam essa camada.

## Fronteira

A spec não define registry, build de imagem ou experiência de administração de um engine.