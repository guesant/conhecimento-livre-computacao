# logrotate

logrotate limita o crescimento de arquivos de log que não são administrados
pelo journald. Ele pode renomear, comprimir, reter e remover arquivos segundo
idade ou quantidade de rotações.

## Ciclo de rotação

O processo abre um arquivo por descritor. Renomear o caminho não move o
descritor já aberto: a aplicação pode continuar escrevendo no arquivo antigo.
Por isso uma configuração de rotação pode precisar de `copytruncate`, de um
sinal de reopen ou de um comando de pós-rotação, conforme o comportamento da
aplicação.

`copytruncate` evita a necessidade de reopen, mas possui uma janela em que
linhas podem ser perdidas. Reabrir o arquivo é geralmente mais limpo quando a
aplicação oferece esse mecanismo.

## Retenção

Defina tamanho máximo, idade, quantidade de cópias e compressão com base em
capacidade e necessidade de diagnóstico. Remover logs cedo demais pode
eliminar evidência de incidente; retê-los indefinidamente pode derrubar o
host por falta de espaço.

## Relações

- [Journal persistente](journald.md) cobre logs estruturados do systemd.
- [systemd timer](../systemd/timer.md) pode disparar manutenção periódica.
- [Capacidade e resiliência](../../confiabilidade/testes/index.md) relaciona retenção
  com limites operacionais.

## Fonte primária

- [logrotate](https://github.com/logrotate/logrotate)
