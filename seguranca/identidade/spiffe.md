# SPIFFE

SPIFFE, Secure Production Identity Framework for Everyone, é uma especificação
para identificar workloads por uma identidade verificável, normalmente expressa
como um SPIFFE ID no formato URI. O modelo separa a identidade do workload de
seu endereço IP, namespace, Pod, máquina ou localização física.

## Identidade de workload

Uma identidade pode ser `spiffe://example.org/ns/payments/sa/api`. O trust domain
define a autoridade que emite a identidade; o restante do caminho representa a
identidade segundo a política da implantação. O valor só tem significado para
quem confia na autoridade emissora e no processo que associou o workload ao ID.

O workload não precisa receber uma chave privada por Secret manual. Um agente
SPIFFE local pode entregar um SVID, normalmente um certificado X.509 ou um JWT,
por uma API de workload. O agente atesta o processo usando informações da
plataforma, e o workload prova a identidade a outro serviço por TLS ou token.

## Componentes

O modelo define três responsabilidades principais:

- Workload API entrega SVIDs e bundles ao workload autorizado.
- SPIFFE Workload Endpoint permite que o workload obtenha material sem conhecer
  a autoridade de emissão.
- SPIRE é uma implementação que registra workloads, realiza attestation e opera
  a autoridade de identidade.

SPIFFE não é um service mesh, um proxy ou um diretório de usuários. Pode ser
usado por um mesh, mas também por aplicações que implementam TLS diretamente.
O ID responde quem é o workload; autorização continua sendo uma decisão do
serviço receptor sobre esse ID, método, recurso e contexto.

## Trust domains e federação

Ambientes separados devem possuir trust domains ou políticas de confiança
explicitamente relacionadas. Aceitar qualquer SPIFFE ID de outro domínio é tão
amplo quanto confiar em qualquer CA. Federação deve definir quais bundles são
aceitos, quais IDs podem atravessar a fronteira e como revogar ou expirar uma
relação.

## Rotação e falhas

SVIDs devem possuir vida curta e rotação automática. O serviço precisa aceitar
overlap durante a renovação, validar cadeia, SAN, validade e política de trust
domain. Falha do agente, atraso na rotação, clock incorreto ou associação errada
entre workload e ID devem ser observáveis. Não grave certificados privados em
logs para investigar uma falha.

## Relações

- [mTLS](../tls/mtls.md) transporta a identidade de certificado.
- [PKI](../pki/index.md) explica autoridades, cadeias e trust stores.
- [Service mesh](../../rede/service-mesh/index.md) pode consumir identidades de workload.

## Fontes primárias

- [SPIFFE specification](https://spiffe.io/docs/latest/spiffe-about/overview/)
- [SPIFFE Workload API](https://github.com/spiffe/spiffe-workload-api)
- [SPIRE](https://spiffe.io/docs/latest/spire-about/overview/)
