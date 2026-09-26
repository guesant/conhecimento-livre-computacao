# Hubble

Hubble é a camada de observabilidade de rede integrada ao Cilium. Ele recebe
eventos produzidos pelo dataplane e apresenta fluxos, decisões de policy,
identidades, Services, DNS e, quando habilitado, informações de protocolos de
camada 7.

Hubble não é um dataplane alternativo. O Cilium encaminha e protege o tráfego;
Hubble observa o que o dataplane consegue expor. Essa separação é essencial
para entender seus modos de operação e seus limites.

## O que Hubble observa

Cada evento representa uma observação de rede produzida por hooks, programas
eBPF, proxy ou componentes do Cilium. Dependendo do caminho, um fluxo pode
conter:

- origem e destino, como IP, porta, protocolo, Pod, namespace e nó;
- identidade de segurança e labels associados aos endpoints;
- direção do tráfego e relação com um Service;
- veredito, como FORWARDED, DROPPED, ERROR ou AUDIT;
- motivo do drop ou da falha;
- flags e estado relevante do TCP;
- consultas e respostas DNS quando há visibilidade DNS;
- requisições e respostas HTTP ou outros protocolos suportados quando há
  visibilidade L7;
- duração, status, latência e contexto do proxy quando esse contexto existe;
- informação sobre tráfego criptografado quando o dataplane consegue classificá-lo.

O conjunto exato de campos depende da versão, do hook que observou o tráfego,
do parser, da policy, do proxy e da configuração de visibilidade. A ausência
de um campo não significa necessariamente que o tráfego não ocorreu.

## Modos de operação

Os modos abaixo podem ser combinados. A escolha principal é entre não rodar
Hubble, observar apenas localmente, expor uma visão multi-nó por Relay ou
publicar dados derivados como UI, métricas e exportações.

### Hubble desabilitado

O Cilium continua funcionando como CNI, dataplane e camada de policy, mas não
expõe a API de observabilidade do Hubble. Esse é o menor consumo de recursos e
o menor risco de exposição de metadados, porém o diagnóstico depende de
comandos do Cilium, métricas, logs e ferramentas externas.

Esse modo pode ser adequado para clusters pequenos, ambientes em que
observabilidade de fluxo não é requisito ou fases iniciais de instalação.

### Hubble local no agente

O servidor Hubble embutido no agente roda em cada nó. Um cliente local pode
consultar o socket Unix do agente para observar fluxos produzidos naquele nó.

Esse modo não exige Relay nem uma UI. Ele é útil para investigação pontual,
testes de policy e ambientes em que não se deseja manter uma superfície de
observabilidade centralizada.

A visão é limitada ao que está disponível naquele agente. Um comando local
não representa automaticamente o cluster inteiro.

### Hubble Relay

O Relay é um componente separado que se conecta aos servidores Hubble dos
agentes e oferece uma API agregada para consulta multi-nó. Ele não substitui
os agentes nem captura pacotes por conta própria.

O Relay é a escolha normal para uma instalação em que o CLI, a UI ou um
cliente gRPC precisa consultar o cluster sem conhecer cada agente. Ele
centraliza acesso, mas também passa a ser um componente que precisa de
recursos, TLS, autenticação e controle de exposição.

O Relay não transforma os fluxos em armazenamento histórico ilimitado. A
retenção e a persistência precisam ser providenciadas por exportadores ou
sistemas externos.

### Hubble CLI

O CLI consulta o servidor local ou o Relay e filtra os eventos de forma
interativa. Ele serve para investigação, validação de policy e diagnóstico de
incidentes.

Exemplos conceituais:

```bash
hubble status
hubble observe --namespace default
hubble observe --pod frontend
hubble observe --verdict DROPPED
hubble observe --protocol http
hubble observe --since 5m
hubble observe --follow
```

Os filtros podem combinar namespace, Pod, identidade, labels, endereço,
porta, protocolo, direção, veredito, tipo de evento e janela de tempo. O CLI
também consegue separar tráfego de resposta, eventos L7 e fluxos criptografados
quando essas informações foram produzidas.

Os comandos e as flags disponíveis variam com a versão do cliente. O
comando `hubble help observe` deve ser a referência para a instalação em uso.

### Hubble UI

A UI apresenta um mapa de serviços e uma lista de eventos recentes. Ela ajuda
a visualizar dependências entre workloads, namespaces e Services, além de
abrir os fluxos individuais para investigação.

A UI é uma camada de consumo. Ela não aumenta a retenção dos eventos nem
descobre tráfego que o agente não observou. Normalmente consome o Hubble Relay
e deve ser protegida com TLS, autenticação e uma exposição de rede restrita.

### Hubble Metrics

As métricas Hubble traduzem comportamento de rede e segurança em séries
Prometheus. Podem representar fluxos, drops, DNS, TCP, distribuição de portas,
HTTP e outros sinais habilitados.

As métricas de Hubble são diferentes das métricas do próprio Cilium. As
métricas do agente mostram o estado dos componentes do Cilium; as métricas
Hubble mostram comportamento de conectividade e segurança dos Pods.

O exporter pode ser estático, configurado na instalação, ou dinâmico, com uma
configuração que pode ser alterada sem reiniciar o agente. Labels de namespace,
workload, Pod, IP e identidade aumentam a cardinalidade. O conjunto precisa
ser pequeno o suficiente para a capacidade do Prometheus.

### Exportação de fluxos

Hubble pode exportar fluxos selecionados para arquivos ou sistemas externos,
conforme o componente e a versão instalados. A exportação deve usar filtros
para não transformar cada evento de rede em um volume ilimitado de dados.

Exportar não é o mesmo que armazenar todos os pacotes. O dado exportado é o
evento estruturado que Hubble produziu. A política de retenção, o formato, o
destino, a rotação e o controle de acesso ficam no sistema que recebe a
exportação.

### Hubble com TLS

O servidor Hubble, o Relay, o CLI e a UI podem usar certificados para proteger
as conexões gRPC. TLS evita que eventos de rede sejam lidos ou alterados no
caminho, mas não decide por si só quem pode consultar quais namespaces ou
fluxos.

Os certificados precisam de uma autoridade confiável, rotação, distribuição e
permissões adequadas. Uma instalação com Relay exposto sem TLS e sem controle
de acesso pode vazar topologia, nomes de workloads, endereços e metadados de
requisições.

## Arquitetura de coleta

O fluxo de dados normalmente segue este caminho:

1. O programa eBPF, o socket layer ou o proxy observa um evento.
2. O agente Cilium transforma o evento em um fluxo Hubble.
3. O servidor Hubble embutido disponibiliza o fluxo localmente.
4. O Relay consulta vários agentes e oferece uma visão multi-nó.
5. CLI, UI, métricas ou exportadores consomem o fluxo.
6. Um sistema externo pode armazenar agregados ou eventos selecionados.

O Hubble server oferece serviços para obter fluxos, nós, namespaces e estado
do servidor. O Relay conhece os peers e agrega consultas, mas não deve ser
confundido com um banco de dados de observabilidade.

## Visibilidade por camada

### L3 e L4

É o nível mais básico e normalmente mostra endpoints, IPs, portas, protocolos,
direção, veredito, drops e decisões de encaminhamento. Ele é suficiente para
descobrir que um Pod não alcança outro, que uma porta foi bloqueada ou que um
Service encaminhou para um destino inesperado.

### Investigação de DNS

Com visibilidade DNS habilitada, Hubble pode mostrar consultas, respostas,
nomes, tipos, endereços retornados e falhas observadas. Isso ajuda a separar
problemas de resolução dos problemas de conexão ao endereço resolvido.

DNS visibility não é um resolver e não substitui logs do CoreDNS ou de outro
servidor DNS. Ela também não prova que uma resposta era correta ou confiável.

### HTTP e outros protocolos L7

A visibilidade L7 depende do proxy e da configuração de policy. Em HTTP, os
eventos podem mostrar método, URL, status, duração e direção. Outros parsers
suportados podem expor eventos próprios.

L7 é poderoso para identificar uma requisição negada, um status de erro ou uma
latência anormal, mas pode expor query strings, cabeçalhos, nomes de usuário,
tokens e outros dados sensíveis. A redação de dados deve ser configurada
antes de tornar o acesso amplo.

## O que é possível investigar

### Conectividade

Hubble ajuda a verificar se o fluxo existiu, qual era a origem, para onde foi,
qual porta foi usada e qual veredito o dataplane produziu. Ele também permite
comparar um caminho permitido com um caminho bloqueado.

### NetworkPolicy

É possível identificar drops por policy, visualizar o contexto de identidade e
separar ausência de rota de negação explícita. Isso é útil para implementar
default-deny gradualmente e descobrir dependências não documentadas.

### DNS

É possível observar se uma aplicação consultou o nome esperado, se recebeu
resposta, se o endereço retornado foi usado e se a falha aconteceu antes ou
depois da conexão TCP.

### Services e balanceamento

Os fluxos mostram relações entre clientes, VIPs, Pods e endpoints. Isso ajuda
a investigar selectors incorretos, backends ausentes, distribuição inesperada,
NodePort, tráfego de entrada e caminhos de egress.

### Dependências entre workloads

A UI e os filtros do CLI podem revelar quais namespaces, Services e workloads
se comunicam. Esse inventário pode orientar políticas, migrações e análise de
impacto.

### Tráfego de entrada e saída

Hubble ajuda a distinguir tráfego interno, tráfego externo, acesso ao host,
egress para world e tráfego entre clusters, desde que o dataplane consiga
classificar os endpoints e o caminho.

### Criptografia

Os filtros do CLI podem separar fluxos criptografados de não criptografados
quando a informação está disponível no evento. Isso permite verificar a
cobertura de WireGuard ou IPsec sem interpretar o payload.

### Latência de rede

Eventos L7 e métricas podem mostrar duração de requisições observadas pelo
proxy. Esse número não é automaticamente a latência de negócio, porque pode
excluir filas, processamento assíncrono, chamadas subsequentes e tempo no
cliente.

### Resposta a incidentes

Durante um incidente, filtros por workload, identidade, destino, veredito e
janela de tempo ajudam a reduzir o espaço de investigação. O resultado deve
ser correlacionado com logs, métricas, traces, mudanças de policy e eventos do
Kubernetes.

## O que Hubble não faz

Hubble não é:

- captura completa de pacotes ou substituto de tcpdump;
- armazenamento histórico ilimitado;
- tracing distribuído de chamadas de negócio;
- coleta de logs da aplicação;
- análise de vulnerabilidades;
- firewall de aplicação independente;
- autorização de usuário ou de operação;
- garantia de que todos os fluxos foram observados;
- substituto de métricas de CPU, memória, disco ou banco de dados.

Ele também não observa magicamente payloads de protocolos que não possuem o
parser ou o caminho de proxy correspondente. TLS aplicado antes do ponto de
visibilidade pode impedir a leitura L7, embora ainda seja possível observar
parte do fluxo L3/L4.

## Privacidade e segurança

Fluxos de rede são dados potencialmente sensíveis. Eles podem revelar nomes de
serviços, topologia, IPs, portas, namespaces, destinos externos, URLs,
parâmetros e cabeçalhos.

Antes de habilitar Hubble em uma plataforma compartilhada:

- limite quem pode consultar o Relay;
- use TLS e uma autoridade de confiança administrada;
- redija query strings, user info e cabeçalhos sensíveis;
- reduza os labels de métricas ao necessário;
- filtre exportações e defina retenção;
- trate a UI como uma superfície administrativa;
- registre o acesso aos dados quando houver requisito de auditoria.

Hubble não deve ser habilitado com visibilidade L7 ampla apenas para produzir
um painel visual. A coleta deve ter uma pergunta operacional clara.

## Custo e capacidade

O custo depende da taxa de eventos, da quantidade de endpoints, do volume L7,
da cardinalidade das métricas, do número de clientes e do tempo de retenção
externa. `follow` no CLI, UI aberta, exportação ampla e labels detalhados
podem gerar carga significativa.

Para controlar custo:

1. Comece com L3/L4 e filtros de investigação.
2. Habilite DNS ou L7 apenas para workloads e protocolos necessários.
3. Escolha poucas métricas e limite os labels.
4. Use Relay para centralizar acesso, sem duplicar consumidores por agente.
5. Defina rotação e retenção no destino das exportações.
6. Meça CPU, memória, drops de eventos e latência antes de ampliar a coleta.

O objetivo de Hubble é produzir evidência útil, não preservar tudo que passou
pela rede.

## Diagnóstico operacional

Uma sequência básica é:

```bash
cilium status
hubble status
hubble observe --last 20
hubble observe --verdict DROPPED --since 10m
hubble observe --namespace default --since 5m
```

Se `cilium status` falhar, o problema pode ser o agente, o kernel, o CRD, o
operator ou o dataplane, e não o Hubble. Se o agente estiver saudável mas o
Relay não responder, investigue Service, DNS, TLS, portas, certificados e
permissões do Relay.

Se não houver fluxos, verifique se houve tráfego na janela consultada, se o
cliente está conectado ao cluster correto, se o filtro excluiu os eventos e se
a visibilidade L7 foi habilitada para o protocolo que está sendo procurado.

Se faltarem campos L7, confirme se existe proxy, policy L7 e parser para o
protocolo. Não conclua que uma requisição não ocorreu apenas porque o Hubble
não exibiu um evento HTTP.

## Boas práticas

- Documente se a instalação usa socket local, Relay, UI, métricas ou exportação.
- Exponha o Relay apenas na rede administrativa necessária.
- Habilite TLS e planeje rotação de certificados.
- Comece com a menor visibilidade que responde à pergunta operacional.
- Mantenha filtros de investigação reproduzíveis.
- Correlacione fluxo, log, métrica, trace e evento de policy.
- Defina retenção e redaction antes de habilitar exportação.
- Teste Hubble depois de mudanças de CNI, policy, proxy e kernel.

## Más práticas

- Expor Hubble Relay publicamente sem autenticação e TLS.
- Habilitar todos os parsers L7 e todas as labels de métricas por padrão.
- Usar a UI como se ela fosse armazenamento histórico.
- Confundir um fluxo permitido com uma autorização de negócio.
- Esperar que Hubble substitua tracing distribuído.
- Exportar todos os eventos sem limite, filtro ou retenção.
- Interpretar ausência de evento como prova de ausência de tráfego.

## Relação com Cilium e observabilidade

[Cilium](cilium.md) explica as decisões de dataplane, policy, routing, IPAM e
Services que produzem os eventos. [Observabilidade](../../observabilidade/index.md)
explica o domínio mais amplo de métricas, logs e traces. [Service mesh](../service-mesh/index.md)
explica quando o proxy e a visibilidade L7 fazem parte de uma composição
maior.

## Fontes primárias

- [Hubble overview](https://docs.cilium.io/en/stable/observability/hubble/)
- [Hubble internals](https://docs.cilium.io/en/stable/internals/hubble/)
- [Hubble CLI](https://docs.cilium.io/en/stable/observability/hubble/hubble-cli/)
- [Hubble UI](https://docs.cilium.io/en/stable/observability/hubble/hubble-ui/)
- [Monitoring and metrics](https://docs.cilium.io/en/stable/observability/metrics/)
- [Layer 7 protocol visibility](https://docs.cilium.io/en/stable/observability/visibility/)
- [Hubble TLS](https://docs.cilium.io/en/stable/observability/hubble/configuration/tls/)
- [Cilium documentation](https://docs.cilium.io/)
