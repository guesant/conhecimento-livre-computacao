# Certificate Authority

Uma Certificate Authority, CA, é uma entidade que assina certificados e permite que verificadores relacionem uma chave pública a uma identidade segundo uma política de emissão.

A confiança numa CA não nasce da assinatura sozinha. O verificador precisa possuir uma âncora de confiança apropriada e aceitar a cadeia apresentada.

## Responsabilidades

Uma CA protege sua chave de assinatura, autentica ou delega autenticação de pedidos, aplica política, emite certificados e participa do ciclo de revogação/renovação conforme o sistema.

## Continue por aqui

[Root CA](root-ca.md), [intermediate CA](intermediate-ca.md), [cadeia de certificados](certificate-chain.md) e [trust store](trust-store.md) detalham o modelo.