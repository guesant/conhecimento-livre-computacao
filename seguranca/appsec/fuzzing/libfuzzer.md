# libFuzzer

libFuzzer é uma engine de fuzzing orientada por cobertura que executa dentro do processo testado. Ela muta entradas, observa caminhos novos e prioriza casos que aumentam a cobertura. O alvo normalmente expõe uma função de entrada, como `LLVMFuzzerTestOneInput`, que recebe bytes arbitrários e chama o parser, protocolo ou API sob teste.

## Modelo de execução

O fuzzer mantém um corpus de entradas e usa instrumentação para descobrir caminhos novos. Quando uma entrada provoca crash, erro de sanitizer ou violação de uma asserção, o caso deve ser preservado como reproducer, minimizado e transformado em teste de regressão.

libFuzzer é uma biblioteca e uma engine, não uma plataforma de gestão de findings. O projeto ainda precisa compilar o alvo com sanitizers, limitar recursos, guardar corpus, analisar crashes e acompanhar correções.

## Sanitizers

AddressSanitizer ajuda a encontrar acessos inválidos e use-after-free. UndefinedBehaviorSanitizer observa classes de comportamento indefinido. MemorySanitizer exige que o código e as dependências relevantes sejam instrumentados, caso contrário pode gerar resultados difíceis de interpretar.

O sanitizer torna o problema observável, mas não prova que o restante do código é seguro. Um alvo sem cobertura relevante pode executar milhões de entradas sem alcançar a lógica importante.

## Quando usar

Use libFuzzer em parsers, formatos binários, bibliotecas de serialização, protocolos e APIs que possam receber entradas arbitrárias. É adequado para execução local, CI e integração com ClusterFuzzLite. Projetos open source elegíveis podem usar OSS-Fuzz para campanhas distribuídas e contínuas.

## Boas práticas

Mantenha o alvo pequeno, determinístico e sem efeitos externos. Limite o tamanho da entrada quando entradas muito grandes não agregarem cobertura. Use dicionários para formatos com tokens estruturados. Reproduza cada crash com a mesma versão do código, reduza o caso e adicione um teste permanente.

## Relações

- [Fuzzing](index.md) explica a técnica e seus modelos.
- [OSS-Fuzz](oss-fuzz.md) executa libFuzzer e outras engines em escala.
- [LLVM](../../../build/llvm.md) fornece compiladores e instrumentação do ecossistema.
- [ClusterFuzzLite](https://google.github.io/clusterfuzzlite/) permite integração contínua fora do serviço OSS-Fuzz.

## Fontes primárias

- [libFuzzer, LLVM documentation](https://llvm.org/docs/LibFuzzer.html)
- [OSS-Fuzz, glossary](https://google.github.io/oss-fuzz/reference/glossary/)
