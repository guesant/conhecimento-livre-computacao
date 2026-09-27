# Context

Context são dados adicionais usados na decisão de autorização, como hora,
origem de rede, dispositivo, método de autenticação, risco ou estado do
recurso.

## Confiabilidade

Contexto só é seguro quando sua origem, integridade e validade são conhecidas.
Um cliente não pode declarar que está em uma rede confiável ou que recebeu MFA.

## Limites

Quanto mais contexto uma policy exige, mais difícil fica reproduzir, testar e
auditar a decisão. Prefira atributos necessários e estáveis.
