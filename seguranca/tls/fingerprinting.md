# Fingerprinting de TLS e HTTP

Fingerprinting de TLS e HTTP é a classificação de uma conexão a partir de propriedades observáveis do handshake e das mensagens, sem depender apenas do endereço IP ou do User-Agent. A técnica pode observar versões, cifras, extensões, grupos, ordem de extensões, parâmetros de HTTP/2, cabeçalhos e outros sinais do cliente ou de um intermediário.

## O que é observado

No TLS, o ClientHello expõe parte das capacidades anunciadas pelo cliente. Implementações diferentes podem produzir combinações e ordens distintas de versões, cifras, extensões, grupos e algoritmos de assinatura. No HTTP/2, a ordem e os parâmetros de SETTINGS, a ordem de cabeçalhos e o comportamento dos frames também podem formar sinais úteis.

JA3 resume campos do ClientHello em uma impressão legível por comparação. JA4 organiza sinais semelhantes com uma representação mais adequada a variações modernas do TLS. Fingerprints de HTTP/2 e PeetPrint ampliam a observação para características de transporte e protocolo que não aparecem no JA3 isolado.

## Para que serve

O fingerprinting pode ajudar a investigar incompatibilidade, comparar clientes em um laboratório, detectar mudanças após uma atualização, correlacionar sinais durante uma janela curta de diagnóstico e alimentar sistemas de abuso ou observabilidade. Ele é um sinal auxiliar, não uma identidade.

Uma atualização do navegador, um proxy, uma biblioteca TLS, uma terminação TLS ou um balanceador pode alterar a impressão. Clientes diferentes podem compartilhar a mesma impressão e um mesmo cliente pode apresentar impressões diferentes em redes ou versões distintas.

## Limites e privacidade

O dado observado pode ser combinável com endereço IP, User-Agent, cabeçalhos e horário. Por isso, a coleta precisa ter finalidade, retenção e controle de acesso definidos. Não use fingerprinting para concluir que duas requisições vieram da mesma pessoa, nem para substituir autenticação, autorização ou uma identificação criptográfica.

Em uma arquitetura com proxy ou terminação TLS, o ponto de coleta determina qual participante está sendo fingerprintado. Antes de interpretar um resultado, identifique se a captura ocorreu no cliente, no proxy, no gateway ou no servidor de destino.

## Diagnóstico

Um serviço como [tls.peet.ws](https://tls.peet.ws/) permite observar uma requisição de teste e consultar o retorno JSON completo em [tls.peet.ws/api/all](https://tls.peet.ws/api/all). Para uma investigação que não deve enviar dados a terceiros, use uma ferramenta autocontrolada como [TrackMe](https://github.com/pagpeter/TrackMe) em uma rede de laboratório.

O resultado deve ser comparado com uma hipótese concreta. Registre o cliente, a versão, o caminho de rede e o ponto de observação. Evite guardar respostas completas quando elas contiverem endereço IP, cabeçalhos ou outros metadados desnecessários.

## Relações

- [TLS](index.md) explica o protocolo e a proteção da conexão.
- [TLS Peet](../../ferramentas/diagnostico/tls-peet-ws.md) descreve o serviço hospedado usado para inspeções pontuais.
- [TrackMe](../../ferramentas/diagnostico/trackme.md) descreve a alternativa autocontrolada para laboratório.

## Fontes

- [TrackMe, repositório do projeto](https://github.com/pagpeter/TrackMe)
- [tls.peet.ws](https://tls.peet.ws/)
