# Hangfire

Hangfire é uma biblioteca .NET para executar métodos como jobs em background. O cliente
cria o job, um storage persistente guarda sua definição e um servidor Hangfire consulta o
storage e executa o trabalho. O servidor pode estar no mesmo processo ASP.NET, em um
worker separado, em um serviço Windows ou em uma aplicação de console.

A persistência diferencia Hangfire de simplesmente colocar uma tarefa no Thread Pool. O
job pode sobreviver à reinicialização do processo quando o provider de storage oferece as
garantias necessárias. Ainda assim, a execução deve ser tratada como pelo menos uma vez:
uma falha durante ou depois de um efeito externo pode levar a uma nova tentativa.

## Componentes

### Cliente

O cliente serializa a invocação, seus argumentos e metadados e grava o job no storage.
O retorno para o chamador acontece depois que a criação foi persistida, não depois que o
trabalho terminou.

Não coloque segredos, objetos enormes ou entidades ORM inteiras nos argumentos. Prefira um
identificador estável e faça o worker carregar os dados necessários no momento da
execução. Isso reduz o tamanho da fila e evita que uma versão antiga do objeto determine
o comportamento do job.

### Storage

O storage guarda jobs, estados, filas, agendamentos e informações de processamento. O
provider escolhido precisa ser avaliado por durabilidade, locks, latência, limpeza,
backup e comportamento quando há vários servidores.

Uma fila persistente não elimina a necessidade de backup. Perder o storage pode significar
perder trabalho que ainda não foi executado, mesmo que o código da aplicação esteja
disponível para ser reconstruído.

### Servidor

O Hangfire Server possui workers e componentes para jobs enfileirados, jobs atrasados,
jobs recorrentes e expiração de estados. Um servidor precisa ser encerrado de forma
graciosa para permitir que o processamento em andamento seja concluído ou devolvido para
a fila conforme as garantias do storage.

Em um ambiente com vários processos, dimensione workers, filas e conexões ao storage.
Mais workers aumentam concorrência, mas também podem sobrecarregar o banco, a API externa
ou o próprio host.

### Dashboard

O dashboard permite consultar estados e falhas dos jobs. Ele deve ser protegido com
autenticação e autorização adequadas. Não exponha uma interface administrativa apenas
porque a aplicação pública já possui um endpoint HTTP.

## Tipos de job

### Fire-and-forget

Executa uma operação assim que houver um worker disponível. É útil para retirar trabalho
do ciclo da requisição, como enviar uma notificação ou recalcular uma projeção.

O chamador não deve prometer que o efeito já ocorreu. A resposta deve comunicar que o
trabalho foi aceito, quando essa é a semântica real.

### Atrasado

Faz o job ser disponibilizado depois de um intervalo. É útil para lembretes, expiração
de tentativas e reprocessamentos deliberados. O atraso não é um mecanismo de precisão em
tempo real; considere o polling, a carga e o agendamento do servidor.

### Recorrente

Um job recorrente possui um identificador e uma expressão de agenda. O scheduler verifica
as agendas e enfileira as ocorrências. O servidor precisa permanecer ativo para executar
essa função. A definição da agenda deve ser idempotente, para que o deploy não crie jobs
duplicados.

### Continuação

Uma continuação inicia depois de outro job atingir um estado compatível. Use-a quando a
dependência entre as etapas fizer parte do fluxo. Se o segundo job puder ser processado
independentemente, uma fila separada pode ser mais simples.

## Retry e idempotência

Hangfire pode reprocessar jobs interrompidos ou falhos conforme sua configuração e o
provider utilizado. Isso é útil para falhas transitórias, mas perigoso para operações
externas não idempotentes.

Um job deve identificar a operação e verificar se ela já foi concluída antes de aplicar
novamente um efeito. Exemplos são uma chave de deduplicação em uma tabela, um idempotency
key enviado ao provedor externo ou uma transação que registra o resultado e a intenção.

Não transforme toda exceção em retry. Erros de validação, autorização, schema ou dados
inexistentes podem permanecer falhos até que alguém corrija a causa. Repetir rapidamente
um job impossível aumenta carga e atrasa trabalhos saudáveis.

## Hangfire em ASP.NET e workers

Executar o servidor junto da aplicação web é conveniente, mas mistura tráfego HTTP com
trabalho de background. O processo precisa estar sempre ativo, ter recursos suficientes
e possuir uma política de encerramento compatível com deploy e autoscaling.

Um worker separado costuma facilitar limites de CPU, memória, conexões e escala. Porém,
ele adiciona um processo que precisa de configuração, logs, health checks e deploy. A
decisão deve considerar o volume e a criticidade dos jobs, não apenas a quantidade de
projetos na solução.

Em Kubernetes, não confunda réplicas de um worker com um scheduler independente. Garanta
que todos os workers compartilhem um storage suportado e que os locks do provider tenham
semântica correta. Não use o filesystem efêmero do pod como a fila principal.

## Com Hangfire e Polly

Polly deve envolver a operação transitória dentro do job. Hangfire deve controlar o
destino do job e a política de reprocessamento do trabalho completo.

Uma composição coerente pode ser:

1. Hangfire recebe um job com um identificador de operação.
2. O handler verifica se o efeito já foi aplicado.
3. Polly aplica timeout e poucas tentativas para a chamada externa.
4. O handler persiste o resultado ou a falha classificável.
5. Uma exceção transitória não resolvida permite que Hangfire reprograme o job.

Evite multiplicar tentativas sem calcular o limite real. Se Polly executar quatro
tentativas e Hangfire repetir o job cinco vezes, o sistema externo pode receber até vinte
chamadas, além de possíveis execuções concorrentes.

## Observabilidade

Monitore quantidade e idade dos jobs, tamanho das filas, duração, taxa de falha, retries,
jobs recorrentes atrasados, expiração e tempo de espera no storage. Registre o
identificador da operação, o job id, a fila, a tentativa e a causa classificada.

Quando o job chama um sistema externo, diferencie tempo em fila, tempo de execução local,
tempo de espera da rede e tempo de processamento remoto. Sem essa separação, um dashboard
pode apontar Hangfire como lento quando o gargalo está na dependência externa.

## Fontes

- [Hangfire, documentação](https://docs.hangfire.io/en/latest/)
- [Hangfire, processamento de jobs](https://docs.hangfire.io/en/latest/background-processing/processing-background-jobs)
- [Hangfire, métodos recorrentes](https://docs.hangfire.io/en/latest/background-methods/performing-recurrent-tasks.html)
- [Hangfire, métodos em background](https://docs.hangfire.io/en/latest/background-methods/calling-methods-in-background.html)
