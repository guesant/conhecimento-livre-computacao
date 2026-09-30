# Alpine Linux

Alpine Linux é uma distribuição pequena e orientada a segurança, baseada em musl libc e BusyBox. Ela é comum em containers, appliances e ambientes com poucos recursos, mas também oferece imagens para instalação tradicional e hardware específico.

## Branches e imagens

| Branch ou imagem | Papel |
| --- | --- |
| Stable | Branch versionada com correções e atualizações de manutenção. |
| Edge | Branch rolling de desenvolvimento, com mudanças contínuas. |
| Standard | Instalação geral para sistemas físicos e virtuais. |
| Extended | Imagem com conjunto maior de pacotes. |
| Netboot e Virtual | Imagens para inicialização pela rede e máquinas virtuais. |
| Raspberry Pi e U-Boot | Imagens para hardware e métodos de boot específicos. |

O gerenciador `apk`, a separação entre base e pacotes e o modelo diskless influenciam como o sistema é administrado. A ausência de componentes comuns de outras distribuições pode exigir adaptação de scripts e binários.

## Lançamento e suporte

Branches estáveis recebem correções durante seu ciclo documentado. Edge é rolling e não deve ser usada como se fosse uma release congelada. O suporte é principalmente comunitário, por wiki, fórum, listas e canais do projeto; não há um contrato comercial padrão fornecido pelo Alpine Project.

## Bugs e CVEs

O projeto mantém informações de segurança e metadados de correções por pacote. CVEs podem ser corrigidas por backport, atualização do pacote ou mudança de branch, dependendo do impacto. A equipe deve verificar a versão do pacote Alpine, e não apenas a versão do projeto upstream.

## Segurança e defaults

Alpine não oferece uma política MAC universal carregada por padrão como baseline de todas as imagens. O sistema usa musl, BusyBox, OpenRC e uma base pequena, mas redução de superfície não substitui AppArmor, SELinux, permissões, capabilities ou isolamento de serviço quando eles forem necessários.

Imagens mínimas podem não instalar `openssh-server`, `sudo` ou um shell completo. A configuração de acesso remoto e de usuários depende do perfil de instalação. Verifique o serviço OpenRC, a autenticação SSH, a conta root, a `umask` e os pacotes realmente presentes.

## Empacotamento

Alpine usa `apk` e pacotes `.apk`. Mantenedores escrevem `APKBUILD`; `abuild` executa o build em ambiente controlado, cria subpacotes e gera índices. Os repositórios distribuem pacotes assinados e metadados que `apk` usa para resolver dependências e verificar confiança.

O sistema distingue branches estáveis e Edge. Um pacote comunitário, uma imagem de container derivada ou um repositório não oficial pode não receber a mesma revisão, assinatura ou cobertura de segurança.

## Fontes primárias

- [Alpine Linux](https://www.alpinelinux.org/about/)
- [Alpine FAQ](https://wiki.alpinelinux.org/wiki/Alpine_Linux:FAQ)
- [Alpine release branches](https://wiki.alpinelinux.org/wiki/Release_Branches)
- [Alpine support](https://wiki.alpinelinux.org/wiki/Alpine_Linux:Support)
