# Mapa de local-first e offline-first

Local-first é um modelo em que a aplicação trata a réplica local como o caminho primário
para leitura e escrita. A rede sincroniza em segundo plano, em vez de ser necessária para
cada interação. Offline-first é o conjunto de requisitos e técnicas que permite continuar
funcionando sem conectividade; uma aplicação pode ser offline-first sem ser completamente
local-first.

## O que muda no modelo tradicional

Em uma aplicação request-response, o cliente envia a operação, espera o servidor e recebe
uma resposta. Em um modelo local-first, o cliente lê um estado persistido localmente,
aplica uma operação, mostra o resultado e registra a mudança para sincronização posterior.

Isso reduz a latência percebida e permite trabalhar durante uma interrupção de rede, mas
cria novas responsabilidades: a escrita local pode ainda não ter sido aceita pela
autoridade, duas réplicas podem divergir e o dispositivo pode ser perdido antes da
replicação.

## Propriedades que devem ser especificadas

Não basta dizer que o produto é offline-first. Defina:

- quais consultas estão disponíveis localmente;
- qual parte do banco é materializada no dispositivo;
- quando uma escrita é considerada localmente durável;
- quando ela chega a um edge ou servidor central;
- quando ela é confirmada pela autoridade de negócio;
- como mudanças são autenticadas e autorizadas offline;
- como conflitos são detectados e resolvidos;
- como o cliente recebe dados apagados ou revogados;
- qual dado local é criptografado, retido e eliminado;
- como exportar, recuperar ou invalidar a réplica.

Uma interface pode mostrar "salvo neste dispositivo" sem afirmar "sincronizado com o
servidor". Estados como pendente, sincronizado, rejeitado e conflito precisam ser
distinguíveis quando tiverem consequências para o usuário.

## Arquitetura comum

Uma composição típica possui:

1. armazenamento local durável, como SQLite, IndexedDB, PouchDB ou uma camada embutida;
2. modelo de mudanças, com identificador de operação, autor e causalidade;
3. fila de alterações locais pendentes;
4. protocolo de sincronização incremental;
5. servidor ou peers que aceitam, encaminham e persistem mudanças;
6. política de merge e de resolução manual;
7. compactação, snapshots e garbage collection.

O protocolo precisa sobreviver a retry, duplicidade, reordenação, reconexão e versões
antigas do cliente. Uma mensagem pode chegar duas vezes; aplicar a mesma operação duas
vezes não pode duplicar um item nem repetir uma cobrança.

## Offline não elimina autoridade

Criar uma tarefa localmente pode ser seguro se o identificador for único e o servidor
aceitar merge. Alterar saldo, reservar um recurso ou revogar acesso normalmente exige uma
autoridade que valide a operação contra estado global.

A solução pode separar intenção local e confirmação global. O cliente registra a intenção,
o servidor valida depois e a interface mostra rejeição ou compensação. Não declare que uma
operação foi concluída somente porque foi aplicada na réplica local.

## Cache local, réplica e fonte de verdade

Um cache local pode ser descartado e recarregado. Uma réplica local participa da
sincronização e precisa de identidade, versão e protocolo de recuperação. Um banco
local-first pode ser a fonte imediata da experiência, enquanto todas as réplicas convergem
para um estado que o domínio considera válido.

Também é possível ter um banco central como autoridade e uma réplica local como cópia
editável. Nesse caso, "local-first" descreve a experiência e o caminho de execução, não a
ausência de autoridade central.

## Segurança

Dados offline ampliam a superfície de perda física, extração e uso depois da revogação.
Considere criptografia em repouso, chaves protegidas, expiração, limpeza remota quando
possível, escopo mínimo de sincronização, autenticação por operação e não apenas por sessão.

Não envie para o dispositivo uma coleção inteira se o usuário só precisa de uma projeção.
Filtros de sincronização precisam ser aplicados no servidor, não somente escondidos na
interface.

## Quando usar

Local-first é atraente para editores colaborativos, notas, checklists, apps de campo,
clientes móveis, ferramentas de desenho, inventários com conectividade irregular e telas
que precisam abrir instantaneamente.

Ele pode ser inadequado quando o dado é muito sensível, o estado local não pode ser
confiável, a autorização muda constantemente ou as invariantes dependem de uma transação
global síncrona.

## Relações

[PouchDB e CouchDB](pouchdb-couchdb.md) usam replicação de documentos e tornam conflitos
explícitos. [Yjs](yjs.md), [Loro](loro.md) e [Diamond Types](diamond-types.md) usam modelos
CRDT para classes diferentes de dados. [Jazz](jazz.md) apresenta um banco relacional
local-first. [Resolução de conflitos](resolucao-de-conflitos.md) explica por que nenhum
algoritmo resolve sozinho o significado de todas as operações.

## Fontes primárias

- [Local-first software, Ink and Switch](https://www.inkandswitch.com/local-first/)
- [PouchDB replication](https://pouchdb.apache.org/guides/replication.html)
- [Jazz local-first data model](https://jazz.tools/docs/concepts/local-first-data-model)
