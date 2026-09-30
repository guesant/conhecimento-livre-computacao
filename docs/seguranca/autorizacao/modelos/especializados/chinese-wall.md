# Chinese Wall

Chinese Wall é um modelo de autorização para conflitos de interesse. O acesso permitido depende do histórico do principal: depois que ele acessa dados de uma empresa ou classe de interesse, o sistema restringe o acesso a dados de empresas concorrentes dentro do mesmo conflito.

## Exemplo

Um consultor pode atender clientes de diferentes setores, mas depois de acessar os dados da Empresa A não deve acessar dados de uma concorrente direta da Empresa A. Ele ainda pode acessar outra classe sem conflito, conforme a política.

## Estado necessário

O sistema precisa registrar a classe de interesse acessada pelo principal e usar esse estado na próxima decisão. Uma permissão stateless baseada apenas em papel não implementa Chinese Wall.

O histórico deve ser associado à identidade correta, ter escopo e retenção definidos e considerar sessões, dispositivos e identidades delegadas. Se o controle vale para a organização, não registre apenas o navegador do usuário.

## Características

O modelo é deliberadamente restritivo e pode impedir uma tarefa legítima depois de um acesso inicial. Antes de implementá-lo, defina se o acesso de leitura, exportação, metadados e dados anonimizados contam da mesma maneira.

## Operação

Audite o primeiro acesso que estabelece a barreira, explique a negação e crie um procedimento de exceção aprovado. A exceção deve ser registrada e não pode simplesmente apagar o histórico para liberar a operação.

## Relação com outros modelos

Chinese Wall complementa RBAC ou ABAC. RBAC pode dizer que o consultor tem uma função; Chinese Wall decide quais classes ele pode acessar depois do histórico. Controle baseado em histórico é a categoria mais geral.

## Fontes

- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
