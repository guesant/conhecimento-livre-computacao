# Red Hat Enterprise Linux

Red Hat Enterprise Linux, RHEL, é uma distribuição empresarial com ciclo previsível, certificações e suporte comercial da Red Hat. A plataforma é publicada em variantes de servidor, workstation, edge e imagens para nuvem, mas a diferença principal está no contrato, no perfil de uso e no conjunto de componentes habilitados.

## Produtos e variantes

| Variante | Foco |
| --- | --- |
| RHEL Server | Servidores físicos, virtuais e em nuvem. |
| RHEL Workstation | Estações profissionais com ferramentas de desenvolvimento e criação. |
| RHEL for Edge | Imagens e operação orientadas a edge, com atualização controlada. |
| RHEL for SAP Solutions | Requisitos certificados para cargas SAP. |
| Universal Base Image | Imagem base redistribuível para aplicações em containers, com suporte associado à subscrição RHEL. |
| RHEL CoreOS | Base imutável usada por plataformas específicas, como OpenShift. |

Essas variantes não são flavors de desktop equivalentes a Kubuntu ou Xubuntu. Elas formam produtos e perfis de suporte dentro da plataforma empresarial.

## Lançamento e suporte

RHEL possui um ciclo de vida empresarial longo, com fases de suporte completo, manutenção e opções estendidas conforme a versão e o contrato. A Red Hat oferece subscrições, suporte técnico, atualizações certificadas, documentação e acesso ao ecossistema de parceiros.

O custo não é apenas o download da imagem. Ele inclui o direito de acesso a repositórios, errata, suporte e certificações que fazem parte do modelo operacional da plataforma.

## Bugs e CVEs

A Red Hat publica RHSA para segurança, RHBA para correções de bugs e RHEA para melhorias e atualizações. O modelo empresarial privilegia errata versionada e backports compatíveis com a release. O administrador deve verificar o advisory específico e a versão corrigida, em vez de comparar apenas o número upstream do pacote.

## Segurança e defaults

RHEL usa SELinux como mecanismo MAC central e normalmente inicia com a política targeted em modo enforcing. A política confina principalmente serviços selecionados; permissões DAC, capabilities, systemd sandboxing e firewall continuam necessários.

O instalador e as políticas do produto normalmente orientam o uso de usuários nominativos, `sudo` e chaves SSH. O estado efetivo de `PermitRootLogin`, autenticação por senha, grupos administrativos e `umask` depende do perfil de instalação e de políticas como crypto-policies. Valide o host com `sshd -T`, `getenforce`, `sudo -l` e a configuração de PAM.

## Empacotamento

RHEL usa RPM, `dnf` e `rpm`. A Red Hat recebe fontes, patches e metadados de build, constrói pacotes em infraestrutura controlada, testa compatibilidade e publica repositórios e errata assinados para os clientes autorizados. Os detalhes internos do build empresarial não equivalem ao pipeline público do Fedora.

O sistema de errata permite associar atualização, bug, CVE, severidade e release. Isso torna a consulta do advisory mais importante que comparar somente o número de versão do projeto upstream. EPEL e outros repositórios não são automaticamente cobertos pelo mesmo escopo de suporte.

## Suporte comunitário

Há documentação pública, comunidades, Bugzilla e projetos relacionados, como CentOS Stream e Fedora. Esses canais são úteis, mas não substituem a cobertura contratual, a certificação ou o SLA de uma subscrição Red Hat.

## Fontes primárias

- [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)
- [Red Hat errata policy](https://access.redhat.com/support/policy/updates/errata)
- [Red Hat security updates](https://access.redhat.com/security/security-updates/)
