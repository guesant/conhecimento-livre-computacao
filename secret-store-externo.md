# Secret stores externos

As implementações de [External Secrets Operator](seguranca/secrets/external-secrets.md)
e [Vault e OpenBao](seguranca/secrets/vault-openbao.md) possuem páginas
canônicas próprias. Este texto compara a composição de um operator de entrega
com um backend de segredos e registra os trade-offs de execução externa.

A alternativa a cifrar um segredo antes do commit, descrita em [criptografia de segredos no Git](criptografia-de-segredos-no-git.md), é não versionar o valor de jeito nenhum: mantê-lo inteiramente fora do repositório, num serviço dedicado a armazenar e controlar acesso a segredos, e deixar no Git apenas uma referência declarativa a ele, como um caminho ou uma chave de busca.

Um operator dentro do cluster busca o valor real no momento da sincronização e o materializa como um `Secret` Kubernetes comum, sem que o texto original jamais passe pelo histórico do repositório. Esta página cobre essa família como conhecimento geral: nenhuma ferramenta descrita aqui roda no cluster deste repositório, que usa SOPS com age como única estratégia de segredos, e o motivo dessa escolha está em [criptografia de segredos no Git](criptografia-de-segredos-no-git.md).

## External Secrets Operator

O External Secrets Operator (ESO) sincroniza valores de múltiplos backends, como Vault, OpenBao, AWS Secrets Manager, GCP Secret Manager e Azure Key Vault, para Secrets Kubernetes, usando uma API declarativa comum, independente de qual backend está por trás. A tabela abaixo resume os recursos declarativos dessa API antes de explicar como eles se conectam entre si.

| Recurso | Papel |
| --- | --- |
| `SecretStore` / `ClusterSecretStore` | Declara qual backend usar e qual credencial autentica nele; o segundo tem escopo de cluster inteiro em vez de um namespace. |
| `ExternalSecret` | Referencia um SecretStore e especifica quais chaves ou caminhos buscar no backend. |
| `Secret` | Recurso Kubernetes nativo gerado e mantido atualizado pelo ESO a cada ciclo de sincronização. |

Um método comum de autenticação contra um backend como o Vault ou o OpenBao dispensa até uma credencial estática guardada no cluster.

O método de autenticação Kubernetes do próprio backend valida diretamente o token projetado de uma ServiceAccount (o mesmo mecanismo de identidade descrito em [RBAC Kubernetes](kubernetes/access/rbac.md)) contra a API do cluster, então a identidade que autentica no backend é a própria ServiceAccount do operator, sem que nenhum segredo de longo prazo precise ser gerado, distribuído e rotacionado manualmente só para essa conexão inicial.

Um ExternalSecret referencia o SecretStore correspondente e especifica quais chaves ou caminhos buscar, gerando e mantendo atualizado o Secret correspondente a cada ciclo de sincronização.

A vantagem central do ESO sobre um operator dedicado a um único backend é a portabilidade: a mesma API de `ExternalSecret` funciona com qualquer backend suportado, o que facilita trocar de provedor sem reescrever os manifestos que os consumidores do segredo já usam. Um operator dedicado a um único backend, em troca, tende a expor recursos mais específicos daquele backend com mais profundidade, ao custo do acoplamento a ele.

Vale o ESO quando o ambiente já usa, ou pode vir a usar, mais de um backend de segredos, ou quando a portabilidade entre eles é uma prioridade explícita; vale um operator dedicado quando o ambiente está comprometido com um único backend e não há expectativa real de trocar.

## OpenBao e Vault

OpenBao é um fork open source do HashiCorp Vault, criado depois que o Vault mudou sua licença para a Business Source License. Os dois compartilham a mesma arquitetura central: um cofre de segredos com controle de acesso granular, trilha de auditoria e, criticamente, um mecanismo de unseal.

Um cofre OpenBao ou Vault armazena seus dados criptografados em repouso, e para servir qualquer segredo precisa primeiro ser destravado, isto é, receber o material criptográfico gerado na sua própria inicialização que permite decifrar a chave mestra interna. Sem esse material, nem um administrador com acesso root ao host consegue ler o que está armazenado ali dentro.

Na prática, inicializar um cofre novo roda `bao operator init`, que devolve as chaves de unseal e o token root numa única vez. Destravar depois de um reinício roda `bao operator unseal` uma vez por chave, até atingir o limiar mínimo. O comando de status do próprio cofre confirma o resultado, reportando quando ele volta a servir segredos normalmente.

Esse mecanismo cria uma dependência circular interessante quando o cofre roda dentro do mesmo cluster que ele protege: se o cluster reinicia e o cofre precisa ser destravado de novo, mas as chaves de unseal só existem dentro desse mesmo cluster, a recuperação trava num círculo sem saída.

As chaves de unseal, ou uma configuração de destravamento automático usando um serviço de chaves externo, precisam existir fora do domínio de falha que o próprio cofre protege. Um serviço gerenciado fora do cluster, ou hospedado por terceiro, evita esse problema por completo, porque a disponibilidade do cofre deixa de depender da disponibilidade do ambiente que ele protege.

## Destravamento automático com um KMS externo

Destravar manualmente um cofre a cada reinicialização tem um custo operacional real quando alguém precisa executar esse passo toda vez que o processo reinicia, seja por um crash, uma atualização ou um failover. O destravamento automático, chamado de auto-unseal, substitui essa apresentação manual por uma chamada automática a um serviço de gerenciamento de chaves (KMS) externo ao próprio cofre, tipicamente um provedor de nuvem.

Na inicialização, o cofre se autentica nesse serviço, solicita a operação de descriptografia da sua chave mestra, já armazenada localmente em forma cifrada, e conclui o destravamento sem intervenção humana.

O ponto central a entender antes de adotar esse mecanismo é que ele não elimina a necessidade de proteger material criptográfico crítico, apenas desloca essa responsabilidade do operador humano, que guardava as chaves de unseal, para o controle de acesso do provedor de nuvem, isto é, a política que autoriza a credencial do cofre a usar aquela chave específica no KMS. Se essa credencial for comprometida ou mal configurada, o efeito é equivalente a expor as chaves de unseal originais.

O destravamento automático se justifica sobretudo em produção, onde uma reinicialização não planejada não pode depender da disponibilidade de um operador humano, e especialmente em topologias com múltiplas réplicas, onde cada uma precisa se destravar de forma independente para participar da eleição de líder.

## Alta disponibilidade

Uma instância única de OpenBao ou Vault é um ponto único de falha: se o processo para, por qualquer motivo, nenhum segredo fica acessível até que ele volte. O modo de alta disponibilidade resolve isso rodando múltiplas réplicas que compartilham o mesmo estado, permitindo que uma assuma o papel de líder automaticamente quando a anterior falha.

Apenas uma réplica é líder a qualquer momento, e é ela que processa as escritas; as demais são standbys, que atendem leituras a partir do estado replicado mas redirecionam qualquer escrita recebida para o líder atual. A eleição segue o mesmo modelo de consenso Raft usado por outros sistemas distribuídos, como o próprio etcd do Kubernetes, e ocorre em segundos quando o líder para de responder, desde que o número de réplicas restantes ainda satisfaça o quorum mínimo.

O quorum, o número mínimo de réplicas que precisa concordar para eleger um líder ou confirmar uma escrita, é calculado como a metade do total de réplicas arredondada para baixo, mais um.

Esse cálculo é o motivo pelo qual topologias de alta disponibilidade quase sempre usam um número ímpar de réplicas: três toleram a perda de uma sem perder quorum, cinco toleram a perda de duas, e duas réplicas não oferecem vantagem nenhuma sobre três, porque perder qualquer uma delas já derruba o quorum.

Cada réplica ainda precisa passar pelo próprio processo de unseal antes de participar do cluster, o que normalmente exige combinar essa topologia com destravamento automático via KMS externo, porque destravar manualmente cada réplica a cada reinicialização anularia boa parte do ganho de disponibilidade que a própria alta disponibilidade deveria trazer.

O backend de armazenamento compartilhado entre as réplicas também importa para essa topologia. O caminho recomendado hoje é o Integrated Storage, baseado em consenso Raft, em que cada réplica guarda sua própria cópia replicada sem depender de um serviço externo adicional; o Consul já foi a alternativa mais estabelecida, mas perdeu espaço depois de mudar para uma licença fora do padrão aberto, e hoje aparece sobretudo como coordenador de bloqueio combinado com outro backend de dados, não como armazenamento primário.

Alta disponibilidade se justifica quando aplicações em produção dependem do cofre para operar, como autenticação ou credenciais de banco de dados emitidas dinamicamente, e uma indisponibilidade breve já tem impacto real. Em ambientes de desenvolvimento, teste, ou clusters pessoais de nó único, a complexidade adicional de múltiplas réplicas, destravamento automático e um balanceador de carga à frente delas raramente compensa o benefício; uma instância única com backup regular da configuração é suficiente nesse contexto.

## Outras opções: Infisical e serviços gerenciados

Além do ESO e do par OpenBao/Vault, existe uma categoria de plataforma de segredos oferecida como serviço, como o Infisical, que combina um backend hospedado (ou auto-hospedável) com um operator próprio para sincronizar valores para o cluster, de forma parecida ao ESO mas acoplada à sua própria API em vez de a um padrão comum entre múltiplos backends.

O Infisical Secrets Operator declara essa conexão com três recursos próprios: `InfisicalConnection`, que aponta para a instância; `InfisicalAuth`, que autentica uma Machine Identity; e `InfisicalStaticSecret`, que referencia o projeto, o ambiente e o caminho a sincronizar. É a mesma estrutura de referência declarativa do ESO, só que os três papéis vêm como CRDs separados em vez de um recurso único.

A escolha entre um serviço desses e o par ESO mais um backend genérico segue a mesma lógica de portabilidade contra profundidade específica já descrita para o ESO: uma plataforma dedicada tende a oferecer uma experiência mais integrada (interface web, convites de equipe, versionamento de segredo) ao custo de acoplar o ambiente à API e ao modelo de autenticação daquele fornecedor específico.

## Continue por aqui

Nenhuma dessas ferramentas resolve, por si só, o problema de como a primeira credencial de acesso a elas chega ao ambiente; [bootstrap e rotação de segredos](bootstrap-e-rotacao-de-segredos.md) descreve esse problema em geral. [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md) cobre a família de estratégia que este cluster efetivamente usa, SOPS com age, e explica por que ela foi preferida a um secret store externo neste ambiente.
