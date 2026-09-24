# Backup da chave age

Quando o repositório GitOps usa SOPS com age, a chave privada age é o material
que permite decifrar os arquivos protegidos. O Git pode continuar íntegro e os
manifestos podem continuar disponíveis, mas a perda dessa chave torna os
segredos irrecuperáveis.

A cópia de recuperação deve ficar fora do repositório e fora do único host que
a usa em produção. A cópia também precisa ser testada periodicamente,
decifrando um arquivo de teste ou um conjunto de dados sem valor operacional.
Uma chave guardada mas nunca testada é uma suposição, não uma garantia.

Uma chave age comprometida não tem revogação remota equivalente à de um token.
A resposta é gerar um par novo e recifrar os arquivos protegidos pelo par
antigo. Por isso, restringir o acesso à chave privada e separar seus backups
por domínio de falha é mais simples do que reagir a uma exposição.

## Relações

- [SOPS e age](sops-age.md) explica o formato e o fluxo de cifragem.
- [SOPS keyservice](sops-keyservice.md) trata da delegação de operações da
  chave privada.
- [Estado fora do Git](../../../operacional/estado-fora-do-git.md) lista o
  material necessário para reconstrução.

## Fonte primária

- [SOPS, age](https://github.com/getsops/sops)
- [age](https://age-encryption.org/)
