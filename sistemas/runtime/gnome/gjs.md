# GJS

GJS, GNOME JavaScript, é um runtime que usa JavaScript para acessar APIs do
ecossistema GNOME por meio de GObject Introspection. Ele não é Node.js e não
oferece automaticamente o mesmo modelo de módulos, filesystem, servidor HTTP
ou package manager.

## Integração com GNOME

O código GJS importa namespaces introspectáveis, cria objetos GObject e
conecta sinais. A aplicação pode usar GLib para main loop, I/O, processos,
timers e utilitários, além de bibliotecas GNOME e GTK quando essas estiverem
instaladas.

GObject Introspection expõe metadados sobre tipos, métodos, propriedades e
signals. A qualidade da API depende da biblioteca C e dos metadados disponíveis.
Nem toda função C é automaticamente segura ou idiomática em JavaScript.

## Modelo assíncrono

O main loop de GLib coordena sources, callbacks e sinais. Código síncrono longo
bloqueia a interface e impede que outras sources sejam processadas. Use APIs
assíncronas quando disponíveis, divida trabalho e mova operações pesadas para
um worker ou processo quando a aplicação exigir responsividade.

## Segurança

GJS possui acesso às APIs que o processo hospedeiro expõe. Não execute scripts
externos como se fossem dados. Controle caminhos, argumentos de processos,
arquivos e extensões. A presença de uma engine JavaScript não cria uma
sandbox para código não confiável.

## Fontes primárias

- [GJS Guide](https://gjs.guide/)
- [GNOME JavaScript documentation](https://gitlab.gnome.org/GNOME/gjs/-/blob/master/doc/Guide.md)
- [GObject Introspection](https://gi.readthedocs.io/en/latest/)
