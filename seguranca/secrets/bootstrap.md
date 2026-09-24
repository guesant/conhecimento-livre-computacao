# Bootstrap de segredos

Bootstrap é a introdução da primeira credencial que permite ao sistema buscar
ou decifrar outras credenciais. Ela não pode depender do próprio secret store
que ainda não consegue autenticar.

## Estratégias

Uma identidade nativa do ambiente, uma chave aplicada manualmente ou um
processo fora do cluster podem iniciar a cadeia. O escopo deve ser mínimo e o
material deve ter duração curta quando possível.

O bootstrap precisa de um caminho de recuperação independente do domínio que
ele habilita. Guardar a única chave dentro do cluster que ela deveria
reconstruir cria uma dependência circular.

## Diagnóstico

Documente onde o bootstrap vive, quem pode usá-lo, como é auditado, como é
rotacionado e como a operação se recupera depois de perder o ambiente. Não
coloque a credencial em Git, imagem, log ou comando persistido.

## Relações

- [Rotação](rotation.md) continua o ciclo.
- [Secret store externo](../../secret-store-externo.md) depende de uma identidade
  inicial.
- [SOPS e age](sops-age.md) exige acesso à chave privada de decifragem.

## Fonte primária

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
