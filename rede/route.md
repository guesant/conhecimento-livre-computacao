# Rota

Uma rota associa um prefixo de destino a uma interface, um próximo salto ou
uma ação local. O kernel escolhe a correspondência mais específica antes de
considerar a rota default.

## Tabela e policy routing

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
- [BGP](roteamento/bgp.md) pode alimentar rotas em escala maior.

## Fonte primária

- [ip-route](https://man7.org/linux/man-pages/man8/ip-route.8.html)
