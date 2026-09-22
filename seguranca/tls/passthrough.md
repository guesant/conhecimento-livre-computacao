# TLS passthrough

TLS passthrough encaminha a conexão cifrada sem terminar TLS no intermediário.

O backend mantém a responsabilidade pela sessão e pelas chaves. O proxy perde acesso ao conteúdo L7 cifrado, embora possa usar informações disponíveis antes da cifra completa, como SNI em modelos compatíveis.

Veja [TLS termination](termination.md).