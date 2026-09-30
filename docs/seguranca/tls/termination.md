# TLS termination

TLS termination ocorre quando um intermediário encerra a sessão TLS, possui acesso ao plaintext e normalmente inicia outra conexão até o backend.

Isso permite roteamento e políticas de camada de aplicação, mas torna o terminador parte da fronteira de confiança e exige acesso às chaves/identidades apropriadas.

Veja [TLS passthrough](passthrough.md) para o modelo em que o intermediário não termina a sessão.
