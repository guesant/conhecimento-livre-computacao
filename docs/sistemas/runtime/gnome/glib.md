# GLib

GLib é uma biblioteca de utilidades em C usada amplamente no ecossistema
GNOME. Ela oferece tipos de dados, strings, arquivos, processos, threads,
event loop, I/O assíncrono, configuração e integração multiplataforma. GLib
não é um toolkit visual e não substitui GTK.

## Main loop

O main loop recebe sources como timers, watchers de arquivos, sockets e
callbacks de I/O. A aplicação registra uma source e o loop a agenda quando há
trabalho. Uma callback longa bloqueia as demais sources, por isso o código deve
ser curto ou delegar trabalho pesado.

## GIO e I/O

GIO fornece abstrações para streams, arquivos, sockets, processos, proxies e
operações assíncronas. A API pode integrar callbacks, cancellables e objetos
GObject. O cancelamento deve ser tratado como parte do lifecycle e não como
uma garantia de que um efeito externo foi desfeito.

## Dados e portabilidade

GList, GHashTable, GString, variantes e outras estruturas reduzem boilerplate,
mas ownership e liberação continuam importantes em C. Convenções de referência,
transferência e finalização precisam ser seguidas, principalmente quando a API
é acessada por bindings como GJS.

## Relações

- [GObject](gobject.md) fornece o sistema de tipos e o modelo de objetos.
- [GJS](gjs.md) acessa APIs GLib por introspecção.
- [GNOME](../../desktop/gnome.md) reúne o ambiente que utiliza essas
  bibliotecas.

## Fonte primária

- [GLib API reference](https://docs.gtk.org/glib/)
- [GIO API reference](https://docs.gtk.org/gio/)
