# Yjs

Yjs é uma implementação de CRDT para aplicações colaborativas. Ele expõe shared types
como `Y.Map`, `Y.Array`, `Y.Text` e `Y.Xml`, que podem ser alterados por vários peers e
observados por bindings de interface. A rede e a persistência são módulos separados, por
isso Yjs pode ser conectado a WebSocket, WebRTC, armazenamento local ou outro provider.

## Y.Doc e shared types

Um `Y.Doc` contém os tipos compartilhados. O tipo não deve ser tratado como um objeto JSON
comum depois de inserido no documento, porque as mutações precisam passar pela API do Yjs
para gerar operações e notificações.

```javascript
const doc = new Y.Doc()
const text = doc.getText("body")

text.insert(0, "Olá")
text.observe(() => {
  console.log(text.toString())
})
```

Os tipos possuem identidade e histórico operacional. Uma atualização pode ser serializada,
persistida e aplicada a outra réplica. O resultado não depende somente do JSON visível;
os metadados do documento fazem parte do modelo colaborativo.

## Providers

Yjs não exige um servidor central para o modelo de dados. Providers podem transportar
updates por WebSocket, WebRTC ou outro meio, e persistence providers podem gravá-los em
IndexedDB, banco ou storage de servidor.

Essa modularidade separa quatro decisões:

- como peers descobrem e autenticam uns aos outros;
- como updates são transportados;
- como updates são persistidos;
- como awareness é distribuída.

O provider ainda precisa ter política de autorização, limites, reconexão, resync, retenção
e garbage collection. Network agnostic não significa segurança ou durabilidade automática.

## Offline e local-first

O provider `y-indexeddb` persiste updates no IndexedDB. O documento pode ser carregado
localmente e sincronizado depois. Isso permite que a interface abra sem esperar a rede, mas
não garante que o conteúdo esteja atualizado nem que uma alteração tenha chegado ao
servidor.

Mostre ao usuário a diferença entre estado local, estado enviado e estado confirmado quando
essa diferença importar. Se o dispositivo for compartilhado ou perdido, proteja e limpe a
cópia local.

## Texto e editores

`Y.Text` pode ser conectado a editores como ProseMirror, Quill, CodeMirror e outros por
bindings. Texto colaborativo tem problemas diferentes de um campo escalar: posição,
inserção simultânea, exclusão, formatação, seleção e undo precisam preservar intenção.

Awareness representa cursores, seleção e presença. Ela não faz parte do documento persistido
e pode desaparecer quando o peer fica offline. Não use awareness para guardar informação
necessária à reconstrução do estado.

## Escala e garbage collection

CRDTs retêm identificadores, tombstones e causalidade para aplicar updates que chegam fora
de ordem. Histórico cresce com edição e duração da sessão. Snapshots, compactação e garbage
collection reduzem custo, mas só são seguros quando todos os peers relevantes já observaram
as operações que serão descartadas.

Defina uma fronteira de retenção, reconciliação de clientes antigos e recuperação a partir
de snapshot. Medir somente tamanho do JSON final subestima o custo real do documento.

## Segurança

Valide identidade e autorização fora do editor e no provider. Um documento compartilhado
não deve permitir que o cliente altere campos administrativos apenas porque o CRDT aceita
a mutação. Separe conteúdo colaborativo de metadados controlados pelo servidor quando as
regras forem diferentes.

Considere criptografia de transporte, autenticação de room, isolamento de documento,
limite de updates, limite de awareness, proteção contra peer malicioso e revisão de
bindings que convertam conteúdo em HTML.

## Quando usar

Yjs é adequado para editores, quadros, cursores, comentários, listas compartilhadas e
estado estruturado que precisa sincronizar por mais de um transporte. Ele é menos adequado
quando o dado depende de transações globais, invariantes financeiras ou autorização que
precisa ser decidida exclusivamente no servidor.

Compare a escolha com [Loro](loro.md), [Diamond Types](diamond-types.md),
[JSON Joy](json-joy.md) e [ShareDB](sharedb.md). O critério deve incluir tamanho do
documento, tipo de edição, bindings, persistência, interoperabilidade, custo de histórico
e maturidade operacional.

## Fontes primárias

- [Yjs documentation](https://docs.yjs.dev/)
- [Yjs shared types](https://docs.yjs.dev/getting-started/working-with-shared-types)
- [Yjs offline support](https://docs.yjs.dev/getting-started/allowing-offline-editing)
- [Yjs awareness](https://docs.yjs.dev/getting-started/adding-awareness)
- [Yjs repository](https://github.com/yjs/yjs)
