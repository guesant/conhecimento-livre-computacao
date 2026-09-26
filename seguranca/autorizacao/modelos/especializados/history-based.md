# Controle baseado em histórico

Controle baseado em histórico decide o acesso usando eventos anteriores. O sistema considera o que o principal acessou, aprovou, alterou ou tentou fazer antes de autorizar a operação atual.

## Modelo

O histórico pode ser uma sequência de eventos, um conjunto de recursos já visitados, um contador ou um estado derivado. Uma política pode impedir que um usuário acesse um segundo cliente depois de consultar o primeiro, ou pode exigir que uma etapa de revisão tenha ocorrido antes da publicação.

Essa autorização é diferente de ABAC simples. Um atributo como `approved=true` pode representar um resumo do histórico, mas a aplicação precisa garantir como o atributo é produzido, atualizado e invalidado.

## Vantagens e custos

O modelo expressa conflitos de interesse, progressão de workflow e limites de uso que não podem ser calculados apenas com identidade e recurso atuais. Em troca, exige armazenamento consistente de eventos ou estados derivados, ordenação, concorrência e retenção.

Se eventos atrasados, duplicados ou removidos alterarem a decisão, defina uma política de correção. Uma autorização baseada em histórico não pode depender de logs que são apenas observabilidade e podem sofrer retenção diferente.

## Casos adequados

Use para workflows, auditoria de ações, limites de acesso, prevenção de conflito e políticas que exigem uma sequência. Para uma permissão estática de leitura, RBAC ou ACL é mais simples.

## Segurança

Proteja a integridade do histórico, registre a versão do estado usada na decisão e teste replay, concorrência e recuperação. A operação que altera o histórico e a operação protegida devem usar uma transação ou uma estratégia de consistência explicitamente documentada.

## Relação com Chinese Wall

Chinese Wall é uma aplicação específica de controle baseado em histórico: depois que um principal acessa dados de uma classe de interesse, o sistema restringe acesso a classes conflitantes.

## Fontes

- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
- [NIST, verification and test methods](https://csrc.nist.gov/pubs/sp/800/192/final)
