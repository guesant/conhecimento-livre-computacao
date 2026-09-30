# MariaDB Operator

MariaDB Operator é um operator Kubernetes para declarar e operar instâncias ou clusters MariaDB a partir de recursos customizados. Ele aplica o padrão de controller para transformar uma descrição declarativa em pods, serviços, configuração, credenciais e operações específicas do banco.

## Fronteira

O operator conhece o ciclo de vida do MariaDB e os recursos que a implementação suporta, mas não conhece o modelo de negócio da aplicação. Schema, migrações, índices, usuários necessários e desenho das consultas continuam pertencendo ao consumidor do banco.

## Quando faz sentido

O recurso é adequado quando o banco precisa seguir o ciclo de vida do cluster, ser provisionado por GitOps e compartilhar mecanismos Kubernetes de configuração, secret e armazenamento. A decisão exige verificar a versão do operator, a maturidade dos recursos de backup e recuperação, os modos de replicação e a compatibilidade com a topologia desejada.

## Limitações

Um operator não elimina os failure domains do cluster nem transforma PVC local em armazenamento resiliente. Recursos como replicação, Galera, backups e restauração devem ser avaliados conforme a versão instalada, porque suporte declarado pelo projeto não equivale a uma política de recuperação testada no ambiente.

## Relações

- [Operators](../../kubernetes-operators.md) explica a reconciliação de recursos customizados.
- [CloudNativePG](cloudnative-pg.md) ocupa uma fronteira equivalente para PostgreSQL.
- [PersistentVolume](../storage/persistent-volume.md) descreve a dependência de armazenamento persistente.

## Fonte primária

- [MariaDB Operator](https://github.com/mariadb-operator/mariadb-operator)
