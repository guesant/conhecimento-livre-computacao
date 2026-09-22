# Dados, mensageria e armazenamento

Esta área separa modelos de dados, bancos, filas, streams e armazenamento persistente. Produtos concretos devem ser entendidos como implementações desses modelos, não como a definição da categoria.

## Bancos não relacionais

[Key-value](bancos/key-value.md) modela acesso principalmente por chave. [Document databases](bancos/documentos.md) armazenam documentos estruturados e permitem consultas sobre sua estrutura.

## Mensageria

[Filas](mensageria/filas.md) distribuem unidades de trabalho ou mensagens entre produtores e consumidores. [Event streaming](mensageria/event-streaming.md) mantém um log ordenado de eventos que pode ser lido por consumidores com posições próprias.

## Armazenamento Kubernetes

O modelo de PV/PVC, storage classes e soluções locais ou distribuídas permanece na área de plataforma Kubernetes, porque ali a pergunta principal é integração com workloads do cluster.