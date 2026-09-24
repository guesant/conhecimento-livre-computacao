# Chart Helm

Um chart é um pacote versionado de recursos Kubernetes. Ele possui um arquivo
de metadados, valores padrão, templates e, quando necessário, dependências de
outros charts. O resultado de uma renderização depende tanto do conteúdo do
chart quanto dos valores fornecidos pelo consumidor.

Templates devem expor valores que representem decisões reais de instalação,
sem transformar cada campo do manifesto em uma opção arbitrária. Dependências
podem ser vendorizadas para reprodutibilidade ou resolvidas por um repositório
confiável, conforme a política de supply chain do ambiente.

## Renderização e validação

Um chart pode ser renderizado sem acesso ao cluster. Essa propriedade permite
executar lint, validação de schema e políticas antes da aplicação. A inspeção
do resultado renderizado é mais confiável do que revisar somente o template,
porque condicionais e valores podem alterar completamente o manifesto final.

## Relações

- [Helm](helm.md) explica o cliente e o ciclo de instalação.
- [kubeconform](../../qualidade/validacao/kubeconform.md) valida o schema
  renderizado.
- [Conftest](../../qualidade/validacao/conftest.md) aplica políticas ao
  manifesto renderizado.

## Fonte primária

- [Helm charts](https://helm.sh/docs/topics/charts/)
