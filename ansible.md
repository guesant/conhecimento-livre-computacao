# Ansible

Ansible é uma ferramenta de gestão de configuração: ela conecta numa máquina remota, tipicamente por SSH, e garante que essa máquina fique no estado descrito num arquivo, chamado playbook. A diferença mais citada entre Ansible e ferramentas parecidas (Puppet, Chef, Salt) é que ele não exige um agente instalado na máquina de destino: como usa SSH, que já vem pronto na maioria dos sistemas Linux, não há nada para instalar antes de começar a gerenciar uma máquina nova. Por isso Ansible costuma ser descrito como *push*: quem inicia a conexão é a máquina do operador, empurrando a configuração para o destino, ao contrário de um modelo *pull* onde o próprio destino puxaria periodicamente sua configuração de um servidor central.

## Idempotência

O conceito mais importante para entender Ansible é a idempotência: rodar o mesmo playbook de novo deve produzir o mesmo resultado, e a execução seguinte não deve fazer nada além de confirmar que o estado já está correto. Isso é o que diferencia um playbook bem escrito de um script shell comum. Um script que faz `mkdir pasta` falha ao rodar de novo porque a pasta já existe, enquanto uma tarefa Ansible equivalente verifica se a pasta já existe antes de decidir se precisa criá-la. O resultado dessa checagem aparece no relatório como `ok`, nada mudou, em vez de `changed`, algo mudou, ou de uma falha. Essa distinção entre `ok` e `changed` é o que permite ler uma execução inteira e saber, sem abrir nada, o que aquela rodada realmente mexeu no node.

Checar antes de agir é o que permite rodar o mesmo playbook contra uma máquina nova e contra uma máquina já configurada sem medo de quebrar nada. Na prática, isso muda como se aplica uma mudança pequena: em vez de identificar o delta e aplicá-lo à mão, reexecuta-se o playbook inteiro e deixa-se que as tarefas já satisfeitas não façam nada. A idempotência não é automática, porém, e vem embutida nos módulos que descrevem estado, não em qualquer tarefa. Uma tarefa que dispara um comando cru precisa dizer ela mesma o que conta como mudança, como faz a role `firewall` deste repositório, que trata a resposta `ALREADY_ENABLED` do `firewall-cmd` como sinal de que a regra já estava lá.

## Modo de verificação (`--check`)

Antes de aplicar de fato, o Ansible pode simular a execução com a flag `--check`: cada tarefa reporta o que faria, sem fazer. É útil para ver o efeito de uma mudança antes de aplicá-la de verdade, mas tem um limite conceitual: uma tarefa que depende do resultado de uma tarefa anterior que ainda não rodou de verdade (por exemplo, ler um arquivo que uma tarefa anterior criaria) não tem como prever esse resultado. Playbooks bem escritos tratam esse limite explicitamente, pulando ou avisando sobre blocos que não têm como ser verificados sem aplicar antes.

## Estrutura: inventário, playbook, role

Um **inventário** lista as máquinas que o Ansible gerencia, agrupadas e com variáveis próprias (endereço, usuário SSH, caminho da chave). Um **playbook** é o arquivo que descreve o que aplicar em quais máquinas do inventário. Uma **role** é uma unidade reutilizável de playbook: uma pasta com uma estrutura de arquivos padronizada (tarefas, templates, variáveis padrão, handlers) que empacota uma responsabilidade específica, como "instalar e configurar um firewall" ou "instalar o k3s". Organizar um playbook grande em roles evita repetir a mesma sequência de tarefas em vários lugares e permite testar e documentar cada responsabilidade separadamente.

## Segredos: o Vault

Um playbook frequentemente precisa de valores sensíveis (senhas, chaves, tokens) que não devem ficar em texto claro dentro de um repositório git. O Ansible Vault resolve isso cifrando um arquivo inteiro (ou um valor dentro de um arquivo) com uma senha, de forma que o arquivo cifrado pode ser commitado com segurança e só é legível por quem tem a senha do Vault. O hl-infrastructure não usa o Vault para os próprios segredos: em vez de uma senha compartilhada, ele cifra com SOPS para um conjunto de chaves públicas age, e o arquivo cifrado também é commitado; a página [Variáveis](../arquitetura/variaveis.md) explica essa escolha específica deste repositório.

## Testando roles: Molecule

Para quem escreve roles reutilizáveis, o Molecule é a ferramenta mais comum de teste: ele sobe um container ou máquina virtual descartável, aplica a role nela, roda verificações sobre o resultado e destrói o ambiente ao final. Isso permite testar uma role de forma isolada e repetível, sem depender de uma máquina real ou de rodar o playbook inteiro para validar uma mudança pequena. O ganho é maior quando a role é publicada para terceiros, que a aplicarão em distribuições e versões que quem a escreveu nunca vai ver. O hl-infrastructure não usa Molecule: as roles daqui existem só para este node, e a verificação equivalente é o `ansible-lint` do `just lint-ansible` somado a rodar o playbook com `--check --diff` contra o Pi real, que é a mesma máquina que a execução de verdade vai tocar.

## Continue por aqui

[Ansible: as roles do bootstrap](../arquitetura/ansible.md), na arquitetura, mostra como o hl-infrastructure aplica esses conceitos: a ordem real das roles listadas em `ansible/site.yml`, seu próprio mecanismo de gate para o modo de verificação, e como ele recupera de um conflito de campo imutável num apply de chart. O [primeiro bootstrap](../operacional/primeiro-bootstrap.md), no operacional, é o comando real que dispara essa execução.
