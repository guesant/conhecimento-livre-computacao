# CapRover

CapRover é uma plataforma PaaS autohospedada que simplifica a publicação de aplicações em
Docker Swarm. Ela reúne uma interface, uma CLI, serviços Docker, Nginx, certificados e um modelo
de aplicações que pode ser operado em um servidor ou em um cluster Swarm.

## Modelo de deploy

Uma aplicação pode ser publicada a partir de código, de uma imagem ou de uma definição
`captain-definition`. A plataforma também possui uma integração com um subconjunto de Docker
Compose. Esse subconjunto não representa a especificação completa do Compose; campos como redes
customizadas, secrets, configs e opções avançadas de deploy precisam ser revisados antes da
migração.

O CapRover usa o nome da aplicação para organizar o serviço e oferece configurações para portas,
diretórios persistentes, variáveis, quantidade de instâncias, domínios e certificados. Em uma
instalação com vários nós, o Swarm fornece o mecanismo de distribuição e o CapRover administra
parte da experiência de publicação.

## Quando faz sentido

CapRover é interessante para quem quer uma experiência de PaaS simples, baseada em Docker e
Swarm, sem entregar os servidores a um fornecedor. Ele pode atender aplicações web, APIs e
serviços pequenos quando o modelo de serviço e a persistência são compatíveis com o ambiente.

O custo dessa simplicidade é aceitar as decisões do projeto sobre Swarm, Nginx, rede e ciclo de
vida. Kubernetes, uma automação Compose direta ou um PaaS gerenciado podem ser opções mais
adequadas quando há requisitos de reconciliação declarativa, políticas detalhadas ou serviços
gerenciados fora do escopo do CapRover.

## Compose e persistência

O suporte a Compose deve ser tratado como uma transformação para aplicações CapRover, não como a
garantia de executar qualquer arquivo Compose sem revisão. Serviços iniciados diretamente com
Compose ficam fora do gerenciamento de escala, backup e ciclo de vida do CapRover.

Volumes persistentes precisam de backup externo e teste de restauração. Escalar réplicas de uma
aplicação não resolve consistência de arquivos locais nem transforma um banco sem replicação em
um banco altamente disponível.

## Segurança e operação

Uma instalação padrão exige atenção a IP público, firewall, portas de administração, Docker
socket, certificados e credenciais. O painel não deve ser exposto sem TLS e autenticação forte.
Restrinja o acesso administrativo, atualize o host e o CapRover, e separe workloads que não
devem compartilhar o mesmo domínio de falha.

Antes de usar em produção, documente a recuperação do manager, do Swarm, do diretório de dados e
das configurações de cada aplicação. Um backup da imagem não recupera automaticamente volumes,
variáveis, certificados e regras de domínio.

## Comparação com plataformas próximas

CapRover é mais específico em torno de Docker Swarm e do seu fluxo de aplicações. Coolify e
Dokploy tendem a oferecer uma superfície mais ampla para servidores, Compose e serviços, mas
também deixam mais escolhas operacionais nas mãos do administrador. Railway desloca a operação
do host para um serviço cloud e cobra conforme seu modelo de uso e de recursos.

## Fontes primárias

- [CapRover, início](https://caprover.com/docs/get-started)
- [CapRover, métodos de deploy](https://caprover.com/docs/deployment-methods.html)
- [CapRover, Docker Compose](https://caprover.com/docs/docker-compose)
- [CapRover, CLI](https://caprover.com/docs/cli-commands)
