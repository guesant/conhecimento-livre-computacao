# Gerar várias instâncias de um recurso com Helm

Um [chart Helm](containers/packaging/helm.md) normalmente declara um recurso do [Kubernetes](k3s.md) por arquivo de template, com o `values.yaml` preenchendo os campos que variam. Isso funciona bem quando existe uma instância só de cada coisa, e deixa de funcionar quando o mesmo tipo de recurso precisa se repetir várias vezes, uma para cada item de uma lista, como um Deployment por microsserviço ou uma Application do [ArgoCD](argocd.md) por satélite.

Escrever um arquivo de template por instância transforma "adicionar um item novo" na tarefa de criar um arquivo novo, copiado do anterior e ajustado à mão. Pior, qualquer mudança na estrutura comum precisa ser replicada em todos os arquivos existentes, e basta esquecer um para o conjunto divergir sem que nada acuse a divergência.

A engine de template do [Helm](containers/packaging/helm.md) resolve isso com o mesmo mecanismo de qualquer motor de template baseado em Go templates: uma diretiva range itera sobre uma lista e repete o bloco de conteúdo entre a abertura e o fechamento do laço uma vez por item, como na tabela abaixo. Dentro do bloco, cada campo do item fica acessível pelo próprio nome, porque range altera o escopo do ponto para o item da iteração atual.

| Sintaxe | Papel |
| --- | --- |
| `{{- range .Values.algo }}` | abre o laço, iterando sobre a lista `algo` dentro de `values.yaml` |
| `{{- end }}` | fecha o laço |
| `.name`, `.repoURL` | campos do item atual, acessíveis pelo nome dentro do laço |
| `---` | separador de documentos YAML entre as instâncias geradas |

O resultado, depois de processado, é um documento YAML de múltiplos recursos separados pelo marcador de documento do próprio YAML, exatamente como se cada um tivesse sido escrito à mão. A diferença está na fonte, que passa a ser uma lista em `values.yaml` em vez de um arquivo por recurso.

Isso muda a operação de "adicionar uma instância nova" de "criar um arquivo" para "acrescentar um item à lista", e reduz "mudar a estrutura comum a todas as instâncias" de "editar N arquivos" para "editar um template só". O preço é que o template fica um nível mais abstrato.

Ler o resultado final passa a exigir rodar o `helm template`, ou consultar a saída já renderizada quando ela existe, porque o arquivo fonte deixou de ser um manifesto [Kubernetes](k3s.md) válido por si só. Ele é um gerador de manifestos, e um erro do gerador só aparece no momento da renderização, não na leitura do arquivo.

## Onde isso esbarra com outra sintaxe de template

Um risco real desse padrão aparece quando o valor de um campo, dentro da lista, é ele mesmo uma expressão de outra linguagem de template, não um dado literal. Muitas ferramentas de CI/CD escrevem suas próprias variáveis numa sintaxe parecida com `{{ }}`, e as duas linguagens passam a disputar a mesma sequência de caracteres.

O motor de template do [Helm](containers/packaging/helm.md) roda primeiro e tenta interpretar essa expressão como se fosse uma diretiva sua. O resultado é a renderização quebrar com erro de sintaxe ou, pior, produzir um valor vazio que passa despercebido até o recurso chegar ao cluster.

A saída é manter a expressão fora do arquivo de template, como uma string dentro de `values.yaml`. O Helm nunca chega a olhar o conteúdo dessa string: ele só substitui o marcador `{{ .Values.campo }}` pelo texto dela.

A expressão da outra ferramenta segue intacta no resultado, pronta para ser interpretada por quem realmente sabe lê-la. O custo é que o valor deixa de estar visível no template e passa a viver em outro arquivo, o que obriga a ler os dois para entender o recurso final.

## Uma alternativa nativa do Kubernetes: `ApplicationSet`

O [ArgoCD](argocd.md) tem seu próprio mecanismo para "um template, várias instâncias", chamado `ApplicationSet`: um recurso que combina um gerador (uma lista embutida, uma consulta a um diretório do git, ou outras fontes) com um template de Application, e o próprio controller do ArgoCD expande isso em uma aplicação de verdade por item, dentro do cluster.

A vantagem é não depender de renderização por fora: o estado desejado fica declarado num recurso só, e o controller cria, atualiza e remove as aplicações conforme a lista muda.

A diferença central em relação a um [chart Helm](containers/packaging/helm.md) com `range` é que esse recurso introduz sua própria sintaxe de template, também baseada em chaves duplas. Essa sintaxe é processada por um controller dentro do cluster, e não pelo [Helm](containers/packaging/helm.md), o que coloca duas linguagens de template no mesmo caminho.

Isso reintroduz o problema da seção anterior num grau a mais. Um recurso desses cujo template contém um campo escrito na notação de chaves duplas de uma terceira ferramenta faz a mesma sequência de caracteres atravessar várias camadas de template antes de virar o valor final.

Cada camada é uma chance de alguém interpretar o que não era seu, e o estrago aparece no valor renderizado, longe do arquivo que o declarou. Quando esse é o caso, ficar com uma engine de template só, bem entendida, costuma custar menos do que a conveniência nativa da outra.

## Continue por aqui

[Helm](containers/packaging/helm.md) explica o que compõe um chart e a sintaxe de template desde o início, para quem chegou aqui sem essa base. [GitOps: root e satélites](../arquitetura/gitops-root-e-satelites.md) mostra esse padrão aplicado de verdade neste repositório, incluindo o motivo de `ApplicationSet` ter sido descartado aqui; [adicionar um satélite novo](../operacional/adicionar-um-satelite.md) é o passo a passo operacional que usa os charts resultantes.
