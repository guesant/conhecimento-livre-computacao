# Segurança do etcd usado pelo Kubernetes

etcd armazena o estado do control plane. Acesso de leitura pode expor objetos
administrativos, credenciais e Secrets. Acesso de escrita pode alterar o
estado desejado do cluster, criar identidades, modificar admission ou remover
recursos. Por isso, acesso amplo ao etcd deve ser tratado como equivalente a
acesso de administrador do cluster.

## Isolamento de rede

O endpoint cliente do etcd deve ser alcançável apenas pelos API servers e por
ferramentas de operação explicitamente autorizadas. Firewall de host, regras
de security group, sub-redes e NetworkPolicies de componentes devem refletir
essa intenção. Não exponha o endpoint cliente à rede de workloads e não use o
endereço do etcd como um serviço interno genérico.

O endpoint de peer tem finalidade diferente do endpoint cliente. Ele deve ser
permitido apenas entre membros do mesmo cluster etcd. Misturar as duas portas,
usar um certificado de cliente em ambas as funções ou aceitar peers de uma
rede ampla facilita uma configuração acidentalmente insegura.

## TLS e identidade

Conexões cliente e peer devem usar TLS com autoridades e certificados
específicos. A autenticação mútua confirma tanto o servidor quanto o cliente;
criptografar o canal sem restringir quem pode autenticar não implementa
autorização.

Certificados do API server, dos peers, do health check e de ferramentas de
backup devem ter finalidades separadas. Os arquivos de chave privada devem
ter permissões restritas, não devem ser incluídos em imagens ou repositórios e
precisam de rotação e revogação planejadas.

## Autorização e operação

Se o etcd expõe autenticação e autorização próprias, aplique contas e roles
específicas. O componente de backup não precisa de permissão de escrita. Uma
ferramenta de diagnóstico não precisa ler o conteúdo de todas as chaves. O
API server precisa do conjunto definido pela distribuição, mas isso não
justifica compartilhar sua credencial com operadores humanos.

Mantenha mudanças de configuração versionadas e revise os argumentos de
inicialização. Opções que desabilitam autenticação, aceitam URLs inseguras ou
escutam em todos os endereços devem ser tratadas como exceções explícitas.

## Backup e recuperação

Um snapshot é sensível por conter o estado do cluster. Proteja-o em trânsito,
em repouso e durante a restauração. Criptografe o armazenamento, limite quem
pode baixar o arquivo e não publique snapshots em artefatos de CI ou buckets
com acesso amplo.

O backup precisa ser testado com a mesma versão ou uma versão suportada, com
as chaves de encryption at rest correspondentes e com um procedimento para
recriar certificados e endpoints. Um snapshot que pode ser baixado, mas não
restaurado sem segredo ausente, não é uma recuperação válida.

Depois de uma restauração, troque credenciais que possam ter sido expostas no
período de falha, confira a integridade do estado, valide as políticas de
admission e verifique se objetos removidos não voltaram a ficar disponíveis.

## Relações

- [etcd](../../control-plane/etcd.md) explica consistência, quorum e snapshot.
- [Auditoria](audit.md) registra operações feitas pela API, não substitui o
  controle de acesso direto ao datastore.
- [Criptografia em repouso](encryption-at-rest.md) protege objetos da API,
  mas depende da proteção das chaves fora do etcd.
- [Backup do etcd](../../../confiabilidade/backup/etcd.md) trata o
  procedimento operacional.

## Fontes primárias

- [Configure and secure etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [etcd security model](https://etcd.io/docs/latest/op-guide/security/)
- [etcd documentation](https://etcd.io/docs/)
