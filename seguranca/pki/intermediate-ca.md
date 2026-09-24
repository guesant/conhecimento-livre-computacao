# Intermediate CA

Uma intermediate CA possui certificado assinado por outra CA e pode assinar certificados abaixo dela conforme as restrições da cadeia.

## Por que usar

Ela separa a âncora de confiança da operação cotidiana. Uma intermediária comprometida pode ser substituída sem necessariamente trocar a root CA em todos os trust stores.

## Limite

A separação reduz exposição da raiz, mas adiciona ciclo de vida, cadeia e material criptográfico para operar.

## Continue por aqui

[Root CA](root-ca.md) é a âncora e [cadeia de certificados](certificate-chain.md) explica a validação entre elas.
