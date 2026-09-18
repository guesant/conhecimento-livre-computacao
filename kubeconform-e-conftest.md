# kubeconform e conftest

Antes de perguntar se um manifesto Kubernetes é seguro ou segue a política da organização, existe uma pergunta mais básica: ele está sequer bem formado, com os campos certos nos tipos certos? kubeconform e conftest cobrem duas etapas sequenciais dessa validação declarativa, feita antes de qualquer aplicação real contra um cluster, cada uma respondendo a uma pergunta diferente.

## kubeconform: validação de schema

Um manifesto YAML sintaticamente válido ainda pode declarar um campo que não existe naquele tipo de recurso, ou atribuir um tipo errado a um campo que existe (uma string onde se espera um número, por exemplo); o parser YAML não detecta esse tipo de erro, porque do ponto de vista dele o documento está perfeitamente formado, só não corresponde ao schema que a API do Kubernetes exige para aquele recurso específico. `kubeconform` valida um manifesto contra o schema OpenAPI publicado pelo próprio Kubernetes, pego por versão exata, o que faz o comportamento da validação acompanhar a versão real do cluster de destino em vez de assumir um schema genérico desatualizado. Recursos customizados via CRD não têm schema embutido no Kubernetes central, cada operator publica o seu próprio; um catálogo de schemas de CRD mantido pela comunidade (mencionado em [Scanning de vulnerabilidade](vulnerability-scanning.md)) estende essa mesma validação a esses tipos, sem o que um erro de digitação num campo de CRD só seria descoberto na hora de aplicar de verdade contra um cluster real, tarde demais para pegar numa etapa de CI antes do deploy.

## conftest: política declarativa contra dado estruturado, fora do cluster

Um manifesto pode ser perfeitamente válido segundo seu schema e ainda violar uma regra própria da organização, como "todo `Deployment` precisa declarar `resources.requests`" ou "nenhum namespace de produção pode montar o socket do Docker"; isso não é um erro de schema, é uma regra de negócio que o schema do Kubernetes não teria como conhecer. `conftest`, construído sobre o mesmo motor de política do Open Policy Agent já descrito em [Policy enforcement e Kubescape](policy-enforcement-e-kubescape.md), testa dado estruturado (não só manifesto Kubernetes, também Terraform, Dockerfile e outros formatos que o motor consiga interpretar) contra políticas escritas em Rego, a mesma linguagem de política do OPA. A diferença central frente ao Pod Security Admission ou a um Kyverno, que atuam no momento da admissão dentro do cluster, é o momento em que a verificação acontece: `conftest` roda fora do cluster, tipicamente na CI, contra manifestos já renderizados mas ainda não aplicados, pegando uma violação de política antes mesmo de o manifesto chegar perto de um cluster real, em vez de rejeitá-lo no momento da aplicação.

## A ordem importa: schema antes de política

Faz sentido rodar `kubeconform` antes de `conftest` (ou de qualquer verificador de política): um manifesto malformado, com um campo inexistente ou um tipo errado, não deveria nem chegar à etapa de avaliar se ele segue a política da organização, porque a pergunta "ele está bem formado" é logicamente anterior e mais barata de responder do que "ele segue a regra X". Inverter a ordem não quebra nada tecnicamente, mas desperdiça o processamento de uma política complexa contra um manifesto que já falharia por um motivo mais básico e mais barato de detectar.

## Continue por aqui

[Policy enforcement e Kubescape](policy-enforcement-e-kubescape.md) cobre o OPA/Gatekeeper e o Kyverno, que aplicam o mesmo tipo de política, mas dentro do cluster no momento da admissão, em vez de fora dele na CI. [Scanning de vulnerabilidade](vulnerability-scanning.md) cita o catálogo de schemas de CRD que estende a validação do kubeconform a recursos customizados.
