# ShareDB

ShareDB é uma biblioteca full-stack para colaboração em documentos JSON em tempo real.
Ela possui servidor Node.js, cliente JavaScript, sincronização, consultas reativas,
presença e um sistema de tipos que define como operações são transformadas. O tipo
`json0` é o tipo tradicional distribuído pelo projeto; outros tipos podem ser adicionados
por plugins.

## Operational Transformation

ShareDB usa Operational Transformation, OT, para transformar operações concorrentes sobre
uma versão conhecida do documento. Se um cliente insere texto em uma posição enquanto
outro cliente insere ou remove conteúdo antes dela, a operação precisa ser transformada
para a nova posição antes de ser aplicada.

O servidor coordena versões e confirma operações. Clientes podem aplicar mudanças de forma
otimista e depois rebater operações locais contra operações remotas. O resultado depende
do contrato do tipo: OT para texto não é a mesma coisa que OT para um mapa JSON.

## Componentes

Uma instalação normalmente combina:

- cliente, que manipula documentos e envia operações;
- servidor, que recebe, valida, transforma e transmite operações;
- backend de persistência, que armazena snapshots ou histórico;
- pub/sub, quando há mais de um processo de servidor;
- tipos OT, que definem operações e transformação;
- middleware, para autenticação, autorização e extensões;
- presença, para cursores e usuários conectados.

O servidor pode ser escalado horizontalmente quando a persistência e a comunicação entre
instâncias possuem uma estratégia adequada. Pub/sub distribui operações entre processos,
mas não substitui a persistência nem garante que um consumidor perdido recupere o histórico.

## Documento, versão e operação

O cliente trabalha sobre uma versão conhecida. Uma operação local pode ser aplicada
imediatamente, mas precisa ser transformada quando o servidor confirma mudanças remotas que
chegaram antes. A operação deve ser identificável para retry e deduplicação.

O sistema precisa definir o que acontece quando o cliente envia uma operação baseada em uma
versão antiga, quando o documento foi excluído ou quando o tipo rejeita a transformação.
Rejeitar uma operação não é o mesmo que resolver um conflito; o produto precisa informar o
usuário ou produzir uma operação compensatória.

## Consultas reativas

ShareDB pode manter assinaturas de consultas para que clientes recebam mudanças relevantes.
Isso exige controle de autorização por consulta, limite de tamanho, invalidação quando
permissões mudam e política para clientes lentos.

Uma consulta reativa em memória não é uma fila durável. Se o cliente perder operações,
deve refazer a assinatura ou solicitar um snapshot compatível com a versão que possui.

## Presença

Presença representa estado efêmero, como cursor, seleção, usuário ativo ou conexão. Não
deve ser confundida com o documento persistido. O servidor deve expirar presença quando a
conexão cai e não usá-la como autoridade para permissões ou auditoria.

## Segurança e operação

Valide identidade, autorização do documento, campos alterados, tamanho da operação e taxa
de publicação. Não permita que o cliente escolha livremente um documento ou uma coleção.
Registre operações sensíveis, mas não coloque conteúdo privado em logs sem uma política de
proteção.

Monitore conexões, operações por segundo, latência de confirmação, tamanho de snapshots,
backlog de pub/sub, erros de transformação, clientes desconectados e tempo de recuperação.
Teste reinício do servidor no meio de uma edição e reconexão com operações locais pendentes.

## ShareDB e CRDT

OT depende de transformar operações em relação ao histórico que o servidor coordena. CRDTs
representam estado ou operações de modo que réplicas possam aplicar mudanças em ordens
compatíveis e convergir. As duas abordagens podem oferecer edição colaborativa, mas têm
modelos de metadados, servidores, compactação, semântica de texto e custos diferentes.

ShareDB é uma escolha natural quando a aplicação já possui um servidor coordenador, precisa
de um modelo operacional baseado em operações e quer integrar tipos e middleware do seu
ecossistema. Um CRDT pode ser preferível quando peers precisam editar offline e sincronizar
sem uma autoridade central obrigatória.

## Fontes primárias

- [ShareDB documentation](https://share.github.io/sharedb/)
- [ShareDB repository](https://github.com/share/sharedb)
- [ShareDB types](https://share.github.io/sharedb/types/)
- [Operational Transformation, ShareDB](https://share.github.io/sharedb/ot/)
