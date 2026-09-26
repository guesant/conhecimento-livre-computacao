# Debian

Debian é uma distribuição comunitária cuja organização, repositórios e política de qualidade são mantidos pelo Debian Project. Ele não oferece flavors de desktop no mesmo sentido do Ubuntu. O instalador e os metapacotes permitem escolher GNOME, KDE Plasma, Xfce, LXQt, Cinnamon, MATE, LXDE e outros ambientes sobre a mesma base.

## Estados de desenvolvimento

| Estado | Papel |
| --- | --- |
| Stable | Release recomendada para produção, com foco em estabilidade e correções. |
| Testing | Próxima Stable, recebendo pacotes que passaram pelos critérios de migração. |
| Unstable, também chamada Sid | Entrada contínua de mudanças e desenvolvimento. |
| Oldstable | Release anterior, mantida durante a transição e o período de suporte definido. |

As arquiteturas suportadas, imagens de instalação e ambientes disponíveis variam por release. O desktop é uma composição de pacotes, não uma distribuição Debian separada.

## Lançamento e suporte

Uma nova Stable costuma ser publicada aproximadamente a cada dois anos, quando os critérios de qualidade e prontidão são satisfeitos. A equipe de segurança mantém a cobertura da Stable durante o período regular e o Debian Long Term Support estende a manutenção para um período adicional, com escopo e arquiteturas definidos para cada release.

O projeto é comunitário. Empresas podem financiar mantenedores, contratar consultoria ou participar do Debian LTS, mas isso não equivale a uma assinatura de suporte centralizada como a de uma distribuição empresarial.

## Bugs e CVEs

O Debian Security Team publica avisos DSA e mantém páginas por release e pacote. Correções são frequentemente backported para preservar a API e a estabilidade da Stable. Bugs de empacotamento devem ser reportados no Debian Bug Tracking System; problemas do software upstream devem ser encaminhados ao projeto responsável quando a análise indicar essa origem.

## Segurança e defaults

Debian fornece AppArmor e SELinux, mas a ativação depende do instalador, da imagem e da escolha do administrador. AppArmor tem integração documentada e perfis disponíveis; não se deve afirmar que toda instalação Debian possui o mesmo conjunto de perfis carregados.

O instalador pode criar um usuário administrativo, instalar `sudo` e deixar o acesso SSH para uma etapa posterior. Em instalações minimalistas, `openssh-server`, `sudo` e até uma política MAC podem não estar presentes. `umask` costuma vir da configuração de shell ou PAM. Audite `sshd -T`, grupos administrativos e o valor efetivo de `umask` após a instalação.

## Empacotamento

Debian usa source packages, que normalmente incluem `.dsc`, arquivos de origem e patches, e produz pacotes binários `.deb`. Builders por arquitetura compilam os pacotes; o archive publica índices e metadados para `apt`, enquanto `dpkg` executa a instalação local.

O projeto mantém repositórios por release e área, como `main`, `contrib`, `non-free` e `non-free-firmware`, conforme a configuração e a política da release. A assinatura e a cadeia de metadados do archive são parte da confiança do APT. Não confunda um pacote no Debian archive com um pacote de um repositório pessoal.

## Fontes primárias

- [Debian releases](https://www.debian.org/releases)
- [Debian Long Term Support](https://www.debian.org/lts/)
- [Debian Security Information](https://www.debian.org/security/)
- [Debian Bug Tracking System](https://www.debian.org/Bugs/)
