# Canais de release

Um canal de release descreve a distância entre uma mudança e o uso considerado
estável. Ele não é automaticamente um nível de suporte nem uma promessa de
qualidade. O mesmo nome pode representar políticas diferentes entre projetos.

## Tipos de canal

| Canal | Objetivo | Risco típico | Uso adequado |
| --- | --- | --- | --- |
| Stable ou general availability | Uso normal | Bugs ainda podem existir | Produção e uso geral |
| LTS ou long-term | Manutenção prolongada | Pacotes podem ficar antigos | Produção com migração planejada |
| Testing, beta ou preview | Validar mudanças | Regressões e mudanças de contrato | Homologação |
| Unstable, canary ou nightly | Integrar mudanças rapidamente | Falhas frequentes e suporte limitado | Desenvolvimento |
| Freeze | Reduzir mudanças antes de uma release | Correções podem aguardar critérios | Preparação de release |

## Insider

Insider é um programa de pré-lançamento. O participante recebe builds antes da
disponibilidade geral e aceita maior probabilidade de regressões, mudanças de
contrato e necessidade de recuperação. O ambiente deve ter backup, imagem e
procedimento de retorno.

No Windows, os canais Canary, Dev, Beta e Release Preview ficam em distâncias
diferentes da release comercial. Os nomes e os detalhes mudam, portanto a
política vigente do produto deve ser consultada antes de classificar uma build.

## Unstable

Unstable é uma linha de integração ativa. No Debian, Sid recebe trabalho antes
das linhas stable e testing e pode exigir intervenção manual. Em outros projetos
o mesmo nome pode significar uma branch rolling ou apenas um repositório que
ainda não foi promovido.

Unstable é útil para desenvolvimento, empacotamento e validação de mudanças. Não
deve ser tratado como uma LTS apenas porque possui muitos pacotes atualizados.

## Freeze

Freeze restringe novas funcionalidades e alterações de alto risco antes de uma
release. Correções críticas, segurança, documentação e problemas de release
podem continuar entrando com revisão adicional. O objetivo é testar um conjunto
candidate sem reabrir continuamente problemas já investigados.

Um freeze não significa que o código deixou de mudar. Significa que os critérios
para aceitar mudanças ficaram mais rigorosos e que o escopo da release passou a
ser protegido.

## Relações

- [LTS](lts.md) explica manutenção prolongada.
- [LTSC](ltsc.md) explica o canal de serviço da Microsoft.
- [Ciclo de vida das distribuições](ciclo-de-vida-e-seguranca.md) relaciona
  canais a bugs, vulnerabilidades e suporte.

## Fontes primárias

- [Debian releases](https://www.debian.org/releases/)
- [Debian testing migration](https://www.debian.org/doc/manuals/developers-reference/testing.en.html)
- [Windows Insider Flight Hub](https://learn.microsoft.com/en-us/windows-insider/flight-hub/)
