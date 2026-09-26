# Descoberta, MVP e evolução do produto

Projetos de software raramente começam com conhecimento completo do problema. A equipe
precisa investigar usuários, domínio, restrições, riscos e formas de medir resultado antes de
decidir o que construir. Depois, precisa entregar uma parte utilizável, observar o efeito,
revisar os requisitos e repetir o ciclo.

Esse modelo não significa trabalhar sem planejamento. Significa tratar o planejamento como uma
hipótese que pode ser atualizada por evidência. A descoberta reduz incerteza; a entrega
incremental reduz o tamanho da aposta; a release disponibiliza uma versão; a operação produz
aprendizado para a próxima decisão.

## Projeto de descoberta e análise

Um projeto de descoberta é um trabalho temporário para entender se existe um problema relevante,
quem é afetado, qual resultado seria valioso e quais caminhos são tecnicamente e
operacionalmente plausíveis. Ele pode existir antes de um projeto de construção ou continuar
em paralelo quando há incerteza alta.

### Perguntas da descoberta

- qual problema é observável e para quem ele importa;
- qual processo existe hoje e quais improvisos, custos e riscos ele produz;
- que evidência confirma frequência, impacto e urgência;
- quais regras, integrações, dados, responsabilidades e restrições existem;
- quais hipóteses precisam ser validadas;
- qual é o menor experimento que pode reduzir a incerteza;
- quais alternativas não dependem de software novo;
- como saberemos que uma solução melhorou o resultado;
- quais riscos exigem um protótipo técnico ou um teste operacional;
- quem decide continuar, mudar de direção ou encerrar a iniciativa.

### Saídas possíveis

A descoberta não precisa terminar em um backlog cheio. Suas saídas podem ser uma decisão de
prosseguir, uma hipótese reformulada, um mapa de atores e processos, um conjunto de requisitos,
um experimento, um protótipo, uma análise de viabilidade, um registro de riscos ou a decisão de
não construir.

Um resultado negativo é válido quando evita investimento em uma solução sem valor. Não transforme
o encerramento da descoberta em fracasso. A função do trabalho é melhorar a decisão, não garantir
que toda ideia chegue ao desenvolvimento.

### Descoberta não é análise infinita

Timebox a investigação quando a incerteza permitir. A equipe deve saber qual pergunta está
tentando responder, qual evidência basta para a decisão e qual custo será aceito para investigar.
Quando a incerteza restante só pode ser reduzida usando a solução com usuários reais, um MVP ou
experimento controlado pode ser mais adequado que mais documentação.

## MVP

Minimum Viable Product, MVP, é a menor versão de um produto que permite testar uma hipótese
relevante com usuários ou stakeholders reais e produzir aprendizado útil. A palavra “viável”
não significa apenas que o software inicia. A versão precisa ser adequada ao contexto de uso,
ter qualidade compatível com o risco e gerar evidência interpretável.

O MVP não é necessariamente a primeira parte técnica do sistema. Pode ser uma operação manual,
um protótipo, uma landing page, uma integração limitada, um serviço usado por poucos clientes
ou uma fatia vertical de produto. A forma depende da hipótese. Se a pergunta é se pessoas usam
uma capacidade, uma implementação parcial pode ser suficiente. Se a pergunta envolve segurança,
latência ou operação, o experimento precisa representar essas propriedades.

### MVP não é desculpa para baixa qualidade

Não são MVPs aceitáveis: uma versão que perde dados sem avisar, expõe informações pessoais,
cobra incorretamente, não permite suporte, não tem rollback quando isso é necessário ou mede um
resultado que não representa a hipótese. Reduzir escopo é diferente de remover controles
necessários.

| Conceito | Para que serve | O que ainda não prova |
| --- | --- | --- |
| Protótipo | Explorar interação, entendimento ou solução | Operação, escala e confiabilidade de produção |
| Proof of Concept | Testar viabilidade técnica | Valor de usuário e modelo sustentável |
| MVP | Testar uma hipótese com a menor solução útil | Que o produto completo terá adoção ou escala |
| Beta | Observar uma versão mais completa com grupo controlado | Que a distribuição ampla está sem riscos relevantes |
| MLP, minimum lovable product | Buscar valor e experiência suficientemente bons para adoção | Que todas as necessidades futuras estão cobertas |

Um MVP deve declarar hipótese, público, escopo, limitações, riscos, métrica, duração do
experimento e decisão esperada. Sem isso, ele vira apenas a primeira versão incompleta de um
produto, sem aprendizado definido.

## Entrega incremental

Entrega incremental produz partes utilizáveis que se somam ao produto. O corte preferível é uma
fatia vertical que atravessa o fluxo necessário para gerar valor, em vez de entregar primeiro
uma camada inteira sem comportamento completo.

Uma entrega pode começar com poucos usuários, um único caso de uso, uma integração ou um limite
de capacidade. O limite deve ser explícito. O incremento precisa preservar segurança, integridade
de dados, observabilidade e possibilidade de recuperação compatíveis com o risco.

Feature flags, permissões, canary, grupos de acesso e rollout gradual podem separar implantação
de disponibilização. Isso permite colocar código e infraestrutura em produção antes de expor o
comportamento, mas aumenta estados possíveis e exige limpeza das flags, métricas e plano de
reversão.

## Incremento, deploy e release

Esses termos descrevem eventos diferentes.

| Termo | Significado |
| --- | --- |
| Incremento | Parte utilizável do produto produzida pelo trabalho da equipe |
| Build | Artefato compilado, empacotado ou gerado a partir do código |
| Deploy | Instalação ou disponibilização do artefato em um ambiente |
| Ativação | Momento em que o comportamento passa a ser usado por um grupo |
| Release | Decisão de disponibilizar uma versão ou conjunto de mudanças a consumidores |
| Rollout | Estratégia e progressão da exposição da release |
| Release notes | Registro das mudanças relevantes para quem usa ou opera a versão |

Um deploy pode ocorrer sem release quando a funcionalidade está atrás de uma flag. Uma release
pode ser gradual quando o tráfego é ampliado em etapas. Uma equipe pode publicar várias releases
em um ciclo de deploy contínuo, ou manter deploys frequentes e releases agendadas.

O Scrum Guide descreve o Increment como utilizável e verificável, mas não exige que ele seja
liberado imediatamente. Isso preserva a diferença entre trabalho pronto, decisão de release e
exposição a usuários.

## Mudanças nos requisitos

Requisitos mudam porque a equipe aprende, usuários mudam de comportamento, leis são alteradas,
dependências evoluem, incidentes revelam riscos ou a estratégia do produto muda. A abordagem
ágil aceita mudanças mesmo tarde no desenvolvimento, mas isso não significa aceitar qualquer
mudança sem avaliar impacto.

Para cada mudança significativa, verifique:

- qual evidência motivou a alteração;
- qual hipótese, objetivo ou regra foi afetada;
- quais itens, fluxos, contratos, dados e testes mudam;
- qual valor é adiado ou removido;
- que riscos de segurança, privacidade e operação aparecem;
- se a mudança é compatível ou exige migração;
- quem deve aprovar e comunicar a decisão;
- qual versão do requisito passa a ser vigente.

Não apague silenciosamente o requisito anterior quando ele tiver valor histórico, contratual ou
de auditoria. Versione o documento ou registre a decisão, mas marque claramente o que está ativo.
Um backlog saudável pode remover itens sem valor; isso é diferente de perder a explicação de por
que a decisão mudou.

## Ciclo de versões

Uma versão deve identificar um estado do produto ou de um contrato. O significado do número
depende da convenção adotada. Semantic Versioning é útil quando há uma API pública e a equipe
consegue distinguir mudanças incompatíveis, adições compatíveis e correções compatíveis.

| Tipo de mudança | Exemplo de decisão em SemVer |
| --- | --- |
| Compatibilidade quebrada | Incrementar MAJOR |
| Funcionalidade compatível | Incrementar MINOR |
| Correção compatível | Incrementar PATCH |
| Estado ainda não estável | Usar pre-release e declarar limites |

SemVer não resolve versionamento de banco, contratos assíncronos, dados persistidos ou compatibilidade
de interface por si só. A equipe precisa definir política de depreciação, janela de coexistência,
migração, rollback, suporte e comunicação.

Não altere o conteúdo de um artefato já publicado sob a mesma versão. Immutable artifacts tornam
o diagnóstico e a reversão mais previsíveis. Se uma versão precisar ser substituída, publique
outra versão e registre o motivo.

## Ciclo de release

Um ciclo de release pode incluir planejamento, seleção de escopo, implementação, validação,
empacotamento, aprovação, rollout, observação e encerramento. O ciclo não precisa ser uma
grande fase anual. A periodicidade deve refletir risco, capacidade de suporte, dependências,
necessidade de aprovação e velocidade de aprendizado.

Uma release madura declara:

- versão, artefatos e origem do build;
- mudanças, incompatibilidades e migrações;
- requisitos e testes executados;
- riscos conhecidos e limitações;
- plano de rollout, métricas e critérios de pausa;
- procedimento de rollback ou mitigação;
- janela de suporte e responsável;
- prazo ou condição de remoção de compatibilidade temporária.

Changelogs devem ser orientados a pessoas. O [Keep a Changelog](https://keepachangelog.com/)
recomenda organizar mudanças notáveis por versão, com datas e categorias compreensíveis. Logs
de commit e changelog servem a finalidades diferentes: commits ajudam a investigar a construção;
release notes ajudam consumidores a entender a mudança.

## Aprendizado após a entrega

Depois da release, observe adoção, conclusão de tarefas, erros, latência, suporte, custo,
incidentes e métricas de resultado. Não confunda quantidade de features entregues com valor
realizado. Se o uso não muda ou o resultado esperado não aparece, a próxima decisão pode ser
alterar a solução, mudar a hipótese, reduzir escopo ou encerrar a iniciativa.

O ciclo de descoberta, entrega, medição e adaptação não termina quando a versão é publicada.
Publicar apenas encerra uma etapa e cria uma nova fonte de evidência.

## Fontes primárias

- [Princípios do Manifesto Ágil](https://agilemanifesto.org/principles)
- [Scrum Guide](https://scrumguides.org/scrum-guide.html)
- [Lean Startup, metodologia](https://theleanstartup.com/principles)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/en/2.0.0/)
- [ISO/IEC/IEEE 29148](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)
