# Mapa de descoberta e priorização de requisitos

Descoberta reduz incerteza sobre problema, usuário, valor, risco e solução. Priorização decide
qual trabalho merece atenção primeiro dentro de capacidade, prazo e dependências. Nenhuma
técnica elimina julgamento. Métodos servem para tornar premissas visíveis e comparáveis.

## Técnicas de descoberta

| Técnica | Pergunta que ajuda a responder |
| --- | --- |
| Entrevista e observação | O que as pessoas fazem, dizem, evitam e improvisam? |
| Jobs to Be Done | Que progresso a pessoa tenta realizar em uma situação? |
| Event Storming | Quais eventos, comandos, políticas e limites existem no domínio? |
| Impact Mapping | Que atores precisam mudar comportamento para alcançar o objetivo? |
| Story Mapping | Como organizar atividades e etapas para revelar um primeiro produto útil? |
| Example Mapping | Quais regras, exemplos, perguntas e critérios precisam ser esclarecidos? |
| Domain Storytelling | Como pessoas, sistemas e objetos participam de um processo? |
| Opportunity Solution Tree | Como conectar resultado, oportunidades e soluções sem saltar direto para implementação? |
| Lean Canvas | Quais problema, cliente, proposta, canais, custos e riscos formam a hipótese de produto? |
| Business Model Canvas | Como os elementos do modelo de negócio se relacionam? |
| Wardley Mapping | Como capacidades evoluem e onde a estratégia depende de componentes maduros ou incertos? |

Use várias fontes. Uma entrevista revela intenção e linguagem; observação revela comportamento;
logs e métricas revelam frequência e impacto; suporte revela falhas e exceções. Nenhuma dessas
fontes sozinha representa o sistema inteiro.

## Métodos de priorização

| Método | Cálculo ou lógica | Melhor uso | Risco |
| --- | --- | --- | --- |
| MoSCoW | Must, Should, Could, Won't | Negociar escopo e compromisso de uma entrega | Tudo virar Must |
| RICE | Reach vezes Impact vezes Confidence dividido por Effort | Comparar oportunidades com alcance e incerteza | Números falsamente precisos |
| ICE | Impact vezes Confidence vezes Ease | Triagem rápida de hipóteses | Ease pode premiar o que é fácil, não o que importa |
| WSJF | Cost of Delay dividido por Job Size | Ordenar trabalho em contexto de fluxo e escala | Estimar custo de atraso sem dados |
| Kano | Básico, desempenho e encantamento | Entender satisfação e efeito da presença da capacidade | Categorias mudam conforme o público |
| Value versus Effort | Valor esperado comparado ao esforço | Visualizar decisões simples | Valor e esforço podem ser incomparáveis |
| Cost of Delay | Valor perdido por esperar | Destacar urgência, risco e oportunidade | Confundir urgência com importância |
| Opportunity Scoring | Importância percebida menos satisfação atual | Descoberta orientada a necessidades | Depende de pesquisa bem desenhada |
| Buy a Feature | Pessoas distribuem orçamento fictício entre opções | Tornar trade-offs visíveis com stakeholders | Influência do grupo e entendimento desigual |
| 100 Dollar Test | Distribuição de cem unidades de valor | Comparar atributos ou problemas | Resultado depende da lista apresentada |
| Stack Ranking | Ordenação total ou parcial dos itens | Forçar decisão explícita | Falsa precisão quando itens são incomparáveis |

## MoSCoW

MoSCoW separa Must have, Should have, Could have e Won't have neste ciclo. O `Won't` não
significa nunca. Significa que a equipe decidiu não comprometer o item dentro do escopo atual.
Para funcionar, a quantidade de Must precisa caber na capacidade e permitir uma entrega útil.
Se tudo é Must, a técnica não está ajudando a negociar.

## RICE, ICE e WSJF

RICE e ICE são modelos de pontuação. Registre a definição local de alcance, impacto,
confiança, facilidade e esforço. Mudar a escala no meio da comparação destrói a utilidade do
ranking. Use intervalos e faixas quando a incerteza for grande.

WSJF é comum em contextos de agilidade em escala. Cost of Delay costuma combinar valor de
negócio, criticidade temporal e redução de risco ou oportunidade. Job Size representa tamanho
relativo. O método não deve ser usado para transformar uma estimativa grosseira em uma promessa
de prazo.

## Priorização por risco e dependência

Valor de usuário não é o único motivo para priorizar. Uma migração, correção de segurança,
requisito legal, redução de dívida, experimento ou trabalho de plataforma pode vir primeiro
porque reduz risco ou desbloqueia outras entregas.

Registre dependências reais, não apenas preferências de ordem. Uma dependência pode ser técnica,
legal, temporal, contratual, de capacidade ou de aprendizado. Às vezes vale fazer um spike ou
um experimento antes de pontuar o item inteiro.

## Métrica não substitui decisão

Scores são argumentos, não autoridades. Apresente dados, confiança, hipótese, impacto da
espera, custo de reversão e alternativas. Depois registre a decisão e o que será observado para
reavaliá-la. Um item de alta pontuação que não tem evidência de resultado deve voltar à descoberta,
não ser tratado automaticamente como compromisso de entrega.

## Relações

- [Engenharia de requisitos](engenharia-de-requisitos.md) explica elicitação e validação.
- [Backlog e hierarquia de trabalho](backlog-e-hierarquia.md) organiza itens e fluxo.
- [BDD e Gherkin](bdd-e-gherkin.md) usa exemplos para esclarecer comportamento.
- [Ciclo de vida de aplicações](../ciclo-de-vida-de-aplicacoes.md) conecta descoberta, entrega e operação.

## Referências

- [IIBA, BABOK Guide](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/)
- [IIBA, Business Analysis Standard](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf)
- [Agile Alliance, Epic](https://agilealliance.org/glossary/epic/)
- [Atlassian, epics e histórias](https://www.atlassian.com/agile/project-management/epics-stories-themes)
