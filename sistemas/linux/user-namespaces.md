# User namespaces

Um user namespace cria um espaço próprio de UIDs e GIDs. O UID 0 dentro dele
pode ser associado a um UID sem privilégios no host, reduzindo o impacto de um
processo que escape das outras camadas de isolamento.

A propriedade importante é o mapeamento, não o número exibido dentro do
container. O kernel compara a credencial traduzida no namespace alvo antes de
decidir se uma operação é permitida.

## Mapeamento

O processo de configuração usa mapas de UID e GID. Em execução rootless, as
faixas subordinadas de `/etc/subuid` e `/etc/subgid` fornecem identificadores
que o usuário pode representar. Ferramentas como `newuidmap` e `newgidmap`
validam a operação conforme as políticas do host.

Um processo pode ser UID 0 dentro do namespace e aparecer como um UID
subordinado fora dele. Arquivos bind-mounted exigem atenção, porque a
propriedade persistida no filesystem depende do UID que o host vê, não apenas
do nome exibido dentro do container.

## Rootful e rootless

No modo rootful, o daemon ou runtime pode criar namespaces em nome de root e
o UID 0 do container pode continuar sendo o UID 0 real do host se o remapping
não estiver habilitado. No modo rootless, o processo nasce sob uma conta comum
e o UID 0 interno é traduzido para uma faixa subordinada.

Rootless reduz privilégios, mas não remove riscos de kernel, configuração de
volumes, sockets privilegiados ou permissões concedidas ao runtime. Capabilities,
seccomp, LSM e filesystem read-only continuam relevantes.

## Diagnóstico

Compare `id` dentro do namespace com `/proc/<pid>/uid_map` e
`/proc/<pid>/gid_map` no host. Confira as faixas subordinadas, o dono de
arquivos montados e o usuário efetivo do processo. Não conclua que dois
processos têm o mesmo privilégio apenas porque exibem o mesmo número de UID em
namespaces diferentes.

## Relações

- [Namespaces](namespaces.md) explica o mecanismo que fornece o espaço de
  identidade.
- [Capabilities](capabilities.md) limita privilégios independentes do UID.
- [Processo Linux](process.md) posiciona credenciais no ciclo de vida.

## Fontes primárias

- [user_namespaces(7)](https://man7.org/linux/man-pages/man7/user_namespaces.7.html)
- [User namespaces](https://docs.kernel.org/admin-guide/namespaces/user_namespaces.html)
