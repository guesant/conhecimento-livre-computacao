# Comparação entre PouchDB e CouchDB

PouchDB é um banco JavaScript executado localmente ou como cliente de um banco remoto.
Apache CouchDB é um banco de documentos JSON com API HTTP e replicação entre bancos. A
combinação permite manter uma cópia local, trabalhar offline e sincronizar alterações
quando a conexão volta.

## Replicação

CouchDB replica de uma base para outra por HTTP. A direção pode ser push ou pull, e uma
sincronização bidirecional normalmente combina as duas. O replicator compara revisões e
transfere o que falta; uma replicação contínua acompanha mudanças novas.

PouchDB implementa o algoritmo de replicação do CouchDB, o que permite usar uma base local
no navegador ou em um dispositivo e sincronizá-la com uma base remota. A replicação não
significa que todos os peers enxergam o mesmo estado imediatamente. O modelo é eventual,
com reconexão, cópia de revisões e possíveis conflitos.

## Revision tree e MVCC

Cada documento possui um identificador e uma revisão. O histórico forma uma árvore de
revisões quando alterações concorrentes partem da mesma base. A revisão vencedora é
escolhida por um algoritmo determinístico, mas as revisões conflitantes podem continuar
armazenadas.

Esse comportamento permite que todos os peers escolham o mesmo vencedor sem exigir um
coordenador online no instante da edição. Porém, vencedor determinístico não significa
merge sem perda. Se dois usuários alterarem campos diferentes, a aplicação pode precisar
combinar os documentos e criar uma nova revisão resolvida.

## Conflitos

Conflitos podem ser imediatos, quando uma gravação usa uma revisão antiga e recebe `409`, ou
eventuais, quando duas bases aceitaram alterações independentes e depois replicaram.

Uma leitura simples pode mostrar somente o vencedor. Para investigar, solicite os conflitos
ou as folhas da árvore, carregue as revisões e aplique uma política de domínio. A resolução
normalmente grava o documento combinado e remove ou marca as revisões obsoletas conforme o
procedimento adotado.

Não ignore conflitos sem medir. Um vencedor automático pode ser adequado para cache ou
preferência recente, mas é perigoso para texto, inventário, permissões, dados financeiros e
registros legais.

## Dados e design

O modelo de documento favorece acesso por documento e replicação de unidades completas.
Defina identificadores estáveis, tamanho máximo, anexos, índices, consultas e política de
retenção de revisões.

Evite um documento gigante para toda a aplicação. Um conflito nesse documento mistura
alterações não relacionadas, aumenta o custo de replicação e torna a resolução mais difícil.
Ao mesmo tempo, dividir demais pode exigir muitas consultas e listeners. A unidade de
replicação deve refletir a unidade que pode ser editada e sincronizada com segurança.

## Segurança e sincronização seletiva

Autentique a base remota e autorize documentos, usuários e operações. Replicação filtrada
precisa considerar criação, atualização e remoção, inclusive quando o documento já não
possui corpo visível.

O dispositivo local pode manter dados depois do logout. Planeje criptografia, remoção da
cópia, expiração de sessão, rotação de credenciais e revogação. Não trate o fato de a
interface esconder um documento como proteção de replicação.

## PouchDB, CouchDB e outras opções

| Opção | Foco | Conflito e sincronização |
| --- | --- | --- |
| PouchDB e CouchDB | Documentos JSON e replicação HTTP | Revision tree e resolução controlada pela aplicação |
| SQLite mais sincronização própria | Dados relacionais locais | Política de patches, versões ou merge definida pelo produto |
| Yjs ou Loro | Edição colaborativa e CRDT | Merge orientado a tipos compartilhados |
| ShareDB | Colaboração com servidor coordenador | Operational Transformation |
| Jazz | Banco relacional local-first | Réplicas locais e sincronização de linhas |

## Fontes primárias

- [Apache CouchDB, introduction to replication](https://docs.couchdb.org/en/stable/replication/intro.html)
- [Apache CouchDB, replication and conflict model](https://docs.couchdb.org/en/stable/replication/conflicts.html)
- [Apache CouchDB, replication protocol](https://docs.couchdb.org/en/stable/replication/protocol.html)
- [PouchDB replication](https://pouchdb.apache.org/guides/replication.html)
- [PouchDB conflicts](https://pouchdb.apache.org/guides/conflicts.html)
