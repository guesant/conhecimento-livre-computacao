# GObject

GObject é o sistema de tipos e objetos baseado em C usado por GLib e GNOME.
Ele oferece identificação de tipos em runtime, herança, interfaces,
properties, signals, referências e convenções para construir APIs extensíveis
sem depender de classes nativas da linguagem C.

## Tipos e ciclo de vida

Cada instância possui um tipo registrado. Referências contam o tempo de vida
conforme as regras da API. Uma propriedade pode ter validação, default e
notificação. Um signal permite que consumidores se conectem a eventos do
objeto, mas a conexão precisa ser removida ou associada ao ciclo de vida
correto para não reter objetos ou disparar callbacks depois da destruição.

Herança e interfaces definem contratos reutilizáveis. A API deve deixar claro
quem possui uma referência, quem pode alterar uma propriedade e em qual thread
um signal pode ser emitido.

## Introspection

Metadados GObject Introspection descrevem funções, tipos, propriedades e
signals para que linguagens como GJS possam consumi-los. A introspecção não
remove regras de ownership, threads ou tratamento de erros. Bindings podem
expor tipos de forma diferente da API C e precisam ser testados no runtime
específico.

## Não é um toolkit

GObject não desenha widgets e não é o event loop completo. GLib oferece
infraestrutura comum; GTK fornece uma camada de interface visual. Separar as
responsabilidades ajuda a escolher dependências menores para uma biblioteca ou
serviço.

## Fonte primária

- [GObject API reference](https://docs.gtk.org/gobject/)
- [GObject Introspection](https://gi.readthedocs.io/en/latest/)
- [GLib](https://docs.gtk.org/glib/)
