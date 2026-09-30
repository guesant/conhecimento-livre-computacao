# cloud-init

cloud-init é um sistema de inicialização que lê dados fornecidos pela plataforma ou pelo operador e configura uma instância na primeira inicialização e em eventos suportados. Ele pode definir hostname, rede, usuários, chaves SSH, pacotes, arquivos e comandos.

cloud-init não é uma imagem e não é um substituto completo de Ansible. Ele é uma camada de bootstrap. Depois que a máquina possui identidade e acesso, uma ferramenta de configuração pode assumir responsabilidades mais complexas.

## Dados de entrada

As fontes principais são:

| Dado | Papel |
| --- | --- |
| User-data | Configuração fornecida pelo usuário, como cloud-config, script ou MIME |
| Meta-data | Identidade da instância, hostname, instance-id e dados da plataforma |
| Vendor-data | Configuração fornecida pelo provedor ou pela imagem |
| Datasource | Mecanismo que informa onde os dados estão |

O datasource pode ser metadata service, config drive, NoCloud, OpenStack, EC2, Azure, VMware, LXD ou outro suportado. O operador normalmente não precisa escolher manualmente quando a plataforma se identifica, mas deve conhecer o datasource ao diagnosticar.

## Estágios

O boot percorre etapas local, network, config e final. A etapa local descobre dados que podem estar disponíveis sem rede. A etapa network processa configuração que depende da rede. A etapa config executa módulos de configuração. A etapa final executa scripts e tarefas tardias.

Um script de user-data não é um serviço de inicialização geral. Ele roda conforme o módulo e a frequência definidos pelo cloud-init. Coloque lógica pequena e observável no bootstrap e mova a configuração longa para uma ferramenta apropriada.

## Exemplo NoCloud

Uma instância local pode receber um seed com metadata e user-data:

```yaml
instance-id: vm-001
local-hostname: app-001
```

```yaml
#cloud-config
users:
  - name: deploy
    groups: sudo
    shell: /bin/bash
    ssh_authorized_keys:
      - ssh-ed25519 AAAA...
packages:
  - curl
runcmd:
  - [systemctl, enable, --now, ssh]
```

O conteúdo real deve usar uma chave pública válida e ser entregue por um mecanismo de seed ou datasource. Não versionar chaves privadas nem senhas no user-data.

## Reexecução e estado

cloud-init identifica a instância por instance-id e mantém estado em disco. Alterar user-data numa instância já inicializada não significa que os módulos serão executados novamente. Para testar uma configuração nova, crie uma instância nova ou use os comandos de limpeza somente em uma máquina descartável.

Depois do boot, consulte:

```bash
cloud-init status --long
cloud-init analyze show
journalctl -u cloud-init-local
journalctl -u cloud-init
journalctl -u cloud-config
journalctl -u cloud-final
```

## Segurança

User-data pode conter scripts executados com privilégio elevado. Trate metadata e config drive como entrada privilegiada, proteja endpoints e não permita que qualquer usuário altere o conteúdo de inicialização.

Não coloque segredos permanentes em user-data. Prefira identidade de máquina, secret manager e rotação. Reduza o tempo de vida de credenciais temporárias e limpe logs que possam conter tokens.

## Relação com configuração

cloud-init deve estabelecer os pré-requisitos de uma máquina: identidade, rede, usuário de automação, repositórios e agente. Ansible, Puppet ou outro sistema pode configurar o restante. Repetir a mesma responsabilidade em cloud-init e na ferramenta posterior cria divergência e falhas difíceis de reproduzir.

## Relações

- [Cloud image](cloud-image.md) explica o artefato que normalmente contém cloud-init.
- [Ansible](../ansible.md) pode assumir configuração posterior.
- [Instalação pela rede](../sistemas/boot/network-install.md) trata o caminho de instalação.

## Fontes primárias

- [cloud-init documentation](https://docs.cloud-init.io/)
- [Datasources](https://docs.cloud-init.io/en/latest/reference/datasources.html)
- [Boot stages](https://docs.cloud-init.io/en/latest/explanation/boot.html)
- [NoCloud](https://docs.cloud-init.io/en/latest/reference/datasources/nocloud.html)
