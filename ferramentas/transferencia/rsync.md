# rsync

rsync sincroniza árvores de arquivos eficientemente, transferindo apenas diferenças relevantes segundo seu algoritmo e opções.

É essencialmente direcional: origem e destino possuem papéis distintos. --delete faz o destino espelhar remoções da origem; não cria sincronização bidirecional.

## Caso de uso

Replicação controlada de diretórios e cópias repetidas entre hosts.

## Má prática

Executar --delete sem validar direção e escopo. Para escrita independente nos dois lados, use ferramenta desenhada para sincronização bidirecional.
