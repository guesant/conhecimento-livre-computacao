# Rota

Uma rota associa um prefixo de destino a uma interface, um próximo salto ou
uma ação local. O kernel escolhe a correspondência mais específica antes de
considerar a rota default.

## Tabela de roteamento

Uma entrada costuma conter destino e prefixo, gateway ou próximo salto,
interface, métrica, escopo e protocolo que instalou a rota. Rotas conectadas
representam redes diretamente alcançáveis. Rotas estáticas são configuradas por
uma pessoa ou automação. Protocolos dinâmicos, como OSPF e BGP, aprendem e
retiram caminhos conforme vizinhança, política e estado do enlace.

O kernel aplica longest prefix match: entre entradas que correspondem ao
destino, vence o prefixo mais específico. Se houver empates, métrica e regras
do sistema determinam a escolha. A rota default, `0.0.0.0/0` em IPv4 ou
`::/0` em IPv6, só é usada quando nenhuma entrada mais específica corresponde.

Linux mantém tabelas com papéis diferentes. A tabela `local` cobre endereços e
broadcast locais, `main` contém as rotas usuais e `default` pode oferecer uma
última política de encaminhamento. Os nomes são convenções do iproute2, e uma
configuração pode adicionar tabelas próprias.

## Policy routing

`ip route` opera a tabela principal. O Linux também mantém tabelas local e
default e pode usar a Routing Policy Database consultada por `ip rule`.
Policy routing permite decidir a tabela por origem, marca, interface ou outras
propriedades.

Um host com duas saídas pode precisar de tabelas por interface e regras que
preservem o caminho de retorno. Adicionar apenas duas rotas default pode
produzir respostas que saem por uma interface diferente daquela que recebeu a
conexão.

## Diagnóstico

Use `ip route get <destino>` para perguntar ao kernel qual caminho escolheria.
Depois confirme gateway, vizinhança, MTU e filtros. Uma rota presente não prova
que o próximo salto responde nem que o retorno usa o caminho esperado.

## Relações

- [Interface de rede](interface.md) fornece o caminho físico ou virtual.
- [NDP e vizinhança](neighbor.md) resolve o próximo salto local.
- [CIDR e subnetting](fundamentos/cidr-e-subnetting.md) mostra como obter o
  prefixo de uma rede.
- [BGP](roteamento/bgp.md) pode alimentar rotas em escala maior.

## Fonte primária

- [ip-route](https://man7.org/linux/man-pages/man8/ip-route.8.html)
