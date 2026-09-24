# NetworkPolicy

NetworkPolicy expressa regras de tráfego permitido entre Pods, Namespaces e
fontes externas conforme o suporte do plugin de rede. Ela pode selecionar
destinos e fontes por labels, Namespace selectors, CIDRs e portas.

## Modelo de isolamento

A presença de uma policy pode tornar um Pod isolado para uma direção específica.
Uma policy de ingress controla tráfego entrando; uma policy de egress controla
tráfego saindo. Regras permitidas são combinadas de forma aditiva entre
policies aplicáveis. Uma policy não cria uma regra de deny universal que todos
os plugins interpretam do mesmo modo se a seleção ou direção estiver errada.

NetworkPolicy não é firewall de host, não inspeciona conteúdo de aplicação e
não substitui autenticação. O plugin de rede precisa implementar a API, e o
comportamento de protocolos, DNS, hostNetwork e tráfego para fora do cluster
precisa ser testado no ambiente real.

## Diagnóstico

Ao bloquear tráfego, verifique labels reais, Namespace, portas, direção,
EndpointSlice, resolução DNS e enforcement do CNI. Uma policy correta no YAML
mas não suportada pelo CNI produz uma falsa sensação de isolamento.

## Relações

- [CNI](cni.md) implementa a conectividade e pode aplicar policies.
- [Service](../core/service.md) oferece descoberta, mas não autoriza tráfego.
- [RBAC](../access/rbac.md) protege a API, não pacotes de rede.

## Fonte primária

- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
