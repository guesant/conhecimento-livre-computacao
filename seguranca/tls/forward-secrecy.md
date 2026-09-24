# Forward secrecy

Forward secrecy é a propriedade pela qual comprometer uma chave de longo prazo no futuro não permite recuperar chaves de sessão passadas a partir de tráfego previamente capturado.

Ela depende do mecanismo de estabelecimento de chaves, não apenas de "usar criptografia".

[TLS 1.3](tls13.md) foi desenhado para usar key exchange com essa propriedade.
