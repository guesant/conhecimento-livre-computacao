# SOPS

SOPS é uma ferramenta para cifrar valores sensíveis em arquivos estruturados,
como YAML, JSON, ENV ou INI, preservando chaves, forma e metadados necessários
para revisão. Ele separa a estrutura que precisa ser editada da parte que
precisa permanecer secreta.

## Modelo

Uma regra de configuração seleciona os arquivos e os recipients autorizados.
O SOPS cifra os valores e mantém metadados que permitem descobrir como
decifrá-los. O arquivo continua versionável, mas o diff não deve revelar
segredos.

SOPS pode usar age, PGP ou outros backends suportados. A ferramenta não cria
uma autoridade de identidade: ela aplica o conjunto de chaves definido pelo
fluxo. A posse da identity privada autoriza a leitura de todos os arquivos
que foram cifrados para ela.

## Edição e rotação

Adicionar um destinatário requer recifrar os dados para proteger a chave de
conteúdo para a nova chave pública. Remover um destinatário exige recifrar sem
ele. Isso torna a alteração de destinatários uma mudança de segurança que
precisa de revisão e validação de recuperação.

SOPS não protege o valor depois da decifragem. Processos, variáveis de
ambiente, manifests renderizados, logs, caches, dumps e artefatos precisam de
controles próprios. Uma pipeline que decifra em um diretório compartilhado pode
expor o segredo mesmo que o Git esteja correto.

## Integração GitOps

Um repositório pode manter recipients públicos no Git e entregar a operação de
decifragem a um operador, plugin ou serviço de chaves. O componente que possui
a identity privada precisa ter permissões mínimas, logs sem valores secretos e
um procedimento de recuperação que não dependa do próprio segredo cifrado.

O sistema também precisa responder o que acontece quando um destinatário é
revogado, quando uma identity é perdida e quando a aplicação precisa trocar o
valor em uso. Backup de chave e rotação de dados são responsabilidades
separadas.

## Relações

- [age](age.md) descreve o backend de recipients e identities.
- [SOPS keyservice](sops-keyservice.md) descreve delegação de operações.
- [Segredos](index.md) trata o ciclo de vida geral.
- [Criptografia de segredos no Git](../../criptografia-de-segredos-no-git.md)
  compara estratégias.

## Fontes primárias

- [SOPS, projeto oficial](https://github.com/getsops/sops)
- [age](https://github.com/FiloSottile/age)
