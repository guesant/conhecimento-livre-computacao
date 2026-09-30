# Dependências systemd

Dependências systemd possuem responsabilidades diferentes. Algumas determinam
ordem, outras exigem existência ou sucesso e outras propagam ações de
lifecycle.

## Ordem e requisito

`After=` e `Before=` ordenam jobs, mas não iniciam nem exigem a unit
referenciada. `Wants=` tenta ativar uma dependência fraca. `Requires=`
expressa uma dependência forte. Em muitos casos, `Requires=` precisa ser
combinado com `After=` para que requisito e ordem descrevam a intenção.

`BindsTo=` é mais estrito quando a unit ligada desaparece. `PartOf=`
propaga paradas e reinícios, mas não cria automaticamente uma cadeia de
ativação.

## Failure modes

Adicionar `After=network.target` não prova que a rede possui conectividade.
Uma aplicação que exige DNS, rota ou serviço externo precisa expressar ou
verificar essa prontidão no lugar correto. Adicionar `Requires=` sem
`After=` pode permitir que uma unit comece antes da dependência ter sido
iniciada.

Dependências circulares, timeouts baixos e restart loops aparecem como jobs
pendentes, units em `activating` ou cascatas de falha. Use
`systemctl list-dependencies`, `systemctl show` e o journal para observar a
relação efetiva.

## Relações

- [systemd unit](unit.md) mostra onde dependências são declaradas.
- [systemd service](service.md) usa dependências para representar readiness.
- [systemd target](target.md) compõe estados do host.

## Fonte primária

- [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
