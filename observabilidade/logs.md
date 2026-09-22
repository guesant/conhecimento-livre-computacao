# Logs

Logs são registros de eventos produzidos por aplicações e infraestrutura. Eles preservam contexto discreto que seria inadequado representar como uma série temporal de baixa cardinalidade.

## Casos de uso

Diagnóstico de exceções, auditoria de eventos, investigação de uma requisição específica e entendimento de transições de estado são usos comuns.

## Boa prática

Prefira logs estruturados quando consumidores automatizados precisam consultar campos. Inclua contexto suficiente para correlação sem registrar secrets ou dados pessoais desnecessários. Defina retenção pelo valor operacional e pelos requisitos aplicáveis.

## Má prática

Usar texto livre inconsistente para tudo dificulta consulta. Registrar tokens, senhas ou corpos sensíveis cria um novo vazamento. Outra má prática é depender de logs locais efêmeros como única evidência após a perda do nó.

## Continue por aqui

[Loki](loki.md) é uma implementação de centralização e consulta. [Tracing](tracing.md) correlaciona operações distribuídas.