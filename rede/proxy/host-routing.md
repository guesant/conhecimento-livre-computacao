# Host-based routing

Host-based routing seleciona backend usando o nome solicitado pelo cliente, normalmente Host em HTTP e informação coerente com a sessão TLS.

Permite que vários serviços compartilhem endereço/porta sem exigir subpaths.

Cada nome precisa de resolução DNS e, quando TLS termina no proxy, cobertura adequada de certificado.