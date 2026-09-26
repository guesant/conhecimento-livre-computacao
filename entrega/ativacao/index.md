# Ativação de funcionalidades

Feature flags separam a entrega do código da ativação de um comportamento. Essa separação permite testar, liberar por grupo, desativar uma função problemática e coordenar mudanças entre backend e frontend sem necessariamente fazer um novo deploy.

## Tipos de uso

Uma flag pode controlar rollout, experimento, compatibilidade temporária, migração ou proteção operacional. Cada finalidade exige um dono, uma data de remoção e uma política de segurança. Flags permanentes acumulam caminhos de código e tornam o sistema mais difícil de entender.

## Segurança e operação

Flags que protegem dados, permissões ou pagamentos não podem ser tratadas apenas como preferências de interface. O servidor deve autorizar a operação independentemente do valor vindo do cliente. Mudanças de flag precisam de auditoria, escopo, rollback e observabilidade.

## Relações

[Rollouts](../rollouts/index.md) controla a exposição de uma revisão. [Versionamento](../versionamento-de-releases.md) identifica o artefato. Uma flag pode complementar as duas estratégias, mas não substitui testes, migrações compatíveis e controle de acesso.
