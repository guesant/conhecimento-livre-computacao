# Ciclo de vida, bugs e CVEs

O ciclo de vida de uma distribuição define por quanto tempo uma determinada combinação de pacotes continua recebendo correções, atualizações de segurança e suporte. Ele é diferente do ciclo de desenvolvimento do projeto. Uma distribuição pode lançar uma versão nova a cada seis meses e manter versões de suporte estendido por vários anos.

## LTS e LTSC

LTS significa Long Term Support. É uma política de suporte prolongado para uma versão específica. Durante essa janela, o projeto prioriza correções de segurança, bugs importantes e compatibilidade em vez de atualizar continuamente todo o conjunto de funcionalidades. LTS não significa que nenhum pacote muda, que toda dependência terá o mesmo prazo ou que o sistema ficará livre de regressões. Significa que existe uma promessa de manutenção mais longa e mais previsível que a de uma release intermediária.

LTSC significa Long-Term Servicing Channel. É o nome usado pela Microsoft para um canal e uma edição de Windows voltados a dispositivos de função especial, como equipamentos industriais, quiosques e sistemas embarcados. O objetivo é reduzir mudanças de funcionalidades durante o ciclo de serviço. LTSC não é simplesmente "Windows comum com mais anos": a edição possui disponibilidade, aplicativos, políticas de atualização e compatibilidade próprios. A Microsoft informa, por exemplo, que Windows 11 Enterprise LTSC 2024 tem ciclo de cinco anos, enquanto a edição IoT Enterprise LTSC 2024 tem ciclo diferente e mais longo. A edição e o contrato precisam ser confirmados antes da implantação.

LTS e LTSC resolvem problemas parecidos, mas não são sinônimos. LTS descreve uma política de manutenção de uma release. LTSC descreve uma linha de serviço e um produto da Microsoft, com um conjunto específico de expectativas sobre mudanças e uso. Em qualquer dos casos, "suporte" precisa ser decomposto em atualizações de segurança, correções de bugs, suporte técnico, cobertura de componentes e possibilidade de adquirir manutenção estendida.

## Exemplos de políticas

### Ubuntu

Ubuntu publica releases intermediárias a cada seis meses e uma LTS a cada dois anos, normalmente em abril de anos pares. A release intermediária recebe atualizações por uma janela curta e serve para quem precisa de kernels, toolchains e funcionalidades mais recentes. A LTS é direcionada a produção e projetos que preferem reduzir migrações frequentes. A política padrão atual informa cinco anos de manutenção de segurança para os pacotes da base principal; Ubuntu Pro pode estender a cobertura com ESM e serviços adicionais, conforme a assinatura e o componente do repositório.

Esse modelo separa cadência de desenvolvimento de compromisso de manutenção. Uma equipe pode testar a próxima geração numa release intermediária ou num ambiente de desenvolvimento, mas manter servidores na LTS e planejar a migração antes do fim do suporte.

### Debian

Debian não chama suas releases de LTS da mesma maneira que Ubuntu. A versão `stable` é a release de produção. O ciclo oficial de uma stable é de cinco anos, com aproximadamente três anos de suporte completo e dois anos de Debian LTS. A cobertura exata depende da arquitetura, do pacote e da capacidade dos mantenedores; pacotes fora do escopo da equipe LTS podem exigir outra estratégia.

Debian mantém simultaneamente `stable`, `testing` e `unstable`. Stable prioriza previsibilidade. Testing recebe pacotes que ainda não entraram na próxima stable depois de satisfazer critérios de migração. Unstable, também chamada Sid, é a linha de desenvolvimento ativa e recebe primeiro grande parte dos pacotes. Testing e unstable não devem ser tratados como equivalentes a uma release LTS para servidores críticos.

### Windows

Nas edições comuns do Windows, o canal de disponibilidade geral recebe atualizações de segurança e funcionalidades conforme a política da versão. O Windows Enterprise LTSC é uma alternativa para dispositivos especializados que não devem receber a mesma cadência de funcionalidades do canal geral. Ele não é a escolha padrão para toda estação de trabalho ou servidor, porque aplicativos, ferramentas e suporte de hardware podem esperar o canal geral.

O Windows Insider permite testar compilações antes da disponibilidade geral. A Microsoft organiza as compilações por canais, como Canary, Dev, Beta e Release Preview, com diferentes níveis de proximidade da release final. Os nomes e a composição dos canais podem mudar, portanto o Flight Hub e as notas atuais devem ser usados para confirmar o estado de cada build.

## Canais de release

Um canal descreve a distância entre uma mudança e o uso considerado estável. Ele não é automaticamente um nível de suporte nem uma promessa de qualidade. O mesmo nome pode significar políticas diferentes entre projetos.

| Canal | Objetivo | Risco típico | Uso adequado |
| --- | --- | --- | --- |
| Stable ou general availability | Entregar uma versão para uso normal | Bugs ainda podem existir | Produção e uso geral |
| LTS ou long-term | Manter uma base por período prolongado | Pacotes podem ficar antigos | Produção com migração planejada |
| Testing, beta ou preview | Validar mudanças antes da estabilidade | Regressões e mudanças de contrato | Homologação e testes |
| Unstable, canary ou nightly | Integrar mudanças rapidamente | Falhas frequentes e suporte limitado | Desenvolvimento e experimentação |
| Freeze | Reduzir ou bloquear novas mudanças | Correções podem esperar critérios especiais | Preparação de release |

### Insider

Insider é um programa de pré-lançamento. O participante recebe builds de desenvolvimento, testa funcionalidades e fornece telemetria ou feedback antes da distribuição geral. Um canal Insider não deve ser instalado em uma máquina que precisa de disponibilidade previsível sem uma estratégia de recuperação. O fato de uma build chegar antes não significa que ela seja uma atualização de segurança mais adequada ou que possa ser revertida sem reinstalação.

No Windows, os canais mais próximos do desenvolvimento recebem mudanças que podem nunca chegar à edição comercial da forma testada. Beta e Release Preview ficam mais próximos da estabilização, mas continuam sendo prévias. O ambiente precisa ser descartável ou possuir backup, imagem e procedimento de retorno.

### Unstable

Unstable é uma linha de integração ativa. No Debian, Sid recebe trabalho de desenvolvimento e pode sofrer mudanças que exigem intervenção manual. Unstable pode ser excelente para empacotadores, desenvolvedores e usuários que precisam acompanhar o estado atual, mas é uma escolha diferente de executar stable com backports.

O termo também aparece em outras distribuições e repositórios. Ele deve ser interpretado pelo projeto que o publica. Em alguns casos representa uma branch rolling; em outros, representa apenas um repositório de pacotes ainda não promovidos.

### Freeze

Freeze é uma restrição deliberada no fluxo de mudanças antes de uma release. Durante um freeze, novos recursos, mudanças de interface ou atualizações de pacotes ficam bloqueados ou passam por critérios mais rigorosos. O objetivo é permitir que mantenedores testem o conjunto candidato sem que novas mudanças reabram problemas já investigados.

Um freeze não significa que o código parou de mudar. Correções de bugs de release, segurança, documentação, tradução e problemas críticos podem continuar entrando, normalmente com revisão adicional. Em Debian, o caminho de testing até stable inclui períodos e critérios de freeze; a política exata e as exceções são definidas pelos responsáveis da release.

## Como combinar ciclo, canal e suporte

Uma política de atualização madura registra três decisões separadas:

1. qual versão ou linha recebe o tráfego de produção;
2. qual canal recebe mudanças antecipadas para teste;
3. qual é o procedimento de migração, rollback e encerramento do suporte.

Uma organização pode executar Ubuntu LTS em produção, acompanhar a próxima release em homologação e usar builds de desenvolvimento em um laboratório. Pode usar Debian stable nos servidores, testing em uma estação de empacotamento e unstable para desenvolver pacotes. Pode usar Windows Enterprise LTSC em um equipamento de função fixa e o canal geral ou Insider em máquinas de validação. O erro é tratar todos esses canais como se fossem apenas números diferentes da mesma versão.

## Tipos de manutenção

Uma equipe pode publicar correções de três formas.

| Estratégia | Como funciona | Benefício | Custo |
| --- | --- | --- | --- |
| Backport | A correção é aplicada ao pacote antigo da release. | Reduz mudanças inesperadas. | Exige manutenção adicional e pode divergir do upstream. |
| Upgrade dentro da release | O pacote é atualizado para uma versão mais nova compatível. | Entrega melhorias além da correção. | Pode alterar comportamento e dependências. |
| Upgrade de release | O sistema migra para uma nova base e um novo conjunto de pacotes. | Renova a plataforma inteira. | Exige planejamento, testes e rollback. |

Uma CVE é uma identificação de vulnerabilidade, não uma instrução universal de upgrade. O administrador deve consultar o aviso da distribuição, verificar o pacote instalado, confirmar a versão corrigida e validar se a instalação realmente recebeu a atualização.

## Bugs e vulnerabilidades

Bugs de empacotamento, regressões e falhas de segurança são problemas diferentes, embora possam compartilhar o mesmo rastreador. Um bug pode afetar apenas uma combinação de hardware e configuração. Uma CVE normalmente tem impacto de segurança documentado, severidade e uma versão corrigida.

O fluxo típico é:

1. o problema é reportado ao projeto upstream ou ao mantenedor da distribuição;
2. o impacto é analisado e, quando aplicável, recebe uma identificação CVE;
3. a correção é preparada para cada branch suportada;
4. o pacote é testado e publicado com um aviso;
5. o usuário atualiza o sistema e valida o serviço afetado.

Em uma distribuição rolling, uma atualização parcial pode misturar versões incompatíveis. Em uma distribuição estável, bloquear atualizações indefinidamente pode deixar uma correção de segurança ausente. A política deve considerar o ambiente, o risco e o suporte disponível, não apenas a idade do pacote.

## Como escolher

Para servidores críticos, prefira uma distribuição com ciclo explícito, avisos de segurança rastreáveis e um canal de suporte compatível com o impacto da indisponibilidade. Para estações de trabalho, uma release intermediária ou rolling pode oferecer hardware e software mais novos, desde que haja capacidade para acompanhar mudanças.

## Fontes primárias

- [CVE Program](https://www.cve.org/)
- [NVD](https://nvd.nist.gov/)
- [Ubuntu Security Notices](https://ubuntu.com/security/notices)
- [Ubuntu release cycle](https://ubuntu.com/about/release-cycle)
- [Debian Security Information](https://www.debian.org/security/)
- [Debian releases](https://www.debian.org/releases/)
- [Red Hat Security Advisories](https://access.redhat.com/security/security-updates/)
- [Windows release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information)
- [Windows Insider Flight Hub](https://learn.microsoft.com/en-us/windows-insider/flight-hub/)
- [Windows Enterprise LTSC 2024 lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/windows-11-enterprise-ltsc-2024)
