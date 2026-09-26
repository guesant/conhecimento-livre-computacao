# OpenFGA

OpenFGA é um serviço de autorização baseado em relações, inspirado no modelo Zanzibar. Em vez de guardar apenas uma lista de papéis, ele representa usuários, grupos, organizações, documentos, pastas e outros objetos como entidades relacionadas. A aplicação consulta se uma relação existe segundo um modelo de autorização e um conjunto de tuplas.

## Modelo mental

Um modelo OpenFGA declara tipos e relações. Uma tupla registra uma relação concreta, como:

```text
user:anne, member, organization:acme
organization:acme, viewer, document:roadmap
```

O modelo pode derivar relações. Por exemplo, `viewer` de um documento pode incluir membros de uma organização que tem essa relação com o documento. O serviço calcula se o usuário tem a relação solicitada, seguindo o modelo e as tuplas persistidas.

O modelo é separado dos dados de relacionamento. Isso permite mudar a forma como relações são interpretadas, desde que a migração e os testes preservem a semântica necessária.

## Operações

As operações principais são:

- **Check**, pergunta se um usuário tem uma relação com um objeto;
- **Write**, cria ou remove tuplas de relacionamento;
- **Read**, consulta tuplas persistidas;
- **ListObjects**, encontra objetos que um usuário pode acessar;
- **ListUsers**, encontra sujeitos que têm uma relação com um objeto;
- **Expand**, explica parte da árvore de relações.

Uma API deve usar `Check` para proteger uma operação individual e usar `ListObjects` ou uma estratégia equivalente para construir listagens autorizadas. Fazer um `List` geral e executar um `Check` para cada linha cria latência e carga previsíveis do padrão N+1.

## Modelo de autorização

Um modelo simplificado pode ser expresso assim:

```fga
model
  schema 1.1

type user

type organization
  relations
    define member: [user]

type document
  relations
    define owner: [user]
    define viewer: [user] or member from owner
```

Esse exemplo é apenas ilustrativo. A cardinalidade, os usuários públicos, grupos, usuários de usuários, restrições e relações derivadas precisam ser definidos conforme o domínio. Evite permitir relações implícitas amplas sem uma justificativa de negócio.

## Consistência

Uma autorização baseada em relações depende do momento em que as tuplas são lidas. OpenFGA oferece opções de consistência para equilibrar latência e visibilidade de escritas recentes. O serviço consumidor precisa escolher o nível compatível com a operação.

Para uma revogação crítica, não assuma que uma resposta cacheada ou uma leitura eventualmente consistente já refletiu a mudança. Para uma tela de navegação, uma pequena janela de atraso pode ser aceitável. A política deve documentar essa diferença.

Tuplas contextuais podem ser enviadas em uma consulta sem serem persistidas. Elas servem para fatos temporários da decisão, como uma relação válida apenas durante uma requisição. Não devem ser usadas como substituto de um fluxo de escrita quando a relação precisa existir para consultas futuras.

## Armazenamento e operação

OpenFGA separa o serviço, o authorization model e o datastore. O modelo deve ser versionado e identificado por um ID. Uma publicação segura testa o novo modelo com seus conjuntos de tuplas antes de torná-lo a versão usada pelas requisições.

O serviço precisa de:

- autenticação entre consumidores e OpenFGA;
- autorização para escrever modelos e tuplas;
- backup e recuperação do datastore;
- limites para tamanho e frequência de escrita;
- métricas de latência, erros e profundidade das consultas;
- rastreamento de correlation ID sem expor dados excessivos;
- estratégia de indisponibilidade e timeout.

O OpenFGA não deve ser acessível diretamente pelo navegador. O backend deve ser o PEP que autentica o chamador, normaliza IDs e solicita somente a decisão necessária.

## Evolução do modelo

Alterar uma relação pode mudar milhares de decisões. Antes de publicar:

1. mantenha o modelo novo ao lado do antigo;
2. crie testes com casos permitidos e negados;
3. compare as decisões para amostras representativas;
4. migre tuplas quando a semântica exigir;
5. acompanhe erros de check e latência;
6. mantenha uma versão anterior para rollback.

O formato `.fga.yaml` permite descrever modelos, tuplas e testes. Esses testes devem ser parte do processo de revisão, não apenas uma ferramenta local do desenvolvedor.

## Casos adequados

OpenFGA é apropriado para compartilhamento de documentos, organizações multi-tenant, projetos colaborativos, hierarquias de pastas, repositórios, grupos e permissões que dependem de relações transitivas.

Ele pode ser excessivo para um CRUD simples com três papéis estáticos. Também não substitui OIDC, OAuth 2.0, LDAP ou um serviço de usuários. A identidade do usuário precisa ser resolvida por outra camada e convertida em um identificador estável usado nas tuplas.

## Relação com outras soluções

Casbin e CASL mantêm a decisão dentro do processo. Cedar pode expressar relações, mas a aplicação normalmente precisa fornecer as entidades necessárias ao engine. OpenFGA é especializado em persistir e consultar o grafo de relações. Casdoor administra identidade, SSO e permissões de IAM, mas não deve ser usado automaticamente como grafo de todos os recursos da aplicação.

## Fontes

- [OpenFGA documentation](https://openfga.dev/docs)
- [OpenFGA modeling overview](https://openfga.dev/docs/modeling/overview)
- [OpenFGA interacting with the API](https://openfga.dev/docs/interacting/overview)
- [OpenFGA perform a Check](https://openfga.dev/docs/getting-started/perform-check)
- [OpenFGA model testing](https://openfga.dev/docs/modeling/testing)
- [OpenFGA repository](https://github.com/openfga/openfga)
