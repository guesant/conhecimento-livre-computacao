# Helm e charts

Helm é o gerenciador de pacotes mais usado do [Kubernetes](k3s.md): em vez de escrever e aplicar manifesto por manifesto (um Deployment, um Service, uma ConfigMap, cada um num arquivo YAML separado), Helm empacota um conjunto inteiro de manifestos relacionados, junto com os pontos de variação entre uma instalação e outra, num pacote único chamado chart.

Instalar uma aplicação complexa, com muitos recursos interdependentes, vira rodar um comando contra um chart, em vez de aplicar cada arquivo na ordem certa manualmente. O empacotamento também dá um contrato de configuração: o chart declara quais campos quem instala pode mexer, e tudo que não estiver ali é decisão de quem o escreveu.

Neste repositório o Helm é a unidade de embrulho quase em toda parte, inclusive para componentes que não vêm de fora, como o chart local `platform-network-policies`, que existe só para gerar as `CiliumNetworkPolicy` dos namespaces de plataforma.

## O que compõe um chart

Um chart é uma pasta com uma estrutura fixa. `Chart.yaml` guarda os metadados do pacote: nome, versão do próprio chart, versão da aplicação que ele empacota, e a lista de outros charts dos quais ele depende, se houver algum.

`values.yaml` guarda a configuração padrão: os valores que os templates vão usar quando ninguém sobrescreve nada, como o número de réplicas, a imagem de container e sua tag, ou se um recurso opcional deve existir. `templates/` guarda os arquivos de manifesto propriamente ditos, só que com marcadores no lugar dos valores que variam, preenchidos a partir do arquivo de values na hora de gerar o resultado final.

## A sintaxe de template

Os marcadores dentro de um arquivo em `templates/` usam chaves duplas, `{{ }}`, a mesma notação que a linguagem de template do Go (a linguagem em que o próprio Helm é escrito) usa para marcar onde um valor deve entrar.

`{{ .Values.replicas }}` lê o campo replicas do arquivo de values; `{{ .Release.Name }}` lê o nome da instalação em andamento, um dos vários objetos embutidos que o Helm expõe além dos valores do próprio chart.

Esses marcadores podem encadear funções com o operador de pipeline, na mesma lógica de um pipe de shell: `{{ .Values.nome | upper | quote }}` primeiro converte o valor para maiúsculas, depois o envolve em aspas, produzindo uma string YAML válida no lugar certo.

Um template não se limita a substituir valores, ele também decide o que entra no resultado. Um mesmo chart pode gerar três manifestos numa instalação e onze noutra, dependendo do que o arquivo de values daquela instalação ligou.

Diretivas de controle de fluxo, como `{{- if .Values.algoOpcional }}` para incluir um bloco só condicionalmente ou `{{- range .Values.lista }}` para repetir um bloco uma vez por item de uma lista, seguem a mesma sintaxe de chaves duplas; veja [gerar várias instâncias de um recurso com Helm](helm-templating-de-lista.md) para o segundo caso em profundidade, incluindo um risco real que aparece quando o próprio valor de um campo é, ele mesmo, escrito nessa mesma notação de chaves duplas por outra ferramenta.

## `helm template` contra `helm install`

`helm template` processa um chart localmente e imprime o resultado, o YAML já com todo marcador substituído, sem tocar em cluster nenhum: é equivalente a rodar só a etapa de geração de texto, útil para inspecionar o que seria aplicado antes de aplicar de verdade, ou para usar a saída com outra ferramenta que só entende manifesto puro.

`helm install`, em vez disso, gera esse mesmo resultado e o aplica diretamente contra o cluster, criando o que o Helm chama de release: uma instalação nomeada e versionada daquele chart, com os valores usados registrados dentro do próprio cluster, por padrão num segredo.

Cada `helm upgrade` subsequente cria uma nova revisão dessa release, e é esse registro que permite a um `helm rollback` voltar para uma revisão anterior sem reconstruir manualmente os valores que ela usava.

A diferença tem uma consequência que costuma pegar quem escreve template, e ela aparece sempre que o template tenta olhar para o cluster. A função `lookup`, que um template usaria para ler um recurso já existente no cluster, por exemplo para reaproveitar um segredo gerado numa instalação anterior em vez de gerar um novo, sempre volta vazia dentro de `helm template`, mesmo com um kubeconfig válido disponível, porque nessa etapa não existe cluster nenhum sendo consultado.

O resultado é um template que funciona ao instalar e falha ao ser validado, ou pior, que gera um segredo novo a cada renderização sem que ninguém perceba.

Vale a mesma ressalva para uma ferramenta que consome a saída de helm template, como o Argo CD ao renderizar um chart antes de aplicá-lo: um chart que depende de `lookup` não se comporta ali como se comportaria num `helm install` direto.

## Dependências entre charts

Um chart pode declarar dependência de outro chart, listado no Chart.yaml como um sub-chart: `helm dependency update` baixa cada dependência declarada, empacotada como um pacote comprimido, para dentro de uma pasta `charts/`, e grava a versão exata de cada uma num arquivo de lock, no mesmo espírito de um lock file de gerenciador de pacote de qualquer linguagem.

Isso separa decisões que parecem uma só: a versão do chart em si, o pacote e a estrutura de templates, e a versão da aplicação que ele instala, que podem evoluir em ritmos diferentes. Commitar ou não a pasta `charts/` é a decisão seguinte, e ela troca tamanho de repositório por independência de quem publica o chart.

Aqui os pacotes ficam versionados, como os do Traefik em `argocd/apps/platform/ingress/charts/`, de modo que uma sincronização não depende do repositório de origem estar no ar naquele momento.

## Vendorizar um chart de terceiro contra escrever um chart local

Existem formas comuns de trazer um chart para um projeto, e a diferença entre elas não é técnica, é sobre quem mantém o conteúdo. Uma é apontar para o chart de um projeto de terceiro, publicado num repositório Helm público, como dependência: o mantenedor do projeto original decide a estrutura dos templates e o que cada versão nova muda, e quem consome só ajusta valores em `values.yaml` e acompanha as versões novas publicadas.

Outra é escrever um chart inteiramente local, sem nenhuma dependência de terceiro, quando o objetivo não é instalar um software publicado por outra pessoa, mas gerar um conjunto de manifestos que só faz sentido dentro do próprio projeto, como um agrupamento de recursos que se repete de instância para instância. Nenhuma delas é logicamente superior à outra; a escolha certa depende de quem é dono do conteúdo que está sendo empacotado.

## Continue por aqui

[Helm e os charts](../arquitetura/helm-e-charts.md), na arquitetura, mostra como o hl-infrastructure aplica cada um desses conceitos de verdade: quais componentes embrulham um chart de terceiro como dependência, quais são charts locais sem dependência nenhuma, e por que nenhum manifesto já renderizado fica vendorizado no repositório. [Gerar várias instâncias de um recurso com Helm](helm-templating-de-lista.md) aprofunda o padrão de repetição usado pelos charts locais deste repositório.
