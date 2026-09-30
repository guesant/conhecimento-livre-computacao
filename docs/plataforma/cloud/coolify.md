# Coolify

Coolify é uma plataforma open source e autohospedada para implantar e administrar aplicações,
bancos e serviços em servidores controlados pelo operador. Sua abstração principal é um control
plane que se conecta aos servidores por SSH e coordena workloads Docker, builds, domínios,
certificados, health checks, logs e operações de ciclo de vida.

## Modelo de execução

O operador fornece o servidor onde o workload será executado. A aplicação pode vir de um
repositório Git, de um Dockerfile, de um arquivo Docker Compose ou de uma imagem já construída.
O Coolify configura o recurso, constrói ou baixa a imagem e inicia containers, volumes e redes
no servidor conectado. O proxy desse servidor encaminha os domínios configurados e pode cuidar
do HTTPS.

A instância do Coolify pode ser autohospedada ou usada como serviço gerenciado no Coolify Cloud.
Mesmo no segundo caso, os servidores dos workloads continuam sendo responsabilidade do usuário.
Essa distinção evita confundir o painel gerenciado com hospedagem integral da aplicação.

## Recursos e responsabilidades

O painel concentra projetos, ambientes, variáveis, deploys, logs, health checks, serviços de um
clique, bancos e configurações de domínio. Um recurso já em execução pode continuar atendendo
mesmo que a instância de controle fique temporariamente indisponível, mas novos deploys,
alterações e operações administrativas dependem dela.

O operador continua responsável por:

- escolher, atualizar e proteger os servidores conectados;
- controlar SSH, firewall, DNS, armazenamento e capacidade;
- proteger o painel, suas chaves e as variáveis secretas;
- fazer backup da instalação, dos volumes e dos bancos;
- testar recuperação do control plane e dos workloads;
- decidir se o build deve ocorrer no host, em um runner separado ou externamente.

## Quando faz sentido

Coolify é uma boa opção para quem deseja uma experiência semelhante a um PaaS sem abandonar
servidores próprios. Ele pode reduzir o custo operacional de aplicações web, APIs, workers,
bancos de laboratório e serviços auxiliares, principalmente quando a equipe já trabalha com
Docker e quer administrar poucos servidores.

Ele não substitui Kubernetes, um sistema de GitOps ou uma estratégia de alta disponibilidade.
Para workloads críticos, confirme como volumes, bancos, backups, rollback, isolamento de
projetos, logs e atualizações serão tratados. O painel simplifica operações, mas o host e os
dados continuam no domínio do operador.

## Segurança

O acesso SSH e a integração com Docker são superfícies de alto privilégio. Restrinja o painel,
use autenticação forte, mantenha chaves com menor escopo possível e separe os servidores por
nível de confiança. Não coloque dados de produção em um volume que só possui cópia local e não
confunda a existência de um health check com uma estratégia de recuperação.

O arquivo de instalação e as chaves internas também precisam entrar no plano de backup. Uma
restauração que recupera containers, mas perde a chave que cifra a configuração do Coolify, não
é uma recuperação completa.

## Relação com outras plataformas

Coolify se aproxima do Dokploy e do CapRover por operar workloads Docker em infraestrutura
própria. A comparação deve considerar a forma de build, o proxy, o modelo de isolamento, a
topologia de servidores, a maturidade do Compose, os backups e a recuperação do control plane.
Railway oferece uma experiência parecida para o desenvolvedor, mas opera a plataforma como
serviço cloud e desloca mais responsabilidades de host para o fornecedor.

## Fontes primárias

- [Coolify, o que é](https://coolify.io/docs/core/what-is-coolify)
- [Coolify, aplicações](https://coolify.io/docs/applications/)
- [Coolify, autohospedado](https://coolify.io/docs/start-with-self-hosted)
- [Coolify, autohospedado versus Coolify Cloud](https://coolify.io/docs/core/selfhosted-cloud-comparison)
