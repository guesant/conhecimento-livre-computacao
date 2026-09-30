# Great Firewall

Great Firewall, ou GFW, é o nome pelo qual é conhecido o conjunto de políticas,
dispositivos e sistemas usados para controlar o tráfego entre a China continental e
serviços externos. Não é uma única caixa com uma única regra. A literatura técnica
descreve uma combinação de manipulação de DNS, bloqueio de IP, filtragem por conteúdo
ou nome, interferência em conexões e sondagem ativa.

## Modelo de funcionamento

O sistema pode observar diferentes momentos de uma conexão:

1. a resolução do nome pode receber uma resposta falsa, ser atrasada ou falhar;
2. o endereço de destino pode ser descartado ou receber tratamento diferente;
3. o início de HTTP pode ser filtrado por host, caminho ou palavra;
4. o ClientHello TLS pode expor um SNI usado em decisões de bloqueio;
5. a sessão pode ser interrompida por descarte, timeout ou pacotes injetados;
6. um endpoint suspeito pode ser sondado para descobrir que serviço oferece.

Esses mecanismos podem ser combinados e podem produzir bloqueios residuais, nos quais
uma conexão posterior também é afetada por algum tempo. Um teste precisa distinguir
falha de resolução, falha de conexão, falha de negociação e bloqueio após o início do
fluxo.

## Por que o caso é importante

O GFW é um estudo de caso de defesa e censura em escala de rede. Ele mostra que
criptografar o payload não remove necessariamente todas as possibilidades de
classificação: endereços, nomes apresentados no handshake, padrões temporais,
características do protocolo e comportamento de conexão ainda podem ser observados.
Também mostra que bloqueios podem ser dinâmicos e que uma política pode causar dano
colateral quando uma regra ampla atinge domínios ou fluxos legítimos.

O [RFC 9505](https://www.rfc-editor.org/rfc/rfc9505.html) apresenta uma taxonomia
geral de técnicas de censura. Pesquisas do [USENIX sobre filtragem em múltiplas
camadas](https://www.usenix.org/publications/loginonline/measuring-great-firewall-s-multi-layered-web-filtering-apparatus)
descrevem observações de DNS, HTTP e HTTPS, incluindo filtros baseados em Host e SNI.

## Medição responsável

Uma investigação não deve testar um destino real de forma agressiva nem provocar
sondagens desnecessárias. Prefira destinos sob controle, baixa frequência e coleta
mínima. Compare:

- respostas de resolvers independentes;
- conexões por IPv4 e IPv6;
- TCP, TLS e QUIC quando o destino os suporta;
- redes e pontos de observação diferentes;
- comportamento imediatamente após a falha e depois de um intervalo.

Registre o método de medição, a versão do cliente, o horário e a topologia. Não trate
uma simples indisponibilidade do servidor, problema de rota ou erro de certificado como
evidência de censura sem controles que eliminem essas hipóteses.

## Relações

- [Censura de rede](index.md) apresenta a taxonomia geral.
- [Deep Packet Inspection](../firewall/deep-packet-inspection.md) explica uma das
  técnicas que pode participar de classificação.
- [Snowflake](snowflake.md) apresenta um transporte anticensura que usa WebRTC.
- [DNSSEC](../dns/dnssec.md) explica autenticidade de respostas DNS, que não garante
  conectividade quando o bloqueio ocorre em outra camada.
