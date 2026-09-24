# Entrega push-based

Na entrega push-based, uma pipeline ou operador externo inicia a alteração no
ambiente de destino. O agente que executa precisa de credenciais de escrita e
conectividade até a API alvo.

## Escolha

Push pode ser simples em ambientes pequenos e útil quando o destino não pode
buscar artefatos. O custo é guardar credenciais de deploy fora do cluster,
coordenar concorrência e perceber divergência criada manualmente.

O modelo não é necessariamente imperativo. Uma pipeline pode aplicar
manifestos declarativos, mas a direção da conexão continua sendo externa para
o ambiente.

## Relações

- [Entrega pull-based](pull-based-delivery.md) reduz credenciais de escrita
  fora do ambiente.
- [GitOps](gitops.md) adiciona reconciliação ao estado versionado.
- [CI/CD](../ci-cd.md) trata o pipeline como um todo.
