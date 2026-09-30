# Rotação de segredos

Rotação substitui uma credencial por outra e revoga a antiga. Uma rotação
segura emite a nova, propaga, confirma uso e só então revoga a antiga.

## Janela de sobreposição

A sobreposição permite que consumidores diferentes mudem em momentos
distintos. Ela exige que o backend aceite as duas credenciais temporariamente
e que exista um prazo claro para retirar a antiga.

Credenciais de curta duração podem rotacionar continuamente por emissão
automática. Isso reduz exposição, mas aumenta dependência de relógio,
disponibilidade e renovação.

## Failure modes

Revogar cedo demais interrompe consumidores atrasados. Não revogar nunca
mantém uma credencial exposta. Um novo valor que não foi propagado pode
parecer válido no secret store e ainda falhar na aplicação.

Meça autenticação, erro e versão de credencial sem registrar o valor. Depois da
troca, procure uso do identificador antigo e destrua-o conforme a política.

## Relações

- [Bootstrap](bootstrap.md) entrega o primeiro valor.
- [Secret](secret.md) define o objeto sensível.
- [Secret store externo](../../secret-store-externo.md) pode automatizar renovação.

## Fonte primária

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
