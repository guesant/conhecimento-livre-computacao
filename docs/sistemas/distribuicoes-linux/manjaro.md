# Manjaro

Manjaro é uma distribuição rolling baseada no ecossistema Arch, mas com repositórios, instaladores, ferramentas e política de promoção próprios. Seu objetivo é oferecer uma entrada mais acessível no modelo rolling sem exigir que o usuário construa uma instalação Arch do zero.

## Branches e flavors

| Branch | Papel |
| --- | --- |
| Unstable | Pacotes chegam primeiro, com maior exposição a mudanças. |
| Testing | Pacotes passam por uma etapa adicional de validação comunitária. |
| Stable | Pacotes promovidos para uso geral depois de testes e correções. |

As principais imagens oficiais usam Xfce, KDE Plasma e GNOME. A comunidade também publica edições com outros ambientes, mas a responsabilidade, a frequência de atualização e a qualidade de suporte podem variar.

## Lançamento e suporte

Não há grandes releases com migração periódica. A instalação evolui pela atualização dos pacotes e pela promoção entre branches. O suporte é principalmente comunitário, por wiki, fórum, documentação e canais de usuários. Não há um contrato empresarial padrão equivalente ao suporte de RHEL ou Ubuntu Pro.

## Bugs e CVEs

Uma correção pode depender do upstream Arch, de uma adaptação do Manjaro e da promoção para a branch Stable. O usuário deve ler os anúncios, manter o sistema consistente e evitar misturar repositórios arbitrários. AUR e pacotes comunitários ampliam a oferta, mas não são parte da mesma garantia dos repositórios oficiais.

## Segurança e defaults

Manjaro não apresenta AppArmor ou SELinux como baseline MAC universal equivalente ao RHEL ou Ubuntu. O administrador pode habilitar esses mecanismos, mas precisa instalar políticas, validar compatibilidade e manter os perfis. A segurança padrão depende bastante da edição, do instalador e do trabalho posterior do usuário.

Imagens desktop normalmente privilegiam a criação de um usuário normal e o uso de `sudo`. SSH server não é uma consequência obrigatória da instalação, e login de root, senha e `umask` devem ser auditados antes de usar a imagem em um servidor.

## Empacotamento

Manjaro usa pacotes Arch compatíveis com `pacman`, mas constrói e promove seus próprios pacotes em repositórios e branches. O processo recebe fontes e receitas, executa builds, testa atualizações e promove pacotes de Unstable para Testing e Stable.

Pacotes oficiais são assinados. AUR contém receitas `PKGBUILD` mantidas por usuários e exige revisão do código antes do build. AUR não é um repositório binário oficial nem uma garantia de que o conteúdo da receita é seguro.

## Fontes primárias

- [Manjaro branches](https://wiki.manjaro.org/index.php?title=Switching_Branches)
- [Manjaro rolling release model](https://wiki.manjaro.org/index.php?title=The_Rolling_Release_Development_Model/en)
- [Manjaro downloads](https://manjaro.org/products/download/x86/)
