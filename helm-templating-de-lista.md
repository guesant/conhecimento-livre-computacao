# Gerar várias instâncias de um recurso com Helm

Um [chart Helm](helm-e-charts.md) normalmente declara um recurso do [Kubernetes](k3s.md) por arquivo de template, com o `values.yaml` preenchendo os campos que variam. Isso funciona bem quando existe uma instância só de cada coisa, mas cria um problema diferente quando o mesmo tipo de recurso precisa se repetir várias vezes, uma para cada item de uma lista, como um `Deployment` por microsserviço ou uma `Application` do [ArgoCD](argocd.md) por satélite: escrever um arquivo de template por instância significa que adicionar um item novo é escrever um arquivo novo, e qualquer mudança na estrutura comum precisa ser replicada em todos os arquivos existentes.

A engine de template do [Helm](helm-e-charts.md) resolve isso com o mesmo mecanismo de qualquer motor de template que processa uma linguagem baseada em Go templates: uma diretiva `range` itera sobre uma lista e repete o bloco de conteúdo entre `{{- range .Values.algo }}` e `{{- end }}` uma vez por item da lista, com cada campo do item acessível dentro do bloco pelo próprio nome (`.name`, `.repoURL`, e assim por diante, já que `range` altera o escopo do `.` para o item da iteração atual). O resultado, depois de processado, é um documento YAML de múltiplos recursos separados por `---`, exatamente como se cada um tivesse sido escrito à mão, só que gerado a partir de uma lista em `values.yaml` em vez de arquivo por arquivo.

Isso muda a operação de "adicionar uma instância nova" de "criar um arquivo" para "acrescentar um item à lista", e reduz "mudar a estrutura comum a todas as instâncias" de "editar N arquivos" para "editar um template só". O preço é que o template fica um nível mais abstrato: ler o resultado final exige rodar o `helm template` (ou usar a saída já renderizada, quando existe), porque o arquivo fonte, por si só, não é mais um manifesto [Kubernetes](k3s.md) válido, é um gerador de manifestos.

## Onde isso esbarra com outra sintaxe de template

Um risco real desse padrão aparece quando o valor de um campo, dentro da lista, é ele mesmo uma expressão de outra linguagem de template, não um dado literal. Muitas ferramentas de CI/CD escrevem suas próprias variáveis numa sintaxe parecida com `{{ }}`, e o motor de template do [Helm](helm-e-charts.md) tentaria interpretar essa expressão como se fosse uma diretiva sua, quebrando a renderização ou produzindo um valor vazio.

A saída é manter a expressão fora do arquivo de template, como uma string dentro de `values.yaml`. O Helm nunca chega a olhar o conteúdo dessa string: ele só substitui o marcador `{{ .Values.campo }}` pelo texto dela, e a expressão da outra ferramenta segue intacta no resultado, pronta para ser interpretada por quem realmente sabe lê-la.

## Uma alternativa nativa do Kubernetes: `ApplicationSet`

O [ArgoCD](argocd.md) tem seu próprio mecanismo para "um template, várias instâncias", chamado `ApplicationSet`: um recurso que combina um gerador (uma lista embutida, uma consulta a um diretório do git, ou outras fontes) com um template de `Application`, e o próprio controller do ArgoCD expande isso em uma `Application` de verdade por item, dentro do cluster. A vantagem é não depender de renderização por fora. A diferença central em relação a um [chart Helm](helm-e-charts.md) com `range` é que o `ApplicationSet` introduz sua própria sintaxe de template, também baseada em chaves duplas, processada por um controller diferente do [Helm](helm-e-charts.md).

Isso reintroduz o problema da seção anterior num grau a mais. Um `ApplicationSet` cujo template contém um campo escrito na notação de chaves duplas de uma terceira ferramenta faz a mesma sequência de caracteres atravessar várias camadas de template antes de virar o valor final, e cada camada é uma chance de alguém interpretar o que não era seu. Quando esse é o caso, ficar com uma engine de template só, bem entendida, costuma custar menos do que a conveniência nativa da outra.

## Continue por aqui

[Helm e charts](helm-e-charts.md) explica o que compõe um chart e a sintaxe de template desde o início, para quem chegou aqui sem essa base. [GitOps: root e satélites](../arquitetura/gitops-root-e-satelites.md) mostra esse padrão aplicado de verdade neste repositório, incluindo o motivo de `ApplicationSet` ter sido descartado aqui; [adicionar um satélite novo](../operacional/adicionar-um-satelite.md) é o passo a passo operacional que usa os charts resultantes.
