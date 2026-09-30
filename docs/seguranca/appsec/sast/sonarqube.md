# SonarQube

SonarQube é uma plataforma de revisão automática de código que combina regras de qualidade, confiabilidade, segurança e manutenção. Ele é mais amplo que um SAST especializado: pode apontar vulnerabilidades e code smells, mas o conjunto de regras, a análise interprocedural, a linguagem e o modo de integração definem o que realmente será coberto.

## Formas de operação

O SonarQube Community Build é uma opção self-hosted para análise automatizada. SonarQube Server adiciona recursos comerciais conforme a edição. SonarQube Cloud é o serviço SaaS. SonarQube for IDE antecipa parte do feedback no editor, mas a análise do pipeline continua necessária para uma decisão centralizada.

O custo operacional do self-hosted inclui banco, armazenamento de histórico, atualização do servidor, plugins, autenticação, backup e disponibilidade. SaaS reduz essa operação, mas introduz dependência de rede, retenção externa e requisitos de tratamento de código e metadados.

## O que ele responde

Uma execução pode responder se uma mudança introduziu uma regra de segurança, um problema de confiabilidade, uma duplicação ou uma dívida de manutenção. Quality Gates transformam métricas em decisão de pipeline, mas os limites precisam ser escolhidos de acordo com linguagem, legado e risco. Bloquear tudo no primeiro dia tende a criar suppressions e perda de confiança.

## Boas práticas

Defina análise de código novo separada da dívida legada. Publique resultados em pull requests, exija correção de vulnerabilidades de alta confiança e revise a origem de cada falso positivo. Combine SonarQube com SCA, secret scanning, testes, DAST e análise de infraestrutura, porque nenhum quality gate cobre dependências, ambiente e runtime sozinho.

Não trate a pontuação como prova de ausência de vulnerabilidades. Ferramentas diferentes têm modelos, regras, linguagens e profundidade semântica diferentes. A seleção deve considerar a pergunta de segurança, não a quantidade de métricas exibidas.

## Relações

- [SAST](index.md) explica análise estática e suas limitações.
- [CodeQL](codeql.md) usa consultas sobre uma representação semântica do código.
- [Checkmarx SAST](checkmarx.md) é uma alternativa comercial focada em análise de segurança.
- [Segurança no ciclo de vida](../seguranca-no-ciclo-de-vida.md) compara SAST, DAST, RASP, fuzzing, AV e EDR.

## Fonte primária

- [SonarQube Community Build](https://docs.sonarsource.com/sonarqube-community-build/)
