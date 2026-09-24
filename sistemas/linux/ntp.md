# NTP e sincronização de tempo

NTP, Network Time Protocol, sincroniza relógios de hosts usando uma hierarquia de fontes de tempo. Um cliente mede diferenças e atrasos em relação a servidores e ajusta o relógio de forma controlada. O protocolo não é um mecanismo de autenticação de usuários, embora o estado do relógio seja uma dependência de outros protocolos de segurança.

## Hierarquia e operação

Fontes NTP são organizadas por estrato e qualidade de referência. Um host pode consultar várias fontes, comparar medições e rejeitar uma fonte que diverge. Servir tempo para uma rede interna exige limitar clientes autorizados e escolher fontes upstream confiáveis.

No Linux, `chronyd` é uma implementação comum de cliente e servidor NTP. Ele mantém estimativas do relógio, pode corrigir grandes diferenças durante a inicialização e oferece `chronyc` para inspeção. O serviço escolhido, seja chrony, systemd-timesyncd ou outro, deve ser único por host para evitar ajustes concorrentes.

## Relação com Kerberos

Tickets Kerberos possuem período de validade e os participantes rejeitam mensagens fora da tolerância de diferença de relógio. A sincronização deve ser tratada como dependência da autenticação, não como um detalhe cosmético de observabilidade.

Uma hierarquia de identidade pode usar servidores NTP internos para reduzir dependência externa. Esses servidores precisam ter suas próprias fontes confiáveis e uma política clara para o caso de perderem sincronização.

## Segurança e diagnóstico

Não aceite clientes arbitrários em um servidor NTP interno ou público. Use fontes suficientes para detectar divergência, monitore estado de sincronização e investigue saltos de relógio antes de renovar credenciais ou alterar políticas Kerberos.

Um relógio incorreto também pode quebrar TLS, validação de certificados, logs e jobs agendados. O diagnóstico deve separar hora local, timezone, sincronização NTP, fonte escolhida e horário observado pelo serviço remoto.

## Relações

- [MIT Kerberos](../../seguranca/identidade/kerberos.md) explica por que a diferença de relógio afeta tickets.
- [FreeIPA](../../seguranca/identidade/freeipa.md) trata tempo como dependência da composição de identidade.
- [BIND](../../rede/dns/bind.md) cobre outra dependência de descoberta de serviços.

## Fontes primárias

- [chrony, documentação](https://chrony-project.org/documentation.html)
- [RFC 5905, Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905)
