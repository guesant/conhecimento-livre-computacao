# strip

`strip` é um utilitário do GNU Binutils que remove símbolos e outras
informações não necessárias para executar um objeto binário. Ele é usado para
reduzir tamanho de executáveis e bibliotecas, separar símbolos de debug e
preparar artefatos de distribuição.

Remover símbolos não transforma um programa em seguro nem substitui assinatura,
proveniência ou hardening. A operação deve ser feita sobre uma cópia do
artefato de build e registrada no processo de empacotamento.

## O que pode ser removido

Um binário pode conter símbolos de debug, símbolos locais, seções de comentários
e metadados que ajudam ferramentas de análise. A opção usada precisa refletir o
objetivo:

```bash
strip --strip-debug ./programa
strip --strip-unneeded ./biblioteca.so
strip --strip-all ./programa-release
```

`--strip-debug` remove informações de debug. `--strip-unneeded` tenta remover
símbolos que não são necessários para relocação. `--strip-all` remove a maior
parte dos símbolos, mas não deve ser aplicado sem entender o formato, a ABI e
as necessidades do loader.

As opções e o resultado dependem do formato do objeto e da implementação de
Binutils. Antes de distribuir, execute testes de inicialização, carregamento de
plugins, backtraces, unwinding, profiling e integração com ferramentas de
crash reporting.

## Símbolos de debug separados

Para manter o deploy pequeno sem perder a capacidade de investigar crashes, uma
pipeline pode guardar um arquivo de debug separado:

```bash
objcopy --only-keep-debug programa programa.debug
strip --strip-debug programa
objcopy --add-gnu-debuglink=programa.debug programa
```

O arquivo separado deve corresponder byte a byte ao build distribuído. Guarde-o
em um repositório de símbolos com acesso controlado, junto ao build ID, commit,
arquitetura e versão das bibliotecas. Se símbolos de outra revisão forem
usados, o GDB pode mostrar linhas e frames incorretos.

## Riscos operacionais

Aplicar `strip` em um arquivo no lugar pode destruir evidências necessárias
para diagnóstico. Não use a ferramenta como etapa manual em servidores e não
sobrescreva o único exemplar de um artefato. Em imagens de container, execute a
remoção durante o build, depois verifique permissões, ownership, capabilities,
assinatura e checksums do resultado.

Uma redução de tamanho também pode remover símbolos exportados necessários a
carregamento dinâmico, plugins ou integração com outra biblioteca. Bibliotecas
compartilhadas devem ser testadas no ambiente real e com as versões de loader e
dependências previstas.

## Relações

- [GDB](../debug/gdb.md) usa símbolos para produzir backtraces e inspeção de
  código.
- [readelf](https://sourceware.org/binutils/docs/binutils/readelf.html) permite
  verificar seções, símbolos, notas e a seção dinâmica.
- [Proveniência](../../../seguranca/supply-chain/provenance.md) explica como
  relacionar o artefato distribuído ao build que o produziu.

## Fontes primárias

- [GNU Binutils, strip](https://sourceware.org/binutils/docs/binutils/strip.html)
- [GNU Binutils, objcopy](https://sourceware.org/binutils/docs/binutils/objcopy.html)
- [GNU Binutils](https://sourceware.org/binutils/)
