# RASP

Runtime Application Self-Protection é uma abordagem em que a aplicação ou seu agente observa o comportamento durante a execução e pode bloquear uma operação que corresponda a uma política de ataque. O mecanismo pode usar instrumentação, hooks de framework, sensores de processo ou contexto de requisição para tomar uma decisão próxima do código protegido.

## O que RASP não é

RASP não é sinônimo de WAF. Um WAF observa tráfego em uma fronteira HTTP; RASP conhece parte do contexto interno do processo e pode observar uma operação depois que a requisição atravessou camadas externas. RASP também não é SAST, porque não inspeciona o programa inteiro antes de executá-lo, e não é EDR, porque o alvo principal é a aplicação e não o endpoint completo.

## Quando faz sentido

RASP pode reduzir o tempo entre detecção e bloqueio quando a aplicação possui uma superfície de ataque conhecida, instrumentação compatível e uma equipe capaz de tratar falsos positivos. É especialmente útil como camada complementar em aplicações que não conseguem corrigir imediatamente uma vulnerabilidade explorável.

O bloqueio deve começar em modo de observação. Depois de medir o tráfego legítimo, escolha ações graduais, como registrar, marcar, limitar ou bloquear. Uma política que bloqueia sem caminho de diagnóstico pode transformar uma tentativa de proteção em indisponibilidade.

## Limitações

O agente adiciona custo de CPU, memória e latência. A cobertura depende da linguagem, do runtime, do framework, do modo de deploy e das bibliotecas instrumentadas. Um ataque que não passa pelos hooks pode escapar; um fluxo legítimo que se parece com um ataque pode ser interrompido.

RASP não corrige a causa raiz. Findings devem voltar para o código, testes e processo de release. O agente também precisa de atualização, controle de acesso, comunicação segura com sua console e uma estratégia para quando a console estiver indisponível.

## Opções

Produtos comerciais de RASP, como Contrast Security, costumam combinar agente, políticas, telemetria e console SaaS ou corporativa. Não existe uma alternativa aberta universal com a mesma cobertura entre linguagens e frameworks. Instrumentação própria com hooks, logs e políticas pode ser self-hosted, mas não deve ser apresentada como substituto equivalente sem validar cobertura e resposta.

## Relações

- [DAST](dast.md) testa a aplicação de fora.
- [SAST](sast/index.md) analisa o código sem executá-lo.
- [Proteção de endpoints Linux](../endpoint/index.md) protege o host e seus processos.
- [Observabilidade](../../observabilidade/index.md) fornece sinais para investigar impacto e falsos positivos.

## Fontes

- [OWASP Runtime Application Self-Protection](https://owasp.org/www-community/Runtime_Application_Self-Protection)
- [Contrast RASP](https://docs.contrastsecurity.com/en/runtime-application-self-protection-rasp.html)
