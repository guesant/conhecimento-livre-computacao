# netlink

Netlink é uma família de sockets usada para comunicação entre processos e o
kernel Linux. Ferramentas como `ip`, `tc`, `nft`, `ss` e gerenciadores de rede
usam mensagens netlink para consultar ou alterar estado de interfaces, rotas,
filas, filtros, vizinhança e outras subsistemas.

## Modelo de mensagens

Uma mensagem possui cabeçalho, tipo, flags, atributos e payload conforme a
família. A estrutura é binária e extensível; o cliente precisa respeitar
alinhamento, tamanho e atributos desconhecidos. Muitas APIs usam dumps para
listar estado e notificações multicast para informar alterações posteriores.

O processo precisa de capabilities ou permissões adequadas para operações de
escrita. Abrir um socket não concede automaticamente autorização para mudar a
rede. Em namespaces de rede, a consulta pode mostrar um estado diferente do
host ou de outro Pod.

## Famílias

`NETLINK_ROUTE` trata interfaces, endereços, rotas e regras. `NETLINK_NETFILTER`
relaciona-se a eventos e configurações de filtragem. Outras famílias servem a
udev, auditoria, sockets de diagnóstico e extensões específicas. APIs novas
podem substituir mensagens antigas, mas o kernel precisa manter compatibilidade
por versões.

## Concorrência e consistência

Um cliente pode receber notificações depois do dump inicial e perder eventos
entre as duas operações. Aplicações robustas repetem a consulta, detectam
sequências e reconciliam o estado observado. Não trate uma mensagem individual
como snapshot completo da rede.

## Diagnóstico

`ip monitor`, `ss`, `nft monitor` e ferramentas específicas expõem diferentes
famílias. Quando uma mudança funciona em um namespace e não em outro, verifique
namespace, capability, tabela, prioridade e processo que reverte a alteração.
Logs e captura de mensagens devem evitar expor endereços ou tokens sem necessidade.

## Relações

- [RPDB](../../rede/roteamento/rpdb.md) usa netlink para regras de rota.
- [sysfs](sysfs.md) expõe outra interface kernel, orientada a objetos e atributos.
- [Netfilter](../../rede/firewall/netfilter.md) trata filtragem e NAT.

## Fontes primárias

- [Linux Netlink Handbook](https://docs.kernel.org/userspace-api/netlink/index.html)
- [rtnetlink](https://www.kernel.org/doc/html/latest/networking/netlink_spec/rt-route.html)
- [netlink(7)](https://man7.org/linux/man-pages/man7/netlink.7.html)
