# Condição de corrida

Condição de corrida ocorre quando o resultado depende da ordem relativa de atividades
concorrentes e essa ordem não é controlada pelo protocolo. O código pode funcionar em
testes e falhar sob carga porque outra thread, processo, requisição ou worker altera o
estado entre a leitura e a escrita.

O problema é uma propriedade da interação entre operações, não da velocidade absoluta.
Mesmo dois comandos muito rápidos podem correr entre si. Também pode existir condição de
corrida sem threads: duas requisições concorrentes em um servidor, dois pods, dois
workers de fila ou dois administradores podem produzir a mesma interleaving.

## Exemplo de check-then-act

Este padrão não protege a unicidade:

```text
if recurso ainda não existe:
    criar recurso
```

Duas atividades podem observar a ausência antes de qualquer uma criar. O resultado pode
ser duplicado, uma exceção inesperada ou uma atualização perdida.

As correções dependem do dono da invariável:

- `UNIQUE` ou outra constraint no banco quando a propriedade é persistida;
- `INSERT ... ON CONFLICT` ou operação atômica equivalente;
- lock de linha ou transação quando a decisão depende de estado existente;
- mutex distribuído quando a operação atravessa um recurso que não oferece atomicidade;
- fila particionada por chave quando a ordem por recurso é suficiente;
- controle otimista com versão esperada e retry quando conflitos são raros.

Um `SELECT` anterior à escrita pode ser útil para uma mensagem amigável, mas não deve ser
a única proteção. A verificação e a mudança precisam compartilhar a garantia correta.

## Formas comuns

### Atualização perdida

Dois leitores carregam o mesmo valor, calculam resultados diferentes e o último `UPDATE`
substitui o trabalho do primeiro. Use `UPDATE ... WHERE version = ...`, lock de linha,
operação atômica ou uma política explícita de merge.

### Dupla execução

Dois workers obtêm o mesmo job, enviam o mesmo email ou aplicam a mesma cobrança. Use
lease com expiração, claim atômico, chave de idempotência e confirmação somente depois do
efeito necessário.

### Confusão entre cache e origem

Uma instância grava um valor antigo depois que outra gravou o novo. Versione a chave,
compare a versão antes de publicar e defina invalidação. TTL reduz a duração do erro, mas
não garante a ordem das escritas.

### Checkpoint de progresso incorreto

Um processo registra progresso antes de persistir o efeito e cai. Outro processo pula o
trabalho. Se registra depois, pode repetir o efeito. O protocolo precisa de idempotência,
outbox, transação local ou uma marca que represente o efeito real.

## Concorrência otimista e pessimista

Controle otimista permite que várias atividades prossigam e detecta conflito no momento
da escrita. É adequado quando conflitos são raros e a operação pode ser repetida.

Controle pessimista reserva o recurso antes de trabalhar. Pode reduzir conflitos, mas
aumenta espera, risco de deadlock e custo de recuperação de locks abandonados. Não mantenha
o lock durante chamadas externas ou interação humana.

## Teste

Teste interleavings, não apenas chamadas isoladas. Use barreiras para pausar duas
atividades entre a leitura e a escrita, injete atrasos, execute com mais de um worker e
verifique a invariável depois de cada rodada. Testes de carga que nunca forçam a janela
crítica podem não revelar o defeito.

## Relações

- [Mutex](mutex.md) protege uma seção crítica local.
- [Semáforos](semaforos.md) coordenam capacidade e sinalização.
- [Deadlock](deadlock.md) é um tipo diferente de falha de coordenação.
- [Idempotência](../../confiabilidade/idempotencia.md) permite retry sem duplicar efeitos.
- [Outbox](../../dados/mensageria/outbox.md) protege a publicação após uma alteração local.

## Fontes

- [PostgreSQL, explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [PostgreSQL, transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
