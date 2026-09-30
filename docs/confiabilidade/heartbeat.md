# Heartbeat

Heartbeat é um sinal periódico que indica que um processo, conexão, sessão, réplica ou
lease ainda está ativo. O receptor considera o participante saudável enquanto recebe
sinais dentro de uma janela definida ou enquanto consegue renovar uma autoridade.

Heartbeat não prova que o trabalho está correto. Um processo pode responder ao sinal e
estar travado em uma fila, sem conseguir persistir dados ou incapaz de atender usuários.
Ele é uma evidência parcial de vivacidade e deve ser combinado com métricas de progresso,
readiness, lag ou confirmação do efeito esperado.

## Intervalo e janela de falha

Um protocolo precisa definir:

- intervalo entre sinais;
- timeout do receptor;
- quantidade de sinais perdidos tolerada;
- jitter e comportamento em reconexão;
- identidade e versão do remetente;
- ação após expiração;
- forma de impedir que o remetente antigo continue exercendo autoridade.

Um heartbeat a cada 10 segundos com timeout de 30 segundos não detecta falha em 10
segundos. Ele detecta ausência depois de uma combinação de atraso, perda, processamento e
agendamento. A janela deve ser compatível com latência e com o custo de um falso positivo.

## Heartbeat e lease

Um lease concede uma autoridade até determinado vencimento. O heartbeat pode renovar o
lease, mas os dois conceitos não são iguais. O sinal indica atividade; o lease é uma
decisão de autorização temporal.

Quando o lease expira, o antigo dono deve parar e o recurso protegido deve rejeitar sua
escrita. Use fencing token ou número de geração monotônico. Apenas comparar timestamps
pode falhar com clock skew e mensagens atrasadas.

## Heartbeat e readiness

Liveness pergunta se reiniciar o processo pode ser necessário. Readiness pergunta se o
processo deve receber tráfego. Heartbeat de um processo pode alimentar observabilidade,
mas não deve ser usado sozinho para decidir ambas.

Um worker pode estar vivo, mas sem capacidade de processar a fila. Nesse caso, liveness
deve continuar saudável, enquanto uma métrica de backlog, uma readiness própria ou o
controle de concorrência sinaliza saturação.

## Heartbeat em conexões

TCP mantém conexão, mas uma conexão estabelecida não garante que a aplicação remota ainda
esteja processando. Protocolos como WebSocket, AMQP e sistemas de cluster podem usar
heartbeat no nível da aplicação para detectar peers silenciosos.

O intervalo deve considerar proxies, NAT, balanceadores e limites de idle timeout. Enviar
sinais demais consome bateria, CPU e rede. Enviar poucos sinais aumenta o tempo de
detecção.

## Heartbeat em filas e workers

Um worker pode renovar a visibilidade ou lease de uma mensagem enquanto processa um job
longo. Se a renovação falhar, o broker pode entregar a mensagem a outro worker. O handler
deve ser idempotente porque o primeiro worker pode ter aplicado o efeito antes de perder a
conexão.

Não prolongue o lease indefinidamente para esconder um job travado. Defina tempo máximo,
cancelamento, dead letter e investigação de jobs que ultrapassam o orçamento.

## Falhas e falsos positivos

Heartbeat pode falhar por partição de rede, sobrecarga de CPU, pausa de garbage
collection, suspensão da máquina, clock incorreto ou fila de eventos bloqueada. Um
receptor que promove imediatamente um novo líder pode criar split brain se o participante
antigo ainda tiver acesso ao recurso.

Use quorum, fencing, epoch, líder observado por uma autoridade e reconciliação. Em sistemas
críticos, perder a confirmação de atividade deve retirar autoridade antes de presumir que o
efeito foi concluído.

## Relações

- [TTL e expiração](../dados/ttl.md) explica validade temporal e seus limites.
- [Liveness probe](../kubernetes/recursos/liveness-probe.md) e [readiness probe](../kubernetes/recursos/readiness-probe.md)
  distinguem restart de tráfego.
- [Replicação](../dados/replicacao.md) trata lag, failover e fencing.
- [Deadlock](../engenharia-software/concorrencia/deadlock.md) trata espera sem progresso.

## Fontes

- [etcd, leases](https://etcd.io/docs/v3.6/learning/api_guarantees/)
- [Kubernetes, node leases](https://kubernetes.io/docs/reference/node/node-status/)
- [RabbitMQ, heartbeats](https://www.rabbitmq.com/docs/heartbeats)
