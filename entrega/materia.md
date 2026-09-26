# materia

materia é uma implementação de GitOps para hosts Podman que organiza o estado
em componentes independentes. Cada componente pode reunir Quadlets, arquivos
de configuração e dados associados, com instalação, atualização e remoção
tratadas como uma unidade.

Essa granularidade reduz artefatos órfãos quando um serviço deixa de ser
atribuído ao host. O modelo também pode aplicar templating e decifrar arquivos
protegidos com age no momento da instalação, desde que o bootstrap da chave
esteja disponível no host.

## Quando usar

materia faz sentido quando um host executa vários serviços que precisam de
ciclos de vida independentes e o operador quer declarar também a limpeza de
recursos associados. O custo é um modelo operacional mais complexo que o de um
sincronizador de diretório.

## Relações

- [orches](orches.md) oferece a alternativa mínima.
- [GitOps](gitops.md) explica a prática geral.
- [Criptografia de segredos no Git](../criptografia-de-segredos-no-git.md)
  explica o modelo de proteção usado com age.
