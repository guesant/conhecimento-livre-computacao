# Backup do CloudNativePG

O CloudNativePG combina backup completo e arquivamento contínuo do
write-ahead log para permitir recuperação para um ponto no tempo. O backup
completo fornece a base; os segmentos de WAL posteriores permitem chegar a um
instante específico em vez de voltar somente ao momento do último backup.

O status do operator precisa ser verificado de forma recorrente. Uma credencial
expirada ou um destino inacessível pode interromper o arquivamento sem que a
configuração declarada deixe de parecer correta. WAL que não consegue ser
arquivado também pode se acumular no disco do banco e transformar uma falha de
backup em incidente de capacidade.

`pg_dump` é outra categoria de cópia. Ele é um backup lógico útil para migração
entre versões e bancos pequenos, mas não guarda o histórico de mudanças do WAL
e não permite recuperação para qualquer instante posterior ao dump.

## Restauração

Uma recuperação do CloudNativePG normalmente cria um cluster novo a partir do
backup. O cluster restaurado pode ser validado ao lado do original antes do
corte, reduzindo o risco de substituir dados ainda necessários durante o
procedimento.

## Relações

- [CloudNativePG](../../kubernetes/extensibility/cloudnative-pg.md) explica o
  operator e seus limites.
- [RPO](rpo.md) define a perda de dados aceitável.
- [Teste de restauração](teste-de-restauracao.md) trata da validação da cópia.

## Fonte primária

- [CloudNativePG, backup](https://cloudnative-pg.io/documentation/current/backup/)
