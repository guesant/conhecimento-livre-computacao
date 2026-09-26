# Quorum

Quorum é a maioria necessária para confirmar uma decisão distribuída. Em um
grupo com `N` membros, a maioria é `floor(N / 2) + 1`; por isso três membros
toleram uma falha e cinco toleram duas. Um número par não adiciona uma faixa de
tolerância, porque perder metade ainda impede qualquer decisão.

No control plane, quorum não é sinônimo de quantidade de Pods saudáveis. Um API
server pode estar em execução e ainda falhar ao ler ou persistir objetos se o
datastore não alcançar a maioria. Réplicas de aplicação também não substituem
membros do protocolo de consenso.

## Bootstrap do quorum

Em um K3s com etcd embarcado, o primeiro servidor cria o estado inicial. O
segundo e o terceiro ingressam usando o endpoint estável da API e o token do
cluster, passam a participar do consenso e só depois devem receber workloads
que não prejudiquem a capacidade de recuperação do control plane.

O endpoint usado por novos servidores e agentes deve ser estável. Um load
balancer ou um DNS adequado evita que o endereço de um único servidor vire um
ponto único de falha, mas não substitui o quorum do datastore.

## Verificar e restaurar o quorum

O estado dos membros deve ser verificado no próprio etcd, não apenas pelo
status dos Nodes no Kubernetes. A perda da maioria interrompe novas escritas;
o retorno de um membro isolado não resolve divergência sem que o protocolo o
reintegre corretamente.

Um snapshot consistente e testado é a base da recuperação. Se o quorum não
voltar, a resposta é restaurar o datastore conforme a distribuição e a
topologia, ou reconstruir o cluster via GitOps quando essa for a fonte de
verdade escolhida. Recuperar o consenso não restaura automaticamente volumes,
backups de banco ou chaves usadas para decifrar segredos.

## Relações

- [etcd](etcd.md) explica a implementação de datastore que usa Raft.
- [Datastore do K3s](datastore.md) compara etcd embarcado, backend externo e
  Kine.
- [Topologias K3s multinó](../../topologias-rede-e-falhas-em-k3s-multino.md)
  aplica quorum a servidores, agentes e manutenção.
- [Backup do etcd](../../confiabilidade/backup/etcd.md) trata do artefato que
  precisa ser restaurável.
