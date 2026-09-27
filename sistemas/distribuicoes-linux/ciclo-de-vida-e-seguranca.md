# Mapa de ciclo de vida das distribuições

O ciclo de vida define por quanto tempo uma combinação de pacotes recebe
correções, atualizações de segurança e suporte. Ele é diferente do ciclo de
desenvolvimento: uma distribuição pode lançar versões com frequência e manter
uma release específica durante vários anos.

## Dimensões que não devem ser confundidas

O nome de uma linha não responde sozinho quanto tempo ela será mantida. Separe:

| Dimensão | Pergunta |
| --- | --- |
| Release | Qual conjunto de pacotes e contratos está instalado? |
| Canal | Com que antecedência mudanças chegam ao usuário? |
| Suporte | Quem corrige bugs e por quanto tempo? |
| Cobertura | Quais pacotes, arquiteturas e repositórios estão incluídos? |
| Manutenção | A correção chega por backport, upgrade ou nova release? |
| Produto | Existe contrato comercial, certificação ou SLA? |

[LTS](lts.md) explica manutenção prolongada. [LTSC](ltsc.md) explica a linha
de serviço da Microsoft, que não é sinônimo de LTS. [Canais de release](canais-de-release.md)
explica stable, testing, unstable, preview, Insider, canary e freeze.

## Exemplos de políticas

Ubuntu possui releases intermediárias e releases LTS. Debian organiza stable,
testing e unstable e possui um período de Debian LTS. RHEL possui uma política
empresarial de ciclo e errata. Fedora entrega uma linha com mudanças mais
rápidas, enquanto CentOS Stream ocupa uma posição de desenvolvimento no
ecossistema Red Hat.

openSUSE diferencia Leap e Tumbleweed. Arch é rolling release. Manjaro promove
pacotes por branches. Alpine mantém linhas estáveis e Edge. KDE neon usa uma
base Ubuntu LTS para entregar o KDE Plasma em ritmo próprio, enquanto Kubuntu é
uma flavor oficial do Ubuntu.

As políticas concretas pertencem às páginas de cada distribuição. O mapa não
substitui a consulta da data de fim de suporte, do advisory ou do contrato da
edição que será implantada.

## Bugs e vulnerabilidades

Um bug pode atingir uma configuração ou combinação de hardware sem ser uma
vulnerabilidade de segurança. [CVE](../../seguranca/cve.md) é um identificador
para uma vulnerabilidade divulgada e não uma medida automática de exploração ou
uma instrução universal de upgrade.

O fluxo de manutenção costuma ser:

1. o problema é reportado ao upstream ou ao mantenedor da distribuição;
2. o impacto e as versões afetadas são analisados;
3. a correção é preparada para cada branch suportada;
4. o pacote ou a imagem é publicado com advisory e assinatura;
5. o operador atualiza e valida o serviço afetado.

Uma distribuição estável pode fazer backport para preservar compatibilidade. Uma
linha rolling pode entregar a versão corrigida do upstream mais rapidamente, ao
custo de maior mudança simultânea. Nenhuma estratégia elimina a necessidade de
testar, observar e planejar rollback.

## Relações

- [Distribuições Linux](index.md) organiza as famílias e páginas de cada projeto.
- [Governança e distribuição](governanca-e-distribuicao.md) separa quem mantém,
  constrói, assina, publica e oferece suporte.
- [Segurança e empacotamento](seguranca-e-empacotamento.md) explica defaults,
  MAC, repositórios, assinaturas e correções.

## Fontes primárias

- [CVE Program](https://www.cve.org/)
- [Ubuntu release cycle](https://ubuntu.com/about/release-cycle)
- [Debian releases](https://www.debian.org/releases/)
- [Red Hat product life cycles](https://access.redhat.com/support/policy/updates/errata)
- [Windows release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information)
