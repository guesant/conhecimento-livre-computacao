# Diagnóstico técnico

Diagnóstico é a investigação orientada por evidências de um comportamento observado. A ferramenta correta depende da pergunta: um teste de conectividade, uma medição de capacidade, uma captura de pacotes e a observação de chamadas de sistema produzem evidências diferentes e não são intercambiáveis.

## Escolha a evidência pela pergunta

Antes de executar um comando, formule a hipótese que ele deve confirmar ou enfraquecer. `iperf3` mede a capacidade de um caminho de rede sob tráfego controlado. `tcpdump` mostra quais pacotes passam por uma interface. `termshark` facilita a exploração interativa de uma captura. `strace` mostra a interação entre um processo e o kernel.

Um resultado negativo também precisa ser interpretado com o contexto do teste. Um `iperf3` limitado pela CPU não prova que o link está limitado. Uma captura sem o filtro correto não prova que um pacote não existe. Um `strace` anexado depois do evento pode não observar a falha. A validade da conclusão depende do ponto de observação, da janela e da carga introduzida pelo diagnóstico.

## Ferramentas canônicas

- [iperf3](../ferramentas/diagnostico/iperf3.md) mede throughput e perda de pacotes em um caminho controlado.
- [tcpdump](../ferramentas/diagnostico/tcpdump.md) captura pacotes para análise de protocolos e fluxo.
- [termshark](../ferramentas/diagnostico/termshark.md) explora arquivos de captura em um terminal.
- [strace](../ferramentas/diagnostico/strace.md) observa chamadas de sistema e sinais de um processo.
- [tls.peet.ws](../ferramentas/diagnostico/tls-peet-ws.md) exibe sinais observáveis da conexão TLS e HTTP de uma requisição de teste.
- [TrackMe](../ferramentas/diagnostico/trackme.md) permite observar fingerprints em um ambiente autocontrolado.

## Composições

[Diagnóstico profundo com iperf3, tcpdump e strace](../diagnostico-profundo-iperf3-tcpdump-e-strace.md) mostra como combinar as ferramentas quando o sintoma pode estar na rede, no transporte ou na interação entre o processo e o sistema operacional.

Para um problema Kubernetes, comece pelo recurso e pelos eventos em [diagnóstico de Pod, nó, certificado e Argo CD](../diagnostico-de-pod-no-cluster-e-do-argocd.md). Ferramentas de baixo nível devem ser usadas depois que a hipótese estiver suficientemente delimitada.

## Segurança e custo

Capturas podem conter dados sensíveis, testes de throughput consomem banda e `strace` altera o tempo de execução do processo. A coleta deve ter escopo, duração, local de armazenamento e descarte definidos antes de começar. Em produção, prefira uma janela controlada e registre o que foi alterado para que o resultado possa ser reproduzido sem transformar o diagnóstico em uma nova causa de incidente.

## Fontes primárias

- [iperf3 no repositório oficial](https://github.com/esnet/iperf)
- [tcpdump no tcpdump.org](https://www.tcpdump.org/)
- [termshark no repositório oficial](https://github.com/gcla/termshark)
- [strace no projeto upstream](https://strace.io/)
