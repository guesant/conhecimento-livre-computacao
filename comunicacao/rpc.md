# Remote Procedure Call

Remote Procedure Call, RPC, é uma abstração em que um processo chama uma
operação implementada por outro processo como se estivesse invocando uma
função local. A aparência de chamada local é conveniente, mas não elimina as
falhas distribuídas: a rede pode atrasar, perder mensagens, duplicar tentativas
ou ficar indisponível depois que o servidor já executou a operação.

RPC é um modelo, não um protocolo único. ONC RPC, JSON-RPC, gRPC, Apache
Thrift, Cap'n Proto e implementações proprietárias são escolhas diferentes
para contrato, serialização, transporte e ciclo de vida.

## Anatomia de uma chamada

Uma chamada RPC normalmente envolve:

1. Um contrato que define serviço, método, argumentos e resultado.
2. Um cliente ou stub que oferece uma interface local.
3. Marshalling, que transforma argumentos em uma mensagem.
4. Transporte, como TCP, HTTP/2, Unix socket ou QUIC.
5. Um dispatcher que identifica o método no servidor.
6. Deserialização, validação e execução da operação.
7. Serialização da resposta, erro ou stream de mensagens.
8. Um cliente que traduz a resposta para o tipo local.

O contrato pode ser escrito em uma IDL, inferido de código ou definido por
convenção. Uma IDL facilita geração de clientes, validação e compatibilidade,
mas também cria um artefato que precisa de versionamento.

## Formas de interação

| Forma | Comportamento | Exemplo de uso |
| --- | --- | --- |
| Unary | Uma requisição e uma resposta | Buscar um usuário ou criar um recurso |
| Server streaming | Uma requisição e várias respostas | Eventos, exportação ou leitura incremental |
| Client streaming | Várias mensagens e uma resposta | Upload ou agregação de lotes |
| Bidirectional streaming | Dois streams independentes | Sessão interativa e telemetria contínua |
| Assíncrona | O resultado é entregue depois ou por evento | Trabalho longo e integração desacoplada |

Streaming não transforma uma operação em uma fila durável. Se o consumidor
precisa retomar depois de uma falha, o sistema precisa de offset, persistência,
idempotência ou uma tecnologia de mensageria apropriada.

## O problema da transparência

Uma chamada local costuma falhar por erro de programa ou por uma exceção
determinística. Uma chamada remota pode falhar por DNS, conexão, TLS,
autenticação, proxy, timeout, saturação, partição de rede, reinício do
servidor ou conclusão desconhecida.

Por isso, APIs RPC precisam declarar deadlines, cancelamento, limites de
mensagem e semântica de erro. O cliente deve saber se pode repetir a operação.
Retries automáticos em uma escrita não idempotente podem criar duplicatas ou
efeitos repetidos.

## Contrato e evolução

Um contrato deve evoluir sem quebrar consumidores ainda não atualizados.
Práticas comuns incluem:

- adicionar campos opcionais sem reutilizar identificadores antigos;
- manter métodos antigos durante uma janela de migração;
- aceitar campos desconhecidos quando o formato permite;
- versionar mudanças incompatíveis;
- testar cliente antigo contra servidor novo e o inverso;
- publicar limites de tamanho, timeout e comportamento de erro.

Renomear um método, mudar a interpretação de um campo ou transformar uma
operação idempotente em não idempotente é uma mudança de comportamento mesmo
quando o schema continua válido.

## Segurança

RPC precisa proteger transporte e operação. TLS protege o canal, mas a
autenticação deve identificar o cliente e a autorização deve verificar o que
ele pode fazer. Metadados não devem ser aceitos como autoridade sem validação.

Limite tamanho de mensagens, profundidade de estruturas, duração de streams,
número de chamadas concorrentes e custo de consultas. Valide todos os campos
antes de executar a operação e evite desserializadores que instanciam tipos ou
executam comportamento arbitrário.

## RPC, REST e mensageria

RPC organiza a interface em operações. REST organiza recursos e suas
representações segundo semântica HTTP. As duas abordagens podem usar JSON,
TLS, autenticação e o mesmo balanceador, mas criam contratos diferentes.

Mensageria separa produtor e consumidor no tempo. Uma chamada RPC normalmente
espera uma resposta dentro de um deadline, enquanto uma fila pode persistir o
trabalho e permitir que o consumidor processe mais tarde.

Uma arquitetura pode usar RPC para consulta síncrona, mensageria para trabalho
demorado e eventos para notificar mudanças. Não use RPC como substituto de fila
quando a durabilidade e o desacoplamento temporal são requisitos centrais.

## Quando usar

RPC é apropriado quando há operações bem definidas, clientes e servidores sob
coordenação suficiente para compartilhar um contrato, baixa latência ou
streaming. Ele costuma funcionar bem na comunicação interna entre serviços e
em agentes de infraestrutura.

Prefira uma interface mais orientada a recursos quando consumidores são
externos, heterogêneos e dependem de cache HTTP, ferramentas de navegador e
interoperabilidade textual. Prefira mensageria quando a operação pode ser
processada depois, precisa de retenção ou deve sobreviver à indisponibilidade
temporária do consumidor.

## Fontes

- [RFC 5531, Remote Procedure Call Protocol Version 2](https://www.rfc-editor.org/rfc/rfc5531)
- [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
- [JSON-RPC specification](https://www.jsonrpc.org/specification)

## Continue por aqui

[gRPC](grpc.md) é uma implementação moderna de RPC. [IPC](ipc.md) trata da
comunicação no mesmo sistema. [GraphQL](graphql.md) usa uma linguagem de
consulta para permitir que o cliente selecione dados.
