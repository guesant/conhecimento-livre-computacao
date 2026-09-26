# Consistência

Distribuir dados significa decidir onde cópias vivem, quem pode escrever, como mudanças são propagadas e o que acontece quando participantes perdem conectividade. Alta disponibilidade, replicação, consenso, sharding e cache são mecanismos diferentes dentro desse espaço.

## Páginas

- [Clustering, redundância e distribuição](../clustering-redundancia-e-distribuicao.md) compara topologias e domínios de falha.
- [Replicação](../replicacao.md) trata cópias de um estado primário.
- [Replicação em cascata](../replicacao-em-cascata.md) reduz fan-out por meio de uma réplica intermediária.
- [Quorum e consenso](../quorum-e-consenso.md) trata decisões sob falha e maioria.
- [Sharding](../sharding.md) divide o conjunto de dados entre partições.

## Distinções

Replicação mantém cópias; sharding distribui partições; consenso coordena decisões; clustering descreve a composição de nós; cache mantém uma cópia derivada e descartável. Uma arquitetura pode usar todos eles, mas nenhum conceito substitui os demais.

## Critérios

Compare consistência desejada, tolerância a partições, latência, custo de sincronização, rebalanço, recuperação, observabilidade e complexidade operacional. O desenho deve indicar o que o sistema faz quando uma réplica está atrasada, quando uma partição perde quorum e quando o consumidor lê dados antigos.
