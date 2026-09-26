# Ciclo de instrução da CPU

O ciclo de instrução descreve como a CPU transforma o conteúdo da memória e dos registradores em efeitos observáveis. A explicação clássica usa três fases: busca, ou fetch; decodificação, ou decode; e execução, ou execute. Processadores modernos sobrepõem muitas instruções em um pipeline, mas a separação continua sendo um modelo útil para entender o fluxo.

## Registradores essenciais

O program counter, ou PC, aponta para o próximo endereço de instrução. O instruction register, ou IR, mantém a instrução que está sendo examinada. O banco de registradores contém operandos e resultados de uso geral. Registradores de estado guardam flags ou informações de controle, embora a forma concreta varie por ISA.

O PC não precisa simplesmente avançar uma instrução por vez. Um salto, uma chamada, uma exceção, uma interrupção ou uma predição pode alterar o próximo endereço. Essa mudança é uma das razões pelas quais o fluxo real de instruções não é uma sequência linear simples.

## Fetch, decode e execute

Na busca, a CPU usa o PC para obter a instrução, normalmente primeiro no cache de instruções. Se a instrução não estiver disponível nos caches, a hierarquia de memória precisa fornecê-la. O PC é então atualizado para o endereço sequencial ou para um destino previsto.

Na decodificação, a CPU interpreta o opcode, identifica registradores, imediatos, modos de endereçamento e dependências. A unidade de controle ou a lógica equivalente transforma a instrução em sinais e operações internas. Em x86, uma instrução pode ser traduzida em várias micro-ops; em outras ISAs, a relação pode ser mais direta, mas não é correto presumir uma implementação única.

Na execução, unidades aritméticas e lógicas, unidades de ponto flutuante, unidades vetoriais, unidades de carga e armazenamento ou outras unidades especializadas realizam o trabalho. O resultado pode ir para um registrador, para a memória, para flags ou para o mecanismo de controle de fluxo. Uma instrução de carga, por exemplo, precisa calcular um endereço e atravessar a hierarquia de memória antes de fornecer o dado.

## Pipeline

Em vez de esperar a execução completa de uma instrução para buscar a próxima, uma CPU pipelineada mantém várias instruções em fases diferentes. Um modelo simplificado é:

```text
tempo       t1       t2       t3       t4       t5
instrucao 1 fetch    decode   execute  memory   writeback
instrucao 2          fetch    decode   execute  memory
instrucao 3                   fetch    decode   execute
```

O pipeline melhora o throughput, mas não torna cada instrução instantânea. Dependências entre instruções, desvios, faltas de cache e conflitos por unidades de execução podem inserir bolhas ou obrigar a descartar trabalho especulado.

## ULA, unidade de controle e unidades funcionais

A unidade aritmética e lógica, ULA, ou ALU em inglês, realiza operações como soma, subtração, comparação, máscaras e operações booleanas. Uma CPU moderna pode ter várias ALUs e unidades separadas para multiplicação, divisão, ponto flutuante, vetores, criptografia e endereços.

A unidade de controle, CU em inglês, coordena o fluxo da instrução. No modelo didático, ela lê a instrução e gera os sinais para registradores, memória e ULA. Em uma implementação moderna, essa função é distribuída por decodificadores, filas, escalonadores, renomeadores, unidades de aposentadoria, controladores de memória e lógica de especulação. O nome permanece útil como abstração, mas não deve ser interpretado como uma caixa única em todo processador.

## Desvios e execução fora de ordem

Um desvio condicional depende de um resultado que pode ainda não estar disponível. O preditor de desvios estima qual caminho será tomado para manter o pipeline ocupado. Se a previsão estiver errada, instruções especulativas são descartadas e o caminho correto é buscado.

Execução fora de ordem permite executar uma instrução independente enquanto outra espera por memória ou por um operando. Renomeação de registradores reduz dependências artificiais. O processador ainda precisa aposentar resultados em uma ordem compatível com o modelo arquitetural e com as regras de exceção.

## Interrupções e exceções

Uma exceção é uma transferência de controle causada pela instrução atual, como uma divisão inválida ou uma página ausente. Uma interrupção normalmente é sinalizada por um dispositivo ou controlador externo. Em ambos os casos, a CPU salva contexto conforme a ISA e entra em um handler privilegiado, que decide se corrige a condição, encerra o processo ou encaminha o evento.

## Modelo mental correto

Fetch, decode e execute explicam a ordem lógica das responsabilidades. Eles não são necessariamente três ciclos de relógio nem três blocos físicos isolados. Uma CPU pode buscar várias instruções por ciclo, decodificá-las em larguras diferentes, executá-las fora de ordem e completar cargas em tempos diferentes. A abstração é correta para explicar o contrato funcional; a microarquitetura explica o paralelismo e os custos.

## Fontes

- [Ciclo de instrução](https://pt.wikipedia.org/wiki/Ciclo_de_instru%C3%A7%C3%A3o)
- [Intel Architecture, The Basics](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/ia-introduction-basics-paper.pdf)
- [Arm Learn the Architecture](https://developer.arm.com/Architectures/Learn-the-Architecture)
- [Computer Systems: A Programmer's Perspective](https://csapp.cs.cmu.edu/3e/perspective.html)
