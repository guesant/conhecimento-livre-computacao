# Topaz

Topaz é um motor de autorização que pode executar decisões localmente ou como
serviço. Ele combina políticas, dados de identidade e relações para responder
decisões próximas do workload.

## Uso

Um PDP local reduz latência e dependência de rede, enquanto uma implantação
centralizada facilita governança e atualização. A escolha precisa considerar
sincronização de políticas, propagação de revogações e comportamento quando o
agente perde contato com a fonte de dados.

## Limites

Topaz não deve receber credenciais sem necessidade e não substitui o PEP. A
aplicação ainda precisa garantir que a decisão seja aplicada ao recurso correto
e que o contexto recebido não possa ser forjado pelo cliente.

## Fonte

- [Documentação do Topaz](https://www.topaz.sh/docs/)
