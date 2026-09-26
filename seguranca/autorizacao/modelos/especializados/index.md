# Modelos especializados de autorização

Algumas políticas não são descritas adequadamente por um papel, um atributo ou uma relação isolada. Elas dependem da tarefa atual, da organização que administra o recurso, do histórico de acessos, da separação de funções ou de propriedades formais de confidencialidade e integridade.

Esses modelos são especializados porque introduzem estado, hierarquia, fluxo de informação ou administração mais formal. Em muitos sistemas eles complementam RBAC, ABAC, PBAC ou ReBAC, em vez de substituí-los.

## Tipos documentados

- [Task-Based Access Control](tbac.md), para permissões ligadas a tarefas e workflows;
- [Organization-Based Access Control](orbac.md), para políticas organizacionais e contextos;
- [NGAC](ngac.md), para administração de privilégios em grafos;
- [separação de funções](separation-of-duties.md), para impedir combinações incompatíveis;
- [controle baseado em histórico](history-based.md), para decisões que dependem de eventos anteriores;
- [Chinese Wall](chinese-wall.md), para conflitos de interesse;
- [Bell-LaPadula](bell-lapadula.md), para confidencialidade e fluxo de informação;
- [Biba](biba.md), para integridade e fluxo de dados confiáveis.

## Quando um modelo especializado é necessário

O sinal mais comum é uma regra que não cabe em um check isolado. Exemplos são: "o usuário pode aprovar somente uma solicitação que não criou", "depois de consultar um cliente, não pode consultar o concorrente", "um processo pode ler dados de baixa classificação, mas não escrever em dados de classificação superior" e "o acesso continua permitido somente enquanto a tarefa estiver ativa".

Transformar essas regras em papéis ou flags pode esconder o requisito e criar combinações impossíveis de auditar. O modelo especializado torna a propriedade explícita e indica quais eventos, estados e invariantes precisam ser armazenados.

## Composição

Um serviço pode autenticar com OIDC, usar RBAC para o acesso geral, ABAC para atributos do recurso, ReBAC para compartilhamento e separação de funções para aprovação. A ordem de avaliação deve ser determinística. Em geral, uma negação de uma restrição obrigatória deve prevalecer sobre uma permissão ampla.

Não misture modelos apenas adicionando condições até que a política fique impossível de revisar. Identifique a responsabilidade de cada camada, escreva testes cruzados e registre a versão do modelo que produziu a decisão.

## Fontes

- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
- [NIST, verification and test methods](https://csrc.nist.gov/pubs/sp/800/192/final)
