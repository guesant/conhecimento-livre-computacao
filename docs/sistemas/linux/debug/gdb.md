# GDB

GDB, GNU Debugger, é um debugger para observar e controlar a execução de
programas. Ele pode iniciar um processo, anexar a um processo existente,
inspecionar um core dump ou conversar com um stub remoto. GDB não é um
profiler completo, não corrige automaticamente um defeito e não substitui
testes, logs ou tracing.

## Símbolos e compilação

Para relacionar endereços a funções, arquivos e linhas, compile com informação
de debug, normalmente usando `-g`. Otimizações podem reordenar, eliminar ou
fundir variáveis e instruções, então o código observado pode não corresponder
literalmente ao fonte.

Uma prática comum é produzir um binário otimizado e guardar símbolos de debug
em um artefato separado. Isso reduz o tamanho do deploy sem perder a capacidade
de investigar crashes, desde que o arquivo de símbolos corresponda exatamente
ao build que falhou.

## Sessão básica

```bash
gdb --args ./programa --config ./dev.conf
```

Dentro da sessão, `break main` cria um breakpoint, `run` inicia a execução,
`continue` retoma, `next` avança sem entrar na função, `step` entra na função,
`backtrace` mostra a pilha e `print expressao` avalia uma expressão no contexto
atual.

```text
(gdb) break main
(gdb) run
(gdb) backtrace
(gdb) info locals
(gdb) print valor
(gdb) continue
```

Use breakpoints condicionais quando a falha depende de uma entrada específica.
Watchpoints são úteis para descobrir quando uma variável ou endereço é alterado,
mas podem ter custo alto e devem ser usados sobre um caso reduzido.

## Processos, threads e sinais

GDB pode mostrar threads, alternar o contexto e inspecionar pilhas individuais.
Uma parada em um breakpoint normalmente interrompe o processo inteiro para
manter um estado observável. O debugger pode alterar o comportamento de timing
de um programa concorrente, por isso uma falha que desaparece sob depuração não
está necessariamente resolvida.

Sinais, exceções, aborts e falhas de memória devem ser analisados considerando
o sistema operacional, o loader, bibliotecas e o processo que gerou o evento.
Ferramentas como `strace`, sanitizers e core dumps podem fornecer evidências
mais representativas quando uma sessão interativa muda o timing.

## Core dump e pós-morte

Um core dump preserva parte do estado de um processo no momento de uma falha.
Ele deve ser aberto com o executável e os símbolos correspondentes:

```bash
gdb ./programa core.1234
```

Depois de obter `backtrace`, registradores, threads e variáveis relevantes,
relacione o endereço ao build, ao commit e às bibliotecas carregadas. Core dumps
podem conter credenciais, dados pessoais e payloads de requisição. Restrinja
permissões, retenção e distribuição como faria com logs sensíveis.

## Depuração remota

No debugging remoto, o processo alvo conversa com um stub ou servidor que
entende o protocolo do GDB. O GDB local usa os símbolos e o fonte, enquanto o
alvo executa o binário. A versão da arquitetura, ABI, bibliotecas e protocolo
precisa ser compatível.

Não exponha um servidor de debugging em uma interface pública. Use uma rede
administrativa protegida, autenticação quando disponível, firewall e uma janela
controlada de operação. O debugger pode ler e alterar a memória do processo.

## Limitações e segurança

Anexar GDB exige permissões do sistema e pode interromper um serviço. Nunca
anexe ou execute comandos em um processo privilegiado sem entender o impacto.
Evite executar scripts de inicialização não auditados, carregar plugins
desconhecidos ou abrir um core dump de origem não confiável em um ambiente que
tenha acesso a dados sensíveis.

## Relações

- [Inspeção de binários](../binarios/index.md) reúne `file`, `readelf`,
  `ldd` e metadados de executáveis.
- [strip](../binarios/strip.md) remove ou separa símbolos de um binário.
- [xxd](../binarios/xxd.md) exibe bytes, mas não interpreta o fluxo de
  execução.
- [strace](../../../ferramentas/diagnostico/strace.md) observa syscalls, não
  substitui breakpoints e inspeção de variáveis.

## Fontes primárias

- [GDB documentation](https://sourceware.org/gdb/documentation/)
- [GDB documentation index](https://sourceware.org/gdb/documentation/)
- [GNU GDB source repository](https://sourceware.org/git/binutils-gdb.git)
