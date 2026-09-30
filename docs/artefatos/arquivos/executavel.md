# Arquivo executável

Um arquivo executável contém instruções ou dados que um loader, uma máquina
virtual ou um interpretador pode iniciar. A permissão de execução do filesystem
é apenas uma condição adicional. Um arquivo pode ser executável por uma
associação de extensão, por um shebang, por um loader de bytecode ou por um
formato nativo reconhecido pelo sistema.

## Formatos nativos

| Formato | Ecossistema principal | Características |
| --- | --- | --- |
| ELF | Linux e Unix | Cabeçalhos, segmentos, seções, símbolos e seção dinâmica |
| PE/COFF | Windows | Headers PE, seções, imports, exports e recursos |
| Mach-O | macOS e outros sistemas Apple | Load commands, segmentos, dylibs e slices |
| WASM | WebAssembly | Módulos portáveis executados por um runtime compatível |

O loader verifica arquitetura, tipo, entry point, segmentos, permissões e
dependências. Um executável dinamicamente vinculado ainda depende de loader,
shared libraries, ABI, certificados, configuração e recursos externos.

## Scripts e bytecode

Um arquivo com `#!/usr/bin/env python3`, `#!/bin/sh` ou outro shebang delega a
execução a um interpretador. Um JAR, um `.pyc`, um módulo Lua ou um artefato
JavaScript pode ser iniciado por uma VM ou host. O fato de não conter
instruções nativas não significa que seja inofensivo: o interpretador e as
dependências serão executados com as permissões do processo.

## Regiões e linking

Executáveis podem conter código, dados somente leitura, dados graváveis,
relocations, símbolos, tabelas de imports, notas, recursos e metadata de build.
O linker monta essas regiões e o loader mapeia segmentos na memória. Seções de
debug podem ser separadas do artefato distribuído sem alterar o código que o
loader precisa.

Bibliotecas dinâmicas permitem compartilhar código e atualizar componentes,
mas introduzem resolução de símbolos, dependências transitivas e risco de
carregar uma biblioteca errada. Use pinagem, diretórios controlados e testes de
ABI.

## Verificação

```bash
file ./programa
readelf -h ./programa
readelf -l ./programa
readelf -d ./programa
```

Esses comandos identificam o formato, arquitetura, segmentos, interpretador e
dependências ELF. Em Windows, use ferramentas PE apropriadas; em macOS,
ferramentas Mach-O. A inspeção revela estrutura, não comprova origem, intenção
ou ausência de vulnerabilidades.

## Segurança

Execute artefatos desconhecidos em sandbox e com permissões mínimas. Valide
assinatura, checksum, proveniência e arquitetura antes de instalar. Não confie
em extensões, nomes ou no bit de execução. Cuidado especial é necessário com
scripts, plugins, loaders e arquivos poliglotas, que podem ser interpretados
por mais de uma ferramenta.

## Relações

- [Estrutura binária](estrutura-binaria.md) explica regiões, offsets e
  endianness.
- [GDB](../../sistemas/linux/debug/gdb.md) depura processos e core dumps.
- [strip](../../sistemas/linux/binarios/strip.md) remove ou separa símbolos.
- [Proveniência](../../seguranca/supply-chain/provenance.md) relaciona o
  executável ao processo que o produziu.
