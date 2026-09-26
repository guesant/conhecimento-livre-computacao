# Relationship-Based Access Control

Relationship-Based Access Control, ReBAC, decide acesso a partir das relações entre entidades. O principal pode ser membro de uma organização, a organização pode ser administradora de um projeto e o projeto pode conter um documento. A autorização resulta da existência de um caminho permitido no grafo.

## Modelo

As entidades têm tipos e identificadores. As relações possuem nomes de negócio, como `owner`, `member`, `viewer`, `editor` ou `parent`. Uma política define quais relações concedem uma capacidade e como relações indiretas são derivadas.

O modelo separa a estrutura do grafo dos fatos concretos. Isso permite que a mesma regra seja usada para muitos projetos e documentos sem criar um papel novo para cada combinação.

## Tuplas e relações derivadas

Uma tupla registra um fato como `user:ana member organization:acme`. O modelo pode derivar que membros da organização são viewers dos documentos pertencentes à organização. A relação derivada precisa ser explícita para que a equipe consiga responder por que uma decisão foi permitida.

Relações podem ser diretas, herdadas, condicionais ou transitivas. Grupos aninhados e hierarquias de pastas exigem limites de profundidade, tratamento de ciclos e testes de cardinalidade. Uma relação pública deve ser uma escolha do modelo, não um efeito acidental de uma tupla vazia.

## Exemplos

ReBAC é natural para:

- usuários pertencentes a organizações;
- grupos aninhados;
- documentos compartilhados;
- pastas e herança de acesso;
- projetos com colaboradores;
- repositórios e equipes;
- contas com delegação temporária.

Uma relação precisa ter limites. `member` de uma organização não deve conceder automaticamente administração em todos os recursos, a menos que o modelo defina essa herança de forma explícita.

## Vantagens

ReBAC evita role explosion e representa colaboração com mais clareza que uma tabela de papéis globais. Ele permite responder tanto se um usuário pode acessar um objeto quanto quais objetos estão disponíveis para aquele usuário.

## Escrita e leitura

Escrever uma relação também é uma operação autorizada. O usuário pode ser viewer de um documento, mas isso não significa que pode adicionar outro viewer. Separe `can_view`, `can_share` e `can_delete`, mesmo quando todos forem derivados do mesmo caminho.

Para listar recursos, prefira uma consulta relacional especializada, uma operação de `ListObjects` ou uma projeção materializada. O resultado da lista deve ser limitado, paginado e consistente com o modelo usado pelo check individual.

## Custos

Consultas podem atravessar muitos níveis e depender de consistência entre escritas. Ciclos, relações públicas, grupos aninhados e explosão de cardinalidade precisam de limites. A aplicação deve monitorar profundidade, latência, cache e comportamento em caso de falha do serviço de relações.

Uma mudança de relação pode afetar muitos objetos sem modificar nenhum registro desses objetos. Por isso, invalidar caches e índices autorizados é parte da operação de escrita. A janela de consistência precisa ser conhecida por cada consumidor.

Não faça uma consulta de autorização para cada item de uma lista sem medir o padrão N+1. Use uma operação de listagem autorizada, uma projeção de relações ou uma consulta no banco que preserve a semântica do modelo.

## OpenFGA

OpenFGA é uma implementação de serviço orientada a ReBAC. Ele fornece modelos, tuplas e operações como Check e ListObjects. A página [OpenFGA](../openfga.md) detalha consistência, modelos, testes e operação do serviço.

Casbin também pode representar relações por grouping policies e matchers, mas isso não significa que tenha o mesmo comportamento operacional de um grafo especializado. Escolha o mecanismo conforme a escala, profundidade e necessidade de consulta.

## Segurança

Use identificadores estáveis, valide o tenant, proteja escritas de tuplas e audite quem criou ou removeu relações. A revogação deve alcançar caminhos indiretos. Teste especialmente remoção de membro, remoção de grupo, transferência de propriedade e relações públicas.

## Consistência e indisponibilidade

Defina se uma decisão pode usar um modelo antigo ou uma leitura eventualmente consistente. Para uma operação destrutiva, a aplicação pode exigir uma leitura mais forte ou uma confirmação no serviço de relações. Nunca transforme timeout em permissão.

## Fontes

- [OpenFGA, modeling overview](https://openfga.dev/docs/modeling/overview)
- [OpenFGA, concepts](https://openfga.dev/docs/concepts)
- [Google Zanzibar paper](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/10683a8982ed8f20d25f61c5b2c8f3a9e4e8e0e0.pdf)
