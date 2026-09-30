# Daemons

Um daemon é um processo que presta um serviço sem depender de uma janela ou de uma sessão interativa. O termo descreve um modo de execução e uma responsabilidade, não um tipo específico de arquivo.

Um daemon costuma esperar trabalho ou eventos, manter estado de runtime e responder a clientes ou ao kernel. Ele pode ser supervisionado por systemd, runit, s6 ou outro supervisor. O supervisor não muda a responsabilidade do processo, mas pode aplicar limites, credenciais, reinício e logs.

Um processo de tarefa curta também pode ser executado por uma service. Por isso, daemon e service não são sinônimos: um é um modo de execução, o outro é uma descrição de lifecycle.
