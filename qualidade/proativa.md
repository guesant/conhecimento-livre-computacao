# Qualidade proativa

Qualidade proativa é a prática de reduzir a probabilidade de defeitos, incidentes e degradação antes que eles atinjam usuários ou operações. Ela começa antes da implementação, continua durante a construção e permanece ativa durante o funcionamento do sistema. Seu objetivo não é prometer que falhas nunca ocorrerão. O objetivo é fazer com que os riscos sejam conhecidos, que as decisões sejam verificáveis e que os caminhos perigosos tenham barreiras antes de chegar à produção.

Qualidade proativa não é sinônimo de testar tudo antes do deploy. Testes são uma parte do sistema de controle, mas a qualidade também depende de requisitos claros, desenho de interfaces, limites de capacidade, migrações compatíveis, autorização, observabilidade e capacidade de recuperação. Um teste pode confirmar que uma implementação atende a um exemplo. Ele não substitui a análise de como a funcionalidade se comporta sob concorrência, dados incompletos, expiração de credenciais ou indisponibilidade de uma dependência.

## Onde ela começa

O primeiro controle proativo é transformar riscos vagos em comportamentos observáveis. Requisitos como "a tela deve ser rápida" ou "o sistema deve ser seguro" precisam ser decompostos em limites de latência, volume, disponibilidade, autorização, retenção e resposta a falhas. A equipe deve registrar o que acontece quando uma entrada é inválida, quando um usuário perde acesso, quando uma fila cresce ou quando uma migration precisa ser interrompida.

Na descoberta e na modelagem, são úteis:

- análise de risco e de impacto;
- modelagem de ameaças;
- FMEA, para relacionar modo de falha, efeito, causa, detecção e tratamento;
- revisão de requisitos não funcionais;
- cenários de qualidade, como latência, disponibilidade, segurança e recuperabilidade;
- contratos de API, eventos, jobs e armazenamento;
- desenho de rollback, feature flags e compatibilidade entre versões.

Essas práticas evitam que decisões importantes sejam descobertas apenas quando o sistema já está sob carga ou durante uma indisponibilidade.

## Controles durante a construção

O código pode ser submetido a controles automáticos antes de ser integrado. Formatter, linter, análise de tipos, SAST, análise de dependências, validação de schemas, testes unitários, integração, contrato e smoke tests formam uma cadeia de evidências. Cada ferramenta precisa ter uma responsabilidade clara. Um linter deve bloquear padrões proibidos e inconsistências; um teste de contrato deve detectar incompatibilidade; uma ferramenta de SAST deve investigar fluxos de dados perigosos; uma suíte de integração deve exercitar as fronteiras reais.

Revisão de código também é um controle proativo quando procura riscos específicos, não apenas preferências de estilo. A revisão deve perguntar se a autorização ocorre no recurso correto, se a operação é idempotente, se o retry pode duplicar efeitos, se a query tem limite, se uma exceção vaza dados, se o log contém segredo e se a mudança é compatível com o rollout.

## Antes da produção

Antes do deploy, a equipe deve validar o artefato que será executado, não somente o código-fonte. Isso inclui build reprodutível quando aplicável, lockfiles íntegros, imagem fixada, migrations aplicadas em base vazia e representativa, backup verificado, probes, limites de recurso, dashboards, alertas e runbooks.

Um rollout seguro usa exposição gradual quando o risco justificar. Canary, blue-green, feature flag e rollback automatizado reduzem o alcance de um defeito. O sistema deve ter sinais que permitam interromper a promoção, como aumento de erro, p95, saturação, filas, falhas de autenticação ou queda de uma métrica de negócio.

## Operação proativa

Revisar alertas antes de eles dispararem, testar restauração, renovar certificados antes do vencimento, fazer exercícios de recuperação, analisar capacidade e remover dependências obsoletas são atividades proativas. O trabalho precisa produzir evidência: resultado do exercício, tempo de recuperação, limitações encontradas e ações pendentes.

## Limitações

Qualidade proativa pode criar uma falsa sensação de segurança quando os controles são executados apenas no caminho feliz. Também pode gerar excesso de gates, lentidão no delivery e testes artificiais. O critério deve ser o risco. Controles caros devem proteger falhas caras, enquanto regras simples podem ser automáticas e amplas.

Qualidade proativa deve ser combinada com [qualidade preventiva](preventiva.md), [qualidade preditiva](preditiva.md) e [qualidade reativa](reativa.md). Incidentes reais revelam riscos que a análise anterior não capturou, e esses aprendizados precisam voltar para requisitos, testes, controles e runbooks.
