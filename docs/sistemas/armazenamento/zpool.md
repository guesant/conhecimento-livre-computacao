# `zpool`

`zpool` é o comando e o modelo de administração dos pools ZFS. Um pool é construído a partir de um ou mais vdevs, que são grupos de dispositivos com uma topologia de redundância específica. Datasets e zvols consomem espaço do pool, mas não definem sua redundância física.

## Pool e vdev

Um disco único é um vdev sem redundância. Um mirror mantém cópias em dispositivos do mesmo vdev. RAIDZ distribui dados e paridade em uma topologia própria. O pool pode reunir vários vdevs, mas a adição de um vdev não transforma os vdevs existentes em outra topologia.

Essa distinção é importante para capacidade e falhas. A tolerância do pool depende de cada vdev, e a perda de um vdev pode tornar o pool indisponível mesmo que outros vdevs permaneçam saudáveis.

## Inspeção

Comece por estado, capacidade e configuração:

```sh
zpool status -v
zpool list
zpool get all
```

`zpool status` mostra a saúde dos vdevs e erros conhecidos. Um pool online não garante que não existam erros históricos, que o backup esteja atualizado ou que a aplicação consiga recuperar seus dados.

## Ciclo operacional

As operações usuais incluem importar e exportar pools, iniciar scrub, substituir dispositivos, anexar ou desanexar membros de mirrors e expandir a capacidade conforme a topologia permitir. Cada uma possui pré-condições diferentes.

```sh
sudo zpool scrub pool
sudo zpool status pool
```

Scrub é uma verificação de integridade, não uma limpeza de dados. Ele pode reparar blocos somente quando existe outra cópia íntegra. Planeje o impacto de I/O e acompanhe o resultado até a conclusão.

## Substituição e falha

Quando um dispositivo falha, preserve o estado e identifique o membro exato do vdev antes de substituir qualquer coisa. Em hosts com caminhos instáveis, confirme se o problema é disco, cabo, controlador ou identificação persistente.

Não use `zpool replace` em um disco escolhido por posição `/dev/sdX` sem confirmar a identidade. A ordem dos dispositivos pode mudar entre boots. Prefira identificadores estáveis e o procedimento da plataforma.

Um spare disponível pode acelerar a recuperação, mas não substitui a redundância planejada. Depois da resilverização, verifique o status e investigue erros de checksum ou I/O que tenham aparecido durante o processo.

## Importação e exportação

Pools podem ser exportados de um host e importados em outro compatível. A transferência exige compatibilidade de versão, acesso aos dispositivos, entendimento das propriedades de montagem e cuidado com pools que pertencem ao sistema raiz.

```sh
sudo zpool import
sudo zpool export pool
```

Não importe um pool em modo de recuperação sem entender os efeitos sobre mounts e boot. Uma importação forçada deve ser uma decisão de incidente, registrada e validada.

## Relações

- [ZFS](zfs.md) explica o sistema integrado de filesystem e armazenamento.
- [`rpool`](rpool.md) explica pools usados pela raiz e pelos ambientes de boot.
- [Btrfs](btrfs.md) oferece uma alternativa com subvolumes e perfis próprios de armazenamento.

## Fontes primárias

- [OpenZFS zpool documentation](https://openzfs.github.io/openzfs-docs/man/master/8/zpool.8.html)
- [OpenZFS administration](https://openzfs.github.io/openzfs-docs/Getting%20Started/)
