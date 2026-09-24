# Fuzzing

Fuzzing testa um programa com entradas geradas, mutadas ou estruturadas para alcançar estados e combinações que casos manuais dificilmente cobrem. O objetivo pode ser encontrar crashes, violações de memória, falhas de parsing, problemas de disponibilidade ou comportamentos que quebram invariantes.

## Modelos

Fuzzing baseado em cobertura usa feedback da execução para priorizar entradas que alcançam caminhos novos. Fuzzers estruturados conhecem o formato do protocolo ou documento e preservam a validade necessária para chegar à lógica mais profunda. Fuzzing em processo reduz a distância entre a entrada e o código testado, enquanto campanhas distribuídas executam muitos casos e preservam corpus e findings.

## Segurança e qualidade

Sanitizers tornam classes de falha observáveis durante a execução, mas não substituem assertions, testes determinísticos ou revisão de tratamento de erro. Um crash reproduzível precisa ser minimizado, triado e transformado em teste de regressão.

## Relações

- [OSS-Fuzz](oss-fuzz.md) aplica fuzzing contínuo a projetos open source elegíveis.
- [libFuzzer](libfuzzer.md) é uma engine orientada por cobertura para execução local e CI.
- [SAST](../sast/index.md) analisa código sem executar a aplicação.
- [DAST](../dast.md) testa uma aplicação em execução por uma superfície externa.
