# System on a chip

Um SoC integra CPU, GPU, controlador de memória, mecanismos de vídeo, segurança, conectividade, aceleradores de aprendizado de máquina e outros periféricos. A integração reduz componentes externos, caminhos de comunicação e consumo de energia, mas também reúne as restrições térmicas e de memória no mesmo sistema.

Nos chips Apple Silicon usados em Macs, CPU, GPU, Neural Engine e outros componentes formam um SoC com arquitetura de memória unificada. CPU e GPU acessam a mesma memória física, evitando cópias tradicionais entre RAM e VRAM em muitos fluxos.

Memória unificada não significa acesso sem custo. Largura de banda, coerência, sincronização, contenção e pressão de memória continuam existindo. A melhor arquitetura depende do padrão de trabalho, não apenas do nome "unificada".

## DMA e coerência

Dispositivos podem usar DMA para ler ou escrever RAM sem a CPU copiar cada byte. A CPU ainda configura a operação e precisa respeitar regras de coerência, sincronização e proteção. Uma IOMMU pode limitar os endereços que um dispositivo pode acessar.

## Fontes

- [Apple, arquitetura de sistema do Apple Silicon](https://developer.apple.com/videos/play/wwdc2020/10686/)
- [Apple, hasUnifiedMemory](https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory)
- [Apple, CPU e GPU em memória unificada](https://developer.apple.com/videos/play/tech-talks/10580/)
