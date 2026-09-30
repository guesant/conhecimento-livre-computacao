# Engenharia de requisitos

Engenharia de requisitos transforma necessidades e restrições em entendimento compartilhado
e evidência verificável. O objeto pode ser um sistema, serviço, produto, processo, interface,
contrato ou mudança em um sistema existente. A disciplina acompanha o ciclo de vida inteiro,
porque requisitos mudam quando o domínio, a legislação, o mercado, a tecnologia ou a operação
mudam.

## As atividades principais

As atividades não precisam ocorrer em uma sequência rígida, mas cada uma deve ter uma intenção
clara.

| Atividade | Pergunta principal | Evidência comum |
| --- | --- | --- |
| Elicitação | Que problema, objetivo ou restrição existe? | Entrevistas, observação, dados, workshops e documentos |
| Análise | O que é causa, sintoma, regra, hipótese ou dependência? | Modelos, cenários, conflitos e impactos |
| Especificação | Como registrar o comportamento e as propriedades esperadas? | Requisitos, casos de uso, exemplos, contratos e cenários |
| Validação | O requisito é necessário, compreensível, consistente e verificável? | Revisão, protótipo, simulação e teste de aceitação |
| Priorização | O que deve ser feito primeiro e o que pode ser recusado? | Valor, risco, urgência, esforço e dependências |
| Rastreabilidade | De onde veio a necessidade e onde ela será demonstrada? | Links entre objetivo, requisito, implementação, teste e release |
| Gestão de mudanças | O que muda, por que muda e qual impacto será aceito? | Decisão registrada, versão, aprovação e comunicação |

O [BABOK Guide](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/)
organiza a análise de negócio em áreas de conhecimento que incluem planejamento, elicitação,
gestão do ciclo de vida, análise, avaliação e colaboração. Ele não exige Scrum, BDD ou uma
ferramenta de backlog. Seu foco é a prática de análise e o valor produzido pela decisão.

## Requisitos bem formados

A ISO/IEC/IEEE 29148 descreve processos e itens de informação de engenharia de requisitos e
orienta características de requisitos bem formados. Na prática, um requisito útil deve ser
necessário, inequívoco, verificável, consistente, rastreável e viável dentro das restrições.

Evite frases como "o sistema deve ser intuitivo", "a API deve ser rápida" ou "o usuário deve
ter uma boa experiência" sem definir contexto e medição. Uma formulação mais útil identifica
o ator, o contexto, o comportamento, a condição e a evidência. Mesmo assim, o texto não deve
prescrever uma implementação quando várias soluções podem satisfazer a necessidade.

## Requisitos, hipóteses e decisões

Uma hipótese é uma afirmação que ainda precisa de evidência. Um requisito é uma condição que
foi aceita como necessária. Uma decisão de arquitetura registra como uma opção foi escolhida
dentro de restrições. Uma regra de negócio expressa uma política do domínio que pode existir
independentemente da tela ou do banco.

Separar esses tipos é importante. Uma equipe pode descobrir que uma hipótese estava errada e
remover a oportunidade sem tratar isso como falha de implementação. Também pode manter o
requisito e mudar a arquitetura sem reescrever a necessidade original.

## Papéis e colaboração

O analista, product manager, product owner, especialista de domínio, usuário, operador,
desenvolvedor, tester, arquiteto e responsável por segurança podem contribuir com perspectivas
diferentes. Nenhum papel deve ser usado como desculpa para excluir os demais. O conhecimento
de domínio pode estar com usuários e operadores, enquanto restrições de segurança e operação
podem estar com equipes que não usam o produto diariamente.

Workshops, entrevistas e revisões devem registrar decisões e dúvidas, não somente transcrever
opiniões. Quando duas necessidades entram em conflito, registre quem é afetado, qual risco é
criado, qual alternativa foi analisada e quem tem autoridade para decidir.

## Validação e aceite

Validação pergunta se estamos construindo o que é necessário. Verificação pergunta se o item
foi implementado conforme sua especificação. Um requisito pode ser verificável e ainda assim
resolver o problema errado. Por isso, testes automatizados, revisão de requisitos, protótipos,
observação do uso e métricas de resultado devem coexistir.

Critérios de aceite devem ser observáveis. Não basta dizer que uma tela existe. Defina estados,
erros, permissões, limites, dados ausentes, concorrência, timeout, auditoria e resultado
esperado. Os critérios podem ser escritos como exemplos, tabela de decisão, cenários BDD,
checklist ou testes de contrato, desde que sejam compreendidos por quem precisa avaliar o
resultado.

## Gestão de mudanças

Mudança de requisito não é automaticamente um problema. Ela pode refletir aprendizado real,
alteração legal, incidente, feedback ou mudança de estratégia. O risco aparece quando mudanças
não são registradas e o sistema passa a ter comportamentos contraditórios.

Para cada mudança relevante, registre a versão anterior, a nova formulação, o motivo, o impacto
em escopo, dados, contratos, testes, segurança, operação e suporte. Reavalie prioridades e
dependências. Não mantenha uma frase antiga apenas para preservar histórico; mantenha histórico
por versão, link ou decisão, deixando claro qual definição está vigente.

## Rastreabilidade proporcional

Rastreabilidade não significa criar uma planilha com links que ninguém mantém. Ela vale mais
quando permite responder perguntas concretas: qual objetivo justifica este item, quais riscos
ele atende, quais testes demonstram o comportamento, qual release alterou o contrato e quem
aprovou a exceção.

Em sistemas críticos, ligue requisitos a controles, ameaças, evidências, testes, mudanças e
incidentes. Em um experimento pequeno, uma decisão e alguns exemplos podem ser suficientes.
O nível de formalidade deve acompanhar risco, custo de falha, exigência regulatória e número de
equipes envolvidas.

## Relações

- [Requisitos funcionais e regras de negócio](requisitos-funcionais-e-regras-de-negocio.md)
  detalha comportamento e política do domínio.
- [Requisitos não funcionais](requisitos-nao-funcionais.md) detalha propriedades de qualidade.
- [Use Cases](use-cases.md) organiza objetivos e fluxos de interação.
- [BDD e Gherkin](bdd-e-gherkin.md) registra comportamento por exemplos.
- [Backlog e hierarquia de trabalho](backlog-e-hierarquia.md) organiza execução e comunicação.

## Fontes primárias

- [ISO/IEC/IEEE 29148](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)
- [IIBA, BABOK Guide](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/)
- [IIBA, Business Analysis Core Standard](https://www.iiba.org/globalassets/standards-and-resources/core-standard/iiba-core-standard.pdf)
