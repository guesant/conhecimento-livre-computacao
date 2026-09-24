# `rpool`

`rpool` é um nome convencional para o pool ZFS que contém o sistema raiz em ambientes que usam ZFS no boot. O prefixo não é um tipo especial de pool: ele descreve uma convenção de nomenclatura e uma responsabilidade operacional. Em alguns ambientes, o dataset raiz aparece sob uma estrutura como `rpool/ROOT/<ambiente>`, enquanto dados persistentes ficam em datasets separados.

## O que o nome significa

O nome `rpool` não transforma um pool comum em um pool de boot. O comportamento depende do sistema operacional, do bootloader, das propriedades ZFS e das convenções da plataforma. Linux com OpenZFS, illumos e Oracle Solaris podem usar estruturas diferentes.

Por isso, não copie uma sequência de boot de Solaris para Linux apenas porque ambos usam ZFS. Primeiro identifique a distribuição, a implementação ZFS, o bootloader e a forma como os ambientes de boot são gerenciados.

## Estrutura comum

Uma organização de raiz costuma separar o dataset que representa o ambiente inicializável dos datasets de dados. O sistema pode manter mais de um ambiente e selecionar qual dataset será usado no próximo boot.

```text
rpool
`-- ROOT
    |-- current
    `-- previous
```

A árvore é ilustrativa. Os nomes, o dataset de boot e as propriedades devem ser consultados no host real com as ferramentas da plataforma.

## Operação segura

Antes de alterar o pool raiz, registre:

```sh
zpool status rpool
zpool get bootfs rpool
zfs list -r rpool
```

Confirme qual dataset está montado como raiz, quais datasets pertencem ao boot, quais snapshots existem e como o bootloader localiza o sistema. Um snapshot de `rpool` ajuda em uma estratégia de recuperação, mas não substitui uma cópia externa nem garante que o host possa inicializá-lo.

Alterações no pool raiz podem impedir o boot antes que o sistema tenha oportunidade de executar um procedimento de reparo. Tenha uma mídia de recuperação e uma forma de acessar o console. Em um host remoto, valide a recuperação fora de banda antes de alterar a estrutura de boot.

## Ambientes de boot

Ambientes de boot baseados em datasets permitem instalar uma atualização em uma árvore separada, testar a inicialização e manter um caminho de retorno. O mecanismo concreto varia entre as plataformas. O conceito não deve ser confundido com um snapshot solto sem configuração de boot.

Uma estratégia de atualização deve definir como criar o ambiente, qual dataset será selecionado, como validar serviços depois do boot e como reverter. Sem esse ciclo completo, ter snapshots no `rpool` não garante rollback operacional.

## Relações

- [ZFS](zfs.md) explica pools, vdevs, datasets, snapshots e replicação.
- [`zpool`](zpool.md) explica as operações de saúde, importação, substituição e scrub.
- [Mídias de instalação e recuperação](../boot/index.md) reúne ambientes para reparar um host que não inicia.
- [Boot pela rede](../boot/network-install.md) descreve uma alternativa quando a mídia local não está disponível.

## Fontes primárias

- [Oracle Solaris, root pool](https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/manage-zfs/root-pool.html)
- [OpenZFS documentation](https://openzfs.github.io/openzfs-docs/)
- [OpenZFS boot environments](https://openzfs.github.io/openzfs-docs/Getting%20Started/)
