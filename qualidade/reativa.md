# Qualidade reativa

Qualidade reativa é a disciplina de detectar, compreender e corrigir problemas depois que um sinal de falha apareceu. O sinal pode ser um bug relatado, um alerta, um aumento de erro, uma degradação de performance, uma falha de segurança, uma inconsistência de dados ou um incidente de disponibilidade. Ela é chamada de reativa porque o trabalho começa em resposta a um evento observado, mas não precisa ser improvisado. Processos reativos maduros são preparados antecipadamente e transformam falhas em aprendizado verificável.

A resposta reativa tem duas responsabilidades diferentes. A primeira é reduzir o impacto atual. A segunda é impedir que o mesmo mecanismo volte a causar o problema. Confundir essas responsabilidades leva a correções temporárias que encerram o alerta, mas deixam a causa intacta.

## Ciclo de resposta

O fluxo começa com detecção e triagem. A equipe precisa determinar se há um defeito isolado, uma degradação, uma violação de segurança ou um incidente amplo. A classificação deve considerar usuários afetados, dados envolvidos, duração, alcance, reversibilidade e dependências. Um erro de tela pode ser apenas um defeito de apresentação, mas também pode indicar que uma migration não foi aplicada ou que um contrato mudou de forma incompatível.

Depois da triagem, a prioridade é contenção. Exemplos incluem desabilitar uma feature flag, interromper um rollout, reduzir concorrência, bloquear uma entrada abusiva, retirar uma versão do tráfego, restaurar um backup ou aplicar um limite temporário. Contenção não deve ser confundida com correção definitiva. A ação precisa ser registrada, ter owner e possuir uma condição explícita para remoção.

A investigação reúne logs estruturados, métricas, traces, eventos de deploy, mudanças de configuração, consultas, filas, auditoria e relatos de usuários. Correlation ID ajuda a reconstruir uma requisição, mas não substitui o contexto de versão, tenant, região, job e dependência. O diagnóstico deve distinguir causa, mecanismo de propagação e condição que permitiu a falha.

## Correção e regressão

A correção reativa deve ser acompanhada de um teste que falharia antes dela. Esse teste pode ser unitário, de integração, contrato, autorização, migration, smoke test ou navegador. O tipo depende do ponto em que o defeito ocorreu. Se uma tela protegida devolveu 500 por tabela ausente, o caso precisa incluir a migration e a montagem da tela. Se uma requisição reativa falhou ao salvar, o teste precisa chamar a ação, não somente abrir o GET.

Depois da correção, é necessário verificar se o incidente deixou efeitos persistentes. Isso inclui dados parciais, mensagens duplicadas, jobs pendentes, cache incorreto, tokens revogados, recursos órfãos e alterações de schema. A validação deve ocorrer no ambiente em que o problema apareceu ou em um ambiente que reproduza suas condições.

## Postmortem

Um postmortem útil descreve o que ocorreu, a linha do tempo, o impacto, os sinais disponíveis, o que atrasou a detecção, as decisões tomadas, as causas contribuintes e as ações de acompanhamento. Ele não deve procurar um culpado individual. Sistemas falham por combinação de código, processos, permissões, observabilidade, dependências, pressão de tempo e pressupostos incorretos.

As ações precisam ser concretas. "Ter mais cuidado" não é uma ação verificável. Exemplos melhores são criar smoke test para todas as rotas protegidas, adicionar alerta para expiração de certificado, validar o schema no CI, limitar o tamanho da fila ou exigir rollback testado antes da promoção. Cada ação deve ter owner, prioridade, prazo e teste de conclusão.

## Métricas reativas

As métricas de resposta ajudam a revelar a capacidade do processo:

- MTTD, tempo médio até detectar;
- MTTA, tempo médio até reconhecer e iniciar resposta;
- MTTR, tempo médio até restaurar o serviço;
- tempo até mitigar;
- reincidência por causa ou componente;
- quantidade de falsos positivos;
- percentual de ações de postmortem concluídas;
- percentual de incidentes com teste de regressão.

Uma redução de MTTR é positiva, mas não deve esconder aumento de recorrência. Encerrar alertas rapidamente sem remover causas pode melhorar a métrica local enquanto piora a confiabilidade real.

## Relação com outras abordagens

Qualidade reativa fornece sinais e aprendizado para o trabalho proativo. Um incidente deve atualizar requisitos, testes, alertas, runbooks ou arquitetura quando revelar uma lacuna. A qualidade preventiva aplica controles para riscos já conhecidos. A qualidade preditiva usa sinais para antecipar condições de falha. As três se reforçam, mas nenhuma substitui as outras.
