# HAProxy

HAProxy é um proxy de alto desempenho para TCP e HTTP. Ele pode terminar conexões,
encaminhar tráfego, distribuir requisições entre servidores, executar health checks e
expor métricas operacionais. É uma implementação de proxy e balanceador, não uma
solução completa de firewall ou uma autoridade de serviço.

## Modelo mental

Uma configuração de HAProxy normalmente separa:

| Seção | Responsabilidade |
| --- | --- |
| `global` | parâmetros do processo, logs, sockets administrativos e limites gerais. |
| `defaults` | valores comuns para timeouts, logs e opções de proxies. |
| `frontend` | ponto que aceita conexões de clientes. |
| `backend` | conjunto de servidores que recebe o tráfego encaminhado. |
| `listen` | combinação de frontend e backend em uma seção única. |

O fluxo prático é aceitar uma conexão no frontend, avaliar regras de roteamento,
selecionar um backend e escolher um servidor saudável dentro dele. A separação permite
que vários frontends usem backends diferentes e que o backend seja trocado sem
alterar toda a borda.

## Camada 4 e camada 7

No modo TCP, HAProxy encaminha conexões sem interpretar a aplicação. Esse modelo é
adequado para TLS pass-through, bancos, SMTP, TLS bruto e protocolos que não devem ser
terminados no proxy. O balanceador consegue usar endereço, porta, estado da conexão e
health checks compatíveis, mas não pode tomar decisões sobre path ou cabeçalho HTTP.

No modo HTTP, HAProxy compreende requisição e resposta. Pode selecionar o backend por
host, path, método, cabeçalho, cookie ou outras amostras. Também pode terminar TLS,
adicionar cabeçalhos, aplicar limites, manter persistência e produzir métricas de
requisição.

Terminar TLS no HAProxy permite inspeção e roteamento HTTP, mas transforma o proxy em
parte da fronteira de confiança. Certificados, chaves, protocolos habilitados, logs e
redação de dados precisam ser tratados como material sensível.

## Balanceamento

Algoritmos comuns incluem round robin, least connections, ponderação por servidor,
hash de endereço ou hash de uma amostra da requisição. A escolha depende do estado da
aplicação:

- round robin distribui de forma simples quando os servidores são equivalentes;
- least connections ajuda quando as conexões têm durações diferentes;
- pesos representam capacidade desigual;
- hash oferece afinidade previsível, mas pode concentrar carga;
- stick tables podem preservar afinidade por uma chave operacional, com custo de
  estado e limpeza.

Balanceamento não torna a aplicação stateless. Se sessões, uploads ou cache local
dependem de um servidor específico, prefira remover a dependência ou documente a
afinidade e seu comportamento durante a falha.

## Health checks e disponibilidade

Um health check deve confirmar a condição que torna o servidor elegível para aquela
operação. Conectar à porta pode provar apenas que existe um processo escutando. Um
check HTTP pode exigir status, cabeçalho, conteúdo ou endpoint de prontidão. Não use o
mesmo endpoint de liveness para concluir que uma dependência crítica está pronta para
receber tráfego.

Defina intervalo, timeout, quantidade de falhas para marcar um servidor como
indisponível e quantidade de sucessos para recuperá-lo. Checks agressivos podem retirar
servidores saudáveis durante uma oscilação breve; checks lentos podem manter um destino
defeituoso na rotação.

O proxy precisa de comportamento para quando não houver servidores disponíveis, quando
um backend estiver parcialmente saudável e quando a própria configuração for inválida.
Valide a configuração antes de recarregar e preserve o processo anterior quando a nova
configuração não puder ser aplicada com segurança.

## Alta disponibilidade

Um único processo HAProxy continua sendo um ponto único de falha. Para eliminar esse
risco, use instâncias redundantes, um endereço virtual ou um balanceador externo, e um
mecanismo que anuncie apenas o membro apto. A redundância do proxy não resolve a
redundância do backend e não impede split brain por si só.

Em Kubernetes, um Service, Gateway API, Ingress Controller ou load balancer externo
pode assumir partes desse papel. HAProxy também pode rodar como appliance, daemon em
host, container ou componente de um controlador. A escolha depende de quem possui a
configuração, como certificados são entregues e onde o health check deve ocorrer.

## Segurança e operação

Restrinja o socket de administração, separe métricas de tráfego público e conceda
apenas os métodos administrativos necessários. Não exponha estatísticas ou capacidade
de alterar backends sem autenticação e controle de rede.

Defina limites de conexão, filas, tamanho de cabeçalho, timeout de cliente, timeout
de servidor e timeout de conexão. Um timeout ausente pode manter recursos ocupados
indefinidamente; um timeout curto pode interromper uploads e respostas legítimas.

Logs precisam diferenciar conexão aceita, requisição, seleção de backend, erro de
conexão, timeout e resposta do servidor. Preserve um identificador de correlação
quando ele já existir, sem transformar dados de usuário em labels de métrica.

## O que HAProxy não é

HAProxy não substitui um DNS autoritativo, um firewall stateful, um WAF completo, uma
fila, um service mesh ou um mecanismo de consenso. Ele pode participar dessas
composições, mas cada garantia precisa vir do componente que realmente a implementa.

Um reverse proxy pode esconder os backends e aplicar roteamento, mas ainda é necessário
controlar exposição de portas, origem permitida, identidade, autorização e tráfego de
saída.

## Relações

- [Proxies](index.md) compara forward proxy, reverse proxy e roteamento.
- [Reverse proxy](reverse-proxy.md) explica a responsabilidade geral de terminar e
  encaminhar requisições.
- [API gateway](../api-gateway/index.md) trata políticas de API, plugins e consumidores.
- [Tipos de firewall](../firewall/index.md) diferencia proxy, filtro e firewall.
- [Health checks](../../observabilidade/application-health.md) explica sinais de saúde.

## Fontes

- [HAProxy documentation](https://docs.haproxy.org/)
- [HAProxy 3.4 starter guide](https://docs.haproxy.org/3.4/intro.html)
- [HAProxy configuration manual](https://docs.haproxy.org/3.4/configuration.html)
