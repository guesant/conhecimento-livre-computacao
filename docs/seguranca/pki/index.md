# PKI

Public Key Infrastructure organiza identidades criptográficas, autoridades certificadoras, certificados, validação e ciclo de vida de confiança.

## Conceitos

TLS usa certificados e chaves para autenticação e proteção de transporte. mTLS autentica ambos os lados. ACME automatiza emissão e renovação. Uma CA privada permite emitir identidades dentro de um domínio de confiança controlado pela organização.

A PKI não é somente o par certificado e chave. Ela inclui uma política de
identidade, uma ou mais autoridades, perfis de emissão, distribuição de trust
stores, validação de caminho, revogação, rotação, auditoria e recuperação. Uma
CA que emite certificados corretamente, mas não consegue retirar uma identidade
comprometida, não fornece o lifecycle completo que o serviço precisa.

Separe três perguntas durante o desenho:

1. quem pode emitir e para qual finalidade;
2. como o consumidor encontra e valida a cadeia;
3. como uma identidade deixa de ser aceita antes de expirar.

O certificado X.509 carrega nomes, usos, emissor e validade, mas a autorização
da aplicação continua sendo uma decisão própria. A existência de um certificado
válido não deve conceder acesso universal.

## Implementações

[step-ca](step-ca.md) implementa uma CA privada e protocolos de provisionamento. [trust-manager](trust-manager.md) distribui bundles de confiança em Kubernetes. cert-manager automatiza ciclo de vida de certificados e pode integrar emissores públicos ou privados. [Dogtag](dogtag.md) fornece uma CA completa com perfis, revogação e integração com FreeIPA. [OpenSSL para PKI](openssl.md) mostra o fluxo manual de geração, emissão, verificação e CRL.

## Continue por aqui

[TLS](../tls/index.md), [mTLS](../tls/mtls.md) e confiança de rede explicam o protocolo e o modelo de confiança. [TLS automático](../../tls-automatico.md) explica automação de emissão.

## Fluxo de lifecycle

Uma identidade normalmente atravessa as seguintes etapas:

1. definir a política e o perfil de emissão;
2. gerar a chave no local que deve protegê-la;
3. criar e validar uma CSR;
4. assinar com a CA intermediária correta;
5. distribuir folha, cadeia e trust store ao consumidor;
6. monitorar validade, uso, falhas e revogação;
7. renovar com sobreposição e retirar o material antigo;
8. registrar a revogação e confirmar seu efeito em cada consumidor.

O ponto de emissão não deve receber uma chave privada que poderia ser gerada no
próprio consumidor. Para workloads modernos, a identidade também pode ser
provisionada por uma autoridade de workload, por ACME ou por um mecanismo de
atestado. A escolha depende de quem controla o consumidor, de quanto tempo a
credencial precisa durar e de qual é o caminho de recuperação.
