# Dolphin

Dolphin é o gerenciador de arquivos do KDE Plasma. Além de operar arquivos
locais, ele pode acessar recursos remotos por meio da arquitetura KIO, que
fornece workers para protocolos e serviços diferentes.

## Acesso SSH

No Dolphin, o acesso remoto pode aparecer como `sftp://` ou `fish://`,
dependendo do worker instalado e do fluxo escolhido. O worker FISH usa uma
sessão SSH e comandos remotos para navegar em hosts Unix-like. O worker SFTP
usa o protocolo de arquivos do SSH.

O endereço remoto deve explicitar o usuário e o host, por exemplo:

```text
sftp://usuario@servidor.example/var/www
fish://usuario@servidor.example/home/usuario
```

O caminho não transforma o servidor em um filesystem local real. O Dolphin
coordena listagem, leitura, escrita e cópia por meio do worker KIO. Aplicações
externas podem não entender a URL remota diretamente; nesse caso, o arquivo
pode ser baixado para um cache local ou acessado por KIO-FUSE, conforme a
instalação.

## Quando usar

Dolphin é apropriado para inspeção manual, cópia pontual e administração de um
host remoto a partir de uma sessão KDE. Ele é especialmente conveniente
quando a pessoa já está trabalhando no Plasma e quer evitar uma segunda
interface para uma operação simples.

Para grandes árvores, transferências repetidas, publicação ou backup, prefira
[rsync](rsync.md). Para múltiplos backends de armazenamento, prefira
[rclone](rclone.md). Para uma sessão de transferência explícita e automatizável,
use [SFTP](sftp.md).

## Segurança

O Dolphin utiliza as credenciais e a configuração SSH do usuário quando o
worker consegue aproveitá-las. A chave do host ainda precisa ser validada e a
conta remota continua limitada pelas permissões do servidor. Não use a
interface gráfica para contornar um erro de autenticação, uma restrição de
permissão ou uma política de acesso.

Editar arquivos diretamente em um host remoto exige atenção à atomicidade,
permissões e recuperação. Para arquivos de configuração críticos, copie uma
versão local, valide-a e faça a instalação por um procedimento que permita
rollback.

## Relações

- [SFTP](sftp.md) define o protocolo de transferência sobre SSH.
- [SSHFS](sshfs.md) monta um caminho remoto como filesystem por FUSE.
- [Acesso a arquivos remotos](acesso/index.md) compara montagem, navegação e
  cópia.
- [KDE Plasma](../../sistemas/desktop/kde-plasma.md) apresenta o ecossistema
  em que o Dolphin é integrado.

## Fontes primárias

- [Manual do Dolphin](https://docs.kde.org/trunk_kf6/en/dolphin/dolphin/dolphin.pdf)
- [Worker FISH do KDE](https://docs.kde.org/stable_kf6/en/kio-extras/kioworker6/fish/)
- [Documentação do KIO](https://develop.kde.org/docs/extend/kioslaves/)
