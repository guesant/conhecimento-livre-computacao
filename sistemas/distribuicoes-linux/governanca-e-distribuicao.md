# Governança e distribuição das distribuições Linux

Uma distribuição Linux não é controlada por uma única entidade em todos os sentidos. Há uma diferença entre quem define a direção do projeto, quem mantém os pacotes, quem opera o processo de build, quem assina e publica os repositórios, quem mantém os espelhos e quem oferece suporte comercial. Em projetos comunitários essas funções podem estar espalhadas entre voluntários, fundações, associações e empresas. Em produtos empresariais, várias delas ficam sob o controle de uma companhia.

## As responsabilidades que costumam ser confundidas

Quando alguém pergunta quem controla uma distribuição, é preciso separar pelo menos seis responsabilidades.

| Responsabilidade | Pergunta respondida | Exemplos de responsáveis |
| --- | --- | --- |
| Governança do projeto | Quem define prioridades, políticas e regras de contribuição? | Conselho, líder eleito, comitês técnicos, mantenedores e contribuidores |
| Propriedade e representação | Quem pode assinar contratos, possuir marcas e administrar recursos? | Empresa, fundação, associação ou entidade legal do projeto |
| Manutenção técnica | Quem revisa código, pacotes, correções e mudanças de release? | Mantenedores, equipes de segurança e comitês técnicos |
| Engenharia de release | Quem compila, testa, promove e publica artefatos? | Equipe de infraestrutura, build farm e release engineering |
| Distribuição | Quem disponibiliza imagens, repositórios, metadados e espelhos? | Arquivo do projeto, CDN, mirrors, parceiros e provedores de nuvem |
| Suporte | Quem responde por correções, documentação, consultoria e SLA? | Comunidade, empresa patrocinadora, revendedores e integradores |

Essas responsabilidades se relacionam, mas não são equivalentes. Uma empresa pode patrocinar uma distribuição sem decidir cada pacote. Uma fundação pode deter marcas e infraestrutura sem aprovar cada mudança técnica. Um espelho pode distribuir um arquivo sem ser seu autor ou mantenedor.

## O caminho de um pacote até o usuário

O processo normalmente começa com o código upstream, uma correção de segurança ou uma receita de empacotamento. Um mantenedor adapta o material para a política da distribuição, declara dependências e produz um pacote fonte. A infraestrutura de build compila o pacote para cada arquitetura, executa testes e gera os artefatos binários.

Depois disso, um sistema de arquivo ou repositório publica os pacotes, índices, metadados e assinaturas. Espelhos e CDNs replicam esse conteúdo. O gerenciador de pacotes do usuário verifica os metadados e instala o artefato. Em imagens imutáveis, containers e sistemas transacionais, a unidade distribuída pode ser uma imagem, um deployment ou um snapshot em vez de um pacote individual.

A cadeia de confiança precisa responder quem construiu, quem assinou, qual origem foi usada e como uma correção chega ao usuário. A assinatura do repositório prova uma relação criptográfica com a chave publicada pela distribuição, mas não significa que o projeto upstream, a distribuição e o espelho sejam a mesma organização.

## Como as decisões são distribuídas

Uma mudança pode passar por vários níveis. O mantenedor decide se o pacote está tecnicamente pronto. Uma equipe de segurança coordena a divulgação e a correção de uma vulnerabilidade. Um comitê ou líder decide uma política que afeta todo o projeto. A engenharia de release escolhe quando promover o artefato. A empresa patrocinadora decide contratos, produtos e suporte comercial. O usuário escolhe quais repositórios e imagens vai consumir.

Em projetos comunitários, o poder costuma vir da combinação entre contribuição reconhecida, consenso, regras técnicas e autoridade delegada. Em produtos empresariais, a companhia pode ter a palavra final sobre marca, ciclo de vida, repositórios de clientes e suporte, mesmo que o desenvolvimento conte com uma comunidade ampla.

## Projetos, empresas e fundações

Uma fundação ou associação pode existir para administrar recursos, marcas, contratos, doações, eventos, infraestrutura e representação legal. Ela não precisa ser a autora de todo o software. Em outros casos, a empresa é simultaneamente proprietária do produto, empregadora dos mantenedores, operadora dos builders e fornecedora do suporte.

Também há projetos que não possuem uma fundação exclusiva. Neles, a governança pode ser exercida por uma comunidade, um conjunto de mantenedores e uma empresa patrocinadora. Essa ausência de uma fundação não significa ausência de regras, mas torna importante identificar onde ficam as decisões técnicas e a responsabilidade legal.

## Comparativo das principais distribuições

| Distribuição ou projeto | Quem coordena | Quem constrói e publica | O papel do patrocinador ou da comunidade |
| --- | --- | --- | --- |
| Debian | Debian Project, com Debian Developers, líder eleito e órgãos técnicos | Mantenedores, equipes de release e o arquivo Debian, administrado pelo fluxo de FTPMaster | Projeto comunitário. Empresas podem financiar pessoas e serviços, mas não possuem o Debian |
| Ubuntu | Canonical define o produto, o ciclo e a oferta comercial; comunidades e conselhos participam do ecossistema | Infraestrutura Canonical, Launchpad, arquivos APT, imagens e CDNs | Canonical mantém o produto e o suporte comercial; a comunidade contribui com pacotes, documentação, flavors e decisões comunitárias |
| RHEL | Red Hat | Infraestrutura de build, repositórios e errata da Red Hat | Produto empresarial sob controle da Red Hat, com subscrição, certificações e suporte |
| Fedora | Fedora Project, Fedora Council e FESCo | Infraestrutura Fedora, Koji, Bodhi, repositórios e mirrors | Red Hat é patrocinadora principal e fornece recursos, mas Fedora é um projeto comunitário com governança própria |
| CentOS Stream | CentOS Project no ecossistema Red Hat | Infraestrutura CentOS e Red Hat, com promoção de mudanças para a linha de desenvolvimento do RHEL | É uma linha comunitária patrocinada pela Red Hat, situada entre Fedora e as atualizações menores do RHEL |
| openSUSE | openSUSE Project e suas equipes comunitárias | Open Build Service, repositórios e mirrors do projeto | SUSE patrocina e compartilha tecnologia, mas uma instalação comunitária openSUSE não equivale a um contrato SUSE Enterprise |
| Manjaro | Comunidade e Core Team do Manjaro | Ferramentas e infraestrutura Manjaro, com promoção entre Unstable, Testing e Stable | Projeto comunitário, com liderança e colaboradores próprios; o suporte principal é comunitário |
| Linux Mint | Linux Mint Development Team | Infraestrutura Mint e repositórios Ubuntu ou Debian usados pela edição escolhida | Projeto orientado à comunidade, financiado por doações e outras receitas; Cinnamon é mantido pelo próprio ecossistema Mint |
| Alpine Linux | Alpine Council, Technical Steering Committee e Developers | aports, abuild, builders, repositórios e mirrors Alpine | Projeto comunitário; o Council possui autoridade final de governança e o TSC conduz políticas técnicas do dia a dia |
| Arch Linux | Projeto voluntário, líder do projeto, desenvolvedores, mantenedores de pacotes e equipe de suporte | Build e repositórios oficiais Arch, com mirrors; AUR é uma camada comunitária separada | Decisões são tomadas pelos contribuidores ativos, normalmente por consenso; não há uma empresa controladora equivalente à Canonical ou Red Hat |
| KDE neon | Projeto KDE neon, separado do Ubuntu e da Canonical | Infraestrutura KDE neon, CI, builders e repositórios próprios sobre uma base Ubuntu LTS | É um projeto do KDE. A base Ubuntu e os pacotes KDE possuem responsabilidades distintas |
| Kubuntu | Comunidade Kubuntu dentro do ecossistema Ubuntu | Infraestrutura e arquivos Ubuntu, com trabalho de empacotamento e integração Kubuntu | Flavor oficial do Ubuntu, com participação comunitária e marca registrada da Canonical |

Essa tabela não deve ser lida como se toda decisão passasse por um único conselho. Ela identifica o centro de gravidade de cada projeto. Um bug do Plasma pode ser decidido no KDE, seu pacote pode ser adaptado pelo mantenedor de uma distribuição e seu suporte pode depender da empresa que oferece o contrato ao usuário.

## Repositórios oficiais, derivados e fontes externas

Uma distribuição geralmente possui um arquivo principal dividido por releases, arquiteturas e componentes. Os mantenedores controlam quais pacotes entram, em qual versão e com quais patches. Derivados podem reutilizar a base e trocar o desktop, adicionar um repositório próprio ou aplicar uma política diferente de atualização.

Isso explica por que duas distribuições baseadas no mesmo projeto podem oferecer versões, defaults e tempo de correção diferentes. O código pode ser o mesmo, mas a receita, o patch, o builder, a chave de assinatura, a política de promoção e o canal de suporte podem não ser.

PPAs, COPR, AUR, overlays e repositórios de terceiros ampliam o catálogo, mas introduzem outro responsável pela construção e pela assinatura. Antes de adicioná-los, identifique quem controla a infraestrutura, se há revisão de código, como ocorre a rotação de chaves e qual é o procedimento quando uma versão deixa de ser mantida.

## Imagens, mirrors e distribuição comercial

O projeto pode publicar imagens de instalação, imagens cloud, imagens para containers, artefatos para máquinas virtuais e repositórios de pacotes. Esses produtos podem compartilhar código e ainda assim ter pipelines, cadências e equipes diferentes.

Mirrors são cópias autorizadas ou sincronizadas do conteúdo publicado. Eles reduzem latência e carga, mas não costumam decidir o conteúdo. A decisão continua no arquivo, no pipeline de release e nas chaves de assinatura da distribuição. CDNs acrescentam cache e disponibilidade, porém também não substituem a autoridade do repositório.

Suporte comercial adiciona uma relação contratual. Ele pode incluir acesso a repositórios, errata, certificações, consultoria, resposta a incidentes e SLA. Não se deve concluir que uma distribuição comunitária deixa de ser confiável por não oferecer SLA, nem que uma distribuição empresarial elimina a necessidade de verificar a origem dos pacotes.

## O que verificar antes de escolher uma distribuição

Além do desktop e da aparência, verifique quem publica correções, como são assinados os repositórios, onde ficam os avisos de segurança, qual é o ciclo de vida, que arquiteturas recebem suporte e qual equipe responde por bugs. Em uma organização, registre também se o contrato cobre os pacotes adicionais, o hypervisor, o kernel, os drivers e os repositórios externos usados pela carga.

Uma decisão madura separa a pergunta técnica, como a forma de atualizar e fazer rollback, da pergunta institucional, como quem aceita o incidente e fornece suporte. Ambas são necessárias para entender o risco real de operar a distribuição.

## Fontes primárias

- [Debian Project Leader](https://www.debian.org/devel/leader)
- [Debian FTPMaster](https://ftp-master.debian.org/)
- [Canonical](https://canonical.com/company)
- [Fedora governance](https://fedoraproject.org/wiki/Leadership)
- [Fedora sponsors](https://fedoraproject.org/fur/sponsors/)
- [Alpine governance](https://docs.alpinelinux.org/governance/0.1b/Teams/index.html)
- [Arch governance](https://wiki.archlinux.org/title/DeveloperWiki%3AGovernance_And_Decision_Making)
- [Manjaro team](https://manjaro.org/team/)
- [Linux Mint](https://www.linuxmint.com/about.php)
- [KDE neon FAQ](https://neon.kde.org/faq)
- [KDE neon development](https://neon.kde.org/develop)
- [Kubuntu community](https://kubuntu.org/community/)
