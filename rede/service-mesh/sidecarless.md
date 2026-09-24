# Sidecarless service mesh

Sidecarless mesh implementa funções de service mesh sem exigir um proxy dedicado por workload.

A responsabilidade pode migrar para proxies por nó, kernel/eBPF ou outros pontos do dataplane. "Sem sidecar" não significa "sem dataplane"; muda onde ele existe.
