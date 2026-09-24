# OSS-Fuzz

OSS-Fuzz é um serviço de fuzzing contínuo para projetos open source. Ele combina fuzzers, sanitizers, execução distribuída e triagem de resultados para procurar bugs de estabilidade e vulnerabilidades em código que possui um alvo de fuzzing adequado.

## Modelo de integração

Um projeto fornece a configuração de build e um ou mais fuzz targets. A infraestrutura compila esses alvos com instrumentação, executa entradas continuamente e coleta crashes, regressões e cobertura. A qualidade do resultado depende do alvo, do corpus, da capacidade de alcançar estados relevantes e do tratamento dos findings.

OSS-Fuzz suporta engines como libFuzzer, AFL++ e Honggfuzz em combinação com sanitizers. A campanha não é uma execução única do scanner: o valor vem da repetição, da mutação de entradas e da preservação do corpus ao longo do tempo.

## Quando usar

O serviço é adequado para projetos open source que têm superfície de entrada relevante, como parsers, bibliotecas de formatos, protocolos, compiladores e componentes de infraestrutura. Projetos fechados ou que não atendem aos requisitos podem usar ClusterFuzzLite ou executar uma plataforma própria.

## Limitações

OSS-Fuzz só encontra comportamentos exercitados pelos targets e pelas entradas geradas. Ausência de crash não prova ausência de vulnerabilidade. Integração de um alvo fraco pode produzir muita execução sem aumentar cobertura, e o projeto ainda precisa corrigir, reproduzir e testar cada finding.

## Relações

- [Fuzzing](index.md) explica os modelos e os limites da técnica.
- [LLVM](../../../build/llvm.md) fornece compiladores e sanitizers usados em parte do ecossistema.
- [SAST](../sast/index.md) cobre uma superfície estática complementar.

## Fonte primária

- [OSS-Fuzz](https://google.github.io/oss-fuzz/)
