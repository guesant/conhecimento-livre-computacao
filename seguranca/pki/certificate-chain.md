# Cadeia de certificados

Uma cadeia de certificados liga o certificado apresentado por uma identidade a uma âncora que o verificador confia.

Cada certificado intermediário é validado usando a chave pública do emissor acima dele, até alcançar uma trust anchor.

## Falha comum

Um servidor pode possuir certificado válido e ainda falhar para clientes se não apresentar as intermediárias necessárias. O cliente também falha se a raiz apropriada não estiver em seu trust store.

## Continue por aqui

[Trust store](trust-store.md), [root CA](root-ca.md) e [intermediate CA](intermediate-ca.md) detalham as peças.