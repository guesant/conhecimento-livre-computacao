# Open Source Security Foundation

A Open Source Security Foundation, ou OpenSSF, é uma iniciativa colaborativa
do ecossistema Linux Foundation dedicada a tornar mais sustentável a segurança
do desenvolvimento, da manutenção, da release e do consumo de software livre e
aberto.

Sua missão não é revisar manualmente todo projeto open source nem centralizar a
segurança em uma equipe. A OpenSSF procura criar práticas, ferramentas,
educação, padrões, sinais verificáveis e comunidades que reduzam o custo de
adotar segurança por mantenedores e consumidores.

## Por que a OpenSSF existe

Software aberto é uma infraestrutura pública compartilhada, mas a capacidade de
manutenção e segurança não é distribuída de maneira uniforme. Um componente
pequeno pode estar presente em milhares de produtos, enquanto seus mantenedores
possuem pouco tempo, pouca infraestrutura e nenhum orçamento dedicado.

Ao mesmo tempo, uma empresa pode consumir um pacote sem saber se a release veio
do source esperado, se o CI foi comprometido, se uma dependência foi trocada ou
se o projeto possui um processo confiável de resposta a vulnerabilidades.

A OpenSSF tenta melhorar esse problema em três frentes:

- tornar práticas seguras mais fáceis de adotar;
- produzir sinais e evidências úteis para quem consome software;
- reunir empresas, comunidades, pesquisadores e mantenedores para resolver
  problemas que nenhum projeto isolado consegue resolver sozinho.

## O que a OpenSSF é

A OpenSSF atua como:

- comunidade técnica para segurança de OSS;
- ambiente para working groups e iniciativas abertas;
- suporte a projetos e ferramentas de segurança;
- fonte de guias, cursos, baselines e práticas de desenvolvimento;
- fórum de colaboração com outras fundações, governos e organizações;
- espaço para discutir padrões, políticas e responsabilidade compartilhada.

Ela pode apoiar projetos como SLSA, Sigstore, Scorecard, GUAC e outros
componentes do ecossistema, mas cada projeto possui seu próprio repositório,
maintainers, escopo e governança. O leitor deve seguir a documentação do projeto
para entender seu status real.

## O que a OpenSSF não é

OpenSSF não é:

- uma certificadora universal de segurança de software;
- um substituto para revisão de código, testes ou threat modeling;
- um scanner que encontra todas as vulnerabilidades;
- uma garantia de que um projeto é seguro porque apareceu no seu catálogo;
- uma autoridade regulatória que aprova ou proíbe todo OSS;
- uma organização que controla os mantenedores de cada projeto aberto.

Uma ferramenta OpenSSF normalmente produz um sinal, uma atestação, um relatório,
uma política ou uma capacidade técnica. O consumidor precisa entender o que foi
medido, quais evidências foram observadas e quais riscos ficaram fora do
escopo.

## Estrutura e governança

A estrutura separa responsabilidades institucionais e técnicas:

| Parte | Responsabilidade típica |
| --- | --- |
| Governing Board | Orçamento, sustentabilidade institucional e direção organizacional |
| Technical Advisory Council | Estratégia técnica e coordenação das iniciativas técnicas |
| Working groups | Discussão e produção aberta em uma área de segurança |
| Maintainers de projetos | Código, releases e governança específica da ferramenta |
| Comunidade | Uso, revisão, issues, documentação e contribuições |
| Membros e apoiadores | Recursos financeiros, experiência e participação, sem autoridade automática sobre o código |

O Board e o TAC não administram diretamente cada working group ou projeto. A
governança técnica de uma iniciativa é definida pelos seus participantes e
mantenedores. Participar de uma empresa membro não concede automaticamente
direito de aprovar uma mudança ou escolher um maintainer.

As working groups são abertas a participantes que não são membros corporativos.
Isso é importante porque segurança de software aberto depende de mantenedores,
pesquisadores, estudantes, usuários e pequenas organizações, e não somente de
quem consegue pagar uma associação.

## Áreas de trabalho

As áreas mudam com o tempo, mas podem ser entendidas por responsabilidade:

### Práticas para desenvolvedores

Guias, checklists e treinamento ajudam projetos a adotar autenticação forte,
revisão, releases seguras, resposta a vulnerabilidades, proteção de dependências
e configuração de CI. O objetivo é transformar práticas difíceis de descobrir em
passos que um mantenedor consiga executar.

### Integridade da supply chain

Proveniência, atestações, assinaturas, SBOM, verificação de builders e políticas
de promoção ajudam a responder se o artefato recebido corresponde ao source e ao
processo esperados. [SLSA](../../seguranca/supply-chain/slsa.md) explica níveis e
garantias de build; [Sigstore](../../seguranca/supply-chain/sigstore.md) trata
de assinatura, identidade e transparência; [SBOM](../../seguranca/supply-chain/sbom.md)
descreve a composição do artefato.

Essas técnicas não são sinônimas. SLSA não é SBOM, Sigstore não é scanner de
vulnerabilidades e uma assinatura não prova que o source é seguro.

### Avaliação de repositórios

[OpenSSF Scorecard](../../seguranca/supply-chain/openssf-scorecard.md) observa
sinais públicos, como proteção de branch, revisão, pinagem de dependências,
testes de CI e publicação de artefatos. O score ajuda a priorizar investigação,
mas um projeto pode obter uma nota baixa por não expor uma prática que realmente
possui, ou uma nota alta sem que todos os riscos de domínio estejam resolvidos.

### Critical projects

Projetos críticos podem precisar de financiamento, engenharia dedicada,
melhoria de infraestrutura, auditorias, apoio a mantenedores, fuzzing e
processos de resposta. O objetivo não é criar um proprietário central para o
software, mas direcionar recursos para componentes cuja falha teria impacto
amplo.

### Educação e força de trabalho

Cursos, guias, mentorias e programas para diferentes perfis ajudam a formar
mantenedores e consumidores capazes de reconhecer risco. Segurança não deve ser
tratada como uma tarefa exclusiva de uma equipe de AppSec depois que o pacote
já foi publicado.

### Políticas e colaboração

A OpenSSF participa de discussões sobre padrões, regulação e práticas de
segurança. Esse trabalho pode apoiar governos, fornecedores e comunidades, mas
uma recomendação da fundação não substitui a interpretação jurídica de uma
regulação aplicável ao contexto da organização.

## Ferramentas e iniciativas relacionadas

| Iniciativa | Responsabilidade |
| --- | --- |
| Scorecard | Avaliar sinais observáveis de segurança e manutenção de repositórios |
| SLSA | Descrever níveis de confiança na origem e no processo de build |
| Sigstore | Assinar e verificar artefatos com identidades e transparência |
| GUAC | Relacionar evidências e metadados da supply chain para investigação |
| OSPS Baseline | Organizar requisitos de segurança para projetos open source |
| Allstar | Automatizar políticas e checks de segurança em repositórios |
| OSS-Fuzz | Executar fuzzing contínuo em projetos open source participantes |

O status e a relação institucional de cada iniciativa podem mudar. Consulte a
página oficial do projeto antes de afirmar que uma ferramenta é mantida,
certificada ou endossada pela OpenSSF.

## Como consumir os resultados

Um consumidor deve transformar sinais em decisões explícitas:

1. definir quais artefatos, dependências e projetos são críticos;
2. escolher propriedades mínimas, como provenance, assinatura ou revisão;
3. verificar a identidade do emissor e a versão da política;
4. distinguir ausência de evidência de evidência de ausência;
5. combinar Scorecard, SBOM, scanner, provenance, testes e revisão humana;
6. registrar exceções, prazo e responsável;
7. bloquear ou colocar em quarentena quando o risco exceder o limite adotado.

Não transforme uma pontuação em autorização cega. Um pacote pode ter bom
processo de release e uma vulnerabilidade grave; outro pode ter poucos sinais
públicos, mas ser operacionalmente importante e exigir investigação manual.

## Como um projeto pode participar

Um projeto pode participar em etapas diferentes:

- ler e aplicar guias de segurança;
- proteger branches, releases, tokens e dependências;
- configurar publicação de SBOM, provenance e assinaturas;
- habilitar reporte privado de vulnerabilidades;
- participar de uma working group ou de um projeto técnico;
- contribuir com código, documentação, testes, triagem ou pesquisa;
- candidatar-se a programas de apoio quando a iniciativa for adequada;
- compartilhar métricas e problemas sem expor dados sensíveis.

O caminho deve começar por controles que reduzam risco real. Produzir um
relatório bonito sem corrigir credenciais, branches desprotegidas, releases
sem identidade ou dependências não fixadas cria conformidade aparente.

## Membros, financiamento e participação

Membros corporativos ajudam a financiar a estrutura, trazer especialistas e
apoiar iniciativas. Entretanto, financiamento e autoridade técnica são
dimensões diferentes. A OpenSSF declara que decisões de projeto ficam com seus
mantenedores e que participação em working groups não exige associação paga.

Uma organização pode apoiar financeiramente a fundação, contribuir com
engenheiros e ainda precisar aceitar decisões que não coincidem com seus
interesses comerciais. Essa separação é parte do valor de uma fundação
colaborativa, mas deve ser conferida na governança de cada iniciativa.

## Limitações e riscos institucionais

Uma fundação depende de pessoas, financiamento, infraestrutura e participação.
Working groups podem perder atividade, projetos podem ser arquivados, e uma
ferramenta pode deixar de acompanhar novas ameaças. Além disso, padrões e
baselines podem ficar atrás de mudanças legais, de linguagem ou de plataforma.

O consumidor deve acompanhar releases, advisories e o estado dos projetos. Não
é suficiente implementar uma versão antiga de uma recomendação e considerar a
cadeia protegida indefinidamente.

Também é preciso evitar concentração excessiva. Se uma única empresa controla
os mantenedores, o builder, o registry e os mecanismos de verificação, a
existência de uma fundação não elimina o risco de dependência institucional.

## Relação com CNCF e Linux Foundation

A [Linux Foundation](linux-foundation.md) fornece a estrutura institucional
mais ampla. A [CNCF](cncf.md) concentra-se no ecossistema cloud native. A
OpenSSF concentra-se na segurança do software aberto e da supply chain.

Os domínios se sobrepõem. Um projeto CNCF pode usar SLSA, Sigstore, Scorecard,
SBOM e práticas OpenSSF. Isso não significa que toda ferramenta CNCF seja
automaticamente aprovada pela OpenSSF, nem que todo controle OpenSSF seja
obrigatório para cada projeto. A integração precisa ser verificada no projeto
concreto e no ambiente que consome o artefato.

## Relações

- [Fundações de software aberto](index.md) compara as entidades.
- [Linux Foundation](linux-foundation.md) explica a estrutura institucional.
- [CNCF](cncf.md) explica o ecossistema cloud native.
- [SLSA](../../seguranca/supply-chain/slsa.md) trata de proveniência e níveis de build.
- [OpenSSF Scorecard](../../seguranca/supply-chain/openssf-scorecard.md) trata de sinais de segurança.
- [OSS-Fuzz](../../seguranca/appsec/fuzzing/oss-fuzz.md) trata de fuzzing contínuo.

## Fontes primárias

- [OpenSSF, about](https://openssf.org/about/)
- [OpenSSF, working groups](https://openssf.org/community/openssf-working-groups/)
- [OpenSSF, getting started](https://openssf.org/getinvolved/)
- [OpenSSF projects](https://openssf.org/projects/)
- [OpenSSF charter](https://github.com/openssf/community/blob/main/CHARTER.md)
- [OpenSSF membership](https://openssf.org/membership-hub/)
