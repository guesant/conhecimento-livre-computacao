# Censura de rede

Censura de rede é a interferência deliberada na disponibilidade, descoberta,
classificação ou transmissão de determinados serviços e conteúdos. Ela pode ser
aplicada por um provedor, uma organização, uma rede local ou um Estado. A análise
técnica deve separar mecanismos observáveis de afirmações sobre intenção, escopo e
responsabilidade.

## Camadas de interferência

Uma política de bloqueio raramente depende de um único mecanismo. Pode combinar:

- manipulação ou falsificação de respostas DNS;
- bloqueio de endereços IP e prefixos;
- filtragem de portas e protocolos;
- análise de Host HTTP, SNI TLS ou outros metadados;
- inspeção de conteúdo em texto claro;
- classificação estatística de fluxos criptografados;
- injeção de resets, timeouts, atrasos ou perda seletiva;
- sondagem ativa de endpoints suspeitos;
- pressão sobre plataformas, domínios, aplicativos ou meios de distribuição.

Cada método tem pontos cegos e efeitos colaterais. DNS seguro pode proteger a
resolução contra alguns intermediários, mas não resolve bloqueio de IP. TLS protege o
conteúdo, mas não necessariamente todos os metadados observáveis. Um transporte
anticensura precisa considerar toda a cadeia, incluindo descoberta, rendezvous,
transporte, destino e atualização.

## Medição e diagnóstico

Não se deve inferir bloqueio apenas de uma falha isolada. Compare resolvers, redes de
origem, famílias IPv4 e IPv6, protocolos, horários e destinos controlados. Preserve
horário, caminho, resposta, código, endereço, handshake e condições do teste sem
coletar dados pessoais desnecessários.

O [RFC 9505](https://www.rfc-editor.org/rfc/rfc9505.html) organiza técnicas de
censura observadas em diferentes regiões. Estudos sobre o Great Firewall também
mostram que DNS, HTTP, HTTPS, IP, SNI e sondagem ativa podem compor camadas diferentes
de filtragem. Uma medição deve registrar a metodologia, porque uma conclusão válida
para uma rede ou período pode não valer para outra.

## Evasão e responsabilidade

Transportes anticensura tentam alterar a aparência ou o caminho do tráfego para
preservar acesso. Isso não significa que sejam invisíveis, permanentes ou adequados a
qualquer risco. Há possibilidade de bloqueio posterior, degradação, observação do
cliente, exposição do proxy voluntário e consequências jurídicas locais.

O objetivo desta documentação é explicar os modelos técnicos e os trade-offs. Uma
implantação deve respeitar leis, políticas de uso, segurança de pessoas e proteção de
dados. Não use uma rede de terceiros para transportar conteúdo sem entender quem pode
observar, registrar ou interromper o fluxo.

## Páginas deste domínio

- [Great Firewall](great-firewall.md) analisa um caso conhecido de filtragem em
  múltiplas camadas.
- [Snowflake](snowflake.md) explica o transporte anticensura do Tor baseado em
  proxies temporários e WebRTC.
- [Deep Packet Inspection](../firewall/deep-packet-inspection.md) explica a análise
  profunda que pode alimentar filtragem, classificação ou diagnóstico.
