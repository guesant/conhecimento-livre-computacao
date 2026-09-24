# kubeconform

kubeconform valida manifests Kubernetes contra schemas de recursos e versões
configurados. Ele é adequado para o gate rápido entre renderização e
aplicação, principalmente quando o repositório mantém manifests ou charts
para mais de uma versão do Kubernetes.

## Funcionamento

O comando recebe um ou mais arquivos ou diretórios, identifica o tipo e a
versão do recurso e procura o schema correspondente. O resultado diferencia
manifesto válido, inválido, não encontrado e ignorado conforme as opções da
execução. O pipeline deve tratar estados sem schema como erro, salvo quando a
ausência for deliberada e explicitamente controlada.

Para CRDs, a fonte de schemas precisa representar os recursos usados pelo
cluster. Validar apenas os objetos nativos não prova que um recurso de uma
extensão está correto.

## Configuração confiável

Fixe a fonte e a versão dos schemas quando a reprodutibilidade for importante.
Use modo estrito para detectar campos desconhecidos e valide o resultado
renderizado, não apenas os templates. A entrada deve ser a mesma que o fluxo
de entrega enviará ao cluster.

Não use exclusões amplas para silenciar recursos desconhecidos. Se um recurso
não possui schema público, documente a origem do schema ou use uma validação
específica que preserve a visibilidade da lacuna.

## O que ele não faz

kubeconform não substitui admission control, policy as code, scanner de
segurança ou teste de execução. Um manifesto válido pode ser inseguro,
ineficiente ou incompatível com a capacidade disponível no cluster.

## Diagnóstico

Quando um recurso não é reconhecido, confira apiVersion, kind, a fonte de
schemas e a versão alvo. Quando há campos desconhecidos, confirme se o
manifesto foi renderizado com o chart e os valores esperados. Quando a saída
parece contradizer o cluster, compare a versão do schema usada no gate com a
versão do API server.

## Relações

- [Schema validation](schema-validation.md) explica a responsabilidade do
  schema.
- [Conftest](conftest.md) cobre regras organizacionais além da estrutura.
- [Quality gates](../../../operacional/rodar-quality-gates-localmente.md) trata
  a execução dos gates deste repositório.

## Fonte primária

- [kubeconform](https://github.com/yannh/kubeconform)
