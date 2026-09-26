# CPU, RAM, GPU e SoC

CPU, RAM e GPU participam do processamento, mas não são nomes intercambiáveis. A CPU executa instruções gerais e coordena o fluxo do programa. A RAM mantém dados e instruções em uma memória volátil de trabalho. A GPU executa muitos cálculos paralelos com um modelo de programação próprio. Um SoC, ou system on a chip, integra vários desses componentes e periféricos em um único pacote ou silício, mas continua sendo uma composição, não um novo tipo de instrução.

## CPU

A CPU possui núcleos de propósito geral, registradores, unidades funcionais, caches e lógica de controle. Ela é adequada para fluxos com decisões, dependências, interrupções, chamadas de sistema e tarefas variadas. Mais núcleos permitem mais trabalho simultâneo quando o software consegue paralelizar, mas não tornam automaticamente uma tarefa serial mais rápida.

Frequência, número de núcleos e tamanho de cache são apenas partes da capacidade. Desempenho depende de instruções por ciclo, latência de memória, largura de vetores, predição, limites térmicos, escalonamento e características do programa.

## RAM

RAM é a memória volátil usada para armazenar código, dados, pilhas, heaps, buffers e páginas que o sistema operacional mantém disponíveis. Ela não executa instruções por conta própria. A CPU e dispositivos fazem leituras e escritas por meio do controlador de memória e do sistema de coerência e ordenação.

Mais RAM permite manter mais dados ativos e reduzir pressão de paginação, mas não aumenta automaticamente o desempenho de um algoritmo que já cabe na memória. Capacidade, largura de banda, latência, canais, tecnologia, frequência e consumo também importam. Quando a RAM acaba, o sistema pode usar armazenamento como backing store, mas isso é muito mais lento e não transforma armazenamento em RAM.

## GPU

Uma GPU contém muitos elementos de execução voltados a throughput. Ela é eficiente quando o mesmo programa pode ser aplicado a muitos dados independentes, como pixels, matrizes, vetores e tensores. O modelo exige transferir ou compartilhar dados, submeter trabalho e sincronizar resultados.

Uma GPU dedicada costuma ter VRAM própria ligada por PCIe ou por outra interconexão. Uma GPU integrada usa a memória do sistema, embora possa ter caches e unidades locais. A GPU não é simplesmente uma CPU com mais núcleos: seus modelos de execução, hierarquia de memória, divergência e APIs são diferentes.

## SoC e chip unificado

Um SoC integra CPU, GPU, controlador de memória, mecanismos de vídeo, segurança, conectividade, aceleradores de aprendizado de máquina e outros periféricos. A integração reduz componentes externos, caminhos de comunicação e consumo de energia, mas também reúne as restrições térmicas e de memória no mesmo sistema.

Nos chips Apple Silicon usados em Macs, CPU, GPU, Neural Engine e outros componentes formam um SoC com arquitetura de memória unificada. CPU e GPU acessam a mesma memória física, evitando cópias tradicionais entre RAM e VRAM em muitos fluxos. Isso não significa acesso sem custo: largura de banda, coerência, sincronização, contenção e pressão de memória continuam existindo.

Em um computador com GPU dedicada, uma textura pode precisar ser copiada ou sincronizada entre a memória do sistema e a memória da GPU. Em um sistema unificado, o compartilhamento pode reduzir esse custo, mas CPU e GPU passam a disputar a mesma capacidade e largura de banda. A melhor arquitetura depende do padrão de trabalho, não apenas do nome “unificada”.

## Comparação

| Componente | Mantém estado principal | Executa | Padrão favorecido |
| --- | --- | --- | --- |
| CPU | Registradores e caches | Instruções gerais | decisões, controle e baixa latência |
| RAM | Dados e instruções voláteis | Não executa | capacidade e acesso compartilhado |
| GPU | Registradores, caches e buffers | kernels gráficos ou de computação | paralelismo de dados e throughput |
| SoC | Integra vários blocos | combina CPU, GPU e aceleradores | eficiência e comunicação local |

## DMA e coerência

Dispositivos podem usar DMA para ler ou escrever RAM sem a CPU copiar cada byte. A CPU ainda configura a operação e precisa respeitar regras de coerência, sincronização e proteção. IOMMU pode limitar os endereços que um dispositivo pode acessar. Em uma arquitetura unificada, compartilhar memória elimina algumas cópias, mas não elimina a necessidade de coordenar quem pode ler ou escrever cada buffer.

## Fontes

- [Apple, arquitetura de sistema do Apple Silicon](https://developer.apple.com/videos/play/wwdc2020/10686/)
- [Apple, `hasUnifiedMemory`](https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory)
- [Apple, CPU e GPU em memória unificada](https://developer.apple.com/videos/play/tech-talks/10580/)
- [Computer Systems: A Programmer's Perspective](https://csapp.cs.cmu.edu/3e/perspective.html)
