# Helm

Helm é um gerenciador de pacotes para Kubernetes. Ele renderiza templates
parametrizados e produz manifestos Kubernetes a partir de um chart e de um
conjunto de valores. O chart empacota templates, valores padrão, metadados e
dependências de uma aplicação ou componente de plataforma.

`helm template` renderiza localmente sem aplicar nada. `helm install` e
`helm upgrade` combinam renderização com a criação ou atualização de uma
release. O primeiro é adequado para inspeção e validação; os últimos introduzem
efeitos no cluster e devem ser usados dentro do fluxo de entrega adotado.

## Relações

- [Chart](chart.md) é a unidade empacotada pelo Helm.
- [Compose, Swarm e Kubernetes](../../comparacoes/plataforma/orquestracao.md)
  compara modelos de execução, não gerenciadores de pacotes.
- [Chart](chart.md) explica a unidade empacotada que o Helm renderiza.
  desta documentação.

## Fonte primária

- [Helm documentation](https://helm.sh/docs/)
