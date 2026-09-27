# sysfs

sysfs é um filesystem virtual que expõe uma representação hierárquica de
dispositivos, drivers, buses, classes e parâmetros do kernel. Ele fica
normalmente montado em `/sys` e permite que ferramentas de user space observem
ou, em alguns casos, alterem atributos definidos pelo kernel.

## Objetos e atributos

Diretórios representam objetos do modelo de dispositivos; arquivos representam
atributos. Links simbólicos conectam um dispositivo à classe, ao driver ou ao
bus correspondente. O layout é uma interface de user space, mas a existência,
permissão e semântica de um atributo dependem da versão do kernel e do driver.

Escrever em sysfs não é editar um arquivo comum. O write aciona código do
kernel, pode alterar estado do dispositivo e pode falhar por política, formato
ou condição de hardware. Valores precisam ser validados conforme a documentação
do atributo, não por tentativa em produção.

## Relação com udev e netlink

O kernel publica eventos de dispositivos por netlink; udev observa esses eventos
e aplica regras ou cria nomes e permissões. sysfs fornece estado consultável,
enquanto o evento informa que algo mudou. Uma aplicação deve tolerar reordenação,
dispositivo removido entre consulta e uso e atributos ainda não disponíveis.

## Energia e hardware

Power management, thermal zones, PCI, USB e blocos de armazenamento aparecem em
árvores diferentes. Um valor em `/sys` pode ser uma leitura instantânea, um
limite configurável ou uma solicitação que o firmware pode ignorar. Registre
unidade, caminho, versão e origem antes de comparar máquinas.

## Relações

- [netlink](netlink.md) explica eventos e mensagens entre kernel e user space.
- [udev](https://www.freedesktop.org/software/systemd/man/latest/udev.html) reage a eventos.
- [VDSO](vdso.md) trata uma interface diferente, voltada a chamadas rápidas de tempo.

## Fontes primárias

- [sysfs no kernel Linux](https://docs.kernel.org/filesystems/sysfs.html)
- [Linux device model](https://docs.kernel.org/driver-api/driver-model/overview.html)
- [udev](https://www.freedesktop.org/software/systemd/man/latest/udev.html)
