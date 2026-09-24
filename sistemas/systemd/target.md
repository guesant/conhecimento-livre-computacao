# systemd target

Uma target é uma unit que agrupa outras units e representa um estado lógico do
sistema. Ela não precisa possuir um processo próprio. Targets substituem o
modelo de runlevels como pontos de sincronização e composição.

## Agrupamento

Uma target pode usar `Wants=` para iniciar um conjunto de units sem tornar a
falha de cada membro uma falha obrigatória da target. `Requires=` declara uma
relação forte. `WantedBy=` em uma unit cria a relação inversa usada por
`systemctl enable`.

O fato de uma service pertencer a uma target não significa que ela esteja
sempre ativa. A relação define o que será iniciado quando a target for
ativada; o estado real ainda pode mudar depois.

## Targets comuns

`multi-user.target` representa um sistema sem ambiente gráfico, enquanto
`graphical.target` adiciona o ambiente gráfico quando presente. O target
padrão pode ser consultado e alterado com `systemctl get-default` e
`systemctl set-default`.

## Diagnóstico

Use `systemctl list-dependencies nome.target` para visualizar a composição e
`systemctl isolate nome.target` somente quando a mudança de estado for
intencional e operacionalmente segura. Isolar uma target pode parar services
que não pertencem ao novo estado.

## Relações

- [systemd unit](unit.md) apresenta o modelo comum.
- [Dependências systemd](dependencies.md) explica `Wants=` e `Requires=`.
- [systemd service](service.md) é o tipo mais comum agrupado por uma target.

## Fonte primária

- [systemd.target](https://www.freedesktop.org/software/systemd/man/latest/systemd.target.html)
