# Dokploy

Dokploy é uma plataforma open source e autohospedada para gerenciar deploys de aplicações,
bancos e serviços containerizados. O nome oficial do projeto é "Dokploy". Ele oferece uma
interface e APIs para organizar recursos Docker, usando Traefik para a entrada HTTP e suportando
deploy por Nixpacks, buildpacks, Dockerfile e Docker Compose.

## Modelo de execução

O Dokploy pode executar aplicações em servidores conectados e também oferece suporte a múltiplos
servidores e clusters Docker Swarm. A plataforma cria e acompanha os recursos que compõem cada
aplicação, gerencia variáveis, logs, domínios, certificados, deploys e operações de banco.

O suporte nativo a Docker Compose é útil para stacks com vários serviços, mas não elimina a
necessidade de revisar volumes, redes, secrets, dependências, política de reinício e backup. A
semântica do Compose precisa ser conferida na versão em uso, especialmente quando a aplicação
usa recursos específicos do Docker ou do Swarm.

## Bancos e persistência

O projeto documenta operações para PostgreSQL, MySQL, MariaDB, MongoDB e Redis, incluindo
configuração de backups. Isso não transforma o banco em um serviço magicamente altamente
disponível. O operador ainda precisa definir retenção, destino externo, criptografia, teste de
restauração, replicação, manutenção e comportamento quando o servidor falha.

Para workloads stateful, trate o volume local como parte do domínio de falha do host. Um backup
gerado no mesmo disco não é suficiente para recuperar uma perda de disco ou de máquina.

## Quando faz sentido

Dokploy pode ser adequado para times que querem uma camada de deploy mais completa que scripts
Docker isolados, mas ainda desejam manter os servidores e o runtime sob seu controle. O suporte
a múltiplos servidores, Compose, API, CLI, logs e controle de usuários pode ser útil para um
ambiente pequeno ou médio.

Ele não deve ser escolhido apenas pela existência de um botão de deploy. Avalie o isolamento
entre projetos, o alcance das credenciais, o acesso ao Docker socket, a forma de atualizar a
plataforma, a recuperação do banco interno e a possibilidade de exportar a configuração sem
depender do painel.

## Segurança e operação

Exponha o painel somente atrás de TLS e autenticação forte. Separe credenciais de leitura e
escrita quando possível, limite o alcance das chaves SSH e evite colocar o control plane no
mesmo host de workloads de confiança incompatível. Registre quem pode alterar imagens, volumes,
variáveis, domínios e redes.

Se o deploy usa uma imagem pronta, mantenha referência imutável por digest quando o risco da
cadeia de fornecimento exigir isso. Se o build ocorre no servidor, trate o código do repositório
e os scripts de build como entrada não confiável para o host.

## Relação com Coolify e CapRover

Dokploy compartilha com Coolify a ideia de uma plataforma de controle para Docker e com CapRover
o foco em facilitar deploy e roteamento em infraestrutura própria. As diferenças mais relevantes
são o mecanismo de build, o suporte a Compose, o modelo de múltiplos servidores, o uso de Swarm,
o proxy, a gestão de bancos e o modo como cada projeto representa aplicações e ambientes.

## Fontes primárias

- [Dokploy, documentação](https://docs.dokploy.com/docs/core)
- [Dokploy, página oficial](https://dokploy.com/)
- [Dokploy, aplicações](https://docs.dokploy.com/docs/core/applications)
- [Dokploy, Docker Compose](https://docs.dokploy.com/docs/core/docker-compose)
