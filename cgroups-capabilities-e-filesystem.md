# Isolamento e controle de processos no Linux

Esta página foi descompactada porque cgroups, capabilities, seccomp e isolamento de filesystem são mecanismos independentes.

- [Cgroups](sistemas/linux/cgroups.md) controlam e contabilizam recursos.
- [Capabilities](sistemas/linux/capabilities.md) decompõem privilégios.
- [seccomp](sistemas/linux/seccomp.md) filtra system calls.
- [Processos, namespaces e usuários](processo-namespaces-e-usuarios.md) explica isolamento de visão e identidade.

A combinação desses mecanismos participa da construção de containers, mas nenhum deles isoladamente representa o modelo inteiro.