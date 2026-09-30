# Revisões editoriais

No hard edit, a identidade lógica permanece e os campos são substituídos. O estado anterior só continua disponível se houver auditoria ou outra cópia. O MVCC do banco preserva versões físicas para concorrência e recuperação, mas isso não é histórico editorial acessível à aplicação.

No versionamento editorial, a entidade permanece estável e cada mudança cria uma revisão imutável. Uma modelagem comum separa identidade, revisão, relações da revisão e auditoria. O registro pode conter `current_revision_id`, `draft_revision_id` e `published_revision_id`.

Uma publicação deve validar a revisão esperada, criar os atributos relacionados, verificar invariantes, mover o ponteiro de forma atômica e invalidar caches depois do commit. Restaurar uma revisão antiga deve criar uma nova revisão, não apagar o histórico posterior.

Revisão não é auditoria. A revisão responde qual conteúdo foi produzido. A auditoria registra ator, ação, momento, origem, autorização e resultado. Uma alteração de slug pode preservar a identidade e criar aliases para rotas antigas.

## Concorrência

Duas edições podem criar revisões simultâneas. Controle otimista com versão esperada, `updated_at` ou uma constraint impede que uma edição substitua silenciosamente a outra. O controle pessimista com `SELECT FOR UPDATE` deve proteger somente a operação curta que realmente exige exclusão mútua.

## Consultas

O caminho público deve ler o ponteiro publicado e selecionar apenas os campos necessários. Índices por entidade, estado e ordenação devem corresponder às consultas reais. Caches são invalidados quando o ponteiro publicado muda, e não apenas quando uma revisão é criada.
