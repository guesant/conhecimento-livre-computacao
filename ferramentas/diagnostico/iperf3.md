# iperf3

`iperf3` é uma ferramenta de medição ativa de rede. Ela executa um processo servidor e um processo cliente que geram tráfego entre duas extremidades, permitindo observar throughput, retransmissões, jitter e perda conforme o modo usado.

## O que mede

No modo TCP, a ferramenta mede a taxa sustentada que a conexão conseguiu transportar durante o intervalo escolhido. O resultado inclui o comportamento do transporte, portanto depende de janela TCP, congestionamento, MTU, CPU, buffers e da capacidade de ambos os hosts. Não é uma medição isolada da capacidade física do enlace.

No modo UDP, o cliente envia datagramas a uma taxa definida e o servidor relata perda e jitter. Esse modo é útil para investigar qualidade de transporte e comportamento de aplicações sensíveis a atraso, mas pode saturar o caminho se a taxa for escolhida sem relação com a capacidade real.

## Modelo operacional

O servidor escuta uma porta e espera conexões. O cliente define duração, direção, número de fluxos e, quando aplicável, a taxa UDP. O teste deve ser repetido em ambas as direções quando o caminho puder ser assimétrico.

Um único fluxo responde se uma conexão comum consegue usar o caminho. Vários fluxos ajudam a distinguir limitação por fluxo de limitação agregada, mas também aumentam a carga e podem esconder problemas de fairness ou de configuração de congestionamento.

## Interpretação

Compare a taxa observada com uma referência do mesmo caminho, horário e tamanho de pacote. Uma taxa baixa com retransmissões elevadas aponta para perda ou congestionamento. Uma taxa baixa sem retransmissões relevantes pode indicar limite de CPU, socket, shaping ou configuração do endpoint.

O teste precisa ser associado a métricas do host e da interface. Sem CPU, memória, erros de interface e contadores de descarte, o número final não identifica sozinho a camada responsável.

## Segurança e impacto

O servidor não fornece autenticação de aplicação. Restrinja a porta ao par de teste e encerre o processo ao final. O tráfego gerado compete com o tráfego real e pode degradar o serviço medido, principalmente no modo UDP ou com vários fluxos.

Não use o resultado de um teste executado sobre um túnel como se fosse a capacidade do enlace físico. O teste mede o caminho completo, incluindo criptografia, encapsulamento e limites do endpoint.

## Relação com outras ferramentas

Use [tcpdump](tcpdump.md) quando precisar verificar se o tráfego chega, é retransmitido ou é descartado em um ponto específico. Use [strace](strace.md) quando a suspeita estiver no processo que abre sockets, e não no caminho de rede. A página de [diagnóstico técnico](../../diagnostico/index.md) organiza a escolha pela pergunta.

## Fonte primária

Consulte a [documentação do iperf3 no repositório oficial](https://github.com/esnet/iperf) para opções, formato de saída e limitações das versões suportadas.
