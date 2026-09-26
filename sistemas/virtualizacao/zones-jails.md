# Solaris Zones e BSD Jails

FreeBSD Jails e Solaris Zones resolveram, cada um à sua forma, o problema de
isolar múltiplos ambientes sobre um único kernel. Eles antecedem os
namespaces do Linux e ajudam a separar o problema geral de isolamento das
decisões específicas do Linux.

## BSD Jails

O mecanismo de jail foi desenvolvido em 1999 para separar ambientes de
clientes em um mesmo servidor físico e entrou no FreeBSD 4.0, lançado em
2000. Um jail parte do conceito de `chroot`, que restringe apenas o sistema de
arquivos, e também virtualiza usuários e rede. O processo isolado, portanto,
não recebe apenas uma raiz de filesystem diferente; ele também opera em um
escopo distinto de identidade e conectividade.

## Solaris Zones

Solaris Zones foi introduzida no Solaris 10. Uma zona global mantém o controle
administrativo do host e uma ou mais zonas não globais isolam conjuntos de
aplicações. Uma kernel zone adiciona um kernel próprio à zona, aproximando seu
modelo do de uma máquina virtual.

## Relação com namespaces

Jails e Zones usam um modelo mais integrado: filesystem, usuários e rede
formam uma unidade de isolamento. O Linux trata cada dimensão como um tipo de
namespace independente, permitindo composições mais granulares, mas exigindo
que a configuração de user namespaces e capabilities seja avaliada em
conjunto.

O modelo compartilhado de kernel reduz o custo em relação a uma VM, mas não
torna automaticamente todos os processos confiáveis. A fronteira de
segurança depende do kernel, do mecanismo de isolamento e das permissões
atribuídas ao ambiente.

## Continue por aqui

[Containers de sistema](system-containers.md) explica LXC, Incus e
`systemd-nspawn`. [Namespaces](../linux/namespaces.md) mostra o mecanismo
granular usado pelo Linux.
