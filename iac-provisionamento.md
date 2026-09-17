# Infraestrutura como código

Infraestrutura como código é a prática de descrever máquinas, redes e serviços num arquivo versionado, em vez de configurá-los manualmente clicando numa interface ou digitando comando por comando numa sessão SSH. O ganho central não é a automação em si, é a repetibilidade: o mesmo arquivo produz o mesmo resultado da próxima vez que rodar, seja num servidor novo depois de um desastre, seja num ambiente de teste que precisa espelhar produção. Sem esse arquivo, o estado real de uma máquina vira conhecimento tácito de quem a configurou, perdido assim que essa pessoa esquece um passo ou sai do time.

O termo cobre famílias de ferramenta que resolvem problemas diferentes, e a confusão entre elas é comum. **Provisionamento** cria e destrói recursos, tipicamente numa nuvem: uma máquina virtual, uma rede, um disco. Terraform, Pulumi e [OpenTofu](../arquitetura/opentofu.md) são exemplos dessa família; elas descrevem o estado desejado de recursos de infraestrutura e calculam o plano de mudança (criar isto, destruir aquilo, deixar isto como está) comparando com o que existe hoje. **Gestão de configuração** parte de uma máquina que já existe e configura o que roda dentro dela: quais pacotes instalar, quais arquivos escrever, quais serviços habilitar. [Ansible](ansible.md), Puppet, Chef e Salt são dessa família.

O hl-infrastructure precisa de ambas as famílias, mas por motivos diferentes: não há nuvem para provisionar o Raspberry Pi, que já existe fisicamente antes do repositório existir, então o [Ansible](ansible.md) entra depois desse ponto, configurando um sistema operacional que já está instalado; o [OpenTofu](../arquitetura/opentofu.md) provisiona o que vive fora do node e do cluster, em APIs externas como a da Cloudflare, a da tailnet do Tailscale e a do Keycloak.

## Declarativo versus imperativo

Uma ferramenta de infraestrutura como código pode ser imperativa (uma lista de passos: "instale o pacote X, depois copie o arquivo Y") ou declarativa (uma descrição de estado: "o pacote X deve estar instalado, o arquivo Y deve ter este conteúdo"). A diferença aparece quando a máquina já está parcialmente configurada: numa ferramenta imperativa, rodar os mesmos passos de novo pode falhar na repetição (tentar criar um arquivo que já existe, por exemplo) ou produzir um resultado diferente; numa ferramenta declarativa bem implementada, rodar a mesma descrição de novo produz o mesmo estado final e não falha por já estar feito. Essa propriedade tem nome próprio e aparece detalhada na página sobre [Ansible](ansible.md).

## Continue por aqui

[Ansible](ansible.md) detalha como essa ferramenta específica implementa idempotência e execução remota; [Ansible: as roles do bootstrap](../arquitetura/ansible.md), na arquitetura, mostra como o hl-infrastructure organiza suas próprias roles.
