# tcpdump

`tcpdump` é um analisador de pacotes baseado na biblioteca libpcap. Ele observa o tráfego visível em uma interface, aplica um filtro de captura e imprime os pacotes ou grava uma captura para análise posterior.

## Perguntas que responde

Uma captura pode confirmar se uma conexão chega à interface, qual endereço e porta são usados, se o handshake TCP termina, se há retransmissões e em qual etapa um protocolo deixa de avançar. Ela observa o tráfego no ponto em que é executada; não representa automaticamente o que outro host ou uma aplicação vê.

O filtro de captura deve ser definido antes de iniciar a coleta. Filtrar por host, porta ou protocolo reduz custo de CPU, volume de dados e exposição de informações alheias à hipótese investigada.

## Captura e análise

Uma captura curta e reproduzível costuma ser mais útil do que um arquivo grande coletado sem hipótese. Registre interface, filtro, horário, direção do teste e condições do host. Quando o objetivo for transportar o arquivo para análise, escreva em formato `pcap` e preserve a cadeia de custódia do dado.

O filtro aplicado durante a captura não é a mesma coisa que o filtro aplicado durante a visualização. A distinção importa porque um pacote descartado pelo filtro inicial não pode ser recuperado depois. Para uma investigação exploratória, escolha um filtro inicial que seja específico sem eliminar a evidência necessária.

## Limitações

Offload de checksum, segmentação, espelhamento de tráfego, namespaces de rede e pontos de captura diferentes podem fazer a captura parecer contraditória com o que o receptor observa. Em ambientes com containers, confirme se a captura está no namespace e na interface que realmente carregam o fluxo.

Um pacote visto na interface não prova que a aplicação o recebeu. O kernel pode descartá-lo depois, uma política de firewall pode rejeitá-lo ou o processo pode não estar escutando o endereço esperado.

## Segurança e custo

Capturas podem conter credenciais, tokens, payloads sem TLS e metadados de terceiros. Armazene-as com permissões restritas, limite a retenção e descarte o arquivo quando a análise terminar. Não use uma captura irrestrita em uma interface de produção quando um filtro por host e porta responder à pergunta.

O privilégio exigido para capturar deve ser concedido ao menor escopo possível. A capacidade de observar a interface não deve ser tratada como uma permissão normal de aplicação.

## Relação com outras ferramentas

[termshark](termshark.md) oferece exploração interativa de uma captura no terminal. [iperf3](iperf3.md) gera tráfego controlado que pode ser observado pelo `tcpdump`. [strace](strace.md) investiga a fronteira entre processo e kernel quando os pacotes não explicam o comportamento.

## Fonte primária

Consulte o [tcpdump.org](https://www.tcpdump.org/) e a documentação da [libpcap](https://www.tcpdump.org/manpages/pcap.3pcap.html) para filtros, formatos e limitações de captura.
