# Fundações e governança dos ambientes desktop

Um ambiente de desktop também possui uma cadeia institucional. O projeto upstream define código, APIs, guidelines e prioridades. Uma fundação ou associação pode cuidar de representação legal, marcas, contratos, doações e infraestrutura. Distribuições empacotam o resultado, escolhem versões e alteram defaults. Empresas podem patrocinar pessoas, eventos e builders sem controlar cada decisão técnica.

Por isso, GNOME, KDE Plasma, Xfce e Cinnamon não devem ser tratados como se fossem produtos equivalentes a Ubuntu, Fedora ou Debian. O desktop é uma camada de software que pode ser empacotada por várias distribuições. A distribuição decide como ele chega ao usuário, mas não necessariamente decide sua arquitetura ou roadmap upstream.

## Quatro planos de responsabilidade

| Plano | Responsabilidade | Exemplo |
| --- | --- | --- |
| Projeto técnico | Código, APIs, arquitetura, bugs e roadmap | GNOME Shell, Mutter, Plasma, KWin, GTK, Qt |
| Entidade legal | Marcas, contratos, contas, propriedade e representação | GNOME Foundation ou KDE e.V. |
| Distribuição | Pacotes, patches, integração, defaults e ciclo de atualização | Fedora GNOME, Debian KDE, Kubuntu |
| Usuário ou organização | Seleção, configuração, operação e suporte local | Escolha de sessão, políticas, extensões e repositórios |

Esses planos podem estar próximos, mas não são a mesma autoridade. Uma distribuição pode aplicar um patch em um pacote sem alterar o projeto upstream. Uma fundação pode administrar o domínio e os ativos do projeto sem revisar cada pull request. Um mantenedor de pacote pode decidir quando uma versão chega ao repositório da distribuição.

## GNOME Foundation

A GNOME Foundation é uma organização sem fins lucrativos que representa o projeto GNOME em assuntos legais e financeiros. Ela administra recursos, apoia infraestrutura e eventos e fornece uma estrutura de participação para membros do projeto. Sua governança inclui conselho eleito, direção executiva, membros e um conselho consultivo.

Isso não significa que a Foundation aprove todas as alterações do GNOME. A implementação é desenvolvida por contribuidores e equipes técnicas que mantêm componentes como GNOME Shell, Mutter, GTK e as aplicações. A Foundation oferece o suporte institucional para que o projeto opere; as decisões de engenharia permanecem distribuídas entre mantenedores, revisores e grupos técnicos.

Quando uma distribuição entrega GNOME, ela ainda precisa empacotar os componentes, escolher a versão, aplicar patches, configurar defaults e integrar serviços como display manager, portals, áudio, rede e atualizações. Um problema pode portanto pertencer ao GNOME upstream, ao pacote da distribuição ou à integração local.

## KDE e.V e a comunidade KDE

KDE é uma comunidade que desenvolve Plasma, KDE Frameworks, aplicações, bibliotecas e ferramentas de desenvolvimento. A KDE e.V. é uma associação sem fins lucrativos que representa a comunidade em assuntos legais e financeiros, administra ativos e marcas, apoia infraestrutura e organiza eventos e programas de contribuição.

A associação não substitui os mantenedores dos componentes. Plasma, KWin, Frameworks e aplicações têm equipes, revisores e ciclos próprios. O projeto KDE neon, por sua vez, constrói uma distribuição específica dos componentes KDE sobre uma base Ubuntu LTS. Kubuntu integra KDE dentro do ciclo Ubuntu. Fedora KDE, Debian KDE e openSUSE KDE fazem outras escolhas de empacotamento.

Assim, dizer que um desktop é “do KDE” pode significar a origem do código ou a comunidade que o desenvolve, mas não identifica sozinho quem publica o pacote instalado nem quem oferece suporte à máquina.

## Xfce

Xfce é um ambiente modular formado por componentes que podem ser empacotados separadamente. O projeto prioriza leveza, modularidade e interoperabilidade com padrões do ecossistema freedesktop.org. Sua coordenação ocorre por contribuidores, mantenedores e canais técnicos do próprio projeto.

Xfce não possui a mesma estrutura institucional da GNOME Foundation ou da KDE e.V. Isso não impede a manutenção do software. Significa apenas que a representação legal, os recursos e o processo de decisão devem ser analisados de acordo com o projeto e com a distribuição que o fornece.

## Cinnamon e outros ambientes

Cinnamon é desenvolvido no ecossistema Linux Mint e funciona como o desktop principal dessa distribuição. O Linux Mint Development Team coordena o desenvolvimento dos projetos Mint, incluindo Cinnamon. Outras distribuições podem empacotá-lo, mas a existência do pacote em outra distribuição não transfere a ela a governança upstream.

MATE, LXQt, Budgie e outros ambientes possuem comunidades e estruturas próprias. Nem todos precisam de uma fundação formal para produzir software estável. Para entender a autoridade de cada projeto, procure sua organização de mantenedores, o repositório upstream, a política de contribuição, os canais de release, a titularidade da marca e a entidade que aceita doações ou contratos.

## Quem decide o que chega ao desktop

Uma decisão de interface pode envolver várias camadas. O projeto upstream decide se uma API, comportamento ou componente será criado. O mantenedor da distribuição decide quando empacotar a versão e se aplicará patches. A equipe de integração decide o tema, os defaults, os aplicativos pré-instalados, a sessão Wayland ou X11 e a configuração de segurança. O administrador decide o que será habilitado na máquina.

Isso também explica conflitos aparentes. Uma funcionalidade pode existir no GNOME upstream, mas estar desabilitada na distribuição. Uma correção pode estar no KDE, mas aguardar revisão do pacote. Uma extensão pode funcionar em uma versão do GNOME Shell e quebrar na próxima sem que a distribuição ou a Foundation tenham decidido removê-la.

## Fundações, patrocinadores e distribuidores

Fundações e associações normalmente resolvem necessidades que um repositório de código não resolve sozinho: possuir uma marca, contratar infraestrutura, receber doações, organizar conferências, empregar pessoas, assinar contratos e representar o projeto perante terceiros. Patrocinadores podem fornecer dinheiro, empregados, servidores e serviços. Distribuições podem financiar empacotadores e ainda manter uma relação independente com o upstream.

Nenhum desses papéis deve ser inferido apenas pela popularidade do desktop. A forma correta de investigar é consultar a governança do projeto, a entidade legal, o conselho ou equipe de mantenedores, os patrocinadores declarados e a documentação da distribuição. Quando a pergunta for sobre suporte, consulte também o contrato e o ciclo de vida da distribuição, não apenas a página do desktop.

## Como analisar um problema

Comece identificando o componente exato. Um problema no compositor, no toolkit, no portal, no pacote ou no driver tem canais diferentes. Depois registre a versão do upstream, a versão empacotada, a distribuição e a sessão usada. Isso evita encaminhar para a Foundation um bug de integração da distribuição ou para o GNOME um problema exclusivo de uma extensão local.

Para uma organização, essa separação também melhora a gestão de risco. O projeto upstream pode oferecer comunidade e revisão pública, enquanto a distribuição oferece atualizações integradas. Um fornecedor comercial pode assumir suporte para a distribuição, mas não necessariamente para extensões, temas e repositórios externos adicionados pelo usuário.

## Fontes primárias

- [GNOME Foundation](https://foundation.gnome.org/)
- [Governança da GNOME Foundation](https://foundation.gnome.org/governance/)
- [KDE e.V.](https://ev.kde.org/)
- [O que é a KDE e.V.](https://ev.kde.org/whatiskdeev/)
- [Xfce](https://xfce.org/about)
- [Comunidade Xfce](https://xfce.org/community?lang=en)
- [Projetos do Linux Mint](https://projects.linuxmint.com/projects.html)
- [freedesktop.org](https://www.freedesktop.org/)
