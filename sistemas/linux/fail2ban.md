# Fail2ban

Fail2ban observa logs, identifica padrões repetidos de falha e solicita ao
firewall um bloqueio temporário para a origem correspondente. Ele reage depois
da tentativa e não substitui autenticação forte, hardening ou firewall.

## Modelo

Um jail combina um filtro, um log, um limite de tentativas, uma janela de
tempo e uma ação. O filtro precisa reconhecer a mensagem real produzida pelo
serviço. A ação precisa bloquear no mecanismo efetivamente usado pelo host,
como nftables ou iptables compatível.

O bloqueio é estado operacional. Uma origem legítima pode ser bloqueada por
um filtro amplo, por NAT compartilhado ou por uma janela configurada sem
considerar o comportamento do serviço.

## Limites

Fail2ban não torna senha fraca segura e não impede exploração que não produza
o padrão de log esperado. Um atacante distribuído pode evitar o limite por
origem. Firewall, chaves SSH, MFA quando disponível, atualização e redução da
superfície continuam necessários.

## Diagnóstico

Confirme que o serviço escreve no log lido pelo jail, valide o filtro com uma
linha real, confira o backend de firewall e observe as prisões ativas. Se o
ban aparece no log mas não bloqueia o tráfego, o problema está na ação ou na
ordem das regras, não na detecção.

## Relações

- [Journal persistente](journald.md) preserva o log necessário ao diagnóstico.
- [Netfilter e nftables](../../netfilter-nftables-e-diagnostico.md) executa o
  bloqueio.
- [Atualizações automáticas](automatic-updates.md) reduz vulnerabilidades que
  não são tratadas por bloqueio reativo.

## Fontes primárias

- [Fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page)
- [nftables wiki](https://wiki.nftables.org/)
