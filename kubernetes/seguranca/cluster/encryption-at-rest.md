# Criptografia em repouso no Kubernetes

Criptografia em repouso protege dados armazenados pelo API server no datastore.
Ela reduz o impacto de alguém obter um disco, snapshot ou backup, mas não
impede um cliente autorizado de ler o objeto pela API e não substitui
autorização, TLS ou proteção do datastore.

## O que deve ser protegido

Secrets são o caso mais óbvio, mas ConfigMaps e recursos customizados também
podem conter credenciais, tokens, material de bootstrap ou dados editoriais
que não deveriam aparecer em um snapshot sem proteção. O conjunto de recursos
protegidos deve ser definido pela política de dados e pela versão do
Kubernetes, não por uma suposição de que somente o kind `Secret` seja
sensível.

A criptografia configurada para a API não criptografa automaticamente o
filesystem de todos os nós, volumes de aplicações, logs, backups externos ou
discos do provedor. Cada cópia precisa de uma decisão própria.

## EncryptionConfiguration e providers

O API server usa uma configuração de encryption providers para decidir como
serializar recursos no datastore. A configuração costuma declarar uma lista
ordenada de providers para leitura e escrita. O provider de escrita atual é
usado para novos objetos; providers anteriores podem permanecer para leitura
durante uma rotação.

Um padrão de rotação precisa manter a chave antiga até todos os objetos terem
sido regravados com a nova. Remover a chave antes dessa migração pode deixar
objetos ilegíveis. Depois de verificar que não há dados antigos, a chave
retirada deve ser revogada, destruída ou arquivada conforme o modelo de
custódia.

## Chaves e separação de responsabilidades

O arquivo de configuração e as chaves não devem ser incluídos em imagens,
logs, repositórios ou bundles de diagnóstico. Proteja permissões do arquivo,
backup da chave e procedimento de recuperação. Uma cópia criptografada sem a
chave correspondente não é uma estratégia de recuperação completa.

Quando o ambiente suporta um KMS externo, a chave local pode ser reduzida a
uma chave de encriptação de dados protegida por uma chave de encriptação de
chave. O KMS não elimina a necessidade de autenticar o API server nem de
proteger o caminho de rede. Latência e disponibilidade do KMS passam a fazer
parte do caminho de leitura e escrita.

## Verificação

Não presuma que habilitar a configuração alterou objetos já existentes.
Verifique o comportamento de leitura e regrave de forma controlada os
recursos cobertos, acompanhando logs e tempo de resposta. Inspecione um
snapshot apenas em ambiente autorizado e confirme que o valor bruto não pode
ser interpretado sem a chave.

Teste também:

- restart de todos os API servers;
- rotação sem interromper leitura;
- restore do etcd com todas as chaves necessárias;
- indisponibilidade temporária do KMS;
- acesso de usuários autorizados e não autorizados;
- descarte das chaves antigas após o período de transição.

## Limites

Se uma identidade possui permissão para `get` ou `list` Secrets, a API entrega
o valor em claro depois da autorização. Criptografia em repouso não reduz esse
privilégio. RBAC, audit log, Secret rotation, admission e menor exposição são
necessários para controlar o uso do dado.

Backups devem ser criptografados separadamente e ter acesso limitado. Uma
exportação feita por uma ferramenta de CI, um dump de suporte ou um snapshot
de volume pode escapar da configuração do API server e precisa ser incluída
no inventário de cópias.

## Fontes primárias

- [Encrypting Confidential Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
- [KMS provider](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)
- [Secrets good practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)
