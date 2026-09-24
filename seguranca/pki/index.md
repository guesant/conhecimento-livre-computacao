# PKI e confiança

Public Key Infrastructure organiza identidades criptográficas, autoridades certificadoras, certificados, validação e ciclo de vida de confiança.

## Conceitos

TLS usa certificados e chaves para autenticação e proteção de transporte. mTLS autentica ambos os lados. ACME automatiza emissão e renovação. Uma CA privada permite emitir identidades dentro de um domínio de confiança controlado pela organização.

## Implementações

[step-ca](step-ca.md) implementa uma CA privada e protocolos de provisionamento. [trust-manager](trust-manager.md) distribui bundles de confiança em Kubernetes. cert-manager automatiza ciclo de vida de certificados e pode integrar emissores públicos ou privados. [Dogtag](dogtag.md) fornece uma CA completa com perfis, revogação e integração com FreeIPA.

## Continue por aqui

[TLS, mTLS e confiança de rede](../../tls-mtls-e-confianca-de-rede.md) explica o protocolo e o modelo de confiança. [TLS automático](../../tls-automatico.md) explica automação de emissão.
