# Containers de sistema

Um container de sistema executa um init e vários serviços dentro de uma
instância isolada. Ele se aproxima da operação de uma máquina virtual, mas
usa namespaces, cgroups e o kernel do host em vez de inicializar um kernel
convidado.

## Diferença para container de aplicação

Um container de aplicação normalmente empacota um processo ou uma unidade
estreita que pode ser substituída por uma nova imagem. Um container de sistema
mantém um ambiente mais completo, com identidade persistente, serviços
coexistentes e uma forma de administração semelhante à de um host.

LXC, Incus e systemd-nspawn atendem partes desse espaço com modelos de
gerenciamento diferentes. Eles não são intercambiáveis apenas porque todos
usam namespaces.

## Quando usar

O modelo pode ser útil para testar uma distribuição completa, executar uma
aplicação legada que espera init e múltiplos serviços ou consolidar ambientes
Linux com menos overhead que VMs. Ele é menos adequado quando a operação deve
ser imutável, substituível e orientada a uma imagem de aplicação.

## Relações

- [Linux namespaces](../linux/namespaces.md) explica o isolamento.
- [MicroVM](microvm.md) adiciona um kernel convidado.
- [VMs e hypervisors](../../vms-e-hipervisores.md) compara as fronteiras.

## Fontes primárias

- [LXC](https://linuxcontainers.org/lxc/introduction/)
- [systemd-nspawn](https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html)
