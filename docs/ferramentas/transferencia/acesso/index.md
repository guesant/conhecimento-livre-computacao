# Acesso a arquivos remotos

Acesso remoto a arquivos significa operar sobre uma árvore que permanece em
outro host. Isso é diferente de transferir uma cópia: latência, indisponibilidade
do servidor e permissões remotas passam a fazer parte do comportamento do
processo local.

## Ferramentas

- [SSHFS](../sshfs.md) monta um filesystem remoto usando o subsistema SFTP do
  SSH.
- [rsync](../rsync.md) pode ser usado como operação de sincronização, mas não
  cria uma montagem persistente.
- [Dolphin](../dolphin.md) usa workers KIO para navegar por recursos remotos no
  desktop KDE.

## Cuidados

Montagens remotas não devem ser tratadas como discos locais. É necessário
considerar timeouts, reconexão, cache, consistência, bloqueios, comportamento
de processos quando a rede cai e o limite de confiança entre cliente e
servidor. Para jobs previsíveis, uma cópia explícita costuma ser mais fácil de
observar e recuperar.
