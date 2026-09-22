# Root CA

Uma root CA é uma autoridade cujo certificado funciona como âncora de confiança. Ele é tipicamente autoassinado porque não existe uma autoridade superior na cadeia local que o assine.

## Impacto

Comprometer a chave da raiz pode exigir substituir a âncora distribuída a todos os consumidores. Por isso ambientes de maior impacto frequentemente mantêm a raiz offline e delegam emissão cotidiana a intermediárias.

## Continue por aqui

[Intermediate CA](intermediate-ca.md) explica a delegação. [Trust store](trust-store.md) explica onde a raiz é confiada.