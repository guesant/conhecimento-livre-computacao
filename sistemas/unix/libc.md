# libc

libc é a biblioteca C que fornece uma interface comum para programas Unix e
Linux. Ela reúne funções de memória, strings, arquivos, processos, sockets,
locale, threads e resolução de símbolos, e frequentemente traduz chamadas de
alto nível em syscalls. A libc não é o kernel, nem é necessariamente o runtime
completo de uma linguagem.

## ABI e implementação

glibc, musl e outras implementações oferecem APIs semelhantes com diferenças
de ABI, comportamento, tamanho, resolução DNS, locale e extensões. Um binário
compilado dinamicamente depende do loader, dos símbolos e das versões esperadas.
Estaticamente ligado reduz dependências de runtime, mas pode carregar dados,
resolver DNS de modo diferente e dificultar atualizações de segurança.

`errno` é associado à thread e informa erros de muitas funções. Um código deve
ler o valor imediatamente quando a API o definir; uma chamada intermediária
pode sobrescrevê-lo. Buffering de stdio também significa que sucesso de uma
chamada `write` ao buffer não é o mesmo que dados persistidos no storage.

## Segurança e compatibilidade

LD_PRELOAD, NSS, locale e resolução de nomes tornam o ambiente parte do
comportamento. Setuid e processos privilegiados recebem tratamento especial e
não devem confiar cegamente em bibliotecas ou variáveis do usuário. Atualizar
libc pode corrigir vulnerabilidades, mas exige reiniciar processos que ainda
mantêm a versão antiga carregada.

## Diagnóstico

`ldd`, `readelf -d`, `objdump`, `file` e o loader ajudam a descobrir dependências
e arquitetura. Use ferramentas da mesma plataforma e não execute `ldd` em
binários não confiáveis quando a implementação puder executar o alvo. Para
containers, compare a libc da imagem, o ABI esperado e os módulos nativos.

## Relações

- [Syscalls](../kernel/system-calls.md) trata a fronteira com o kernel.
- [pthread](pthread.md) trata threads POSIX.
- [malloc](malloc.md) trata alocação de memória.

## Fontes primárias

- [glibc manual](https://sourceware.org/glibc/manual/)
- [musl libc](https://musl.libc.org/)
- [Linux man-pages](https://man7.org/linux/man-pages/)
