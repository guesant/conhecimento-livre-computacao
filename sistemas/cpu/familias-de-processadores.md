# Famílias e gerações de processadores

"Geração" pode significar coisas diferentes: uma revisão de microarquitetura, uma coleção comercial, uma família de produto, um processo de fabricação ou uma geração de SoC. Comparar apenas o número impresso no nome pode esconder mudanças importantes. Esta página usa as famílias para mostrar a evolução e aponta para os catálogos oficiais quando a identificação exata de um modelo for necessária.

## Intel

A história da Intel inclui o 4004, 8008, 8080, 8086, 286, 386, 486, Pentium, Pentium Pro, Pentium II, Pentium III e Pentium 4. A família x86 preservou compatibilidade enquanto adicionava modos, instruções, extensões e mecanismos internos novos.

Na evolução mais recente do mercado de PCs, a linha Core passou por Core 2 e pelas microarquiteturas Nehalem, Westmere, Sandy Bridge, Ivy Bridge, Haswell, Broadwell, Skylake e suas sucessoras. A nomenclatura comercial também inclui coleções como Comet Lake, Rocket Lake, Alder Lake, Raptor Lake, Meteor Lake e Arrow Lake. Alder Lake introduziu na linha Core uma arquitetura híbrida com P-cores e E-cores, e Thread Director ajuda o sistema operacional a encaminhar cargas.

O catálogo "geração" não é uma linha perfeitamente uniforme. Há produtos móveis, desktop, workstation e Xeon com codinomes e datas diferentes. Uma CPU de 13ª geração, um Core Ultra e um Xeon não devem ser comparados apenas pelo número. Consulte o nome do codinome, a microarquitetura, os núcleos, as extensões, o envelope térmico e a plataforma.

## AMD

A AMD passou por famílias como K5, K6, Athlon, Duron, Opteron, Phenom e Bulldozer antes da família Zen. Zen reestruturou o núcleo e sustentou Ryzen para consumidores, Threadripper para workstations e EPYC para servidores.

A sequência Zen, Zen 2, Zen 3, Zen 4 e Zen 5 representa revisões de arquitetura. As séries Ryzen 1000, 3000, 5000, 7000, 8000 e 9000 são coleções de produto associadas a essas arquiteturas, mas nem toda série é uma correspondência simples de um para um. Em servidores, EPYC 7001, 7002, 7003, 9004 e 9005 refletem gerações e plataformas distintas.

A estratégia de chiplets da AMD separa núcleos e I/O em blocos que podem ser combinados. Isso favorece escala de núcleos e reutilização de componentes, mas a latência entre chiplets, a hierarquia de cache e o Infinity Fabric passam a fazer parte da análise de desempenho.

## Arm

Arm não vende uma única CPU equivalente a uma geração Intel Core. O ecossistema combina versões da arquitetura, núcleos Cortex, designs licenciados e implementações próprias. ARMv7-A foi uma base importante de 32 bits; Armv8-A introduziu AArch64 e o conjunto A64; Armv9-A acrescentou recursos e extensões voltadas a segurança, vetores e computação moderna.

Cortex-A, Cortex-R e Cortex-M atendem a perfis diferentes. Cortex-A é voltado a aplicações e sistemas operacionais ricos; Cortex-R a requisitos de tempo real e determinismo; Cortex-M a microcontroladores. Um SoC pode combinar núcleos, aceleradores e periféricos sem deixar de usar a mesma família arquitetural.

## Apple Silicon

Apple projeta implementações próprias da ISA Arm para as famílias A, usadas em dispositivos móveis, e M, usadas em Macs. M1 foi a primeira geração do Apple Silicon para Mac; M2, M3, M4 e gerações posteriores representam evoluções de SoC, não apenas uma troca de frequência da CPU.

Esses chips combinam núcleos de desempenho e eficiência, GPU, Neural Engine, mídia, segurança e memória unificada. O resultado precisa ser avaliado como sistema: a memória compartilhada, o acelerador de vídeo, o compilador, o Metal, o consumo e o software podem importar tanto quanto a CPU isolada.

## Como comparar gerações

Compare primeiro o trabalho. Para CPU geral, observe desempenho por núcleo, desempenho sustentado, latência, extensões e eficiência. Para servidor, considere memória máxima, canais, NUMA, I/O, virtualização, confiabilidade e suporte. Para GPU, compare unidades de execução, largura de banda, memória, APIs e workload. Para um SoC, inclua aceleradores e limites térmicos.

Processo de fabricação não é sinônimo de desempenho. "Nanômetros" de fabricantes diferentes não são medidas perfeitamente equivalentes, e uma melhoria de processo pode ser compensada por uma microarquitetura, cache, frequência ou limite de potência diferente. Benchmarks devem declarar aplicação, versão, configuração, duração e comportamento térmico.

## Fontes

- [Intel, coleções Core e datas de lançamento](https://www.intel.com/content/www/us/en/support/articles/000099655/processors.html)
- [Intel, fundamentos da arquitetura](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/ia-introduction-basics-paper.pdf)
- [AMD Zen Core Architecture](https://www.amd.com/en/technologies/zen-core.html)
- [AMD Ryzen para desktops](https://www.amd.com/en/products/processors/desktops/ryzen.html)
- [Arm Architecture](https://developer.arm.com/Architectures)
- [Apple Silicon e arquitetura de sistema](https://developer.apple.com/videos/play/wwdc2020/10686/)
