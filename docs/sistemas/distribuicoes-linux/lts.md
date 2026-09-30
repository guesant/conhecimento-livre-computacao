# LTS

Long Term Support, LTS, é uma política de manutenção prolongada para uma
release. Durante essa janela, o projeto prioriza correções de segurança, bugs
importantes e compatibilidade em vez de trocar continuamente todo o conjunto de
funcionalidades.

## O que a promessa significa

Uma LTS deve informar quais componentes recebem correções, por quanto tempo,
qual equipe mantém cada pacote e se existe suporte estendido comercial. A
palavra não garante que todos os pacotes tenham o mesmo prazo nem que nenhuma
dependência mude. Também não elimina regressões, mudanças de kernel, transições
de hardware ou a necessidade de testar atualizações.

O operador deve separar suporte de segurança, correção de bugs, suporte técnico,
certificação e manutenção de componentes opcionais. Uma release pode ter cinco
anos de manutenção da base principal e uma cobertura diferente para repositórios
externos, toolchains, drivers ou extensões contratadas.

## Quando usar

LTS é adequada quando a organização prefere planejar migrações maiores e receber
mudanças em ritmo previsível. Servidores, appliances e aplicações com testes
longos costumam se beneficiar dessa estabilidade. Ela é menos adequada quando o
hardware ou o software dependem de versões muito novas que não entram por
backport.

Uma política madura mantém uma release de teste, define a data de início da
migração e não espera o fim do suporte para começar a validar a sucessora.
Backports de segurança não substituem a renovação periódica da plataforma.

## Exemplos

Ubuntu usa releases LTS com ciclo mais longo que suas releases intermediárias.
Debian usa a versão stable como base de produção e possui um período de Debian
LTS, com cobertura condicionada ao pacote e à arquitetura. RHEL oferece um
ciclo empresarial próprio, com errata e suporte vinculados à política da Red Hat.

Os prazos e componentes cobertos mudam. A decisão deve consultar a política
vigente da distribuição e registrar qual edição, repositório e contrato foram
escolhidos.

## Relações

- [Ciclo de vida das distribuições](ciclo-de-vida-e-seguranca.md) compara LTS,
  canais e manutenção.
- [LTSC](ltsc.md) descreve a linha de serviço da Microsoft, que não é sinônimo
  de LTS.
- [Canais de release](canais-de-release.md) compara stable, testing, unstable,
  preview e freeze.

## Fontes primárias

- [Ubuntu release cycle](https://ubuntu.com/about/release-cycle)
- [Debian releases](https://www.debian.org/releases/)
- [Red Hat product life cycles](https://access.redhat.com/support/policy/updates/errata)
