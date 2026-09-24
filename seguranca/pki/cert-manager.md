# cert-manager

cert-manager automatiza emissão, renovação e distribuição de certificados no
Kubernetes. Ele observa recursos declarativos e conversa com uma autoridade
como ACME público, uma CA interna ou um issuer específico.

## Recursos

Issuer e ClusterIssuer descrevem a autoridade disponível. Certificate declara
a identidade desejada. O controller produz Secret com certificado, chave e
cadeia conforme a configuração. O escopo do issuer define se a autoridade
pode ser usada apenas por um Namespace ou pelo cluster.

O Secret é um artefato de saída e precisa de controle de acesso, retenção e
distribuição compatíveis com a sensibilidade da chave privada.

## Failure modes

Uma renovação pode falhar por desafio ACME, DNS, conectividade, política da
CA, nome fora do SAN ou Secret inacessível. Observe eventos dos recursos,
status do CertificateRequest e logs do controller antes de apagar e recriar
objetos.

## Relações

- [ACME](acme.md) automatiza provas de controle.
- [Certificate](certificate.md) descreve o artefato emitido.
- [Trust manager](trust-manager.md) distribui CAs confiáveis.
- [Ingress](../../kubernetes/networking/ingress.md) pode consumir certificados.

## Fonte primária

- [cert-manager](https://cert-manager.io/docs/)
