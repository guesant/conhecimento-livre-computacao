# Rate limiting

Rate limiting limita consumo de uma operação por janela, identidade, origem,
rota ou recurso. Ele protege capacidade e pode representar uma quota contratual,
mas não substitui autenticação, autorização ou controle de concorrência.

## Dimensões

Defina quem é limitado, qual operação conta, qual resposta é produzida e qual
estado precisa ser compartilhado entre réplicas. Limitar por IP pode agrupar
clientes legítimos atrás de NAT; limitar por consumer exige identidade confiável.

## Estado

Estado local é rápido e não depende de rede, mas conta por réplica. Estado
compartilhado representa o total agregado, ao custo de latência, disponibilidade
e uma dependência adicional.

## Algoritmos

- [Fixed window](fixed-window.md) é simples e pode permitir rajadas na borda.
- [Sliding window](sliding-window.md) suaviza a borda com mais estado.
- [Token bucket](token-bucket.md) controla taxa e permite burst configurado.
- [Leaky bucket](leaky-bucket.md) drena em ritmo constante.

## Relações

- [API gateway](../api-gateway/index.md) aplica limite na borda.
- [Rate limiting local e compartilhado](../../rate-limiting-politica-local-e-compartilhada.md)
  compara o estado.
- [Filas](../../dados/mensageria/filas.md) podem absorver trabalho em vez de
  rejeitar tudo.

## Fonte primária

- [IETF HTTP 429](https://www.rfc-editor.org/rfc/rfc6585)
