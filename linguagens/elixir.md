# Elixir

Elixir é uma linguagem funcional, dinâmica e concorrente que executa na
máquina virtual BEAM. Ela combina pattern matching, imutabilidade, funções de
primeira classe e sintaxe voltada a produtividade com os processos leves,
supervisão e distribuição oferecidos pelo ecossistema Erlang/OTP.

Elixir não é apenas um framework web. Phoenix, Ecto e outras bibliotecas são
projetos do ecossistema; a linguagem e o runtime continuam sendo conceitos
separados.

## Modelo de execução

Processos da BEAM são unidades isoladas de execução que comunicam por mensagens.
Eles não compartilham memória mutável como o modelo comum de threads. Um
processo pode falhar sem corromper diretamente o estado privado de outro, mas
mensagens, filas, memória e supervisores ainda precisam de limites.

O scheduler da BEAM distribui processos por schedulers e threads do runtime.
Isso favorece muitas unidades concorrentes, porém não elimina custos de CPU,
garbage collection, I/O, serialização e contenção de recursos externos.

## Imutabilidade e pattern matching

Dados imutáveis permitem que processos raciocinem sobre seu estado sem
sincronizar escritas compartilhadas. Pattern matching descreve a forma esperada
de valores e torna comum modelar sucesso, falha e mensagens como tuplas ou
estruturas explícitas.

Imutabilidade não impede crescimento de memória. Referências mantidas por
processos, filas de mensagens e caches continuam vivas até serem liberadas.
Monitore mailbox, heap por processo, latência de garbage collection e tamanho
de estruturas.

## OTP e supervisão

OTP fornece comportamentos, supervisores, aplicações, releases e bibliotecas
para organizar sistemas concorrentes. Um supervisor reinicia componentes de
acordo com uma estratégia declarada. Isso é diferente de capturar qualquer
exceção e reiniciar indefinidamente: falhas persistentes podem causar loops,
tempestades de restart e perda de disponibilidade.

Defina árvore de supervisão, limites de reinício, estratégias de escalonamento,
timeouts e o que deve acontecer quando uma dependência externa está
indisponível. A política de recuperação deve preservar idempotência e não
duplicar efeitos externos.

## Distribuição

Nós BEAM podem trocar mensagens e executar processos distribuídos. A rede não
transforma comunicação remota em chamada local. Partições, atrasos, perda de
mensagens, autenticação entre nós, versionamento e divergência de relógio
precisam ser tratados explicitamente.

Distribuição também amplia a superfície de segurança. Restrinja portas,
proteja cookies de nós, use redes confiáveis e monitore conexões. Não exponha
um nó distribuído diretamente à Internet sem entender o protocolo e a
autenticação usados.

## Toolchain e aplicações

Mix gerencia projetos, dependências, testes e tarefas. Hex distribui pacotes e
releases normalmente empacotam o runtime ou dependem de uma instalação
compatível de Erlang/OTP. Fixe Elixir, OTP, dependências, flags e bibliotecas
nativas para obter builds reproduzíveis.

Elixir é adequado para serviços concorrentes, sistemas de mensagens, APIs,
processamento de eventos e aplicações que precisam de recuperação estruturada.
É menos conveniente quando o ecossistema exigido depende principalmente de
bibliotecas que só existem em outra plataforma ou quando o modelo de processos
não combina com o domínio.

## Relações

- [Erlang](erlang.md) usa a BEAM e os princípios de OTP com outra sintaxe e
  ecossistema.
- [BEAM](https://www.erlang.org/doc/system_principles/system_principles.html)
  é a família de runtime que executa Erlang, Elixir e outras linguagens.
- [JVM](jvm.md) e [V8](../sistemas/runtime/v8.md) são outros modelos de
  runtime, com diferentes unidades de execução e garbage collectors.

## Fontes primárias

- [Elixir documentation](https://hexdocs.pm/elixir/introduction.html)
- [Elixir language](https://elixir-lang.org/)
- [Mix and OTP guide](https://hexdocs.pm/elixir/mix-otp/introduction-to-mix.html)
- [Erlang/OTP documentation](https://www.erlang.org/docs.html)
