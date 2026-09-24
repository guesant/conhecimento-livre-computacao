# Mapa de compatibilidade: mensageria

Esta página foi descompactada porque fila e event stream possuem modelos de consumo e retenção diferentes.

- [Filas](dados/mensageria/filas.md) são adequadas para distribuir mensagens ou trabalho entre consumidores.
- [Event streaming](dados/mensageria/event-streaming.md) preserva um log que consumidores podem ler e reler mantendo posições próprias.

Produtos concretos podem oferecer características de ambos, mas isso não elimina a diferença conceitual.
