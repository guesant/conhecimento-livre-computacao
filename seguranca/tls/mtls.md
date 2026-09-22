# Mutual TLS

Mutual TLS, mTLS, usa autenticação por certificado nos dois lados da conexão.

No TLS de servidor comum, o cliente valida a identidade do servidor. Em mTLS, o servidor também solicita e valida certificado do cliente.

mTLS autentica identidade criptográfica; autorização continua sendo uma decisão separada. Um certificado válido não concede automaticamente permissão para qualquer operação.