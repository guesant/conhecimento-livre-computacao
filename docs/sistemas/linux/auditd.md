# auditd

`auditd` é o daemon do Linux Audit. Ele recebe eventos produzidos pelo kernel e
por componentes de user space e grava registros que permitem reconstruir ações
relacionadas a identidade, processos, arquivos, capabilities e chamadas de
sistema. Ele não é um antivírus nem um sistema de detecção completo: registra
fatos segundo regras, enquanto a interpretação, retenção e resposta pertencem
à operação.

## Modelo de eventos

Um evento de auditoria pode envolver várias mensagens com o mesmo `event ID`.
Uma execução de `execve`, por exemplo, pode produzir a chamada, o caminho
resolvido, os argumentos, o usuário efetivo e o resultado. Correlacionar apenas
uma linha pode omitir parte da operação. O campo `auid` é especialmente útil
para atribuir a sessão original mesmo quando há troca de usuário, enquanto
`uid`, `euid`, `suid` e `fsuid` descrevem identidades diferentes do processo.

As regras podem observar chamadas de sistema, caminhos, diretórios, alterações
de identidade e eventos de autenticação. Regras por syscall são amplas e podem
gerar muito volume; regras por caminho são mais focadas, mas não capturam toda
forma de alteração indireta. O desenho deve começar pelos eventos que precisam
ser provados, não por habilitar tudo.

## Regras e persistência

As regras temporárias, aplicadas com `auditctl`, são úteis para investigação,
mas desaparecem quando o serviço é reiniciado. Regras persistentes devem ficar
em `/etc/audit/rules.d/` e ser carregadas pelo mecanismo de distribuição da
distribuição. Valide a configuração antes de recarregar, porque uma regra
inválida pode impedir o serviço de iniciar ou deixar a cobertura diferente da
esperada.

Exemplo de observação de alterações em um diretório sensível:

```text
-w /etc/sudoers.d -p wa -k sudoers_changes
```

O exemplo registra escrita e alteração de atributos. A chave `sudoers_changes`
facilita a busca, mas não substitui a documentação de por que aquele diretório
é importante, por quanto tempo os registros serão guardados e quem pode apagar
ou alterar a coleta.

## Integridade e limites

Um atacante com privilégios suficientes pode tentar parar o daemon, alterar
regras, apagar arquivos locais ou causar perda por saturação da fila. Encaminhe
os eventos para armazenamento com controle de acesso e retenção, monitore
`backlog`, perdas e erros de gravação e restrinja quem administra o sistema de
auditoria. A presença de um registro não prova que o evento foi enviado para
um destino externo nem que seu conteúdo permaneceu íntegro.

O modo de falha precisa ser uma decisão. Em um sistema crítico, bloquear uma
operação quando a fila de auditoria está cheia pode preservar a prova, mas
também interromper o serviço. Em outro ambiente, descartar eventos pode ser
aceitável apenas com alerta, limite e retenção alternativa. Não existe uma
política segura sem conhecer o custo de perder o evento e o custo de parar a
operação.

## Diagnóstico

Ao investigar, compare regras carregadas, status do serviço, logs do kernel,
ocupação da fila, espaço em disco, permissões e horário do sistema. Use
`ausearch` para buscar eventos correlacionados e `aureport` para sumarizar
categorias, mas preserve também o registro bruto para uma auditoria posterior.
Não use uma busca textual simples como prova de ausência: um filtro errado,
um relógio divergente ou um evento perdido pode produzir um resultado vazio.

## Relações

- [Syscalls](../kernel/system-calls.md) explica a interface observada por muitas regras.
- [SELinux](../../seguranca/mac-selinux.md) e [AppArmor](../../seguranca/mac-apparmor.md) aplicam controle, enquanto auditd registra fatos.
- [Sistemas de auditoria](../../auditoria-e-abordagens.md) trata retenção, evidência e revisão.

## Fontes primárias

- [Linux Audit documentation](https://linux-audit.com/)
- [audit-userspace no kernel Linux](https://github.com/linux-audit/audit-userspace)
- [auditd.conf](https://man7.org/linux/man-pages/man5/auditd.conf.5.html)
- [audit.rules](https://man7.org/linux/man-pages/man8/audit.rules.8.html)
