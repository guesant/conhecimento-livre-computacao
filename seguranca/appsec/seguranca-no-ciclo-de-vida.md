# Segurança no ciclo de vida

Manter um sistema seguro e funcional exige combinar prevenção, descoberta, resposta e recuperação. Nenhuma ferramenta observa todas as superfícies. Um resultado confiável depende de escolher o teste pelo objeto analisado, executar no momento adequado, controlar o impacto sobre o ambiente e transformar findings reproduzíveis em correções e testes de regressão.

## O que cada técnica observa

| Tecnologia | O que faz | Tipo de análise | Quando é usada | Alvo principal |
| --- | --- | --- | --- | --- |
| SAST | Lê código ou uma representação sem executá-lo e procura padrões de falha, fluxos perigosos e violações de segurança | Caixa branca | Desenvolvimento, pull request e CI | Código escrito pela equipe |
| DAST | Envia requisições à aplicação em execução e observa respostas, estados, autenticação e configuração exposta | Caixa preta ou cinza | Homologação e ambientes controlados | Web, API, proxy e configuração implantada |
| RASP | Instrumenta ou acompanha o processo em runtime e pode bloquear comportamentos considerados ataques | Instrumentação em runtime | Operação contínua, com política gradual | Fluxos ativos dentro da aplicação |
| Fuzzing | Gera ou muta entradas para alcançar caminhos e estados difíceis de cobrir manualmente | Caixa cinza, orientada por cobertura | CI, campanha contínua e pré-release | Parsers, protocolos, bibliotecas e invariantes |
| SCA | Identifica dependências, versões e vulnerabilidades conhecidas | Composição de software | Pull request, build e release | Componentes de terceiros |
| Secret scanning | Procura credenciais e material sensível em arquivos, commits e artefatos | Análise de conteúdo e histórico | Pre-commit, pull request e CI | Repositório e cadeia de entrega |
| AV | Detecta e bloqueia malware por assinaturas, heurísticas e outros sinais | Proteção de endpoint | Contínua no host | Sistema operacional e arquivos |
| EDR | Coleta telemetria, detecta comportamento e apoia investigação e resposta | Detecção e resposta no endpoint | Contínua no host | Processos, rede, arquivos e atividade do endpoint |

SAST não enxerga uma porta publicada por engano. DAST não sabe necessariamente qual linha originou um comportamento. RASP pode reagir ao ataque, mas não corrige uma autorização mal modelada. AV e EDR protegem o host, não substituem testes da aplicação. Essas limitações são complementares, não falhas de uma ferramenta individual.

## Camadas de prevenção

Uma sequência razoável começa com revisão de ameaça e desenho seguro, passa por validação local e chega ao ambiente implantado:

1. Defina ativos, fronteiras de confiança, abuso esperado, dados sensíveis e comportamento de recuperação.
2. Use formatadores, compilador estrito, testes unitários e regras de SAST para feedback rápido.
3. Verifique dependências, SBOM, secrets, imagens e workflows antes de produzir um artefato.
4. Execute fuzzing em interfaces que recebem entradas complexas, principalmente parsers e protocolos.
5. Faça DAST autenticado e não autenticado em ambiente descartável, com dados que possam ser alterados pelo scanner.
6. Proteja endpoints, logs, métricas, traces e alertas sem expor os próprios dados sensíveis.
7. Prepare resposta, rollback, rotação de credenciais, restauração e teste de regressão antes de um incidente.

O gate deve distinguir falha de segurança, falha de qualidade e sinal operacional. Um finding crítico pode bloquear uma release; um aviso de complexidade pode exigir correção antes do próximo ciclo; um erro de telemetria pode demandar investigação sem interromper o tráfego. Misturar tudo em um único número produz decisões ruins.

## Produtos e formas de operação

| Área | Opções gratuitas ou abertas | SaaS ou produtos pagos | Self-hosted e observações |
| --- | --- | --- | --- |
| SAST | CodeQL em contextos elegíveis, Semgrep Community Edition | SonarQube Cloud, Checkmarx, Semgrep Code | SonarQube Community Build, SonarQube Server, CodeQL CLI e Semgrep CE; cobertura e regras variam |
| DAST | OWASP ZAP | Burp Suite Professional e Enterprise, StackHawk, Invicti | ZAP em container ou pipeline; Burp e plataformas comerciais têm recursos de colaboração e escala |
| RASP | Não há uma alternativa aberta universal com paridade de suporte | Contrast Security e produtos equivalentes | Instrumentação própria e WAF não são RASP equivalente; valide linguagem, framework e impacto de latência |
| Fuzzing | libFuzzer, AFL++, Honggfuzz, ClusterFuzzLite | Serviços gerenciados de fuzzing e consultorias especializadas | OSS-Fuzz para projetos open source elegíveis; ClusterFuzzLite ou infraestrutura própria para outros casos |
| AV e EDR | ClamAV para antivírus; Wazuh para detecção e resposta com limites claros | Sophos, SentinelOne, Symantec, Microsoft Defender for Endpoint | ClamAV e Wazuh não têm paridade automática com EDR comercial; valide kernel, distribuição e resposta |
| Qualidade e segurança de código | SonarQube Community Build, linters e scanners especializados | SonarQube Server, SonarQube Cloud | A plataforma pode agregar qualidade, confiabilidade e segurança, mas não substitui SAST dedicado em todos os casos |
| Erros e performance | Sentry self-hosted, OpenTelemetry e backends próprios | Sentry SaaS | Sentry observa erros e performance; não é SAST, DAST, AV ou EDR |

O custo não é apenas licença. Considere ingestão, retenção, armazenamento, tráfego, atualização de agentes, triagem, integração com identidade, ruído e capacidade da equipe de corrigir os resultados. Uma ferramenta gratuita que ninguém opera não oferece o controle que seu nome sugere.

## Boas práticas de operação

Use uma política de severidade com prazo e responsável, não apenas um limiar numérico. Mantenha o scanner e suas regras atualizados. Faça o finding reproduzir antes de alterar o código. Registre a justificativa para aceitar um risco e defina validade para a exceção.

Não teste DAST agressivo contra produção sem autorização, isolamento e plano de rollback. Não habilite bloqueio RASP, EDR ou WAF em modo amplo sem observar falsos positivos e caminhos de recuperação. Não faça fuzzing destrutivo contra dados reais. Não publique stack traces, tokens, payloads sensíveis ou dados pessoais no sistema de observabilidade.

## Relações

- [SAST](sast/index.md) detalha análise estática.
- [DAST](dast.md) detalha testes dinâmicos.
- [Fuzzing](fuzzing/index.md) e [libFuzzer](fuzzing/libfuzzer.md) detalham entrada gerada e execução orientada por cobertura.
- [OSS-Fuzz](fuzzing/oss-fuzz.md) explica campanha contínua para projetos open source.
- [OpenSSF Scorecard](../supply-chain/openssf-scorecard.md) avalia práticas do repositório e da cadeia de entrega.
- [Sentry](../../observabilidade/sentry.md) cobre erros e performance em runtime.
- [SonarQube](sast/sonarqube.md) cobre análise integrada de código e qualidade.

## Fontes primárias

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Source Code Analysis Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools)
- [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/en)
