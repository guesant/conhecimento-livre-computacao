# Discretionary Access Control

Discretionary Access Control, DAC, permite que o proprietário de um objeto, ou outro sujeito explicitamente autorizado a administrar seu acesso, conceda ou remova privilégios. A decisão não fica totalmente concentrada em uma política central; a autoridade é delegável dentro dos limites do sistema.

## Exemplo

Permissões tradicionais de arquivos Unix combinam proprietário, grupo e outros. POSIX ACL amplia esse modelo com entradas para usuários e grupos específicos. O proprietário pode alterar permissões quando possui a autoridade correspondente.

Essa flexibilidade torna DAC útil em colaboração, mas também permite que uma pessoa compartilhe um recurso de forma mais ampla que a política organizacional pretendia.

## Propriedades

O modelo costuma ser associado a:

- identificação do sujeito ou grupo;
- proprietário do objeto;
- direitos sobre o objeto;
- capacidade de delegar ou alterar direitos;
- herança opcional em hierarquias de objetos.

O fato de uma aplicação usar tabelas `owner_id` e `shared_with` não prova que seu modelo seja um DAC completo. A classificação depende de quem pode alterar essas associações e das regras que limitam a delegação.

## Riscos

O risco clássico é a propagação indevida. Um usuário autorizado pode conceder acesso a outro usuário, copiar o conteúdo para um lugar menos protegido ou alterar permissões de uma subárvore. Revogação também pode ser incompleta quando cópias, caches e links compartilhados sobrevivem à remoção.

Para reduzir risco, limite o poder de compartilhamento, registre alterações, valide destinatários, imponha escopo de tenant e use políticas de classificação ou restrições centrais quando necessário. DAC e least privilege exigem revisar tanto o acesso ao objeto quanto o poder de conceder acesso.

## Delegação

Delegação pode ser total, limitada por ação, limitada por recurso ou limitada por tempo. Uma aplicação segura não permite que um usuário conceda mais direitos do que possui. Também deve distinguir conceder leitura de conceder a capacidade de compartilhar novamente.

Quando a delegação atravessa organizações, exija consentimento, expiração e registro da cadeia de concessões. Uma tabela `shared_with` sem essas regras pode se comportar como uma capability permanente e difícil de revogar.

## DAC em sistemas de arquivos

Em Unix, modo, proprietário, grupo e ACL POSIX são avaliados pelo kernel segundo regras próprias. O proprietário, capabilities e mecanismos MAC podem alterar o resultado prático. Em storage de objetos, ACLs podem coexistir com policies de bucket e identidade do serviço.

Ao documentar DAC, declare a camada: filesystem, banco, objeto, aplicação ou serviço. Uma permissão chamada `owner` em uma API não tem automaticamente a mesma semântica do proprietário do sistema operacional.

## DAC em relação a outros modelos

RBAC administra permissões por papéis e normalmente reduz concessões individuais. MAC impede que o proprietário relaxe certas regras centrais. ABAC pode expressar a regra de que apenas o proprietário pode compartilhar, ou de que o compartilhamento é permitido apenas dentro da organização.

DAC pode ser combinado com esses modelos. A aplicação deve documentar a precedência quando uma ACL permite e uma política central nega.

## Fontes

- [NIST, DAC glossary](https://csrc.nist.gov/glossary/term/discretionary_access_control)
- [NIST, access control methodologies](https://csrc.nist.gov/CSRC/media/Publications/white-paper/2010/12/01/economic-analysis-of-rbac-final-report/final/documents/20101219_RBAC2_Final_Report.pdf)
