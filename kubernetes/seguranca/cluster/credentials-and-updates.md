# Credenciais do cluster

Segurança de cluster é um processo de ciclo de vida. Certificados, tokens,
chaves de bootstrap, imagens, feature gates, componentes de terceiros e a
própria versão do Kubernetes mudam ao longo do tempo. Uma configuração segura
no dia da instalação pode perder essa propriedade se credenciais não forem
rotacionadas, APIs experimentais permanecerem abertas ou uma vulnerabilidade
for corrigida somente no repositório e não no cluster.

## Bootstrap e rotação

Credenciais usadas para ingressar um nó devem ter validade curta e escopo
restrito. Depois do bootstrap, tokens que não são mais necessários devem ser
revogados. Certificados de clientes e servidores precisam de um inventário,
datas de expiração, autoridade emissora, destino e procedimento de substituição
sem indisponibilidade.

A rotação deve ser testada antes do vencimento. O teste precisa incluir um nó
novo, um API server reiniciado, um Kubelet reconectando e um operador que use
credenciais externas. Não remova a credencial antiga antes de confirmar que a
nova está sendo usada por todos os consumidores necessários.

Quando uma credencial pode ter sido exposta, apenas gerar uma nova cópia não
basta. Revogue ou remova a credencial antiga, invalide tokens derivados,
inspecione audit logs, verifique backups e considere substituir chaves que
tenham sido copiadas para imagens, logs ou máquinas de operação.

## Feature gates e APIs experimentais

Features alpha e beta podem mudar sem a estabilidade e o modelo de segurança
de uma API estável. Ative somente as que têm necessidade documentada. Desative
features não utilizadas, removendo também controllers, RBAC, webhooks e
dependências que existiam apenas para elas.

Uma feature gate pode mudar a capacidade de um componente sem mudar o
manifesto do workload. Ela precisa estar registrada no inventário de versão,
ser testada na mesma combinação de control plane e nodes e ser revisada antes
de um upgrade.

## Atualizações e vulnerabilidades

Acompanhe avisos de segurança do Kubernetes, do distribuidor, do runtime, do
CNI, do CSI, do kernel, das imagens e dos provedores externos. O inventário
deve relacionar versão do control plane, versão dos kubelets e componentes
instalados, porque corrigir apenas um deles pode deixar a cadeia vulnerável.

Planeje rollout com backup verificado, janela de observação, critérios de
rollback e teste das políticas de segurança. Um upgrade pode alterar defaults,
admission, APIs removidas, comportamento de certificados e compatibilidade de
webhooks. A validação precisa incluir rejeição de um Pod privilegiado, acesso
da ServiceAccount, NetworkPolicy, probes e restauração de dados.

## Comunicação de vulnerabilidades

Não publique detalhes de uma falha não corrigida em issues ou canais abertos
antes de seguir o processo de divulgação responsável. Use os canais oficiais,
coordene o impacto com o distribuidor e preserve evidências sem expor
credenciais. Em um incidente ativo, separar canal de coordenação, canal de
comunicação e canal de execução reduz confusão.

## Checklist de ciclo de vida

- descobrir versões, imagens, certificados e feature gates;
- conferir o inventário de identidades e permissões;
- validar backups e chaves de criptografia;
- testar rotação em um ambiente equivalente;
- aplicar correções e observar os eventos de rollout;
- testar autenticação, autorização, admission e isolamento;
- registrar o resultado e a decisão de manter ou remover exceções;
- atualizar o procedimento antes do próximo ciclo.

## Fontes primárias

- [Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
- [Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
- [Kubernetes security disclosure](https://kubernetes.io/security/)
- [Kubernetes release notes](https://kubernetes.io/releases/)
