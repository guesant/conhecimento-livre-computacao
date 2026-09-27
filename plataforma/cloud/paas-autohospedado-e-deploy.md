# Mapa de PaaS autohospedado e plataformas de deploy

Uma plataforma de deploy reduz o trabalho repetitivo entre o código e a aplicação em
execução. Ela pode conectar um repositório Git, construir uma imagem, configurar uma rede,
emitir certificados, publicar um domínio, acompanhar o estado do processo e permitir rollback.
O nome PaaS, porém, não significa que todas as responsabilidades desapareceram. A pergunta
central é quem opera o control plane, os servidores, o sistema operacional, os dados e a
recuperação.

## Dois modelos diferentes

Em um PaaS gerenciado, o fornecedor opera a plataforma e parte significativa da infraestrutura.
Railway é um exemplo desse modelo. O usuário trabalha com projetos, ambientes, serviços,
deployments, volumes, domínios, variáveis e observabilidade, mas não administra diretamente o
host que executa cada workload.

Em uma plataforma autohospedada, o software de controle roda em infraestrutura escolhida pelo
operador e geralmente provisiona workloads Docker em um ou mais servidores. Coolify, Dokploy e
CapRover pertencem a essa família, embora tenham arquiteturas, abstrações e limites diferentes.
O operador continua responsável pelo host, pelo firewall, pelo armazenamento, pelas credenciais,
pelos backups, pelas atualizações e pela disponibilidade do próprio control plane.

## O que uma plataforma costuma abstrair

As plataformas não abstraem necessariamente a mesma camada. Antes de escolher, verifique se o
recurso é realmente gerenciado ou apenas exposto por uma tela:

| Capacidade | Pergunta que precisa ser respondida |
| --- | --- |
| Build | A plataforma usa buildpacks, Nixpacks, Dockerfile, imagem pronta ou Compose? |
| Deploy | Há health check, rollout, rollback, pausa e histórico de versões? |
| Rede | Quem termina TLS, configura DNS, proxy reverso e rede privada? |
| Estado | Volumes, banco e backups são duráveis, exportáveis e testados? |
| Operação | Logs, métricas, alertas e acesso ao shell continuam disponíveis? |
| Escala | A escala é por processo, host, serviço, Swarm, região ou apenas manual? |
| Segurança | Como são isolados usuários, projetos, secrets, builds e sockets Docker? |
| Recuperação | O que acontece se o control plane ou o host desaparecer? |

## Quando usar

Uma plataforma autohospedada pode ser adequada para pequenos times, laboratórios, projetos
pessoais, aplicações web com poucos hosts e organizações que preferem controlar a infraestrutura
sem escrever toda a automação de Docker, proxy e certificados. Ela também pode servir como uma
camada de conveniência sobre VPS, desde que os limites do ambiente sejam conhecidos.

Ela é menos apropriada quando o workload exige consenso distribuído, isolamento forte entre
tenants, políticas detalhadas de rede, auditoria regulatória, múltiplas regiões, volumes
altamente disponíveis ou uma separação rigorosa entre build e deploy. Nesses casos, Kubernetes,
uma plataforma gerenciada ou uma automação declarativa dedicada pode representar melhor o
problema.

## Riscos de operação

O socket Docker e as credenciais SSH usados por essas plataformas têm grande poder sobre o host.
Uma aplicação comprometida, uma integração Git mal configurada ou uma conta administrativa exposta
pode alcançar workloads vizinhos e, em alguns desenhos, o próprio host. O painel deve ficar atrás
de autenticação forte, rede restrita, TLS e atualizações regulares.

Não trate volume local como backup. Mantenha imagens reproduzíveis, arquivos de configuração
versionados, secrets fora do repositório, cópias independentes dos dados e um procedimento de
restauração exercitado. A facilidade do primeiro deploy não prova que a plataforma atende aos
requisitos de produção.

## Relação com IaaS e GitOps

IaaS entrega recursos que ainda precisam ser operados. Uma plataforma autohospedada pode ser
instalada sobre IaaS para reduzir trabalho cotidiano, mas cria outro componente stateful para
atualizar e recuperar. GitOps, por sua vez, trata o repositório como fonte declarativa de estado
e usa reconciliação; um painel de deploy pode ser apenas um mecanismo imperativo de operação.

É possível combinar os modelos, mas é importante definir uma única fonte de verdade para cada
recurso. Alterar o mesmo Deployment pelo painel, por scripts SSH e por um reconciliador GitOps
produz drift e torna o rollback ambíguo.

## Plataformas desta seção

- [Coolify](coolify.md), control plane autohospedado para workloads Docker.
- [Dokploy](dokploy.md), plataforma autohospedada com Docker Compose e suporte a múltiplos servidores.
- [CapRover](caprover.md), PaaS baseado em Docker Swarm, Nginx e aplicações orientadas a serviços.
- [Railway](railway.md), plataforma cloud gerenciada com projetos, serviços e ambientes.

## Fontes primárias

- [Coolify, o que é](https://coolify.io/docs/core/what-is-coolify)
- [Dokploy, documentação](https://docs.dokploy.com/docs/core)
- [CapRover, início](https://caprover.com/docs/get-started)
- [Railway, documentação](https://docs.railway.com/)
