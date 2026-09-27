# Kubewarden

Kubewarden é um sistema de políticas para Kubernetes que executa policies
compiladas para WebAssembly. A abordagem permite escrever políticas em mais de
uma linguagem e distribuí-las como módulos.

## Modelo

As policies são avaliadas durante admission. O operador registra módulos,
configura escopos e define se uma violação deve bloquear ou apenas auditar.

## Trade-offs

WebAssembly facilita portabilidade, mas introduz ciclo de build, assinatura,
distribuição e compatibilidade do runtime. O módulo deve ser tratado como
artefato de supply chain.

## Fonte

- [Documentação do Kubewarden](https://docs.kubewarden.io/)
