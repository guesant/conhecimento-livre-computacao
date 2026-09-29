# Manutenção corretiva

Manutenção corretiva é o trabalho realizado depois que um defeito, falha ou degradação foi identificada. Ela pode restaurar o serviço, reparar um componente, corrigir dados, reverter uma versão ou substituir uma implementação. Em sistemas digitais, geralmente começa como resposta a incidente e termina com uma mudança permanente, um teste de regressão e uma revisão da causa.

## Correção emergencial

Quando o impacto está ocorrendo, a prioridade é limitar dano e restaurar o comportamento essencial. A ação pode ser rollback, desabilitação de feature, failover, aumento temporário de capacidade, bloqueio de tráfego, restauração de backup ou correção de configuração. A mudança deve ser pequena, observável e reversível sempre que possível.

Uma correção emergencial não deve aproveitar a janela para refatorações não relacionadas. Misturar mitigação com limpeza estrutural amplia o risco e dificulta entender o resultado. Depois que o serviço estabilizar, registre o que foi alterado e preserve evidências suficientes para investigar.

## Correção definitiva

A correção definitiva remove ou reduz a causa que permitiu a falha. Ela pode exigir alteração de código, schema, arquitetura, política, processo, monitoramento ou documentação. O trabalho deve responder por que o defeito passou pelos controles existentes e qual controle será adicionado ou ajustado.

Um teste de regressão é parte da correção. O teste deve reproduzir a condição relevante e falhar sem a mudança. Em um erro de carregamento de página, pode ser um smoke test de rota. Em um erro de formulário, pode ser um teste de montagem e de ação reativa. Em uma inconsistência de dados, pode ser uma constraint, uma transação ou um teste de idempotência.

## Dados e recuperação

Falhas de banco, fila ou storage podem deixar efeitos parciais. A manutenção corretiva precisa verificar registros incompletos, duplicados, eventos não publicados, jobs presos, cache desatualizado e relações quebradas. O plano deve definir se os dados serão corrigidos, reprocessados, restaurados ou preservados para investigação.

Correção de dados em produção precisa de backup, consulta de validação, limite de escopo, transação quando possível e plano de rollback. Um script que corrige a aplicação, mas não verifica o resultado, pode trocar uma falha visível por uma inconsistência silenciosa.

## Encerramento

O trabalho não termina quando o alerta desaparece. É preciso verificar métricas, logs, traces, filas, usuários afetados e dependências. Depois, faça o postmortem quando o impacto justificar, transforme a causa em teste ou controle e acompanhe as ações pendentes.

Manutenção corretiva é inevitável em sistemas complexos, mas sua recorrência pode diminuir quando os aprendizados alimentam [qualidade preventiva](../qualidade/preventiva.md) e [qualidade preditiva](../qualidade/preditiva.md). O objetivo não é eliminar toda correção emergencial. É tornar a correção segura, rápida, reversível e cada vez menos repetitiva.
