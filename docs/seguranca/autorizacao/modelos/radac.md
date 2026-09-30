# Risk-Adaptive Access Control

Risk-Adaptive Access Control, RAdAC, usa uma estimativa de risco para ajustar a decisão de acesso. O sistema pode permitir uma ação de baixo risco, exigir autenticação adicional para uma ação sensível ou negar quando o risco supera o limite definido.

## Sinais de risco

O risco pode considerar:

- nível de autenticação e presença de MFA;
- dispositivo e postura de segurança;
- localização e rede;
- horário e padrão de comportamento;
- sensibilidade do recurso;
- histórico recente de falhas;
- estado da conta e da sessão;
- indicadores de comprometimento.

Os sinais precisam ter origem confiável, retenção definida e explicação suficiente para auditoria. Um score opaco não deve ser a única justificativa para bloquear uma pessoa em uma operação crítica.

## Decisão adaptativa

RAdAC normalmente não substitui RBAC ou ABAC. Ele os complementa. Uma política pode exigir que a identidade tenha o papel `editor`, que o recurso pertença ao tenant e que o risco atual esteja abaixo do limite. Se o risco for intermediário, a política pode exigir step-up authentication.

Os limiares precisam ser calibrados para evitar tanto acesso inseguro quanto bloqueios excessivos. Mudanças de score não podem criar uma autorização implícita durante uma falha do sistema de risco.

## Step-up e redução de privilégio

Uma resposta adaptativa não precisa ser apenas permitir ou negar. Ela pode exigir MFA, restringir a operação a leitura, reduzir o escopo do recurso ou encaminhar a uma aprovação humana. Essas respostas devem ser modeladas como estados verificáveis, não como mensagens exibidas no frontend.

O step-up deve produzir uma evidência que o PEP consiga validar, como um `acr` ou `amr` apropriado no contexto da sessão. Não aceite um parâmetro do cliente dizendo que a autenticação adicional ocorreu.

## Privacidade e segurança

Dados comportamentais e de localização podem ser sensíveis. Colete apenas o necessário, explique a finalidade, limite retenção e proteja o acesso ao pipeline de risco. Um atacante que controla os sinais pode manipular a decisão, então os atributos precisam ser atestados ou obtidos de fontes protegidas.

## Operação

Registre decisão, fatores relevantes, versão do modelo de risco e ação tomada. Separe logs de auditoria de dados brutos. Teste cenários de serviço de risco indisponível, score atrasado, relógio incorreto, dispositivo novo e alteração repentina de localização.

## Modelos e calibração

O score não é a política. Um modelo de risco pode fornecer sinais, mas a policy define quais ações são permitidas em cada faixa e quais evidências são exigidas. Valide falsos positivos, falsos negativos, deriva de comportamento e impacto por grupo de usuários.

## Casos adequados

RAdAC é útil para acesso administrativo, transações financeiras, dados de alta sensibilidade e ambientes em que o contexto muda rapidamente. Para um CRUD simples com papéis estáveis, ele adiciona complexidade sem ganho proporcional.

## Fontes

- [NIST, ABAC project](https://csrc.nist.gov/projects/attribute-based-access-control)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
- [NIST glossary, risk-adaptive access control](https://csrc.nist.gov/glossary/term/risk_adaptive_access_control)
