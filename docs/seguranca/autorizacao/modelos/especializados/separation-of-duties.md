# Separação de funções

Separação de funções, Separation of Duties, SoD, impede que uma única pessoa acumule funções incompatíveis em uma mesma operação. O objetivo é reduzir fraude, erro e abuso de privilégio, exigindo que etapas críticas sejam executadas por identidades diferentes ou em contextos distintos.

## Separação estática

Static Separation of Duties impede que um usuário receba simultaneamente papéis incompatíveis. Um exemplo é proibir que a mesma conta tenha os papéis `payment.requester` e `payment.approver`.

Essa regra é simples de auditar, mas pode ser rígida demais para organizações pequenas. A atribuição e a revogação precisam ser transacionais para que uma janela intermediária não deixe o usuário com os dois papéis.

## Separação dinâmica

Dynamic Separation of Duties permite que um usuário tenha mais de um papel, mas impede ativá-los simultaneamente na mesma sessão ou tarefa. Isso é útil quando uma pessoa trabalha em funções diferentes em momentos distintos.

A aplicação precisa modelar sessão, contexto ou workflow. Apenas esconder o segundo botão não aplica separação dinâmica.

## Relação com RBAC e TBAC

SoD é frequentemente uma restrição de RBAC. TBAC pode aplicar a separação durante uma tarefa de aprovação. ABAC pode verificar que `requester_id != approver_id`, mas uma expressão isolada não substitui uma política completa quando a incompatibilidade depende do histórico ou da organização.

## Segurança e auditoria

Proteja operações de atribuição de papéis, registre mudanças e gere relatórios de conflitos. Teste criação, transferência, delegação, contas de serviço, break glass e recuperação de acesso.

## Fontes

- [NIST RBAC FAQs](https://csrc.nist.gov/Projects/Role-Based-Access-Control/faqs)
- [Apache Casbin, constraints](https://casbin.apache.org/docs/syntax-for-models/)
