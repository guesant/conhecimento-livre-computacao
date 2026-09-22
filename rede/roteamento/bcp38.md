# BCP 38

BCP 38 descreve ingress filtering para reduzir tráfego com endereços de origem forjados saindo ou entrando por fronteiras onde essa origem é implausível.

O objetivo é combater IP source address spoofing e reduzir capacidade de reflexão/amplificação.

[uRPF](urpf.md) é uma técnica que pode participar de filtros de origem em determinadas topologias.