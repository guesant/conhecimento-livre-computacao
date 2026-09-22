# DAST

Dynamic Application Security Testing testa uma aplicação em execução pela superfície que ela expõe. Em vez de inferir comportamento a partir do código, a ferramenta envia requisições, manipula entradas e observa respostas.

## O que DAST enxerga

DAST consegue observar a composição real entre aplicação, servidor, proxy, headers, autenticação e configuração implantada. Isso permite encontrar comportamentos que não aparecem claramente numa análise do source.

A contrapartida é perda de contexto interno. Um scanner pode demonstrar que uma entrada provoca comportamento vulnerável sem saber qual função ou linha de código criou a falha.

## Casos de uso

DAST é apropriado para testar um ambiente de staging, verificar superfícies HTTP expostas, detectar configurações inseguras observáveis externamente e complementar SAST com evidência do comportamento real.

Um cenário típico é executar testes passivos e seguros em cada deployment de staging e reservar testes ativos mais invasivos para um ambiente isolado preparado para recebê-los.

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
- OWASP ZAP: <https://www.zaproxy.org/docs/>

## Continue por aqui

[SAST](sast/index.md) observa o código sem executar a aplicação. As duas abordagens produzem evidências diferentes e complementares.
