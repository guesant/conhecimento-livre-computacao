# termshark

`termshark` é uma interface de terminal para explorar capturas de pacotes usando o formato e os dissecadores do ecossistema Wireshark. Ele é uma camada de análise; não substitui o ponto de captura nem altera o protocolo observado.

## Modelo de uso

O fluxo normal é capturar um arquivo com [tcpdump](tcpdump.md), transferi-lo para o ambiente de análise e abrir o `pcap` no `termshark`. A interface permite navegar por conversas, protocolos e campos sem exigir uma sessão gráfica, o que é útil em hosts acessados apenas por SSH.

A captura original deve ser preservada antes de aplicar filtros de visualização. Um filtro de exibição muda o que é mostrado, mas não recupera campos que não foram capturados nem desfaz a perda causada por um filtro aplicado durante a coleta.

## Quando usar

Use `termshark` quando a captura já existe e a pergunta exige correlação entre pacotes, conversas e camadas do protocolo. Para uma verificação rápida de presença, ausência ou contagem, ferramentas de linha de comando podem ser mais simples. Para dissecção visual avançada, a interface gráfica do Wireshark pode ser mais adequada.

## Limitações e segurança

O `termshark` herda os riscos e as limitações da captura que está lendo. Um arquivo pode conter payloads, nomes, endereços, tokens ou dados pessoais. A análise deve ocorrer em um ambiente protegido, com cópia mínima e descarte conforme a retenção definida para o incidente.

A interpretação depende do ponto de captura, de offloads, de encapsulamento e de protocolos cifrados. O dissecador pode mostrar metadados de TLS, mas não transforma tráfego cifrado em texto claro sem as chaves e condições necessárias.

## Relação com o diagnóstico

[Diagnóstico técnico](../../diagnostico/index.md) explica a divisão entre geração de tráfego, captura, análise e observação do processo. [iperf3](iperf3.md) pode gerar um experimento reproduzível; [strace](strace.md) ajuda quando a falha está antes de o pacote sair ou depois de chegar ao host.

## Fonte primária

Consulte o [repositório oficial do termshark](https://github.com/gcla/termshark) para os formatos suportados, dependências e opções de execução.
