# strace

`strace` observa chamadas de sistema, sinais e respostas do kernel associadas a um processo. Ele torna visível a fronteira entre o código da aplicação e operações como abrir arquivos, resolver nomes, criar sockets, ler, escrever, aguardar e alterar atributos.

## O que ele revela

Mensagens de aplicação como "arquivo não encontrado" e "permissão negada" podem ser insuficientes quando há múltiplos caminhos de configuração, links simbólicos, namespaces ou usuários efetivos. O `strace` mostra o caminho tentado e o erro retornado pelo kernel, permitindo distinguir configuração incorreta de ausência de capacidade.

Ele também ajuda a identificar dependências implícitas: um processo que parece iniciar sem rede pode estar bloqueado esperando DNS; um serviço que não termina pode estar aguardando um descritor; um binário pode estar procurando uma biblioteca ou arquivo em uma localização inesperada.

## Anexar ou iniciar

Iniciar o processo sob observação captura desde o começo, mas pode exigir alterar o comando de execução. Anexar a um processo existente preserva seu contexto, mas pode perder a falha que já ocorreu e depende das permissões do kernel e do usuário que executa o diagnóstico.

Em containers, o processo pode estar em outro PID namespace e a política de segurança pode impedir a observação. Ter UID zero dentro do container não equivale a possuir todas as capabilities do host.

## Custo e interpretação

Interpor-se em cada chamada de sistema altera o tempo de execução e pode aumentar o volume de saída. Use filtros por chamada, processo ou descritor e uma janela curta. O traço deve responder a uma hipótese, não ser coletado indefinidamente para depois procurar um problema.

Uma chamada bloqueada não significa necessariamente que o kernel está com defeito. Ela pode ser o comportamento esperado de uma operação síncrona, de um socket sem dados ou de um processo aguardando outro componente. Interprete a sequência de chamadas junto com o estado do processo e as métricas do host.

## Segurança

O traço pode revelar argumentos contendo caminhos, nomes, tokens e partes de dados transmitidos. Armazene a saída como dado sensível. Não encaminhe um traço para logs públicos nem o inclua em uma issue sem revisar seu conteúdo.

## Relação com outras ferramentas

[tcpdump](tcpdump.md) observa pacotes no caminho de rede. `strace` mostra se e quando o processo pediu ao kernel para iniciar essa comunicação. [iperf3](iperf3.md) mede o caminho sob tráfego controlado. A página de [diagnóstico técnico](../../diagnostico/index.md) organiza essas fronteiras.

## Fonte primária

Consulte o [projeto upstream do strace](https://strace.io/) para a documentação da versão instalada e as limitações de suporte do sistema operacional.
