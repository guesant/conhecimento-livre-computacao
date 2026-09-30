# Exclusão de dados

Soft delete marca um registro como excluído sem removê-lo fisicamente. O modelo pode usar `deleted_at`, `deleted_by`, motivo e estado. Consultas públicas filtram registros ativos; consultas administrativas precisam declarar explicitamente quando incluem excluídos.

Soft delete facilita recuperação e preservação de referências, mas não é anonimização nem apagamento legal. O conteúdo continua em tabelas, índices, réplicas, backups, snapshots, caches, logs e possivelmente WAL. Toda leitura precisa aplicar o filtro correto e a retenção precisa ter uma purga controlada.

Hard delete remove fisicamente o registro lógico e as relações definidas. Ainda pode haver cópias em backups, réplicas, caches, exportações e logs. A purga deve usar transação, predicado identificável, limite operacional, contagem esperada, revisão e um plano de recuperação compatível com o risco.

`ON DELETE CASCADE` expressa integridade referencial. Ele não decide autorização, retenção, publicação ou apagamento de dados pessoais.

Não use o mesmo comando para retirar um item da publicação e apagar definitivamente. São intenções e consequências diferentes.
