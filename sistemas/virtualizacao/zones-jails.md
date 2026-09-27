# Comparação entre Solaris Zones e BSD Jails

FreeBSD Jails e Solaris Zones resolveram, cada um à sua forma, o problema de
isolar múltiplos ambientes sobre um único kernel. Eles antecedem os
namespaces do Linux e ajudam a separar o problema geral de isolamento das
decisões específicas do Linux.

## BSD Jail

[BSD Jail](bsd-jail.md) é o mecanismo de isolamento do FreeBSD baseado em
kernel compartilhado, com escopos próprios de processos, filesystem, identidade
e rede. A página canônica explica a evolução a partir de `chroot`, VNET,
`devfs`, ciclo de vida, limites de segurança e critérios de operação.

## Solaris Zones

[Solaris Zones](solaris-zones.md) separa zonas globais e não globais sobre o
kernel Solaris. A página canônica detalha zonas tradicionais, kernel zones,
recursos delegados, ciclo de vida, fronteiras de segurança e relação com VMs.

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

[BSD Jail](bsd-jail.md), [Solaris Zones](solaris-zones.md) e
[Containers de sistema](system-containers.md) são páginas canônicas das
implementações comparadas aqui. [Namespaces](../linux/namespaces.md) mostra o
mecanismo granular usado pelo Linux.
