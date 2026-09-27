# Mapa de segurança e empacotamento

Uma distribuição não é segura apenas porque usa um kernel recente ou porque oferece um gerenciador de pacotes assinado. A segurança do sistema resulta da combinação entre imagem inicial, serviços instalados, política MAC, permissões, atualização, origem dos pacotes e configuração do operador.

## Defaults não são universais

Os defaults dependem da edição, do instalador, da imagem de nuvem e de alterações feitas durante o provisionamento. A mesma distribuição pode iniciar com um servidor SSH instalado em uma imagem de servidor e sem o pacote em uma instalação desktop. Por isso, a documentação deve distinguir política do projeto de estado observado em uma máquina.

Antes de aceitar uma imagem como baseline, verifique pelo menos:

```text
cat /etc/os-release
command -v sshd
sshd -T
sudo -V
umask
getenforce
aa-status
systemctl --type=service --state=running
```

`sshd -T` mostra a configuração efetiva, mas deve ser executado com uma configuração válida. `getenforce` só existe quando SELinux está instalado. `aa-status` só existe quando AppArmor está disponível. A ausência do comando não prova sozinha que nenhum mecanismo de confinamento existe.

## MAC nas distribuições

[AppArmor](../../seguranca/mac-apparmor.md) e [SELinux](../../seguranca/mac-selinux.md)
são implementações de Mandatory Access Control. Elas complementam DAC,
capabilities, namespaces, seccomp e isolamento de serviços. Não substituem
atualização, autenticação, firewall, auditoria ou autorização da aplicação.

O default depende da distribuição, da edição, da imagem e da configuração do
operador. A presença de um pacote ou perfil não prova que o mecanismo está
carregado e em enforcing. Verifique o host real e leia as páginas canônicas para
interpretar a política e as negações.

## SSH, sudo e umask

Não existe um único default de SSH que seja seguro para todos os ambientes. A imagem pode instalar `openssh-server`, habilitar o serviço, importar uma chave, desabilitar senha ou permitir uma configuração temporária para o instalador. O baseline deve revisar `PermitRootLogin`, `PasswordAuthentication`, `KbdInteractiveAuthentication`, `AllowUsers`, `AllowGroups`, algoritmos criptográficos e origem das chaves.

`sudo` também é uma escolha da imagem. Em algumas instalações o primeiro usuário administrativo é colocado em `sudo` ou `wheel`; em outras o pacote nem é instalado, ou o operador usa root diretamente. A política deve exigir contas nominativas, autenticação forte, menor privilégio, logs e regras estreitas. Adicionar todos os usuários a um grupo administrativo não é uma política de autorização.

`umask` é um valor de criação de arquivos, não um controle de acesso completo. Valores como `022` são comuns em instalações tradicionais, enquanto serviços e imagens endurecidas podem usar valores mais restritivos. Verifique a origem efetiva do valor em shell, systemd, PAM, containers e aplicações. Um serviço pode ter `UMask=` próprio e não herdar o valor da sessão do usuário.

## Como o pacote chega ao sistema

O fluxo típico separa fonte, build, assinatura e distribuição:

1. o mantenedor declara a fonte, versão, patches, dependências e metadados;
2. um builder reproduz o build em ambiente controlado;
3. o artefato recebe checksums e assinatura do projeto ou da distribuição;
4. o repositório publica índices e metadados assinados;
5. o gerenciador verifica dependências, assinatura e política do repositório;
6. hooks de instalação atualizam cache, serviços, usuários, initramfs ou contexts.

O usuário deve preferir repositórios oficiais e verificar a procedência de repositórios adicionais. Um pacote que compila localmente não passa automaticamente a ser confiável. PPAs, COPR, AUR, OBS de terceiros, overlays e repositórios empresariais têm políticas diferentes.

## Formatos e ferramentas

| Ecossistema | Formato | Gerenciador | Build e distribuição |
| --- | --- | --- | --- |
| Debian e Ubuntu | `.deb` | `apt` e `dpkg` | Source package, builders de archive e repositórios APT com metadados assinados. |
| RHEL, Fedora e CentOS | `.rpm` | `dnf` e `rpm` | Spec, source RPM, builders controlados e repositórios RPM com errata e assinaturas. |
| openSUSE | `.rpm` | `zypper` e `libzypp` | Open Build Service, projetos e repositórios RPM. |
| Arch e Manjaro | `pkg.tar.zst` | `pacman` | `PKGBUILD`, `makepkg`, repositórios assinados e promoção por branch. |
| Alpine | `.apk` | `apk` | `APKBUILD`, `abuild`, índices APK e pacotes assinados. |

## CVEs e atualização

A equipe de segurança pode corrigir a vulnerabilidade com backport, upgrade do pacote ou rebuild da imagem. O número da versão upstream não basta para decidir se uma CVE está corrigida. Consulte o advisory da distribuição, a versão do pacote e os changelogs.

Pacotes de terceiros quebram a suposição de que uma atualização segue o ciclo da distribuição. Para workloads críticos, mantenha uma lista de repositórios permitidos, monitore os avisos de segurança, valide a assinatura e teste a atualização antes de promovê-la.

## Fontes primárias

- [Ubuntu AppArmor](https://ubuntu.com/server/docs/how-to/security/apparmor/)
- [Debian Handbook, AppArmor](https://www.debian.org/doc/manuals/debian-handbook/sect.apparmor.el.html)
- [Red Hat SELinux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/index)
- [Arch package signing](https://wiki.archlinux.org/title/Pacman/Package_signing)
- [Arch package creation](https://wiki.archlinux.org/title/Creating_packages)
- [Alpine APKBUILD](https://wiki.alpinelinux.org/wiki/APKBUILD_Reference)
- [Ubuntu Launchpad PPAs](https://ubuntu.com/docs/launchpad/user/reference/packaging/ppas/ppa/)
- [openSUSE Build Service](https://build.opensuse.org/)
