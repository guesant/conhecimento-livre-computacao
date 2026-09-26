# Railway

Railway é uma plataforma cloud gerenciada para provisionar infraestrutura, desenvolver localmente
e publicar aplicações. O modelo organiza recursos em projetos, ambientes, serviços, volumes,
domínios e deployments. A plataforma oferece integração com Git, CLI, templates, serviços de
banco, rede privada, logs, métricas, tracing e uma API.

## Modelo de execução

O usuário escolhe um repositório, uma imagem ou um template e configura o processo de build,
comando de início, variáveis, health checks, domínio e recursos. A Railway executa o workload e
administra a infraestrutura subjacente. Serviços de uma mesma aplicação podem se comunicar por
rede privada, enquanto uma exposição pública usa os mecanismos de domínio e rede da plataforma.

O serviço reduz o trabalho de administrar sistema operacional, proxy, máquinas e parte da
observabilidade. Em troca, o desenho passa a depender das APIs, limites, regiões, preços,
políticas de armazenamento e mecanismos de exportação da Railway.

## Casos de uso

Railway pode ser conveniente para protótipos, aplicações web, APIs, workers, ambientes de
revisão, projetos pequenos e times que precisam reduzir o intervalo entre commit e ambiente
executando. Templates ajudam a iniciar serviços comuns, mas devem ser revisados antes de receber
dados importantes.

A plataforma também pode servir como ambiente de desenvolvimento e validação de uma aplicação
que depois será migrada para IaaS, Kubernetes ou outra nuvem. Para isso, o projeto precisa
manter Dockerfiles, migrations, configuração e backups independentes da interface do provedor.

## Estado e recuperação

Volumes, bancos, backups e point-in-time recovery precisam ser analisados separadamente da
aplicação stateless. Verifique retenção, região, custos de armazenamento, recuperação para outro
projeto e exportação para um destino externo. Um deployment bem-sucedido não é evidência de que o
estado pode ser restaurado.

Também é necessário verificar limites de CPU, memória, rede, tempo de build, egress, processos
longos, jobs agendados e comportamento durante uma indisponibilidade regional. A conveniência
do PaaS não remove a necessidade de definir RPO, RTO, observabilidade e plano de saída.

## Segurança e governança

Proteja tokens de projeto, integrações Git, variáveis secretas e grupos de acesso. Use o princípio
do menor privilégio, separe ambientes e não coloque credenciais de produção em previews sem uma
justificativa clara. Para organizações, verifique RBAC, SSO, trilhas de auditoria, retenção de
logs e requisitos de conformidade disponíveis no plano contratado.

## Railway em comparação com PaaS autohospedado

Railway reduz a quantidade de infraestrutura que a equipe precisa operar. Coolify, Dokploy e
CapRover oferecem mais controle sobre os hosts e os dados, mas transferem ao usuário a operação
do painel, do sistema operacional, da rede, dos volumes e da recuperação. A escolha não é apenas
entre interfaces: é uma decisão sobre domínio de falha, responsabilidades, custo e portabilidade.

## Fontes primárias

- [Railway, documentação](https://docs.railway.com/)
- [Railway, plataforma](https://docs.railway.com/reference/philosophy)
- [Railway, quick start](https://docs.railway.com/quick-start)
- [Railway, checklist de produção](https://docs.railway.com/reference/production-readiness-checklist)
