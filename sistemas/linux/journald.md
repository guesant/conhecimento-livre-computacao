# Journal persistente

journald é o componente do systemd que armazena eventos estruturados de
serviços, kernel e unidades. Sem armazenamento persistente configurado, parte
do journal pode existir apenas em memória e desaparecer no reboot.

## Persistência e retenção

A persistência exige um diretório de journal em disco e uma política de
retenção. O limite de espaço é necessário porque logs sem retenção competem
com dados de aplicação, imagens, volumes e o próprio sistema.

Rotação e compressão devem ser avaliadas junto da capacidade do disco. Um host
que perdeu espaço pode parar serviços mesmo quando a causa inicial foi apenas
um log crescente.

## Consulta

`journalctl -b` restringe a inicialização atual. `journalctl -u nome.service`
filtra por unit e `journalctl -k` mostra eventos do kernel. Use intervalo de
tempo e prioridade para reduzir o volume antes de procurar o evento causal.

Quando um processo escreve seu próprio arquivo, logrotate ainda pode ser
necessário. Depois de renomear um arquivo, o processo pode continuar usando o
descritor antigo até receber um sinal ou reabrir o log.

## Failure modes

Se os logs desaparecem no reboot, confirme o diretório de armazenamento e a
permissão de escrita. Se o journal ocupa todo o disco, ajuste retenção e
investigue a origem do volume antes de apenas apagar dados. Se um serviço não
aparece, confirme a unit, o namespace de execução e se ele escreve em outro
backend.

## Relações

- [systemd service](../systemd/service.md) produz eventos de lifecycle.
- [Fail2ban](fail2ban.md) depende de logs confiáveis para detectar falhas.
- [Atualizações automáticas](automatic-updates.md) deve registrar a execução.

## Fonte primária

- [systemd-journald](https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html)
