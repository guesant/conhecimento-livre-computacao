# Policy Enforcement Point

Policy Enforcement Point, PEP, é o componente que aplica a decisão do PDP.
Pode ser um middleware, controller, gateway, banco, proxy ou serviço de
domínio.

## Regra

O PEP deve negar ou interromper a operação quando a decisão não for permitida.
Renderizar ou esconder um botão não é enforcement.

## Cuidados

O PEP precisa proteger todos os caminhos equivalentes, inclusive endpoints
internos, jobs, exportações, downloads e operações administrativas.
