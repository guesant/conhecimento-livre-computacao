# Qualidade preventiva

Qualidade preventiva é o conjunto de controles criado para evitar falhas conhecidas antes que elas aconteçam. Ela faz parte da qualidade proativa, mas tem foco mais específico: existe um modo de falha identificado e um controle é introduzido para reduzir sua probabilidade ou seu impacto. A distinção permite ligar cada controle a um risco concreto, acompanhar sua eficácia e revisar a decisão quando o sistema mudar.

Um exemplo é a ausência da tabela usada por um formulário administrativo. Depois que esse risco é conhecido, a prevenção pode incluir migration versionada, execução das migrations em uma base vazia no CI, verificação do status no deploy e smoke test da página. O controle não garante que toda falha desapareça, mas impede que a mesma dependência fique invisível.

## Identificação de falhas conhecidas

Controles preventivos normalmente nascem de incidentes, auditorias, análise de ameaças, requisitos regulatórios, testes de carga ou experiência operacional. Para cada risco, registre:

- evento que pode ocorrer;
- causa provável;
- efeito no usuário, no dado ou na operação;
- probabilidade e severidade;
- controle preventivo;
- forma de verificar que o controle está ativo;
- owner e periodicidade de revisão.

FMEA, checklists de lançamento, threat modeling e revisão de mudanças ajudam a produzir esse inventário. O objetivo não é listar todos os eventos imagináveis, mas tornar explícitas as falhas plausíveis e custosas.

## Tipos de controle

Na entrada, controles preventivos validam schema, tamanho, formato, autorização e limites. No processamento, impõem idempotência, timeout, concorrência máxima e transações. Na persistência, usam constraints, chaves únicas, foreign keys, índices e políticas de retenção. Na infraestrutura, aplicam RBAC, NetworkPolicy, security context, probes, limites de CPU e memória. No delivery, usam gates, imagens fixadas, revisão de dependências e rollout gradual.

Controles preventivos podem ser:

- bloqueantes, quando a operação não deve seguir sem a condição;
- orientativos, quando exibem risco mas permitem uma decisão consciente;
- compensatórios, quando o controle ideal não é possível e outra barreira reduz o impacto;
- detectivos, quando não impedem a ação mas identificam a violação rapidamente.

Uma boa arquitetura combina controles independentes. Se uma única validação de frontend protege um campo sensível, uma requisição manual pode contorná-la. A mesma regra precisa existir na fronteira correta do backend e, quando necessário, no banco.

## Prevenção sem excesso

Prevenção pode se transformar em burocracia se cada risco gerar um gate pesado. O controle deve ser proporcional. Uma migration destrutiva em uma tabela pequena pode exigir revisão e backup; a mesma operação em uma tabela de grande volume exige ensaio, medição de locks, estratégia online e rollback. A equipe deve remover controles que não reduzem mais o risco ou que criam uma falsa sensação de segurança.

Também é importante medir exceções. Se uma regra é ignorada frequentemente, isso pode indicar que o controle está incorreto, que o requisito mudou ou que o fluxo legítimo não foi modelado. Exceções permanentes devem virar uma decisão arquitetural explícita, não uma coleção de bypasses.

## Verificação

Todo controle preventivo precisa de evidência. Um backup configurado sem restauração testada não prova recuperabilidade. Um scanner instalado sem gate ou triagem não prova segurança. Uma policy escrita sem teste de admissão não prova que o cluster a aplica. A prevenção deve ser exercitada no CI, em ambientes efêmeros e em exercícios operacionais quando o risco exigir.

Qualidade preventiva reduz falhas recorrentes, mas não substitui qualidade reativa. Controles podem estar desatualizados, ser contornados ou falhar por uma combinação nova de condições. Os incidentes devem alimentar o inventário preventivo e indicar quais barreiras precisam ser fortalecidas.
