# openSUSE

openSUSE reúne produtos comunitários com modelos diferentes. A escolha entre Leap, Tumbleweed e MicroOS muda o ciclo de atualização, o grau de mutabilidade do sistema e o modo de operação.

## Produtos e flavors

| Produto | Modelo | Uso típico |
| --- | --- | --- |
| openSUSE Tumbleweed | Rolling release com snapshots integrados e testados. | Desktop atualizado, desenvolvimento e uso técnico. |
| openSUSE Leap | Release estável alinhada a componentes do ecossistema SUSE. | Desktop e servidores que preferem mudanças agrupadas. |
| openSUSE MicroOS | Sistema transacional e orientado a workloads, com atualizações atômicas. | Containers, edge e hosts especializados. |
| openSUSE Leap Micro | Variante mínima e transacional para infraestrutura. | Edge, virtualização e serviços pequenos. |
| Aeon | Desktop imutável baseado no ecossistema openSUSE. | Estação GNOME transacional. |
| Kalpa | Desktop imutável baseado no KDE Plasma. | Estação KDE transacional. |

Os ambientes GNOME, KDE Plasma, Xfce e outros podem ser instalados conforme o produto e a imagem escolhida. O ambiente não substitui o modelo de atualização da distribuição.

## Lançamento e suporte

Tumbleweed publica snapshots contínuos depois de testes automatizados e integração de pacotes. Leap usa releases estáveis e um ciclo próprio, que deve ser conferido na documentação da versão em uso. MicroOS e seus derivados usam atualização transacional e não devem ser tratados como um servidor tradicional que recebe alterações arbitrárias no sistema em execução.

A relação com a SUSE fornece integração tecnológica e opções comerciais no ecossistema, mas o suporte oficial de uma instalação openSUSE comunitária não deve ser presumido como um contrato SUSE Enterprise. A comunidade oferece documentação, fóruns, listas, Bugzilla e openQA.

## Bugs e CVEs

O projeto usa openQA, Bugzilla e anúncios de segurança para detectar e comunicar problemas. Em Tumbleweed, uma correção pode chegar junto com uma atualização de snapshot e novas versões de dependências. Em Leap e MicroOS, o processo preserva a política de estabilidade ou transacionalidade do produto.

## Segurança e defaults

openSUSE oferece AppArmor como mecanismo MAC integrado ao sistema e aos perfis disponíveis para serviços. O perfil carregado, o modo enforcing e a política de cada produto devem ser verificados com `aa-status`; MicroOS e desktops imutáveis também acrescentam restrições e fluxos de atualização próprios.

O servidor SSH, `sudo` e a associação do usuário ao grupo administrativo dependem do padrão da imagem e das escolhas do instalador. A distribuição não transforma uma senha de root, uma chave importada ou uma regra de firewall em uma política universal. Verifique `sshd -T`, os arquivos de sudoers e `umask` no host final.

## Empacotamento

openSUSE usa RPM, `zypper` e `libzypp`. Pacotes são definidos por spec e construídos no Open Build Service, que produz artefatos para projetos, arquiteturas e repositórios. `zypper` resolve dependências, preserva a origem do fornecedor e distingue atualizações de patches de distribuição.

Tumbleweed promove snapshots integrados depois de testes automatizados. Leap e MicroOS usam repositórios e políticas adequados à estabilidade ou à atualização transacional do produto. Um repositório OBS de terceiros pode ter outra política de assinatura, teste e manutenção.

## Fontes primárias

- [openSUSE](https://www.opensuse.org/)
- [Portal do Leap](https://en.opensuse.org/Portal:Leap)
- [Portal do Tumbleweed](https://en.opensuse.org/Portal:Tumbleweed)
- [Portal do MicroOS](https://en.opensuse.org/Portal:MicroOS)
- [openSUSE downloads](https://get.opensuse.org/)
