# Ingress e Gateway API

Ingress e Gateway API publicam tráfego HTTP e HTTPS para Services, mas
organizam responsabilidades de forma diferente. A comparação não é apenas
entre dois `kind`: envolve ownership, expressividade, suporte do controlador e
forma de evolução da configuração.

## Responsabilidade e recursos

| Dimensão | Ingress | Gateway API |
| --- | --- | --- |
| Recurso principal | `Ingress` combina regras de entrada e extensões | `GatewayClass`, `Gateway` e `HTTPRoute` separam plataforma e aplicação |
| Ownership | frequentemente concentrado no objeto compartilhado | listeners ficam com a plataforma e rotas podem ficar com a aplicação |
| Extensões | dependem bastante de annotations do controller | possui tipos e relações padronizados, com extensões explícitas |
| Caso comum | roteamento HTTP simples | múltiplos listeners, namespaces e políticas de associação |
| Migração | ampla disponibilidade em controllers existentes | exige controller compatível e revisão do modelo de ownership |

Ingress continua adequado quando o ambiente precisa de poucas regras HTTP e o
controller já fornece as capacidades necessárias. Gateway API é mais adequada
quando a equipe precisa separar a administração do ponto de entrada da
publicação de rotas por cada aplicação.

## TLS e backends

Ambos os modelos podem terminar TLS no ponto de entrada e encaminhar para um
Service. A existência de um recurso não garante que o tráfego esteja
publicado: um controller compatível precisa observar a configuração e possuir
acesso aos Secrets e endpoints necessários.

No Ingress, detalhes do controller frequentemente aparecem como annotations.
Na Gateway API, `Gateway` declara listeners e `HTTPRoute` declara o
encaminhamento, mas recursos proprietários continuam existindo para capacidades
que a especificação não padroniza.

## Critério de escolha

Prefira Ingress quando simplicidade, compatibilidade e uma única equipe
administrando as regras forem mais importantes que a separação de papéis.
Prefira Gateway API quando a plataforma precisa oferecer um gateway comum sem
entregar a cada aplicação a posse dos listeners, certificados ou portas.

## Relações

- [Ingress](../../kubernetes/networking/ingress.md) explica o modelo clássico.
- [Gateway API](../../gateway-api.md) apresenta o modelo decomposto.
- [HTTPRoute](../../rede/gateway-api/http-route.md) é a unidade de rota da
  Gateway API.

## Fontes primárias

- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Gateway API](https://gateway-api.sigs.k8s.io/)
