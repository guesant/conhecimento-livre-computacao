# Task-Based Access Control

Task-Based Access Control, TBAC, associa autorização ao estado de uma tarefa ou workflow. A permissão não depende somente de quem é o usuário, mas também da atividade que está sendo executada, da etapa atual e das obrigações que precisam ser cumpridas.

## Modelo

Uma tarefa pode ter estado, responsável, participantes, recurso alvo, pré-condições e transições possíveis. A política autoriza operações dentro de uma tarefa ativa, como revisar, aprovar, executar ou encerrar.

Uma pessoa pode ter permissão para aprovar uma despesa em uma tarefa específica sem ter uma permissão geral para aprovar todas as despesas. Depois que a tarefa termina, a autoridade pode deixar de existir.

## Relação com UCON e SoD

TBAC frequentemente precisa de UCON para reavaliar a permissão enquanto a tarefa está ativa. Também pode usar separação de funções para impedir que o criador e o aprovador sejam a mesma pessoa.

RBAC pode determinar quem pode assumir uma etapa, enquanto TBAC determina se a etapa está disponível e se a transição é válida. O sistema precisa impedir que o usuário pule uma transição apenas chamando a API diretamente.

## Vantagens e custos

O modelo representa processos de aprovação e incidentes com mais precisão que papéis estáticos. O custo é manter estado confiável, controlar concorrência, tratar timeouts e definir o que acontece com tarefas abandonadas, duplicadas ou reabertas.

## Segurança

Registre quem iniciou, assumiu, transferiu, aprovou e encerrou cada tarefa. Faça as transições em uma operação transacional e reavalie a autorização no momento da mudança. Não confie apenas no status enviado pelo cliente.

## Casos adequados

Use TBAC para aprovação financeira, change management, resposta a incidentes, revisão de código, onboarding e processos regulados. Para leitura simples de documentos, RBAC, ABAC ou ReBAC normalmente são mais simples.

## Fontes

- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
- [NIST, verification and test methods](https://csrc.nist.gov/pubs/sp/800/192/final)
