# Comparação entre OSI e TCP/IP

OSI e TCP/IP são modelos relacionados, mas não são duas versões equivalentes
da mesma especificação. OSI é uma referência formal de sete camadas. TCP/IP
é uma família de protocolos e uma forma prática de organizar os protocolos da
Internet. O modelo de cinco camadas usado em cursos é uma adaptação
pedagógica do TCP/IP, não uma substituição normativa do modelo de quatro
camadas.

## Mapeamento aproximado

| OSI | TCP/IP de quatro camadas | TCP/IP de cinco camadas | Exemplos |
| --- | --- | --- | --- |
| Aplicação | Aplicação | Aplicação | HTTP, DNS, SSH, SMTP |
| Apresentação | Aplicação | Aplicação | TLS, JSON, compressão e codificação |
| Sessão | Aplicação | Aplicação | sessão RPC, diálogo e retomada |
| Transporte | Transporte | Transporte | TCP, UDP, QUIC, portas |
| Rede | Internet | Rede | IPv4, IPv6, ICMP |
| Enlace | Acesso à rede | Enlace | Ethernet, Wi-Fi, VLAN, ARP |
| Física | Acesso à rede | Física | cobre, fibra, rádio |

O mapeamento é aproximado. Uma implementação pode distribuir uma função por
mais de uma camada, e um protocolo pode encapsular outro. O objetivo do mapa
é facilitar a conversa, não provar que todo cabeçalho possui uma posição
universal.

## Diferenças de origem e finalidade

| Dimensão | OSI | TCP/IP |
| --- | --- | --- |
| Origem | modelo de referência formal da ISO | protocolos desenvolvidos para a Internet e organizados pela experiência |
| Número mais conhecido | sete camadas | quatro camadas, ou cinco em uma decomposição didática |
| Camadas superiores | aplicação, apresentação e sessão separadas | normalmente agrupadas em aplicação |
| Camadas inferiores | enlace e física separadas | normalmente agrupadas em acesso à rede |
| Relação com protocolos reais | vocabulário para análise | protocolos operacionais e interfaces implementadas |
| Uso comum | ensino, arquitetura e diagnóstico | implementação, interoperabilidade e operação da Internet |

## Confusões comuns

### "OSI é o que a Internet usa"

A Internet usa protocolos TCP/IP, Ethernet, Wi-Fi, TLS, HTTP e muitos outros.
O OSI ajuda a classificar suas funções, mas não é o conjunto de protocolos
executado por um computador conectado à Internet.

### "TCP é a camada 4 e sempre fica abaixo de TLS"

TCP é um protocolo de transporte. TLS geralmente usa TCP, mas QUIC incorpora
funções tradicionalmente associadas a transporte confiável e usa UDP. TLS
também pode ser analisado como uma função de apresentação, aplicação ou
segurança, dependendo do objetivo da conversa.

### "A camada 2 é o switch e a camada 3 é o roteador"

São papéis, não definições exclusivas de equipamento. Um switch pode fazer
roteamento de camada 3 e um roteador pode executar bridge de camada 2. A
camada descreve a informação usada na decisão, não o formato físico do chassi.

### "Cada camada tem um protocolo único"

Uma camada reúne responsabilidades. Transporte pode usar TCP, UDP, QUIC ou
SCTP. Aplicação pode usar HTTP, DNS, SSH ou um protocolo proprietário. Além
disso, túneis, proxies, overlays e offloads criam novas fronteiras de
encapsulamento.

### "Se ping funciona, HTTP deve funcionar"

Ping usa ICMP e testa uma propriedade diferente de resolução de nome, porta,
TLS, autenticação e aplicação. O fato de um pacote ICMP retornar não prova que
o serviço TCP ou UDP está acessível.

### "VLAN é a camada de segurança"

VLAN cria separação de camada 2 e reduz domínios de broadcast. A comunicação
entre VLANs passa por camada 3 e pode ser filtrada, mas a segurança depende de
ACLs, firewall, autenticação, isolamento de administração e configuração
correta de trunks.

## Usando os modelos no diagnóstico

O OSI é útil quando a pergunta é "qual responsabilidade está falhando?". O
TCP/IP é útil quando a pergunta é "qual protocolo ou interface devo observar?".
Uma investigação pode combinar os dois: identificar uma falha de enlace no
modelo OSI, observar uma interface Ethernet no modelo de cinco camadas e usar
`ip`, `ss` e `tcpdump` para verificar a implementação TCP/IP.

Não se deve forçar um sintoma a uma camada antes de observar a evidência. Um
timeout pode envolver DNS, roteamento, filtragem, transporte, TLS e aplicação.
O modelo organiza hipóteses; captura, logs, métricas e testes confirmam ou
rejeitam essas hipóteses.

## Regra prática de comunicação

Ao explicar um problema, nomeie o modelo e o objeto observado. "Falha na
camada 2" é menos preciso do que "a interface recebeu link, mas o trunk não
permitiu a VLAN 30". "Problema na camada 4" é menos preciso do que "o SYN para
TCP/443 não recebeu resposta". A combinação de camada, protocolo, endereço,
porta e evidência torna o diagnóstico reproduzível.

## Fontes primárias

- [ISO/IEC 7498-1](https://www.iso.org/standard/14256.html)
- [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
