# Padrões defensivos de script operacional

Um script que executa comandos administrativos contra um host ou um cluster real carrega um risco que um script de desenvolvimento comum não carrega: um erro no meio da execução pode deixar o sistema num estado pior do que antes de começar, sem um "desfazer" automático disponível. Um conjunto pequeno de padrões, reunidos numa biblioteca de funções compartilhadas entre scripts em vez de reescritos a cada novo script, cobre a maior parte do risco previsível desse tipo de execução.

## Verificar a pré-condição antes de agir, não depois de falhar

Duas verificações de pré-condição resolvem a classe de erro mais barata de evitar: confirmar que um comando necessário existe no `PATH` antes de tentar usá-lo, e confirmar que uma variável obrigatória foi de fato definida (não vazia) antes de montar um comando com ela. Sem essa verificação, o erro real só aparece no meio da execução, na forma de um comando não encontrado ou de um valor vazio silenciosamente interpolado numa string, um sintoma mais difícil de diagnosticar do que uma mensagem explícita logo no início dizendo exatamente o que falta. O mesmo raciocínio se estende a uma verificação de ambiente mais ampla, como confirmar que o script roda sobre a distribuição Linux para a qual foi escrito antes de executar qualquer comando específico dela, evitando que uma suposição implícita sobre o ambiente vire uma falha confusa a meio caminho.

## Download com verificação de checksum, sempre

Baixar um binário ou um instalador de uma URL externa e executá-lo sem verificar sua integridade (o problema já descrito em [Pinagem por digest e hash em cada ecossistema](pinagem-por-digest-e-hash.md)) é uma prática comum, mas evitável a baixo custo: uma função de download reutilizável que já embute a verificação de checksum contra um valor esperado, recusando prosseguir se não bater, transforma essa proteção em um hábito automático em vez de um passo que depende de alguém lembrar de adicionar manualmente a cada novo script.

## Confirmação explícita antes de uma ação destrutiva

Uma ação irreversível ou de alto impacto (apagar um recurso, sobrescrever uma configuração, remover um nó do cluster) executada dentro de um script automatizado tira do operador o momento de pausa que normalmente existiria ao digitar o comando manualmente e ler o que está prestes a rodar. Um portão de confirmação explícito, que exige digitar uma palavra específica (não apenas "s/n", fácil de pressionar por reflexo) antes de prosseguir com a parte destrutiva do script, reintroduz esse momento de pausa deliberada, sem eliminar a conveniência de automatizar o resto do processo. O detalhe que faz esse portão funcionar de verdade é a mensagem que o acompanha: nomear explicitamente qual ação vai acontecer e sobre qual alvo, não um aviso genérico de "isto é perigoso", para que a pessoa confirmando saiba exatamente o que está prestes a autorizar.

## Esperar uma condição em vez de um tempo fixo

Um `sleep` de duração fixa depois de disparar uma operação assíncrona (reiniciar um serviço, aguardar um Pod ficar pronto) é uma aposta: tempo demais desperdiça execução à toa, tempo de menos segue em frente antes da condição real estar satisfeita, produzindo uma falha na etapa seguinte que na verdade é sintoma de pressa, não de um problema real. Uma função de espera que repete uma verificação de condição em intervalos curtos até ela ser satisfeita, ou até estourar um teto máximo de tempo (retornando erro explícito nesse caso, em vez de simplesmente prosseguir como se a condição tivesse sido atendida), resolve esse problema de forma mais robusta que uma pausa às cegas, adaptando o tempo de espera real à velocidade real da operação em vez de a uma estimativa fixa escrita antecipadamente.

## Limpeza garantida mesmo em caminho de erro

Um script que cria um diretório temporário, ou qualquer outro recurso que precisa ser removido ao final, corre o risco de deixar esse recurso para trás se o script terminar de forma inesperada no meio do caminho, por um erro não tratado ou por interrupção manual. Registrar a limpeza como uma ação disparada pela saída do processo (um `trap` associado ao sinal de saída, no caso de um script shell), em vez de como o último comando na sequência normal esperada, garante que a limpeza aconteça mesmo quando o script não chega até aquele ponto final por um caminho feliz, incluindo o caso de alguém interromper a execução manualmente no meio.

## O padrão só protege quando é usado

Nenhum desses padrões resolve nada sozinho como biblioteca; eles só protegem o script que de fato os invoca em vez de reimplementar (ou pior, omitir) a mesma verificação de forma inconsistente a cada novo script. Uma biblioteca de funções defensivas que existe no repositório mas não é chamada pelos scripts reais é, na prática, documentação de uma boa intenção, não uma proteção efetiva; o valor só se realiza quando todo script novo é escrito reutilizando essas funções já testadas, em vez de reescrever a mesma lógica de verificação (ou esquecer de escrevê-la) cada vez.

## Continue por aqui

[Smoke test e o limite da automação de checklist](smoke-test-e-o-limite-da-automacao-de-checklist.md) cobre saída estruturada e o que vale ou não a pena automatizar, um princípio complementar a este. [Shells e scripts](shells-e-scripts.md) cobre `set -euo pipefail` e as demais opções de shell que tornam um script mais seguro por padrão, antes mesmo de qualquer função defensiva adicional.
