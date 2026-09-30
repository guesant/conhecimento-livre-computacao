# SLSA

SLSA, pronunciado "salsa", significa Supply-chain Levels for Software
Artifacts. É uma especificação e um conjunto de práticas para descrever e
melhorar progressivamente a segurança da cadeia de software. O projeto é uma
colaboração orientada por consenso da indústria e faz parte do ecossistema da
OpenSSF.

SLSA não é um scanner, uma ferramenta única, um formato de SBOM ou uma
certificação automática. Ele fornece vocabulário, requisitos, níveis de
garantia e formatos de atestação que permitem responder se um artefato foi
produzido a partir da fonte esperada, por qual plataforma e sob quais
controles.

A especificação atual é a [SLSA v1.2](https://slsa.dev/spec/v1.2/). A versão
1.0 continua sendo uma referência histórica importante, mas a documentação
oficial a marca como retirada. Quando uma política mencionar um nível, uma
atestação ou um predicate, ela deve declarar a versão da especificação que está
sendo aplicada.

## O problema da cadeia de software

O source revisado não é necessariamente o mesmo código que foi compilado, e o
artefato publicado não é necessariamente o mesmo arquivo que o builder
produziu. Entre esses pontos existem workflows, dependências, imagens base,
compiladores, workers, caches, registries e credenciais com capacidade de
publicação.

Um scanner pode analisar o source correto e ainda assim não analisar o binário
que será executado. Um checksum pode provar que o arquivo recebido não mudou
desde a publicação, mas não prova de onde ele veio. Uma assinatura pode provar
que uma identidade assinou uma mensagem, mas não prova que essa identidade
usou a fonte correta.

SLSA trata a integridade da cadeia como uma propriedade verificável. O objetivo
é tornar difícil ou detectável a substituição do source, a alteração do build,
a publicação de um artefato que não corresponde ao build ou a distribuição de
um artefato diferente daquele que foi verificado.

## O que SLSA protege

O foco primário é a integridade da cadeia. Disponibilidade também é relevante,
mas não é resolvida por um nível de build isoladamente.

### Integridade do source

Uma revisão precisa representar a intenção do produtor, seguir o processo de
mudança esperado e não ser modificada silenciosamente depois de aceita. Isso
envolve histórico, identidade, proteção de referências, controles técnicos e,
em níveis mais altos, revisão por duas pessoas.

### Integridade do build

O pacote precisa ser produzido a partir das fontes e dependências corretas,
seguindo o processo esperado. A proveniência precisa descrever o resultado e
ser gerada por uma parte confiável do build platform, não por uma etapa que o
próprio tenant possa alterar livremente.

### Integridade da distribuição

O artefato que chega ao registry, ao mirror ou ao consumidor precisa continuar
sendo identificável pelo digest e acompanhado das evidências esperadas. Um
artefato que aparece em um registry, mas não tem a proveniência correspondente
ou não foi produzido pelo builder autorizado deve ser rejeitado ou colocado em
quarentena.

### O que não está coberto automaticamente

SLSA não determina que o produtor seja honesto, não avalia sozinho a qualidade
do código e não prova que uma dependência esteja livre de vulnerabilidades. A
proveniência de uma aplicação também não confere automaticamente o mesmo nível
às dependências transitivas. Cada dependência pode ser verificada
recursivamente, mas a decisão sobre o conjunto continua sendo uma política do
consumidor ou do ecossistema.

## Modelo mental da supply chain

SLSA modela a cadeia como um grafo acíclico dirigido de fontes, builds,
dependências e pacotes. A cadeia de um artefato combina o source e o processo
que o produziu com as cadeias dos artefatos que foram usados como dependência.

| Termo | Significado |
| --- | --- |
| Artifact | Blob imutável de dados, como um commit, binário, firmware ou imagem |
| Source | Artefato diretamente criado ou revisado por pessoas |
| Build | Processo que transforma entradas em uma ou mais saídas |
| Package | Artefato destinado à distribuição, mesmo quando o build foi trivial |
| Dependency | Pacote usado como entrada de um build, mas que não é o source direto |
| Distribution | Canal que publica ou resolve nomes de pacote para artefatos |
| Attestation | Declaração autenticada sobre um artefato ou processo |
| Provenance | Attestation que descreve origem, processo, entradas e execução |

Uma tag, um nome de pacote ou uma branch são referências convenientes. O
artefato que será verificado deve ser identificado por um digest ou por outro
identificador imutável. A política precisa distinguir o nome mutável do pacote
do artefato concreto que recebeu a atestação.

## Participantes

Uma mesma organização pode ocupar mais de um papel, mas as responsabilidades
devem ser separadas conceitualmente.

| Papel | Responsabilidade |
| --- | --- |
| Producer | Cria e distribui software, definindo expectativas sobre a origem |
| Build platform | Executa builds, isola ambientes e produz proveniência |
| Infrastructure provider | Opera registry, builder, sistema de source ou outro serviço |
| Verifier | Compara proveniência e artefato com uma política de confiança |
| Consumer | Instala, promove ou executa o artefato |

Um registry pode ser produtor da própria distribuição, mas não deve ser
tratado automaticamente como um builder confiável. O consumidor precisa saber
qual identidade produziu o artefato e qual identidade publica a evidência.

## Tracks e níveis

SLSA é organizado em tracks. Cada track trata uma parte da cadeia e possui
níveis próprios. Não existe um único número que descreva corretamente toda a
segurança de um produto.

### Build Track

O Build Track descreve a confiança e a integridade da proveniência do pacote.
Os níveis atuais são:

| Nível | Requisito resumido | Ameaça principal tratada |
| --- | --- | --- |
| Build L0 | Nenhum requisito SLSA | Ausência de garantia declarada |
| Build L1 | Proveniência existe | Erros, falta de rastreabilidade e documentação |
| Build L2 | Builder hospedado gera e autentica a proveniência | Alteração depois do build |
| Build L3 | Builder hospedado é endurecido e isola builds | Alteração durante o build |

#### Build L0

L0 representa um processo sem garantia SLSA. É adequado para builds locais de
desenvolvimento ou testes quando o resultado não será tratado como release. Um
build L0 não deve ser confundido com um artefato inseguro em todos os sentidos;
ele apenas não faz uma afirmação SLSA verificável.

#### Build L1

L1 exige que a plataforma gere proveniência que identifique o pacote por
digest, descreva como ele foi produzido e seja distribuída ao consumidor. A
proveniência pode ser incompleta ou não assinada, portanto é útil para evitar
erros, investigar releases e formar expectativas, mas é trivial de forjar para
um adversário que possa alterar a execução ou a declaração.

L1 já traz um benefício operacional relevante. O time consegue localizar a
revisão, o processo e os parâmetros que originaram um artefato, comparar
releases e reconstruir o caminho de uma falha.

#### Build L2

L2 adiciona um build platform hospedado e a proveniência autenticada pelo
próprio platform. O consumidor precisa validar essa autenticidade. A ideia é
tirar a decisão de confiança de um arquivo que o usuário do build poderia
editar depois de produzir o artefato.

L2 reduz o risco de adulteração entre build e publicação. Ele não significa que
o ambiente de build esteja fortemente isolado de um tenant malicioso; essa
garantia é tratada por L3.

#### Build L3

L3 exige um build platform endurecido. Os builds precisam ser isolados para
evitar que uma execução influencie outra, inclusive dentro do mesmo projeto.
Segredos usados para autenticar a proveniência não podem ficar disponíveis às
etapas definidas pelo usuário.

L3 aumenta o custo de um ataque que tenta modificar o resultado durante a
execução, comprometer credenciais de outro tenant ou forjar a evidência. Ele
não torna o código benigno e não elimina a necessidade de proteger o controle
de acesso ao source, ao registry e ao processo de promoção.

### Source Track

O Source Track trata a confiança na forma como uma revisão de source foi criada
e mantida. Ele não exige que o sistema use Git. A revisão precisa ser
identificável, o histórico precisa ser preservado conforme o nível e os
controles precisam gerar evidência consumível.

| Nível | Requisito resumido | Resultado esperado |
| --- | --- | --- |
| Source L0 | Nenhuma garantia SLSA | Nenhum processo de source afirmado |
| Source L1 | Source control system | Revisões discretas e identificáveis |
| Source L2 | Histórico preservado e source provenance | Evidência contemporânea das mudanças |
| Source L3 | Controles técnicos organizacionais | Evidência dos controles aplicados a referências protegidas |
| Source L4 | Revisão por duas pessoas | Redução de mudanças unilaterais em branches protegidas |

Source L2 é mais do que ter um repositório. O sistema deve conservar o
histórico da referência, atribuir atores autenticados e emitir evidência sobre
a revisão. Em um sistema Git, proibir force push em uma branch protegida é um
exemplo de controle que preserva continuidade histórica.

Source L3 permite demonstrar que controles técnicos específicos foram aplicados
a referências nomeadas. Source L4 exige que alterações em referências protegidas
sejam aprovadas por pelo menos duas pessoas confiáveis, ressalvadas exceções
explicitamente autorizadas para robôs confiáveis.

### Tracks não são uma média

Um projeto pode possuir Build L3 e Source L1, ou Source L4 e um builder L1.
Isso não deve ser resumido em "SLSA 3" sem informar a track. A matriz precisa
mostrar quais propriedades foram realmente verificadas e quais ainda não foram
adotadas.

## Build platform e fronteira de confiança

SLSA considera build platform a união transitiva de hardware, software,
serviços, pessoas e organizações capazes de influenciar a construção. Não é
apenas o container do job. Inclui o control plane, schedulers, cache, registry,
identidades, runners, plugins, imagens base e mecanismos que montam os
segredos.

O modelo separa alguns conceitos:

- tenant: quem define etapas e parâmetros do build;
- control plane: componente confiável que inicializa a execução e produz a
  proveniência;
- build environment: conjunto de máquinas, containers ou VMs onde as etapas
  executam;
- build steps: comandos definidos pelo tenant;
- build cache: artefatos intermediários indexados por entradas explícitas;
- builder dependency: software ou artefato necessário para o próprio builder;
- output: artefato produzido e identificado pelo subject.

Essa distinção evita chamar qualquer container de builder confiável. Um job
privilegiado pode executar o compilador, mas se o mesmo job puder editar a
proveniência assinada, a evidência não tem a garantia correspondente a L2 ou
L3.

## Proveniência no formato SLSA

O formato recomendado de build provenance usa uma attestation in-toto. A
declaração identifica o output no campo `subject`, informa o tipo do predicate e
separa a definição do build dos detalhes da execução.

Os principais campos são:

| Campo | Função |
| --- | --- |
| `subject` | Nome e digest do artefato produzido |
| `predicateType` | URI que identifica o schema da proveniência |
| `buildDefinition` | Entradas e contrato para iniciar o build |
| `buildType` | URI que define como interpretar parâmetros e dependências |
| `externalParameters` | Valores controlados por quem invocou o build |
| `internalParameters` | Valores derivados ou controlados pela plataforma |
| `resolvedDependencies` | Artefatos externos resolvidos, preferencialmente com digest |
| `runDetails.builder.id` | Identidade do build platform |
| `builderDependencies` | Componentes necessários para o builder |
| `metadata` | ID da invocação e horários da execução |
| `byproducts` | Saídas auxiliares relevantes para a execução |

Um exemplo simplificado de predicate é:

```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "registry.example/app",
      "digest": {
        "sha256": "<digest-do-manifesto>"
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://example.com/build-types/container/v1",
      "externalParameters": {
        "repository": "https://github.com/example/app",
        "revision": "<commit-sha>"
      },
      "resolvedDependencies": [
        {
          "uri": "oci://registry.example/base",
          "digest": {
            "sha256": "<digest-da-imagem-base>"
          }
        }
      ]
    },
    "runDetails": {
      "builder": {
        "id": "https://ci.example/builders/production"
      },
      "metadata": {
        "invocationId": "<id-da-execucao>"
      }
    }
  }
}
```

O exemplo não é uma política completa nem substitui o schema. `buildType` deve
apontar para uma especificação compreensível por humanos e verificadores. O
`subject` deve apontar para o digest do resultado que será distribuído, não
para uma tag que pode mudar.

### Parâmetros e dependências

Um parâmetro externo deve conter o valor realmente fornecido à interface do
build. Metadados derivados desse valor, especialmente o digest de um artefato,
devem aparecer em `resolvedDependencies` quando possível. Isso permite que um
verificador compare a referência humana com o objeto imutável que foi usado.

Quando a configuração do build é transformada no cliente antes de ser enviada
ao servidor, o control plane pode não conseguir provar a origem daquela
configuração. A abordagem preferível é fazer a plataforma ler a configuração
diretamente do source versionado. Se a transformação for inevitável, ela deve
ser tratada como uma etapa própria e receber evidência independente.

`resolvedDependencies` existe para permitir análise recursiva. A completude
depende do nível e da plataforma, mas cada dependência que pode alterar o
resultado deve ser fixada ou registrada. Uma URI sem digest é uma pista de
origem, não uma identificação imutável suficiente.

### Autenticidade, completude e precisão

SLSA separa propriedades que às vezes são confundidas:

- completude: quanto das entradas e do processo foi descrito;
- autenticidade: se a declaração pode ser vinculada ao build platform;
- precisão: se a declaração foi gerada fora do controle do tenant e resiste à
  falsificação durante o build.

L1 exige a existência da proveniência, sem exigir autenticidade ou precisão. L2
exige autenticidade. L3 exige que a geração seja fortemente resistente à
forja pelo tenant. O nível não deve ser anunciado apenas porque um JSON com o
nome `provenance` foi anexado ao release.

## Atestação e assinatura

Uma attestation é uma declaração autenticada, normalmente estruturada em uma
mensagem in-toto. Proveniência é um tipo de afirmação; outras atestações podem
descrever SBOM, teste, scan ou decisão de política.

A assinatura protege a integridade da declaração e vincula o documento a uma
identidade. Ela não diz se a identidade é adequada, se o builder foi seguro ou
se o conteúdo atestado é bom. Essas decisões são feitas pela política de
verificação.

Em L2, a plataforma deve gerar e assinar a proveniência, e o consumidor precisa
validar a autenticidade. Em L3, o material secreto usado na autenticação deve
ficar fora das etapas controladas pelo tenant e sob gestão adequada de
segredos.

## Verificação

SLSA só produz valor quando alguém inspeciona a proveniência e toma uma decisão.
Verificar significa comparar o artefato e a attestation com expectativas
definidas para aquele nome de pacote, repositório, ambiente ou sistema.

Uma verificação deve, em geral:

1. localizar o artefato pelo digest;
2. obter a proveniência correspondente;
3. identificar o builder e o nível esperado para a track;
4. validar a assinatura ou outro mecanismo de autenticidade;
5. conferir `buildType` e `externalParameters`;
6. conferir o digest do `subject` contra o artefato recebido;
7. conferir source, branch, tag, workflow e dependências esperados;
8. rejeitar parâmetros externos desconhecidos, salvo exceções documentadas;
9. registrar o resultado e impedir promoção quando a política falhar.

As expectativas podem ser definidas pelo produtor, pelo ecossistema do pacote,
pelo source ou por uma política de confiança inicial. Trust on first use pode
ser útil para começar, mas mudanças posteriores precisam gerar alerta e passar
por uma forma de aprovação. A expectativa está ligada ao nome do pacote; a
proveniência está ligada ao artefato concreto.

### Onde verificar

Há três pontos complementares:

| Ponto | Vantagem | Risco se for o único controle |
| --- | --- | --- |
| Upload no registry | Rejeita cedo um artefato incorreto para todos os consumidores | O registry pode não conhecer a política de cada consumidor |
| Download ou instalação | O consumidor aplica sua própria política | Cada consumidor pode configurar regras diferentes ou não verificar |
| Monitor contínuo | Detecta mudanças e desvios depois da publicação | Detecção sem bloqueio ou resposta não reduz o impacto sozinha |

Defesa em profundidade é preferível. Um registry pode verificar o mínimo
comum, enquanto o pipeline de deploy verifica requisitos específicos do
ambiente e o runtime recusa imagens sem evidência válida.

## Verification Summary Attestation

Uma Verification Summary Attestation, ou VSA, resume o resultado de uma
verificação. Ela permite que um consumidor confie em um verificador delegado
sem precisar reavaliar toda a proveniência do artefato e de cada dependência.

Uma VSA normalmente registra:

- o artefato sujeito e seu digest;
- a identidade do verifier;
- o recurso verificado;
- a política e seu digest;
- as atestações usadas como entrada;
- `verificationResult`, como `PASSED` ou `FAILED`;
- os níveis SLSA verificados;
- a contagem de dependências por nível;
- a versão da especificação.

Esse resumo é uma delegação de confiança, não um atalho para ignorar a
política. O consumidor precisa confiar no verifier, conferir o recurso e
verificar se o resultado é `PASSED` e se os níveis atendem ao mínimo esperado.
Uma VSA pode ser útil quando detalhes internos do pipeline não podem ser
publicados, mas não deve esconder informações necessárias para investigação
de incidentes.

## Ameaças e limites

As ameaças aparecem em pontos diferentes da cadeia. SLSA trata algumas com
mais força conforme o nível e deixa outras para controles complementares.

| Ponto do ataque | Exemplo | Resposta ou limite de SLSA |
| --- | --- | --- |
| Produtor | O próprio produtor distribui software malicioso | Não resolve intenção maliciosa do produtor |
| Revisão | Mudança maliciosa é aprovada por uma única pessoa | Source L4 exige revisão por duas pessoas |
| Source control | Histórico ou branch protegida são alterados | Source Track preserva continuidade e controles |
| Parâmetros | Build usa source diferente do anunciado | Proveniência registra parâmetros e materiais |
| Build platform | Worker injeta código durante a construção | Build L3 endurece e isola a plataforma |
| Publicação | Credencial de upload publica binário diferente | Digest e proveniência permitem rejeição |
| Distribuição | Mirror entrega outro artefato | Verificação no consumo confere digest e origem |
| Seleção | Typosquatting cria pacote com nome parecido | Nome do pacote e política do ecossistema continuam necessários |
| Uso | Aplicação possui credencial padrão ou falha de configuração | Fora do escopo de SLSA |
| Dependência | Dependência transitiva é comprometida | Verificação precisa ser recursiva |

Um nível SLSA não substitui revisão de código, SAST, DAST, SCA, secret
scanning, SBOM, assinatura, controle de acesso, backup, disponibilidade ou
resposta a incidentes. Ele protege uma propriedade diferente: a confiança no
caminho entre o source, o build e o artefato consumido.

## SLSA e builds reproduzíveis

SLSA não exige que todo build seja reproduzível. Ainda assim, builds
reproduzíveis podem aumentar a confiança, validar a saída de um builder e
permitir que uma segunda parte confira o resultado de forma independente.

Proveniência registra o que aconteceu. Reprodutibilidade permite repetir o que
aconteceu. Uma declaração pode ser autêntica e apontar para um build não
reproduzível; por outro lado, um build pode ser reproduzível sem possuir
proveniência assinada. A combinação de ambos é mais forte do que qualquer um
isoladamente.

Consulte [builds reproduzíveis](reproducible-builds.md) para timestamps,
dependências, ambientes herméticos, ordem de arquivos, toolchains e
comparação independente.

## Casos de uso

### Software de primeira parte

Uma organização pode exigir que produção aceite somente imagens produzidas por
um workflow específico, a partir de uma branch protegida, com uma identidade de
builder conhecida e com proveniência válida. Isso reduz o risco de uma conta
comprometida publicar manualmente uma imagem que não passou pelo CI.

### Open source

Um registry ou package manager pode vincular o nome do pacote ao repositório
canônico e rejeitar uploads sem proveniência compatível. O consumidor passa a
confiar em um número menor de builders, em vez de confiar individualmente em
cada conta que pode publicar no ecossistema.

### Software de fornecedor

O consumidor pode pedir proveniência e exigir um nível mínimo como condição de
contrato. Quando o fornecedor não revela todo o pipeline, uma VSA assinada por
um verifier confiável pode comunicar o resultado sem expor detalhes internos.

### Promoção GitOps

Um controlador de promoção pode verificar o digest e a proveniência antes de
alterar o manifesto desejado. A tag pode continuar existindo para descoberta
humana, mas a promoção deve ser feita pelo digest exato que foi verificado.

### Dependências transitivas

Um produto pode exigir que dependências críticas possuam proveniência própria e
um nível mínimo. A análise percorre `resolvedDependencies`, associa cada digest
à attestation correspondente e falha quando a cadeia não pode ser ligada a
uma origem ou builder confiável.

## Como adotar

SLSA deve ser implantado como uma sequência de capacidades, e não como um
projeto que bloqueia toda entrega até alcançar L3.

### Primeiro passo: inventário e identidade

Liste os artefatos, os registries, os builders, as fontes, as dependências e os
pontos de promoção. Defina uma identidade imutável para cada artefato e um
conjunto mínimo de expectativas. Sem essa etapa, não há como saber o que uma
proveniência deveria afirmar.

### Segundo passo: gerar proveniência

Comece em Build L1 para que cada pacote possua digest, fonte, processo,
dependências relevantes e builder identificados. Distribua a declaração junto
do pacote ou por uma convenção do ecossistema.

### Terceiro passo: autenticar e verificar

Passe para Build L2 quando a plataforma puder gerar e autenticar a proveniência
fora do controle do job. Configure verificadores para conferir identidade,
assinatura, `buildType`, parâmetros, source e digest antes da publicação ou da
promoção.

### Quarto passo: endurecer a plataforma

Avalie isolamento entre jobs, acesso a caches, montagem de secrets, privilégios
dos workers, controle do control plane, atualização de imagens e logs. A meta
de Build L3 só é coerente quando a plataforma impede que etapas controladas
pelo tenant alterem a evidência ou influenciem outra execução.

### Quinto passo: proteger o source

Adote Source L1 ao versionar revisões identificáveis. Depois preserve o
histórico, gere source provenance, proteja referências nomeadas e exija revisão
de duas pessoas conforme o risco e o nível desejado.

### Exceções

Nem todo artefato precisa do mesmo nível. Ferramentas internas temporárias,
builds de desenvolvimento e releases públicas podem possuir políticas
diferentes. A exceção precisa declarar o motivo, o escopo, o prazo, o risco
aceito e quem autorizou. Não chame uma exceção de Build L3 nem use um nível
como selo geral para componentes que não foram verificados.

## Relações

- [Proveniência](provenance.md) detalha a declaração de origem e execução.
- [Builds reproduzíveis](reproducible-builds.md) trata da repetição determinística.
- [Atestação](attestation.md) explica o envelope de afirmações autenticadas.
- [Assinatura de artefatos](artifact-signing.md) trata de integridade e identidade.
- [SBOM](sbom.md) descreve os componentes presentes no artefato.
- [Supply chain](index.md) organiza os conceitos relacionados.

## Fontes primárias

- [SLSA v1.2](https://slsa.dev/spec/v1.2/)
- [About SLSA](https://slsa.dev/spec/v1.2/about)
- [Supply chain threats](https://slsa.dev/spec/v1.2/threats-overview)
- [Use cases](https://slsa.dev/spec/v1.2/use-cases)
- [Tracks](https://slsa.dev/spec/v1.2/tracks)
- [Build Track basics](https://slsa.dev/spec/v1.2/build-track-basics)
- [Build terminology](https://slsa.dev/spec/v1.2/terminology)
- [Build requirements](https://slsa.dev/spec/v1.2/build-requirements)
- [Build provenance](https://slsa.dev/spec/v1.2/build-provenance)
- [Distributing provenance](https://slsa.dev/spec/v1.2/distributing-provenance)
- [Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts)
- [Assessing build platforms](https://slsa.dev/spec/v1.2/assessing-build-platforms)
- [Source requirements](https://slsa.dev/spec/v1.2/source-requirements)
- [Verification Summary Attestation](https://slsa.dev/spec/v1.2/verification_summary)
