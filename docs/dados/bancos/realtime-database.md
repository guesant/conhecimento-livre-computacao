# Bancos de dados em tempo real

Um banco de dados em tempo real mantém dados persistidos e notifica clientes sobre
alterações sem que cada cliente precise repetir manualmente uma consulta. O termo pode
descrever um modelo de armazenamento, um protocolo de sincronização ou um produto que
combina os dois. Essas coisas devem ser separadas durante o planejamento.

Uma API que consulta um banco a cada segundo não é necessariamente um banco em tempo
real. Um websocket que transmite eventos sem persistência também não é um banco. Para
chamar uma solução de banco em tempo real, deve existir uma fonte de dados durável, uma
forma definida de observar mudanças e uma semântica clara para reconexão, ordem,
consistência e conflito.

## Modelo mental

O cliente mantém uma visão local de um conjunto de dados. Ele pode ler um valor inicial,
assinar um caminho ou consulta, receber alterações e atualizar a interface. O servidor
persiste a mudança, verifica autorização, publica uma notificação e acompanha o estado de
conexão conforme o protocolo adotado.

O fluxo pode ser dividido em:

1. leitura inicial ou recuperação de um estado local;
2. registro de uma assinatura;
3. alteração validada no servidor;
4. persistência e eventual commit;
5. evento de mudança associado à versão ou ao cursor;
6. atualização do cliente e confirmação de que ele está sincronizado.

Cada etapa pode falhar. A aplicação precisa saber se uma leitura é local ou confirmada,
se uma escrita foi aceita ou apenas enfileirada, se uma assinatura perdeu eventos e como
recuperar um estado completo.

## Persistência e sincronização não são a mesma coisa

O banco é responsável por durabilidade, consultas, transações, índices, concorrência e
recuperação. O mecanismo de sincronização é responsável por conexões, listeners,
reconexão, ordenação, cursors, backpressure e entrega ao cliente.

Alguns produtos implementam as duas partes como uma plataforma única. Em outra arquitetura,
um banco transacional publica mudanças por CDC ou outbox, um serviço de sincronização cria
um read model e clientes recebem eventos por WebSocket ou outro transporte. A segunda
abordagem oferece mais controle, mas exige operar mais componentes e definir o atraso entre
a fonte de verdade e a projeção.

## Estado, eventos e consistência

Uma atualização pode ser observada por diferentes clientes em momentos diferentes. A
documentação precisa dizer se o modelo oferece consistência forte para uma operação, leitura
eventual entre réplicas, ordenação por entidade, ordenação global ou somente uma garantia
de que o cliente converge após reconectar.

Também é importante distinguir:

- estado atual, que representa o valor mais recente;
- evento, que representa uma mudança e pode precisar de replay;
- snapshot, que permite reconstruir um estado em um ponto;
- presença, que representa conexão ou atividade e pode ser efêmera;
- mensagem, que pode ser entregue sem virar parte do estado persistido.

Um listener de estado não substitui um log de eventos. Se o consumidor precisa reprocessar
histórico, auditar transições ou reconstruir uma projeção, retenção, cursor e replay devem
ser requisitos explícitos.

## Escritas concorrentes e conflitos

Dois clientes podem alterar o mesmo registro sem conhecer a mudança do outro. Estratégias
possíveis incluem transação otimista, compare-and-set, versão monotônica, last-write-wins,
merge por campo, operação comutativa, autoridade única ou resolução explícita pelo usuário.

Last-write-wins é simples, mas pode apagar uma alteração válida sem que o usuário perceba.
Merge por campo reduz alguns conflitos, mas não entende invariantes de domínio. Uma
transação resolve a concorrência dentro de sua fronteira, mas não transforma múltiplos
serviços remotos em uma transação global.

Não use o relógio do dispositivo como única autoridade para ordenar mudanças. Relógios
podem estar adiantados, atrasados ou mudar durante uma viagem. Prefira versão do servidor,
sequência do stream ou uma regra de conflito compatível com o domínio.

## Offline e reconexão

Suporte offline normalmente significa que o SDK mantém uma cópia local, aceita algumas
operações sem conexão e tenta sincronizá-las depois. Isso não significa que qualquer
operação possa ser feita offline nem que não exista conflito.

Defina:

- quais dados podem ser lidos localmente;
- quais escritas podem ser enfileiradas;
- quanto espaço a cópia local pode consumir;
- como expirar, apagar ou criptografar dados locais;
- como representar estado pendente, confirmado e rejeitado;
- como repetir sem duplicar efeitos;
- o que acontece quando as regras de autorização mudam offline;
- como detectar perda de eventos e fazer resync completo.

O cliente deve conseguir recuperar de uma reconexão sem depender de cada evento perdido.
Um cursor persistido, uma versão de snapshot ou uma leitura inicial seguida da assinatura
costumam ser mais seguros que presumir que a conexão nunca falhará.

## Segurança

Regras de segurança não devem viver somente na interface. O servidor precisa autenticar o
cliente, autorizar cada leitura e escrita, validar schema e tamanho, limitar frequência e
impedir que um cliente assine uma árvore inteira por conveniência.

Avalie também:

- enumeração de identificadores;
- exfiltração por consultas amplas;
- vazamento de dados para clientes desconectados;
- permissões herdadas em subárvores;
- alteração de dados de outro tenant;
- abuso de listeners e conexões persistentes;
- retenção de dados em cache local;
- logs de payloads sensíveis;
- rotação e revogação de tokens durante uma sessão.

Autorização de leitura e autorização de assinatura precisam ser coerentes. Uma regra que
permite consultar um item isolado, mas permite assinar a coleção inteira, ainda expõe dados
demais.

## Schema, consultas e custo

Modelos de banco em tempo real frequentemente favorecem leituras por caminho e atualização
de subárvores. Isso pode ser eficiente para telas pequenas, mas uma árvore profundamente
aninhada cria acoplamento: uma mudança em um ramo pode transferir dados que o cliente não
precisa.

Projete pela forma de leitura real, mantendo referências ou projeções quando necessário.
Defina índices, limites de resultado, paginação, ordenação estável e tamanho máximo de
payload. Um listener de coleção que cresce sem limite transforma cada alteração em custo
de rede, memória, serialização e renderização.

Evite duplicação sem política de consistência. Denormalizar pode reduzir consultas, mas toda
cópia precisa de ownership, atualização atômica ou processo de reconciliação. A duplicação
de dados editoriais, de permissões ou de saldos financeiros exige critérios diferentes.

## Escala e operação

Meça conexões simultâneas, listeners, mensagens por segundo, bytes por segundo, tamanho de
payload, atraso de propagação, reconexões, rejeições, backlog e tempo de resync. CPU do banco
é apenas uma parte do custo; conexões abertas e fanout podem pressionar gateway, memória,
rede e dispositivos clientes.

Defina limites para:

- número de conexões por identidade e por cliente;
- listeners por sessão;
- profundidade e tamanho de consulta;
- frequência de escrita e fanout;
- retenção de eventos e tamanho de snapshot;
- reconexões e retry;
- clientes lentos e buffers de saída.

Clientes lentos exigem uma política. O servidor pode aplicar backpressure, descartar
atualizações intermediárias quando somente o estado final importa, desconectar o consumidor
ou exigir um resync. Não permita que um consumidor lento faça a memória do serviço crescer
indefinidamente.

## Realtime Database do Firebase

O [Firebase Realtime Database](https://firebase.google.com/docs/database) é um banco cloud
NoSQL que armazena dados como JSON e sincroniza atualizações aos clientes conectados. O SDK
também oferece suporte a operação offline, regras de segurança e acesso por plataformas
como web, Android, Apple, Flutter, C++ e Unity.

O modelo é adequado para presença, colaboração simples, dashboards, telemetria moderada,
chat e estado de interface que precisa ser compartilhado rapidamente. O desenho de dados
deve considerar a árvore JSON, os listeners e as regras, em vez de tratar o serviço como
um banco relacional com joins arbitrários.

O próprio Firebase diferencia Realtime Database de Cloud Firestore. Firestore oferece um
modelo de documentos e consultas diferente, com outras propriedades de escala, índice,
custos e disponibilidade. A escolha deve partir de consultas, consistência, tamanho do
estado, offline, necessidade de agregação e modelo operacional, não somente do nome
"tempo real".

## Alternativas

Há várias formas de entregar atualização contínua:

| Abordagem | Fonte de verdade | O que entrega | Risco principal |
| --- | --- | --- | --- |
| Banco em tempo real gerenciado | Serviço gerenciado | Estado e sincronização integrados | Acoplamento e custo por leitura/conexão |
| Banco tradicional mais WebSocket | Banco próprio | Eventos derivados ou estado projetado | Operar conexão, fanout e reconexão |
| CDC ou outbox mais stream | Banco e log de eventos | Mudanças reprocessáveis | Consistência e atraso entre fonte e projeção |
| Polling curto | Banco ou API | Estado em intervalos | Carga repetida e atraso previsível |
| Server-Sent Events | API ou read model | Stream unidirecional para clientes | Reconexão e proxy intermediário |
| WebSocket | Serviço de sessão | Comunicação bidirecional | Autorização e escala de conexões |

Escolha polling quando a frequência é baixa, a simplicidade importa e alguns segundos de
atraso são aceitáveis. Escolha sincronização contínua quando o benefício de atualização
rápida compensa o custo de conexões, fanout, cache local e tratamento de falhas.

## Relação com ReactiveX e Flow

Um banco em tempo real produz ou consome mudanças persistidas. [ReactiveX](../../comunicacao/reactivex.md)
e [Kotlin Flow](../../comunicacao/kotlin-flow.md) são abstrações para trabalhar com fluxos
de valores dentro da aplicação. Eles podem consumir listeners de um banco, mas não fornecem
durabilidade, autorização ou recuperação por si próprios.

## Fontes primárias

- [Firebase Realtime Database](https://firebase.google.com/docs/database)
- [Firebase Realtime Database, security rules](https://firebase.google.com/docs/database/security)
- [Firebase Realtime Database, offline capabilities](https://firebase.google.com/docs/database/web/offline-capabilities)
- [Firebase Cloud Firestore](https://firebase.google.com/docs/firestore)
