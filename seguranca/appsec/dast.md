# DAST

Dynamic Application Security Testing testa uma aplicação em execução pela superfície que ela expõe. Em vez de inferir comportamento a partir do código, a ferramenta envia requisições, manipula entradas e observa respostas.

## O que DAST enxerga

DAST consegue observar a composição real entre aplicação, servidor, proxy, headers, autenticação e configuração implantada. Isso permite encontrar comportamentos que não aparecem claramente numa análise do source.

A contrapartida é perda de contexto interno. Um scanner pode demonstrar que uma entrada provoca comportamento vulnerável sem saber qual função ou linha de código criou a falha.

## Casos de uso

DAST é apropriado para testar um ambiente de staging, verificar superfícies HTTP expostas, detectar configurações inseguras observáveis externamente e complementar SAST com evidência do comportamento real.

Um cenário típico é executar testes passivos e seguros em cada deployment de staging e reservar testes ativos mais invasivos para um ambiente isolado preparado para recebê-los.

## Teste passivo e teste ativo

Um modo passivo observa requisições e respostas sem tentar explorar agressivamente a
aplicação. Ele pode encontrar headers ausentes, cookies inseguros, configurações
fracas e informações expostas, com menor risco de alterar estado.

Um modo ativo envia payloads, altera parâmetros e tenta provocar comportamentos que
indicam uma vulnerabilidade. Ele pode criar registros, disparar e-mails, consumir
recursos, alterar dados ou acionar integrações reais. A autorização, o escopo e o
ambiente precisam estar definidos antes da execução.

## Superfície e autenticação

Crawler encontra somente o que consegue alcançar. Rotas sem links, endpoints de API,
parâmetros opcionais, fluxos dependentes de estado e funcionalidades atrás de login
podem ficar fora da cobertura. Use OpenAPI, sitemap, rotas conhecidas, navegação
gravada ou uma lista de endpoints para complementar a descoberta.

Crie contas de teste com dados descartáveis e permissões controladas. Teste papéis
anônimos, usuários comuns e administradores em sessões separadas. Não reutilize uma
conta de produção nem forneça ao scanner uma credencial que permita atingir dados
irreversíveis.

## DAST de API

Em APIs, o contrato OpenAPI pode orientar a descoberta de endpoints, métodos,
parâmetros e tipos. Isso melhora cobertura, mas não substitui fluxos de negócio,
autorização por objeto, concorrência, limites de tamanho ou validação de efeitos
colaterais.

Teste também respostas de erro, redirecionamentos, autenticação expirada, tokens
com escopo incorreto, content types inesperados, paginação e operações que deveriam
ser somente leitura. Um endpoint que retorna 200 para uma requisição inválida pode
ser um bug de contrato mesmo quando o scanner não classifica a resposta como uma
vulnerabilidade.

## Telemetria do teste

Identifique o tráfego de DAST com uma conta, ambiente ou marcador controlado e
preserve correlation ID nas requisições. Logs devem permitir distinguir scanner,
usuário de teste e tráfego real sem registrar tokens ou payloads sensíveis.

Relacione resultados do scanner com logs, métricas e traces. Um aumento de 500,
timeout, fila ou rate limiting durante o teste pode ser um efeito do próprio scanner,
um limite necessário ou uma falha que merece investigação. Não descarte esses sinais
apenas porque o teste foi autorizado.

## Limites e segurança operacional

Defina concorrência máxima, taxa de requisições, timeout, tamanho do payload e
condições de parada. O scanner precisa respeitar o rate limit do ambiente e, quando
apropriado, usar uma janela de execução que não concorra com carga real.

Proteja segredos, dados de teste e evidências. Evite payloads que possam alcançar
serviços externos, apagar dados ou enviar mensagens para destinatários reais. Se o
teste exigir comportamento destrutivo, faça uma cópia restaurável e use um ambiente
isolado.

## Resultados

DAST produz evidência de comportamento observado, não uma prova de ausência de falhas.
Registre alvo, versão implantada, autenticação usada, rotas descobertas, regras
executadas, exclusões, limitações e horário. Um finding deve conter requisição,
resposta, condição de reprodução, impacto e confiança.

Triagem deve separar vulnerabilidade, falso positivo, configuração deliberada,
limitação de cobertura e falha do próprio teste. Repetir o scanner sem corrigir a
causa, ou zerar o relatório por meio de uma allowlist ampla, não aumenta a segurança.

## Boas práticas

Defina claramente o alvo e o nível de agressividade. Use dados descartáveis quando o scanner puder criar, alterar ou excluir estado. Autentique o scanner quando a superfície importante fica atrás de login. Preserve evidências que permitam reproduzir o comportamento. Combine DAST com conhecimento do sistema para distinguir comportamento esperado de vulnerabilidade.

## Más práticas

Nunca trate um scanner ativo como se fosse uma simples leitura. Rodá-lo sem autorização contra produção pode causar efeitos reais. Outra má prática é testar apenas endpoints anônimos quando quase toda a superfície está autenticada, ou interpretar ausência de findings como cobertura de caminhos que o crawler nunca alcançou.

## Limitações

Cobertura depende da capacidade de descobrir rotas, estados e fluxos. APIs e aplicações com navegação complexa podem exigir configuração adicional. DAST também não substitui SCA, secret scanning ou revisão do código.

## Alternativas e complementos

Ferramentas de proxy de segurança, scanners web automatizados, testes de API orientados por especificação e pentests manuais ocupam pontos diferentes do espectro entre automação e investigação humana.

## Fontes

- OWASP Web Security Testing Guide: <https://owasp.org/www-project-web-security-testing-guide/>
- OWASP Developer Guide, DAST: <https://devguide.owasp.org/en/06-verification/02-tools/01-dast/>
- OWASP Attack Surface Detector: <https://owasp.org/projects/attack-surface-detector>
- OWASP ZAP: <https://www.zaproxy.org/docs/>

## Continue por aqui

[SAST](sast/index.md) observa o código sem executar a aplicação. As duas abordagens produzem evidências diferentes e complementares.
