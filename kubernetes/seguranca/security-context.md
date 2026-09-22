# SecurityContext

SecurityContext configura propriedades de segurança de Pods e containers, como identidade de usuário, privilege escalation, capabilities, seccomp e filesystem.

Ele é um agrupador de configuração. Cada mecanismo subjacente possui semântica própria e não deve ser tratado como uma única proteção.

Veja [run as non-root](run-as-non-root.md), [allowPrivilegeEscalation](allow-privilege-escalation.md), [capabilities](linux-capabilities.md), [seccomp](seccomp.md) e [read-only root filesystem](read-only-root-filesystem.md).