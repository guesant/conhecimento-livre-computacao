# Cloud Native Computing Foundation

A Cloud Native Computing Foundation, ou CNCF, é uma fundação colaborativa da
Linux Foundation dedicada ao ecossistema cloud native. Ela hospeda projetos,
organiza comunidades e cria mecanismos para que tecnologias abertas de
containers, orquestração, observabilidade, redes, armazenamento, segurança e
entrega possam evoluir com participação de múltiplas organizações.

A missão declarada da CNCF é tornar a computação cloud native ubíqua. Na
prática, ela trabalha menos como uma empresa que vende uma plataforma única e
mais como uma estrutura de projetos, comunidades, eventos, certificações e
programas de adoção.

## O que significa cloud native

Cloud native descreve uma forma de construir e operar aplicações escaláveis em
ambientes públicos, privados e híbridos. Containers, service meshes,
microservices, infraestrutura imutável e APIs declarativas são exemplos de
técnicas que podem fazer parte dessa abordagem.

O termo não significa automaticamente Kubernetes, microservices ou uma nuvem
pública. Uma aplicação pode usar Kubernetes sem ser bem projetada para
ambientes dinâmicos, e uma aplicação monolítica pode usar princípios cloud
native em uma escala apropriada. A classificação deve considerar o modelo de
operação, automação, observabilidade, resiliência e ciclo de entrega.

## O papel da CNCF

A CNCF cria um ambiente no qual projetos independentes podem:

- manter repositórios, canais e infraestrutura sob uma estrutura neutra;
- obter orientação sobre governança, segurança e maturidade;
- participar de um ecossistema comum de usuários, fornecedores e contribuidores;
- receber apoio para eventos, documentação, release engineering e comunidade;
- demonstrar evolução por um ciclo de maturidade público;
- oferecer certificações e programas de conformidade quando aplicável.

Ela não escolhe automaticamente uma ferramenta vencedora para cada problema.
Projetos diferentes podem disputar a mesma categoria, ter trade-offs
distintos ou ser adequados a ambientes completamente diferentes.

## Portfólio

O portfólio inclui projetos de responsabilidades diferentes. Alguns exemplos
conhecidos são:

| Categoria | Exemplos |
| --- | --- |
| Orquestração e scheduling | Kubernetes, KubeVirt e projetos de workload |
| Observabilidade | Prometheus, OpenTelemetry, Fluentd, Fluent Bit, Jaeger e Grafana Tempo |
| Proxy e rede | Envoy, Cilium, CoreDNS, Gateway API e projetos de service mesh |
| Armazenamento | Rook, Longhorn e interfaces ou operadores de storage |
| Segurança | Falco, SPIFFE, SPIRE, Kyverno, Tetragon e projetos de policy |
| Entrega e automação | Argo, Flux, Helm, Tekton e iniciativas de CI/CD |
| RPC e comunicação | gRPC, CloudEvents e componentes para sistemas distribuídos |
| Bancos e dados | Vitess, TiDB, Strimzi e outros projetos de dados cloud native |

O catálogo e o status dos projetos mudam. A presença na paisagem CNCF não
equivale a hospedagem, recomendação ou garantia de produção. Confirme no
catálogo oficial se o projeto é CNCF, qual estágio possui e qual organização
mantém o código.

## Ciclo de vida dos projetos

A CNCF usa um ciclo de vida com estágios que comunicam expectativas diferentes.
O estágio não é uma nota universal de qualidade e não substitui a avaliação do
consumidor.

### Sandbox

Sandbox é a porta de entrada para projetos experimentais ou inovadores. APIs,
arquitetura e processo de release podem mudar bastante. O projeto pode ser
usado em produção por alguns adotantes, mas o estágio não promete estabilidade
ou suporte amplo.

O valor principal é permitir que uma comunidade explore uma ideia dentro de uma
estrutura que oferece orientação e critérios para evoluir. Um consumidor deve
aceitar mudanças incompatíveis e a possibilidade de o projeto não chegar a um
estágio posterior.

### Incubating

Um projeto incubating já demonstrou conceito e começa a mostrar adoção,
estabilidade e maturidade maiores. Mudanças incompatíveis tendem a ser menos
frequentes, e o Technical Oversight Committee passa a avaliar mais ativamente
adoção, governança, segurança, robustez e saúde da comunidade.

Incubating não significa que toda API esteja estável ou que qualquer cenário de
produção seja suportado. A decisão deve considerar a capacidade do time de
acompanhar releases e operar o projeto.

### Graduated

Graduated representa um nível alto de maturidade, adoção e governança. O projeto
deve demonstrar práticas consistentes, segurança, comunidade ativa e capacidade
de atender expectativas de produção.

Graduated é um sinal positivo, mas não um selo de adequação para qualquer caso.
Ele não elimina incidentes, vulnerabilidades, mudanças de mantenedores ou
custos de operação. O consumidor ainda precisa avaliar documentação, licenças,
integrações, desempenho, disponibilidade e suporte.

### Archived

Archived identifica projeto inativo ou que não é mais recomendado pelo processo
da CNCF. O código pode continuar disponível e ainda ser útil para estudo ou
migração, mas uma adoção nova precisa tratar o projeto como legado e investigar
alternativas e riscos de manutenção.

## Governança

O Technical Oversight Committee, ou TOC, é o principal corpo de decisão técnica
da CNCF. Ele avalia propostas, estágios, saúde e critérios dos projetos. O
Governing Board trata de aspectos institucionais, financeiros e estratégicos,
enquanto os mantenedores continuam responsáveis pelo trabalho técnico cotidiano
de cada projeto.

Essa separação é importante. A CNCF pode fornecer regras comuns, infraestrutura
e avaliação de maturidade, mas não transforma o TOC no mantenedor de cada
repositório. Cada projeto pode possuir um steering committee, maintainers,
working groups, SIGs e regras próprias.

A análise de um projeto deve identificar:

- quem pode fazer merge e release;
- como um contributor se torna reviewer ou maintainer;
- como decisões controversas são resolvidas;
- como conflitos de interesse e concentração empresarial são tratados;
- como vulnerabilidades são reportadas e corrigidas;
- como os ativos e a marca são administrados;
- que serviços a CNCF fornece e quais o projeto precisa operar sozinho.

## Due diligence

Ao mudar de estágio, o projeto passa por uma análise de critérios. A due
diligence considera repositórios, releases, métricas, segurança, governança,
adoção, processos e outras evidências. O objetivo é verificar se o resultado
real corresponde ao estágio pretendido, não apenas se o projeto possui uma
documentação bem escrita.

Critérios relevantes incluem comunidade saudável, contribuidores de mais de uma
organização, prática de releases, segurança, documentação, uso em produção e
governança transparente. Um projeto pequeno pode ter uma ideia excelente, mas
demonstrar pouca evidência de maturidade para um estágio mais alto.

## Conformance e certificação

A CNCF mantém programas de conformidade e certificação para alguns ecossistemas
e perfis profissionais. É importante separar três coisas:

| Conceito | O que significa |
| --- | --- |
| Projeto hospedado | O projeto participa da estrutura da fundação |
| Conformance | Um produto atende a critérios técnicos definidos por um programa |
| Certificação profissional | Uma pessoa demonstrou conhecimentos ou habilidades numa prova |

Um produto certificado pode ter interoperabilidade melhor em um escopo
específico, mas isso não garante performance, segurança completa ou qualidade de
implementação fora do escopo testado. Uma certificação profissional não prova
que o candidato já operou todos os componentes em produção.

## Eventos e ecossistema

KubeCon + CloudNativeCon, encontros regionais, webinars, grupos de usuários e
programas de treinamento criam espaços para compartilhar experiências,
discutir projetos e contratar profissionais. Eventos também funcionam como
lugares de negociação e marketing, portanto uma palestra, um estande ou um caso
de sucesso não deve ser tratado como evidência independente de qualidade.

O landscape ajuda a descobrir categorias e projetos. Ele não substitui a
documentação canônica, benchmarks reproduzíveis, análise de licença ou uma
prova de conceito no ambiente real.

## Como participar

Uma pessoa pode contribuir sem ser membro corporativo. Caminhos comuns incluem
documentação, triagem, testes, tradução, suporte comunitário, código,
segurança, organização de eventos e participação nos canais públicos.

Empresas podem apoiar por associação, patrocínio, contratação de contribuidores,
doação de projetos, participação em grupos de usuários e adoção responsável.
O pagamento de uma associação não deve ser confundido com autoridade para
alterar a direção técnica de um projeto.

## Como avaliar uma tecnologia CNCF

Use o status como um filtro inicial, não como a decisão final:

1. identifique a responsabilidade exata da ferramenta;
2. compare-a com alternativas que resolvem o mesmo problema;
3. leia a política de compatibilidade e o ciclo de release;
4. verifique vulnerabilidades, SBOM, assinatura e proveniência;
5. teste backup, recuperação, upgrades e observabilidade;
6. calcule custo de operação, conhecimento necessário e lock-in;
7. confirme se o estágio e os serviços disponíveis ainda são atuais.

## Relação com a Linux Foundation e a OpenSSF

A CNCF é parte da Linux Foundation, mas possui uma missão cloud native, um TOC
e um ciclo de maturidade próprios. A [OpenSSF](openssf.md) tem foco em segurança
de software aberto e cadeia de fornecimento. As comunidades podem colaborar,
mas um projeto CNCF não é automaticamente OpenSSF e um controle OpenSSF não é
automaticamente exigência para todos os projetos CNCF.

## Relações

- [Fundações de software aberto](index.md) compara CNCF, OpenSSF e Linux Foundation.
- [Linux Foundation](linux-foundation.md) explica a estrutura institucional mais ampla.
- [OpenSSF](openssf.md) trata da segurança do software aberto.
- [Kubernetes](../../kubernetes/index.md) é um projeto central do ecossistema cloud native.

## Fontes primárias

- [CNCF, who we are](https://www.cncf.io/about/who-we-are/)
- [CNCF projects](https://www.cncf.io/projects/)
- [Project lifecycle and process](https://contribute.cncf.io/projects/lifecycle/)
- [Technical Oversight Committee](https://contribute.cncf.io/community/toc/)
- [TOC due diligence](https://contribute.cncf.io/community/toc/operations/dd-toc-guide/)
- [CNCF charter](https://github.com/cncf/foundation/blob/main/charter.md)
- [CNCF landscape](https://landscape.cncf.io/)
