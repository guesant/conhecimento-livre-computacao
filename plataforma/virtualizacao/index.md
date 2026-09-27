# Virtualização

Virtualização apresenta uma fronteira de execução que permite separar o
ambiente convidado dos recursos físicos ou do sistema hospedeiro. O grau de
isolamento, o custo de operação e a fidelidade do ambiente variam conforme a
abstração usada.

## Escopo

- [Máquinas virtuais](../../vms-e-hipervisores.md) virtualizam hardware para um
  sistema operacional convidado.
- [Hypervisor](../../sistemas/virtualizacao/hypervisor.md) administra a
  execução e a distribuição de recursos entre convidados.
- [MicroVM](../../sistemas/virtualizacao/microvm.md) reduz a superfície de uma
  máquina virtual para workloads de inicialização rápida.
- [Containers de sistema](../../sistemas/virtualizacao/system-containers.md)
  compartilham o kernel do host, mas apresentam um ambiente de sistema mais
  amplo que um container de aplicação.
- [Solaris Zones](../../sistemas/virtualizacao/solaris-zones.md) e [BSD Jail](../../sistemas/virtualizacao/bsd-jail.md)
  representam mecanismos históricos e específicos de isolamento de sistema.
- [Comparação entre Solaris Zones e BSD Jails](../../sistemas/virtualizacao/zones-jails.md)
  relaciona as duas implementações.

## Fronteiras

Uma máquina virtual não é apenas um container mais pesado. O convidado possui
seu próprio kernel, enquanto containers de aplicação normalmente compartilham
o kernel do host e usam namespaces, cgroups e mecanismos de segurança. MicroVMs
ficam entre esses modelos em alguns runtimes, mas a classificação depende da
implementação e do objetivo operacional.
