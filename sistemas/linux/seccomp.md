# seccomp

seccomp restringe as system calls que um processo pode realizar. Em seu modo de filtragem, políticas baseadas em BPF avaliam chamadas na entrada do kernel e determinam ações como permitir, negar ou encerrar o processo.

## Casos de uso

Runtimes de container usam perfis seccomp para reduzir a superfície do kernel exposta a workloads. Sandboxes e serviços de alto risco podem aplicar políticas mais específicas quando seu conjunto de syscalls é suficientemente conhecido.

## Boas práticas

Comece por perfis mantidos e testados pelo runtime ou plataforma. Crie perfis customizados quando houver benefício concreto e capacidade de testá-los em todas as rotas relevantes da aplicação. Observe falhas para distinguir syscall bloqueada de outros erros de autorização.

## Más práticas

Desabilitar seccomp globalmente para resolver uma incompatibilidade elimina proteção de todas as cargas. No extremo oposto, gerar uma allowlist a partir de uma única execução de teste pode bloquear caminhos raros que não foram exercitados.

## Relação com outros controles

seccomp responde "esta syscall pode ser tentada?". Capabilities e LSMs respondem perguntas diferentes sobre privilégio e acesso. Permitir uma syscall não significa que a operação será autorizada.

## Fontes

- Linux kernel, seccomp filter: <https://docs.kernel.org/userspace-api/seccomp_filter.html>
- seccomp(2): <https://man7.org/linux/man-pages/man2/seccomp.2.html>

## Continue por aqui

[System calls](../kernel/system-calls.md) explica a superfície filtrada. [Capabilities](capabilities.md) explica outro eixo de restrição.
