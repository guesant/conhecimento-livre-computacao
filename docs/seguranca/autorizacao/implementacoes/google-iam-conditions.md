# Google Cloud IAM Conditions

Google Cloud IAM Conditions acrescenta expressões condicionais às concessões
de IAM. A decisão pode considerar recurso, tempo, atributos e contexto da
requisição.

## Uso

Condições podem limitar uma permissão a um recurso, prefixo ou janela de
tempo. O escopo deve ser pequeno e testado, porque uma expressão incorreta
reduz acesso legítimo ou amplia acesso indevido.

## Limites

IAM Conditions não substitui autorização por objeto dentro de uma aplicação.
Ela controla acesso aos recursos reconhecidos pela plataforma Google Cloud.

## Fonte

- [Visão geral de IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview)
