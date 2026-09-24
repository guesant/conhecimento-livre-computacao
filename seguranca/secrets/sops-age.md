# SOPS e age

SOPS cifra valores estruturados e preserva chaves e forma do arquivo. age é um
backend moderno de criptografia que usa destinatários públicos para cifrar e
chaves privadas fora do Git para decifrar.

## Modelo

O arquivo pode continuar revisável sem revelar os valores. A configuração de
destinatários define quem pode decifrar. Adicionar um destinatário exige
recifrar os dados; remover acesso exige recifrar sem a chave pública antiga.

A chave privada age é uma credencial administrativa do conjunto de arquivos
que ela abre. Ela precisa de backup, controle de acesso e procedimento de
recuperação fora do repositório.

## Limites

SOPS não protege valores depois de decifrados. O processo, ambiente,
manifesto renderizado e logs precisam de política própria. Uma chave privada
perdida pode impedir recuperação; uma chave exposta exige recifrar e revogar a
confiança no destinatário.

## Relações

- [Secret](secret.md) define o problema.
- [Bootstrap](bootstrap.md) trata a chave inicial.
- [SOPS keyservice](sops-keyservice.md) delega operações de chave sem alterar o formato do arquivo.
- [Criptografia de segredos no Git](../../criptografia-de-segredos-no-git.md)
  descreve alternativas e decisão de uso.

## Fontes primárias

- [SOPS](https://github.com/getsops/sops)
- [age](https://age-encryption.org/)
