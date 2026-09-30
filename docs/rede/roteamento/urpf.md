# Unicast Reverse Path Forwarding

uRPF verifica plausibilidade do endereço de origem de um pacote consultando informação de roteamento.

Modos estritos e permissivos fazem trade-offs diferentes em redes com caminhos assimétricos.

uRPF é uma técnica de filtragem de origem; não é o mesmo problema de autorização de origem BGP resolvido por [RPKI](rpki.md).
