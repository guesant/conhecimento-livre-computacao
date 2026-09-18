# commitlint e lychee

Dois problemas de manutenção contínua, além da correção do código em si, tendem a se acumular silenciosamente num repositório: mensagens de commit inconsistentes que dificultam gerar um changelog automaticamente, e links que apontavam para uma página válida no dia em que o texto foi escrito e apontam para um 404 meses depois. Cada uma dessas ferramentas ataca um desses dois problemas de forma automatizada.

## commitlint: a convenção de commit como regra verificável, não como acordo de cavalheiros

Convenções de mensagem de commit (como o formato Conventional Commits, `tipo(escopo): descrição`) só funcionam de verdade quando são seguidas de forma consistente, porque a maior parte do valor prático delas, gerar um changelog automaticamente a partir do histórico, ou filtrar o histórico por tipo de mudança, depende de cada mensagem realmente seguir o formato. Um acordo de equipe sem verificação automatizada degrada com o tempo: alguém sob pressão de prazo escreve uma mensagem fora do padrão, ninguém percebe na revisão, e a inconsistência se acumula até o histórico deixar de ser confiável para qualquer processamento automatizado. `commitlint` verifica cada mensagem de commit contra as regras configuradas antes de aceitar o commit (tipicamente via um hook de git, ou como uma verificação de CI sobre a mensagem de um pull request), transformando a convenção de uma expectativa social numa regra que efetivamente barra uma mensagem fora do formato.

## lychee: um link é uma promessa que só se cumpre no momento da checagem

Um link para uma página externa é correto no momento em que foi escrito, mas nada garante que continua correto depois: a página pode ser removida, o domínio pode expirar, o conteúdo pode mudar de endereço sem deixar um redirecionamento. Isso é particularmente relevante para uma documentação técnica que cita fontes externas com frequência, como referências e leitura adicional; um link quebrado não avisa ninguém sozinho, alguém precisa clicar nele para descobrir que já não funciona. `lychee` varre um conjunto de arquivos (Markdown, HTML, texto simples) procurando URLs e verificando cada uma contra o destino real, reportando as que retornam erro ou deixaram de responder; rodar essa verificação periodicamente, ou a cada mudança no repositório, converte um link quebrado de "alguém vai notar um dia, talvez" em um item de ação detectado no momento em que a quebra acontece, ou logo depois.

## Continue por aqui

[Comandos de Git](../referencia/comandos-de-git.md) cobre o fluxo de commit que `commitlint` verifica. [Renovate: atualização automática de dependência](renovate-atualizacao-automatica-de-dependencia.md) cobre em profundidade a ferramenta que resolve o problema irmão destes dois, uma dependência que fica desatualizada por ninguém lembrar de checar.
