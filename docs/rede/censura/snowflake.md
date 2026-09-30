# Snowflake

Snowflake é um transporte anticensura do projeto Tor. Ele usa proxies temporários
operados por voluntários e WebRTC para conectar um cliente a uma ponte Tor. O nome
descreve o transporte do Tor, não o data warehouse Snowflake.

## Componentes

Uma sessão normalmente envolve:

- cliente Snowflake, integrado ao Tor Browser ou executado como transporte;
- broker, que ajuda a encontrar um proxy disponível;
- proxy Snowflake, executado em um navegador, extensão ou processo standalone;
- servidor ou ponte que recebe o fluxo do proxy e o encaminha para a rede Tor;
- servidores STUN ou TURN quando necessários para descobrir ou intermediar a
  conectividade WebRTC.

O broker não é o destino final do usuário. Ele participa do rendezvous, enquanto o
proxy cria a conexão de transporte e a ponte encaminha o tráfego para a rede Tor.

## Fluxo conceitual

O cliente solicita ao broker informações para encontrar um proxy. O cliente e o
proxy negociam uma conexão WebRTC, normalmente usando ICE e servidores auxiliares para
atravessar NATs. O proxy estabelece a próxima perna com a ponte ou servidor Snowflake.
O conteúdo do destino final não é escolhido pelo proxy voluntário; ele participa da
ponte de transporte definida pelo protocolo.

Esse desenho reduz a necessidade de cada usuário operar um servidor dedicado e permite
que proxies apareçam e desapareçam. Em troca, há dependência de broker, descoberta,
NAT traversal, disponibilidade voluntária, capacidade dos proxies e capacidade das
pontes.

## Por que WebRTC

WebRTC é comum em chamadas de áudio e vídeo no navegador. Usá-lo como transporte
permite que o fluxo se pareça com uma comunicação interativa legítima em vez de exigir
um protocolo de proxy reconhecível em uma porta dedicada. Isso não oferece
indetectabilidade: redes podem observar endpoints, temporização, falhas de negociação,
características do transporte e padrões de uso.

## Operação de um proxy

Executar um proxy Snowflake contribui com banda e conexões temporárias para usuários
que precisam alcançar a rede Tor. Antes de fazê-lo, considere consumo de rede, política
do provedor, logs locais, atualizações e exposição do host. Execute o processo com
privilégios mínimos, limites de recursos e isolamento adequado. Um proxy não deve ser
tratado como um relay Tor completo nem como uma forma de conceder confiança ao
tráfego que o atravessa.

## Limitações e falhas

Snowflake pode ser afetado por bloqueio do broker, indisponibilidade de proxies,
restrições de WebRTC, NAT simétrico, filtragem de STUN ou TURN, mudanças de
fingerprint, capacidade insuficiente e bloqueio específico do próprio transporte.
Quando o fluxo falha, o diagnóstico precisa separar descoberta, negociação WebRTC,
conectividade do proxy, conexão com a ponte e disponibilidade da rede Tor.

O transporte também não resolve todos os riscos do endpoint. Malware, extensão
maliciosa, vazamento de identidade por fora do Tor, configuração incorreta do
navegador ou conta autenticada podem revelar informações independentemente do caminho
de rede.

## Relações

- [Censura de rede](index.md) apresenta bloqueio, medição e responsabilidade.
- [WebRTC](../../comunicacao/webrtc.md) explica ICE, STUN, TURN, mídia e DataChannel.
- [Peer-to-peer](../modelos-comunicacao/p2p.md) explica o papel de peers e servidores
  auxiliares.
- [VPN](../conectividade/vpn.md) é uma composição diferente, com outro modelo de
  confiança e de exposição.

## Fontes

- [Tor Project, Snowflake](https://snowflake.torproject.org/)
- [Tor Support, What is Snowflake?](https://support.torproject.org/anti-censorship/what-is-snowflake/)
- [Snowflake source repository](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake)
