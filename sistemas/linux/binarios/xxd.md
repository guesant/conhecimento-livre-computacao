# xxd

`xxd` é um utilitário para produzir um hexdump de arquivos ou de entrada
padrão. Ele mostra bytes em hexadecimal e uma representação textual, e também
pode reconstruir bytes a partir de um dump em formatos compatíveis. O programa
é distribuído com o Vim e serve para inspeção, pequenos patches e diagnóstico
de formatos binários.

`xxd` não é um parser ELF, um desassembler, um verificador de assinatura ou um
editor estrutural. A saída mostra bytes; interpretar o significado deles exige
conhecer o formato, endianness, offsets e versão do protocolo.

## Dump básico

```bash
xxd arquivo.bin
xxd -g 1 -c 16 arquivo.bin
xxd -l 64 arquivo.bin
xxd -s 128 -l 64 arquivo.bin
```

`-g` escolhe o agrupamento dos bytes, `-c` controla quantos bytes aparecem por
linha, `-l` limita o tamanho e `-s` começa em um offset. A coluna hexadecimal
mostra os valores e a coluna textual representa bytes imprimíveis.

Para um dump contínuo, sem espaços e sem a coluna ASCII, use `-p`:

```bash
xxd -p arquivo.bin
```

Esse formato é conveniente para transportar bytes como hexadecimal, mas não
deve ser confundido com Base64, texto UTF-8 ou uma codificação de protocolo.

## Reconstrução

`-r` faz a operação inversa para dumps que seguem um formato que `xxd` consiga
interpretar:

```bash
xxd -r dump.hex arquivo-restaurado.bin
xxd -r -p dump-continuo.hex arquivo-restaurado.bin
```

Use um arquivo de saída diferente do original, compare tamanho e checksum e
valide o formato com a ferramenta correspondente. Um hexdump truncado pode
produzir um arquivo aparentemente válido, mas com dados ausentes.

## Inspeção segura

O dump é uma representação dos bytes, não uma prova de origem ou integridade.
Ao investigar artefatos desconhecidos, trabalhe em uma cópia sem permissões de
execução e combine `xxd` com checksums, assinaturas, `file`, `readelf` ou um
parser específico.

Não redirecione a saída para o mesmo arquivo de entrada. Verifique os offsets
antes de usar `-r` ou modos de escrita e mantenha o artefato original para
comparação e recuperação.

## Casos de uso

`xxd` é útil para verificar magic numbers, comparar cabeçalhos, localizar
bytes de uma estrutura, confirmar endianness, investigar diferenças entre
arquivos e preparar uma pequena alteração reproduzível. Para mudanças maiores,
use uma ferramenta que conheça o formato e gere uma validação estrutural.

Para analisar um executável, a sequência pode começar assim:

```bash
file ./programa
xxd -l 32 ./programa
readelf -h ./programa
```

O primeiro comando identifica o formato, o segundo mostra o cabeçalho bruto e o
terceiro interpreta a estrutura ELF. Cada etapa responde uma pergunta
diferentemente; uma não substitui a outra.

## Relações

- [Inspeção de binários](index.md) reúne ferramentas para
  formato, loader, bibliotecas e metadados.
- [strip](strip.md) altera símbolos e seções de um objeto, enquanto `xxd`
  apenas representa bytes até que seja usado com `-r`.
- [readelf](https://sourceware.org/binutils/docs/binutils/readelf.html)
  interpreta estruturas ELF.

## Fontes primárias

- [xxd source in Vim](https://github.com/vim/vim/tree/master/src/xxd)
- [xxd manual](https://vimhelp.org/xxd.txt.html)
- [Vim source repository](https://github.com/vim/vim)
