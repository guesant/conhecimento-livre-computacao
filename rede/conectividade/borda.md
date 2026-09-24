# Borda de rede

A borda é a região em que uma rede encontra outra rede, usuários externos ou provedores. Gateways, firewalls, reverse proxies, load balancers e túneis podem existir ali, mas cada um implementa responsabilidades diferentes.

## Casos de uso

Na borda é comum terminar TLS, aplicar políticas de entrada, encaminhar tráfego para serviços internos, limitar exposição e observar tentativas externas.

## Boa prática

Mantenha explícita a cadeia de confiança: quem aceita a conexão, onde TLS termina, qual identidade chega ao backend e quais componentes podem alterar headers ou origem percebida.

## Má prática

Empilhar proxy, túnel, gateway e ingress sem registrar responsabilidade de cada camada produz falhas difíceis de diagnosticar e políticas duplicadas ou contraditórias.

## Continue por aqui

[Reverse proxy e split-horizon DNS](../../reverse-proxy-e-split-horizon-dns.md) mostra duas peças que frequentemente aparecem próximas da borda.
