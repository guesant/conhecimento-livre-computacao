# Transferência de arquivo: rsync, sshfs, sftp e rclone

Essas quatro ferramentas resolvem problemas diferentes o suficiente para não serem intercambiáveis, mesmo compartilhando o mesmo transporte SSH na maioria dos casos: uma transfere lotes de arquivo de forma eficiente, outra monta um filesystem remoto para navegação e edição pontual, outra abre uma sessão interativa de transferência, e a última estende essa mesma lógica de sincronização para armazenamento em nuvem em vez de outro host SSH.

Usar uma no lugar da outra produz um resultado tecnicamente possível mas mal ajustado ao problema real.

## rsync: sincronização unidirecional eficiente

`rsync` compara os arquivos de origem e destino e transfere só as diferenças, o que o torna eficiente em execuções repetidas contra o mesmo destino, ao contrário de simplesmente copiar tudo de novo a cada vez.

O ponto que confunde quem usa a flag `--delete` pela primeira vez é achar que ela torna a sincronização bidirecional: não torna. `--delete` só faz o destino espelhar exatamente o que existe na origem, removendo lá o que já não existe aqui, mas a direção da cópia continua sendo sempre da origem informada primeiro para o destino informado depois.

Uma mudança feita direto no destino nunca volta para a origem, por mais vezes que o mesmo comando rode; uma sincronização de verdade bidirecional, com mudanças propagadas nos dois sentidos e conflitos resolvidos, exige uma ferramenta desenhada especificamente para isso, não rsync com uma flag a mais.

Rodando sobre SSH, `--delete` herda o mesmo privilégio da sessão, o que significa que inverter por engano a ordem de origem e destino num comando com essa flag pode apagar dados do lado que deveria continuar intacto, não do lado que deveria ser atualizado.

## sshfs: filesystem remoto sob demanda

`sshfs` monta um caminho remoto como se fosse um diretório local, através de FUSE (um mecanismo que permite implementar um filesystem inteiro em espaço de usuário, sem exigir um módulo de kernel dedicado); cada leitura ou escrita nesse ponto de montagem vira, por trás, uma requisição SFTP contra o host remoto, o que faz a latência de rede afetar diretamente a responsividade de qualquer operação, ao contrário de um filesystem local de verdade.

Isso o torna adequado para navegação e edição pontual de um arquivo remoto diretamente no editor local, mas inadequado para mover um lote de arquivos de uma vez, o trabalho que cabe ao `rsync`.

Um detalhe que surpreende quem edita um arquivo montado por sshfs com um editor que salva de forma atômica (grava um arquivo temporário e o renomeia por cima do original, uma prática comum para nunca deixar o arquivo original num estado parcialmente escrito): sobre uma conexão instável, essa sequência de operações pode se comportar de um jeito inesperado que não aconteceria contra um filesystem local.

Um ponto de montagem que perde a conexão de rede sem ser desmontado corretamente antes tende a travar num estado inconsistente, reportando que o "destino de transporte não está conectado" até ser forçado a desmontar.

Desmontar deliberadamente ao terminar, em vez de deixar a montagem persistente sem necessidade, evita esse estado e também evita que outra pessoa com acesso à mesma máquina local herde, sem perceber, o mesmo acesso ao filesystem remoto que a sessão montada concedeu.

## sftp: uma sessão, não um filesystem

`sftp` abre uma sessão interativa de transferência sobre SSH, com comandos próprios como `get/put/ls/cd` que operam contra o lado remoto sem montar nada no sistema de arquivos local.

É o meio-termo entre um `scp` pontual (uma cópia só, sem sessão) e um `sshfs` completo (um ponto de montagem persistente).

Diferente do sshfs, que faz um arquivo remoto parecer local para qualquer programa, uma sessão sftp só serve para quem está literalmente digitando comandos dentro dela, ou para um script que a automatiza via um cliente de biblioteca; nenhum outro processo do sistema enxerga o lado remoto como parte do próprio filesystem.

Isso torna sftp adequado exatamente para o caso que não justifica nem uma cópia isolada nem uma montagem permanente: uma sessão de exploração e transferência pontual, sem deixar rastro depois de fechada.

## rclone: a mesma lógica de sincronização, para armazenamento em nuvem

`rclone` estende a lógica de sincronização do `rsync`, comparar origem e destino e transferir só a diferença, para um universo muito mais amplo de destinos do que outro host SSH: dezenas de provedores de armazenamento em nuvem, como S3 e qualquer serviço compatível com sua API, Google Drive ou Backblaze B2, entre muitos outros.

Um único cliente cobre todos eles com uma sintaxe de comando consistente, escondendo as diferenças de API de cada provedor atrás do mesmo verbo (`copy/sync/move`).

Isso o torna a ferramenta natural quando o destino de uma cópia ou de um backup não é outro servidor com SSH, mas um bucket de object storage, algo que nem rsync nem scp foram desenhados para falar diretamente.

`rclone bisync` resolve especificamente a limitação unidirecional do rsync descrita acima, sincronizando mudanças nos dois sentidos entre dois destinos e resolvendo conflitos segundo uma política configurável, ao custo de mais complexidade operacional do que uma sincronização de mão única; vale a pena só quando os dois lados realmente recebem escrita independente, não como padrão para todo caso de sincronização.

## Continue por aqui

[SSH](ssh.md) cobre a sessão que ambas as ferramentas herdam, incluindo identidade e privilégio. [Filesystems](../referencia/comandos-de-processos-disco-e-arquivos.md) reúne outros comandos de manipulação de arquivo que complementam estes dois.
