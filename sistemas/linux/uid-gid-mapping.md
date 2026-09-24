# Mapeamento de UID e GID

O mapeamento de UID e GID define como uma credencial num user namespace
corresponde a uma credencial em outro namespace. Ele é a ponte entre a
identidade apresentada por uma aplicação e a identidade que o filesystem ou
um recurso do host realmente verifica.

## Regras do mapa

Um mapa contém intervalos de identificadores internos e externos. Um
identificador interno sem correspondência aparece como overflow e não pode
ser usado para obter privilégios no namespace externo. A faixa deve ser
concedida explicitamente pelo host ao usuário que cria o namespace.

UID e GID possuem mapas separados. Uma operação que cria ou altera um GID
mapeado pode exigir `setgroups` desabilitado antes da escrita do mapa, porque
grupos suplementares poderiam contornar a intenção da configuração.

## Bind mounts

Um arquivo criado por UID 0 interno pode aparecer no host com o UID subordinado
correspondente. Se a aplicação precisa editar arquivos do workspace como o
usuário real, a configuração precisa alinhar o ID interno ao ID do host ou usar
uma estratégia explícita de permissões.

Alterar ownership dentro do container não muda a identidade que o kernel
persistirá fora do namespace. Diagnostique o caminho montado no host e dentro
do processo antes de aplicar `chown` indiscriminadamente.

## Relações

- [User namespaces](user-namespaces.md) fornecem o espaço em que o mapa é
  aplicado.
- [Processo Linux](process.md) usa credenciais ao acessar recursos.
- [Filesystem de container](../../containers/index.md) mostra como imagens e
  mounts participam da execução.

## Fontes primárias

- [user_namespaces(7)](https://man7.org/linux/man-pages/man7/user_namespaces.7.html)
- [Subordinate user and group IDs](https://man7.org/linux/man-pages/man5/subuid.5.html)
