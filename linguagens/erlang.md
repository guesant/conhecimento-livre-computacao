# Erlang

Erlang é uma linguagem funcional, concorrente e distribuída criada para
sistemas que precisam continuar operando diante de falhas. Ela executa no
runtime Erlang/OTP, normalmente conhecido por BEAM ou ERTS, e usa processos
leves, troca de mensagens, supervisão e atualização controlada de software.

Erlang e OTP não são sinônimos. Erlang é a linguagem; ERTS fornece o runtime; e
OTP reúne bibliotecas, comportamentos, ferramentas e princípios de projeto que
organizam aplicações de produção.

## Processos e mensagens

Processos Erlang têm estado privado e se comunicam por mensagens. O isolamento
reduz a necessidade de locks para estado local, mas não elimina condições de
corrida no protocolo, filas sem limite, mensagens fora de ordem ou falhas entre
serviços.

O scheduler da BEAM distribui processos sobre schedulers e threads do runtime.
O modelo favorece muitas unidades concorrentes e tolera espera de I/O, mas uma
função CPU-bound, uma fila de mensagens crescente ou um NIF bloqueante ainda
pode degradar o sistema.

## Supervisão e tolerância a falhas

A ideia de deixar processos falharem é acompanhada por supervisão, reinício e
isolamento. Um supervisor conhece seus filhos e aplica uma estratégia quando
um deles termina. A árvore precisa distinguir uma falha recuperável de uma
falha que exige interromper um grupo inteiro.

Reiniciar não corrige automaticamente estado externo, mensagens já enviadas ou
efeitos parcialmente concluídos. Operações devem ser idempotentes, ter
timeouts e registrar correlação suficiente para que um operador entenda o
motivo da recuperação.

## OTP

OTP define comportamentos como `gen_server`, `supervisor` e `gen_statem`, além
de aplicações, releases e bibliotecas para sistemas concorrentes. Esses
comportamentos oferecem convenções de ciclo de vida e chamadas, mas não
substituem o desenho do protocolo do domínio.

Uma aplicação OTP deve definir sua árvore de supervisão, dependências,
estratégia de shutdown, limites de restart, configuração e observabilidade.
Misturar componentes sem conhecer seus donos de estado pode produzir ordem de
inicialização incorreta e recuperação incompleta.

## Distribuição e atualização

Nós Erlang podem formar sistemas distribuídos e trocar mensagens. A rede
introduz atrasos, particionamento, autenticação, falhas de nó e necessidade de
versionar protocolos. Uma chamada remota não tem as mesmas garantias de uma
função local.

O runtime oferece mecanismos para atualização de código e releases, mas uma
implantação segura precisa controlar compatibilidade entre versões, migração de
estado, rollback e dependências externas. Hot code loading não torna qualquer
mudança compatível nem substitui uma estratégia de release.

## Memória e operação

O garbage collector opera por processo, e o consumo deve ser analisado por
heap, mailbox, tabelas ETS, binários e processos que mantêm referências. Uma
aplicação com muitos processos ainda pode saturar CPU, memória, sockets ou
filas de mensagens.

Instrumente latência, reinícios, tamanho de mailboxes, filas, schedulers,
memória e mensagens entre nós. O diagnóstico deve diferenciar um problema do
runtime de um protocolo que envia trabalho demais ou mantém estado sem limite.

## Escolha

Erlang/OTP é forte quando disponibilidade, concorrência, supervisão,
distribuição e recuperação são requisitos centrais. A curva de aprendizado
inclui o modelo de processos, pattern matching, OTP, observabilidade e
limitações da distribuição. Para um serviço simples sem necessidade dessas
propriedades, outra linguagem pode reduzir o custo de operação.

## Relações

- [Elixir](elixir.md) usa a BEAM e os princípios de OTP com outra sintaxe e
  ecossistema.
- [Concorrência](../engenharia-software/concorrencia/modelos/concorrencia.md)
  diferencia unidades de execução e paralelismo.
- [Filas](../dados/mensageria/filas.md) ajuda a comparar mensagens entre
  processos com mensageria durável.

## Fontes primárias

- [Erlang/OTP documentation](https://www.erlang.org/docs.html)
- [Erlang Reference Manual](https://www.erlang.org/doc/system_principles/system_principles.html)
- [OTP Design Principles](https://www.erlang.org/doc/system_principles/system_principles.html)
- [Erlang/OTP source repository](https://github.com/erlang/otp)
