# Emissão de certificados e distribuição de confiança

PKI operacional exige duas direções diferentes: entregar identidade a quem apresenta um certificado e entregar confiança a quem precisa validá-lo.

## Emissão

Uma CA assina certificados. ACME pode automatizar prova, emissão e renovação. step-ca pode operar como CA privada e oferecer ACME. cert-manager automatiza o ciclo de certificados em Kubernetes usando Issuers.

## Distribuição de confiança

O cliente precisa possuir as CAs que considera confiáveis. trust-manager pode distribuir bundles em Kubernetes. Sistemas operacionais e runtimes possuem seus próprios trust stores.

Emitir corretamente um certificado não faz um cliente confiar automaticamente na CA.

## Cenário público

Uma CA pública já está presente nos trust stores comuns. O principal problema é automatizar emissão e renovação para nomes publicamente validáveis.

## Cenário privado

Uma CA privada permite nomes e identidades internas, mas cria a responsabilidade de distribuir e rotacionar confiança. A arquitetura precisa tratar CA compromise, sobreposição durante rotação e consumidores offline.

## mTLS

No mTLS, os dois lados apresentam identidade. Isso amplia a importância de provisionamento e trust distribution, mas não substitui autorização: possuir certificado válido prova uma identidade dentro do modelo adotado, não que ela pode realizar qualquer operação.

## Anti-patterns

Não distribua a chave privada da CA para workloads. Não confunda bundle de CA com certificado de identidade. Não renove certificados automaticamente sem também monitorar falhas de renovação e expiração.

## Continue por aqui

[PKI](../../seguranca/pki/index.md), [step-ca](../../seguranca/pki/step-ca.md) e [trust-manager](../../seguranca/pki/trust-manager.md) aprofundam as peças.
