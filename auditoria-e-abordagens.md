# Auditoria e abordagens de auditoria

Auditoria é um processo sistemático para obter e avaliar evidências diante de critérios definidos. O resultado não é apenas uma lista de falhas. Uma auditoria deve permitir concluir algo sobre um escopo, uma afirmação ou um conjunto de controles, explicando quais evidências foram examinadas, quais limitações existiram e qual ação precisa acontecer depois.

Auditoria, monitoramento, teste e inspeção são relacionados, mas não são sinônimos. Um teste pode verificar uma propriedade de uma versão do software. Monitoramento acompanha um sinal ao longo do tempo. Auditoria avalia evidências contra critérios e comunica uma conclusão com responsabilidade e rastreabilidade. Um scanner pode gerar evidência para uma auditoria, mas não substitui o planejamento, o julgamento e a independência necessários para avaliar o resultado.

## O que é um sistema de auditoria

A expressão sistema de auditoria possui mais de um significado. Antes de escolher uma ferramenta, separe as camadas que precisam existir.

### Sistema de governança e assurance

É a distribuição de responsabilidades entre quem executa, quem supervisiona riscos e controles, quem fornece assurance independente e quem exerce supervisão. O [Three Lines Model do IIA](https://www.theiia.org/en/resources/statements-of-position) é uma referência para essa organização.

- O órgão de governança supervisiona objetivos, riscos, prestação de contas e assurance.
- A primeira linha administra operações, entrega produtos e serviços e mantém controles no trabalho cotidiano.
- A segunda linha fornece conhecimento, políticas, monitoramento, challenge e suporte sobre riscos e conformidade.
- A terceira linha, normalmente auditoria interna, fornece assurance e aconselhamento independentes e objetivos.
- Auditores externos, reguladores e certificadoras fornecem assurance externa dentro de escopos definidos.

As linhas não são departamentos obrigatórios nem uma sequência de etapas. Uma organização pequena pode acumular funções, desde que registre conflitos de interesse e preserve objetividade quando uma pessoa avaliar um controle que ela mesma desenhou ou executou.

### Sistema de gestão da auditoria

É o conjunto de políticas, critérios, competências, plano, procedimentos, registros e mecanismos de melhoria que permite executar auditorias repetidamente. A [ISO 19011:2026](https://www.iso.org/standard/19011) fornece diretrizes para princípios de auditoria, gestão de programas, condução de auditorias e competência de pessoas envolvidas.

Um sistema de gestão deve responder:

- qual é o objetivo e o escopo da auditoria;
- qual critério será usado;
- quais riscos e processos justificam a prioridade;
- quem pode auditar e quem deve permanecer independente;
- quais evidências serão aceitas;
- como divergências serão validadas;
- como findings, ações corretivas e exceções serão acompanhados;
- como a eficácia das ações será verificada;
- como o programa aprende com resultados anteriores.

### Sistema de controles e evidências

É a ligação entre riscos, requisitos, controles, procedimentos e evidências. Um controle não é somente uma frase na política. Ele deve ter objetivo, frequência, responsável, população afetada, mecanismo, exceções e resultado esperado.

Uma matriz mínima pode representar:

| Elemento | Pergunta |
| --- | --- |
| Risco | O que pode acontecer e qual seria a consequência? |
| Requisito | Qual obrigação, objetivo ou regra precisa ser atendida? |
| Controle | Qual atividade reduz a probabilidade ou o impacto? |
| Procedimento | Como a atividade é executada e registrada? |
| Evidência | O que demonstra execução, período, escopo e resultado? |
| Responsável | Quem executa, revisa, aprova e corrige? |
| Exceção | O que acontece quando o controle não pode operar normalmente? |
| Teste | Como será avaliado desenho e funcionamento? |
| Ação | Qual correção terá dono, prazo e critério de encerramento? |

### Sistema de informação de auditoria

É a ferramenta ou plataforma usada para planejar auditorias, manter o catálogo de controles, coletar evidências, controlar acessos, registrar entrevistas, emitir findings, acompanhar ações e preservar o histórico. Esse sistema pode ser uma combinação de repositório versionado, gerenciador de chamados, armazenamento de documentos, banco de dados, pipeline e dashboards.

Plataformas GRC comerciais costumam integrar riscos, controles, auditorias, fornecedores, políticas e evidências. Há também alternativas self-hosted, como [eramba](https://www.eramba.org/), e implementações internas. O produto não cria independência nem qualidade de evidência. Uma plataforma que permite marcar controles como concluídos sem vincular uma evidência verificável apenas automatiza uma falsa sensação de conformidade.

## Tipos de auditoria

### Pela relação entre as partes

- Auditoria de primeira parte é conduzida pela própria organização, incluindo auditoria interna ou autoavaliação controlada.
- Auditoria de segunda parte é conduzida por uma parte interessada sobre um fornecedor, parceiro ou serviço contratado.
- Auditoria de terceira parte é conduzida por uma entidade independente, como certificadora, auditor externo ou avaliador autorizado.

Essa classificação não é uma classificação de profundidade. Uma autoavaliação pode ser tecnicamente rigorosa e uma auditoria externa pode ser limitada por escopo, amostragem ou evidência disponível.

### Pela finalidade

- Auditoria de conformidade compara práticas e evidências com lei, contrato, política, norma ou requisito.
- Auditoria financeira avalia demonstrações, transações, controles financeiros e afirmações contábeis.
- Auditoria operacional avalia eficiência, eficácia, economia, controles e capacidade de atingir objetivos.
- Auditoria de tecnologia avalia sistemas, processos de TI, acesso, mudanças, operação, continuidade e controles gerais.
- Auditoria de segurança avalia ameaças, controles preventivos e detectivos, configuração, vulnerabilidades e resposta.
- Auditoria de privacidade avalia coleta, finalidade, acesso, retenção, compartilhamento, direitos e incidentes relacionados a dados pessoais.
- Auditoria de produto avalia se o produto atende requisitos funcionais e de qualidade definidos.
- Auditoria de processo avalia se uma atividade é executada conforme o processo e se o processo produz o resultado esperado.
- Auditoria de fornecedor avalia capacidade, controles, subcontratados, evidências e riscos de uma cadeia de fornecimento.
- Auditoria de desempenho avalia resultados, capacidade, custo, latência, disponibilidade, produtividade ou outros indicadores definidos.

Uma auditoria pode combinar essas finalidades, mas o plano precisa indicar qual conclusão cada procedimento pretende sustentar. Segurança, privacidade, disponibilidade e custo não devem ser misturados em uma pontuação única sem explicar a perda de informação.

## Abordagens de auditoria

### Abordagem baseada em risco

A auditoria começa pelos riscos e objetivos com maior impacto, incerteza ou exposição. O plano considera criticidade do serviço, dados, mudanças recentes, incidentes, dependências, histórico de findings, concentração de privilégio, terceirização e requisitos externos.

Essa abordagem ajuda a concentrar recursos, mas não significa ignorar controles básicos. Risco baixo precisa de uma justificativa proporcional, e não de ausência completa de evidência. O risco deve ser revisado quando o sistema, o contexto ou o impacto mudar.

### Abordagem baseada em controles

O auditor parte de um catálogo de controles e verifica desenho, implementação e operação. Ela funciona bem quando existe uma norma ou contrato com controles explícitos, mas pode produzir conformidade superficial se os controles não forem relacionados aos riscos que deveriam tratar.

Para cada controle, pergunte se ele foi bem desenhado, se está implementado no escopo certo, se operou no período e se foi eficaz. Um controle de backup pode existir e rodar diariamente, mas continuar ineficaz se os backups não puderem ser restaurados.

### Abordagem baseada em processos

O auditor acompanha um fluxo de ponta a ponta, como criação de usuário, mudança em produção, atendimento de incidente ou publicação de artefato. A abordagem revela handoffs, controles duplicados, lacunas, dependências manuais e divergências entre o procedimento escrito e o trabalho real.

Ela é útil quando o risco aparece na interação entre equipes. Também evita revisar cada controle isoladamente sem perceber que uma entrada não tem dono ou que a saída não é validada pelo próximo processo.

### Abordagem baseada em requisitos

O escopo é construído a partir de uma fonte normativa, legal, contratual ou técnica. Cada requisito deve ser interpretado no contexto e ligado a um controle e a uma evidência.

Não transforme uma referência normativa em uma transcrição automática. O auditor precisa registrar aplicabilidade, interpretação, escopo, exceção e justificativa. Uma norma pode ser uma diretriz não certificável, uma obrigação de sistema de gestão ou um requisito legal, e essas situações exigem conclusões diferentes.

### Abordagem substantiva

Em vez de confiar principalmente no controle, o auditor examina diretamente transações, configurações, resultados, dados ou amostras para procurar distorções e exceções. É útil quando controles são fracos, quando a população pode ser analisada com segurança ou quando a afirmação exige confirmação direta.

Testes substantivos não substituem a compreensão do processo. Uma amostra sem contexto pode encontrar um erro, mas não explicar sua causa, sua extensão ou a possibilidade de repetição.

### Abordagem baseada em evidências

A conclusão é sustentada por evidências relevantes, suficientes, confiáveis e apropriadas ao objetivo. A evidência pode ser documental, observada, técnica, testemunhal, analítica ou obtida por reexecução.

Uma captura de tela isolada raramente prova operação contínua. Prefira registros com identidade do objeto, data, período, origem, responsável, resultado e proteção contra alteração indevida. A evidência deve ser minimizada quando contém dados pessoais, segredos ou informação operacional sensível.

### Abordagem orientada a dados

Ferramentas de análise assistida por computador, consultas, amostragem estatística, detecção de outliers e correlação de logs ajudam a avaliar populações grandes. A automação pode examinar todas as mudanças de produção, todos os acessos privilegiados ou todos os artefatos publicados.

Análise de dados precisa de qualidade de fonte, definição de população, controle de versão da consulta, tratamento de valores ausentes e validação de falsos positivos. Um dashboard não é evidência por si só se ninguém consegue explicar sua origem, transformação e período.

### Auditoria contínua e monitoramento contínuo

Monitoramento contínuo pertence normalmente à operação ou à segunda linha: observa controles, indicadores e exceções enquanto o serviço funciona. Auditoria contínua usa tecnologia e procedimentos de assurance para avaliar continuamente riscos e controles do ponto de vista da auditoria interna.

Os dois podem usar a mesma telemetria, mas possuem finalidade e responsabilidade diferentes. Se a mesma pessoa cria um monitoramento e depois declara, sem revisão independente, que o controle está eficaz, existe risco de autoavaliação. A separação não exige sistemas separados, mas exige papéis, regras e evidências claros.

### Abordagem ágil

Uma auditoria ágil reduz lotes grandes e feedback tardio. O trabalho pode ser dividido em ciclos curtos, com objetivo, hipótese, evidência, revisão e resultado parcial. Isso é útil em ambientes que mudam rapidamente, desde que não reduza o rigor da conclusão.

Auditoria ágil não significa aceitar evidência incompleta nem eliminar independência. Significa priorizar, validar cedo, comunicar incerteza e ajustar o plano conforme novos riscos aparecem.

## Ciclo de uma auditoria

### Planejamento

Defina objetivo, escopo, critérios, período, locais, sistemas, populações, equipe, independência, riscos, cronograma e forma de comunicação. Registre o que está fora do escopo, pois essa fronteira evita que a conclusão seja interpretada de forma mais ampla do que a evidência permite.

### Entendimento e avaliação preliminar

Conheça o sistema, o processo, os ativos, os dados, os responsáveis e os controles existentes. Identifique afirmações importantes, pontos de falha, dependências e mudanças recentes. Um walkthrough pode acompanhar uma operação real desde a entrada até o resultado.

### Programa de testes

Para cada risco ou requisito, defina procedimento, população, amostra, critério de aprovação, evidência esperada e tratamento de exceção. Escolha entre inspeção, observação, entrevista, confirmação, cálculo, análise, reexecução e teste automatizado conforme a afirmação.

### Execução e validação

Colete evidência com cadeia de custódia e acesso proporcional. Diferencie fato observado, relato de uma pessoa, inferência do auditor e conclusão. Valide divergências com o responsável antes de transformá-las em finding e registre quando a administração discorda.

### Findings e relatório

Um finding claro contém:

- critério, o que deveria ocorrer;
- condição, o que foi observado;
- causa, por que ocorreu;
- consequência ou risco, o que pode acontecer;
- evidência e limitação do teste;
- classificação de severidade;
- recomendação ou ação corretiva;
- responsável e prazo;
- critério de encerramento.

O relatório deve declarar opinião ou conclusão compatível com o escopo, as amostras e as limitações. Não é correto dizer que "o sistema está conforme" quando apenas alguns controles de um ambiente foram examinados em um período limitado.

### Acompanhamento

O encerramento do finding não deve ser apenas uma mudança de status. Verifique se a ação foi executada, se o controle passou a funcionar e se o risco residual é aceitável. Quando a ação não é viável, registre a exceção, o aceite de risco, a validade e o responsável pela revisão.

## Técnicas de teste

| Técnica | O que fornece | Limitação típica |
| --- | --- | --- |
| Entrevista | Conhecimento de contexto, intenção e exceções | O relato pode não corresponder à execução real. |
| Inspeção documental | Políticas, registros, contratos e evidências | Documento pode existir sem ser aplicado. |
| Observação | Execução real em um momento específico | O comportamento pode mudar fora da observação. |
| Walkthrough | Relação entre entrada, pessoas, sistema e saída | Normalmente cobre poucos exemplos. |
| Confirmação | Validação por uma fonte independente | A fonte pode não conhecer o escopo completo. |
| Reexecução | Verificação independente de um cálculo ou controle | Pode não capturar o comportamento ao longo do tempo. |
| Análise de dados | População, tendência, outlier e correlação | Depende de completude, qualidade e interpretação da fonte. |
| Amostragem | Conclusão sobre uma população com custo controlado | O desenho da amostra e a taxa de erro importam. |
| Teste automatizado | Repetibilidade, escala e detecção frequente | Regra errada pode produzir muitos resultados errados. |

Use mais de uma técnica quando uma única fonte puder ser manipulada, estiver incompleta ou não demonstrar operação contínua. A triangulação entre logs, configuração, entrevista e reexecução tende a ser mais forte que qualquer evidência isolada.

## Independência, objetividade e competência

Independência é a posição e a liberdade para concluir sem interferência indevida. Objetividade é a capacidade de avaliar sem deixar interesses, relações ou conclusões anteriores distorcerem o julgamento. Uma pessoa pode ser tecnicamente competente e ainda não estar suficientemente independente para uma auditoria específica.

Antes do trabalho, registre conflitos de interesse, acesso necessário, informações privilegiadas, limitações de competência e necessidade de especialista. Se a auditoria avaliar uma mudança que o próprio auditor aprovou, deve existir revisão independente ou outro mecanismo de salvaguarda.

## Relação entre auditoria, compliance e segurança

Compliance pergunta se requisitos aplicáveis foram atendidos e demonstrados. Auditoria avalia essa afirmação contra critérios e evidências. Segurança trata riscos técnicos e organizacionais. Governança define direção, responsabilidade e tolerância a risco. Um programa maduro relaciona essas camadas sem tratar qualquer uma como substituta das outras.

O [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) oferece um catálogo de controles; o [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) orienta procedimentos de avaliação. O [NIST CSF 2.0](https://www.nist.gov/cyberframework) ajuda a organizar resultados de cibersegurança. A [ISO 27001](frameworks-de-compliance.md) trata o sistema de gestão de segurança da informação. Esses materiais se relacionam, mas não possuem o mesmo propósito.

## Ferramentas e automação

Um sistema de auditoria pode conter os seguintes componentes:

- catálogo de riscos, requisitos e controles;
- calendário e plano de auditorias;
- workflow de aprovação e revisão;
- cofre ou repositório de evidências com retenção e acesso;
- coleta automatizada de configurações, logs e resultados de testes;
- gestão de findings, exceções, aceite de risco e ações corretivas;
- trilha de auditoria das próprias mudanças no sistema;
- dashboards de cobertura, atraso, severidade e risco residual;
- integrações com IAM, CI/CD, tickets, cloud, Kubernetes, SIEM e observabilidade.

Ferramentas GRC podem ser comerciais, SaaS ou self-hosted. A escolha depende de escopo, residência dos dados, integrações, retenção, segregação de acesso, exportação, automação, custo e capacidade de operar a plataforma. Uma solução menor e transparente pode ser mais confiável que uma plataforma extensa sem responsáveis e sem processo de revisão.

Automatize coleta e comparação quando a regra for determinística. Preserve revisão humana para escopo, risco, interpretação, exceção, causa e decisão. Automação deve reduzir trabalho repetitivo, não esconder incerteza.

## Falhas comuns

- auditar somente documentos e não observar a operação;
- tratar presença de uma ferramenta como prova de controle eficaz;
- usar uma amostra sem definir a população ou o motivo da seleção;
- classificar todos os findings pela facilidade de correção, e não pelo risco;
- permitir que a área auditada defina sozinha o critério e a conclusão;
- misturar auditoria interna, consultoria e operação sem salvaguarda de independência;
- coletar evidências excessivas, com segredos ou dados pessoais desnecessários;
- fechar ações corretivas quando o ticket foi encerrado, sem testar o resultado;
- medir quantidade de findings e criar incentivo para produzir ruído;
- declarar conformidade fora do período, produto ou ambiente efetivamente auditado.

## Relações com este repositório

- [Normas e frameworks de boas práticas](normas-e-frameworks-de-boas-praticas.md) organiza referências de desenvolvimento, operação, incidentes, suporte e compliance.
- [Frameworks de compliance](frameworks-de-compliance.md) compara SOC 2, ISO 27001 e padrões setoriais.
- [Checklist de segurança](../arquitetura/checklist-de-seguranca.md) registra controles e decisões deste ambiente.
- [Resposta a incidente](../operacional/resposta-a-incidente.md) descreve um procedimento operacional específico.
- [Alertas acionáveis](observabilidade/alertas-acionaveis.md) relaciona telemetria a uma ação esperada.
- [Supply chain e SBOM](seguranca/supply-chain/index.md) fornece evidências sobre componentes e artefatos.
- [Qualidade e validação](qualidade/validacao/index.md) trata schema validation e policy as code.

## Fontes primárias

- [ISO 19011:2026, guidelines for auditing management systems](https://www.iso.org/standard/19011)
- [The IIA, Global Internal Audit Standards](https://www.theiia.org/en/standards/2024-standards/)
- [The IIA, Statements of Position](https://www.theiia.org/en/resources/statements-of-position)
- [COSO, Internal Control Integrated Framework](https://www.coso.org/guidance-on-ic)
- [NIST SP 800-53A, assessment procedures](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)
- [AICPA, SOC Suite of Services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [COBIT](https://www.isaca.org/resources/cobit)
- [ISO standards catalogue](https://www.iso.org/standards.html)
