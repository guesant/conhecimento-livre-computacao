# Entrega pull-based

Na entrega pull-based, um agente no ambiente de destino busca a configuração e
a aplica. O pipeline publica uma revisão em um repositório ou registry, e não
precisa iniciar uma conexão administrativa para o cluster.

## Benefícios e custos

O modelo reduz a superfície de credenciais de deploy e permite que o ambiente
controle o momento de observar a mudança. Ele exige um agente saudável,
acesso de saída, credenciais de leitura e observabilidade para saber quando a
mudança foi aplicada.

Uma falha no agente pode deixar o ambiente parado numa revisão válida sem que
o pipeline externo perceba. Status de reconciliação precisa ser exposto e
monitorado.

## Relações

- [GitOps](gitops.md) fornece o modelo declarativo.
- [Reconciliação](reconciliation.md) aplica convergência.
- [Entrega push-based](push-based-delivery.md) mantém o contraste operacional.

## Fonte primária

- [OpenGitOps principles](https://opengitops.dev/)
