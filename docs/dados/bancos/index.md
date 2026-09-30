# Bancos

Bancos persistem estado e oferecem operações para consultar, alterar, indexar e recuperar dados. A categoria deve separar o modelo do dado, o mecanismo de consistência, o formato de consulta e o produto concreto que implementa essas propriedades.

## Modelos documentados

- [Key-value](key-value.md) organiza acesso principalmente por uma chave conhecida.
- [Document databases](documentos.md) armazenam documentos estruturados e consultáveis.
- [Bancos de dados em tempo real](realtime-database.md) combinam estado persistido com listeners e sincronização.

Bancos relacionais, bancos de documentos e stores chave-valor fazem compromissos diferentes entre esquema, consulta, transação, distribuição e operação. Uma estrutura JSON conveniente para a aplicação não prova que um banco documental é a melhor escolha.

## Decisão

Defina consultas críticas, volume, padrão de escrita, concorrência, retenção, recuperação, consistência e limites de latência. Índices e particionamento precisam ser derivados de consultas reais. Replicação, cache e backup também devem ser tratados como capacidades distintas, porque uma réplica disponível não substitui uma cópia recuperável.

## Relações

[Consistência e distribuição](../consistencia/index.md) trata replicação, quorum, sharding e consenso. [Armazenamento](../armazenamento/index.md) trata caches, objetos e cópias derivadas. [Mensageria](../mensageria/index.md) trata trabalho e eventos que não pertencem ao modelo de consulta do banco.
