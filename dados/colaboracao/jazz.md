# Jazz

Jazz é uma plataforma de banco de dados relacional local-first com sincronização em tempo
real, permissões por linha e suporte offline. A aplicação mantém uma réplica local e
assina consultas; leituras e escritas podem ocorrer localmente enquanto a sincronização
continua em segundo plano.

## Modelo relacional local

O modelo do Jazz continua organizado em tabelas, linhas e schema, mas cada réplica mantém
estado e histórico suficientes para sincronizar alterações. Isso difere de uma coleção
JSON colaborativa: o domínio pode usar relações e consultas filtradas, enquanto o runtime
gerencia atualização e propagação.

Uma query subscription define as linhas que o cliente pode ver e acompanhar. Quando uma
linha passa a satisfazer ou deixar de satisfazer a consulta, a réplica deve refletir essa
mudança. Permissão precisa ser aplicada no servidor; filtrar a interface não é controle de
acesso.

## Escritas e durabilidade

Uma escrita comum pode ser aplicada localmente antes de chegar ao servidor. A aplicação
precisa distinguir sucesso local de durabilidade em edge ou no núcleo global quando esse
estado for relevante. O usuário pode continuar trabalhando offline, mas a confirmação de
uma regra que depende da autoridade remota pode ficar pendente.

Transações agrupam alterações. Uma transação mergeable pode seguir as regras normais de
convergência. Uma transação exclusiva é adequada quando uma autoridade precisa validar uma
invariante como unidade, o que pode exigir conectividade.

## Conflitos

Quando duas escritas alteram o mesmo campo, Jazz usa uma política determinística de
last-writer-wins baseada em relógio lógico híbrido. Alterações em campos diferentes podem
ser preservadas simultaneamente.

LWW resolve qual valor fica visível, mas não entende o significado do domínio. Se duas
edições representam decisões incompatíveis, a aplicação precisa modelar uma operação
exclusiva, revisão humana, evento de conflito ou validação no servidor.

## Sincronização

O modelo pode possuir camadas local, edge e global. As camadas podem discordar
temporariamente enquanto updates sobem e descem. O sistema precisa controlar query
subscriptions, replay, reconexão, retenção e mudanças de schema.

Essa arquitetura reduz dependência de request-response para cada leitura, mas introduz
questões de cache local, revogação, migração e suporte. Dados presentes offline podem estar
antigos ou deixar de ser autorizados antes da próxima sincronização.

## Autenticação e permissões

Uma aplicação local-first precisa proteger o dispositivo e a identidade local. O fato de
uma escrita ser aceita na réplica não deve permitir que o cliente ultrapasse a policy do
servidor. Credenciais locais, recovery secrets, cookies e tokens devem ter ciclo de vida
separado da persistência do dado.

Revogação exige um comportamento explícito quando o dispositivo está offline. O produto
pode impedir operações sensíveis sem confirmação remota, limitar escopo local ou marcar a
operação para rejeição posterior.

## Quando usar

Jazz é interessante quando o domínio é relacional, a interface precisa de leitura local
imediata, há sincronização contínua e o produto aceita convergência eventual. Ele deve ser
comparado com SQLite mais sync própria, PouchDB/CouchDB, Yjs, Loro e uma API tradicional.

## Fontes primárias

- [Jazz overview](https://jazz.tools/docs)
- [Jazz local-first data model](https://jazz.tools/docs/concepts/local-first-data-model)
- [Jazz how sync works](https://jazz.tools/docs/concepts/how-sync-works)
- [Jazz transactions](https://jazz.tools/docs/writing/transactions)
- [Jazz permissions](https://jazz.tools/docs/auth/permissions)
