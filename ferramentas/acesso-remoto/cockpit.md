# Cockpit

Cockpit é uma interface web para administrar servidores Linux. O navegador se conecta ao serviço web do Cockpit, normalmente na porta 9090, e a interface usa as APIs do sistema para exibir logs, serviços, armazenamento, rede, contas, máquinas virtuais e containers conforme os módulos instalados.

## O que ele é

O Cockpit é uma camada de administração e observação sobre o sistema operacional. Ele não é um hypervisor, um orquestrador de containers, um sistema de identidade ou um substituto do SSH. A autenticação normalmente usa as contas do próprio sistema, e a operação continua sujeita às permissões do usuário e às políticas do host.

O serviço web inicia o `cockpit-bridge` para a sessão do usuário. O bridge conversa com as APIs e comandos do sistema, mantendo a interface alinhada ao modelo operacional do Linux em vez de criar uma base paralela de estado.

## Casos de uso

Cockpit é adequado para:

- inspecionar rapidamente saúde, logs e consumo de recursos;
- administrar hosts Linux sem transformar cada tarefa simples em uma sequência de comandos;
- ensinar administração de servidores a pessoas que ainda não dominam todo o vocabulário da linha de comando;
- combinar uma visão gráfica com SSH, Ansible e ferramentas de terminal;
- adicionar outros hosts por SSH e alternar entre eles na mesma interface.

Ele é menos adequado quando a operação precisa ser reproduzível, revisável e aplicada a uma frota. Nesse caso, comandos versionados, Ansible ou outro mecanismo declarativo devem continuar sendo a autoridade, enquanto Cockpit pode ser usado para inspeção e intervenções pontuais justificadas.

## Segurança e exposição

Expor a porta 9090 diretamente na internet amplia a superfície de autenticação do host. Uma implantação segura deve preferir rede administrativa, VPN, firewall e proxy com política explícita. O acesso ao Cockpit deve ser tratado como acesso administrativo ao servidor, não como uma página pública comum.

A sessão web também não transforma uma conta sem privilégios em administradora. O que o usuário consegue executar depende das permissões do Linux, de `sudo`, dos módulos instalados e das políticas do ambiente. A auditoria deve considerar tanto os eventos do sistema quanto o caminho de acesso ao Cockpit.

## Relação com automação

Uma alteração feita manualmente no Cockpit pode criar drift em relação ao código ou ao inventário de configuração. Antes de alterar um host gerenciado por automação, identifique a fonte de verdade e registre a mudança no mecanismo correto. Para observação, o Cockpit tende a ser complementar; para mudanças repetíveis, a automação deve prevalecer.

## Fontes primárias

- [Cockpit Project](https://cockpit-project.org/)
- [Documentação do Cockpit](https://cockpit-project.org/documentation.html)
- [Guia de deployment do Cockpit](https://docs.cockpit-project.org/)
- [Descrição do serviço cockpit-ws e cockpit-bridge](https://docs.cockpit-project.org/cockpit-guide/366/man/cockpit.1.html)
