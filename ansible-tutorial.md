# Tutorial de Ansible

Ansible automatiza configuração e operações por meio de um inventário, um playbook e módulos que descrevem estados. No modo mais comum, a máquina operadora conecta por SSH, executa as tarefas em ordem e registra o que mudou. Não há necessidade de instalar um agente Ansible no host gerenciado.

O objetivo deste tutorial é chegar de um diretório vazio a um playbook seguro, idempotente, testável e adequado para execução controlada em produção.

## Pré-requisitos

Instale uma versão compatível de `ansible-core`, tenha acesso SSH ao host e confirme a identidade do servidor. Não desabilite `host_key_checking` para contornar uma chave desconhecida. Registre a chave correta ou corrija o DNS e o inventário.

```bash
ansible --version
ssh-keygen -F server.example.test
ansible-inventory -i inventories/dev/hosts.yml --graph
```

Uma estrutura inicial pode ser:

```text
automation/
  ansible.cfg
  inventories/
    dev/
      hosts.yml
      group_vars/
      host_vars/
    prod/
      hosts.yml
      group_vars/
      host_vars/
  playbooks/
    site.yml
  roles/
    web/
      defaults/main.yml
      handlers/main.yml
      tasks/main.yml
      templates/
      vars/main.yml
  collections/requirements.yml
  requirements.yml
```

Separe inventários de ambientes para reduzir o risco de usar um host de produção durante um teste local. O playbook pode ser comum, enquanto variáveis e grupos descrevem as diferenças.

## Configurando o inventário

O inventário associa nomes lógicos a hosts e grupos:

```yaml
all:
  children:
    web:
      hosts:
        web-01:
          ansible_host: 192.0.2.10
          ansible_user: deploy
    databases:
      hosts:
        db-01:
          ansible_host: 192.0.2.20
          ansible_user: deploy
```

O endereço real, o usuário e a chave devem vir de uma configuração protegida quando não forem informações públicas. `ansible_host` é o endereço usado na conexão; o nome do host continua sendo a identidade usada em variáveis e relatórios.

Use grupos por responsabilidade e não somente por localização. Isso permite que o playbook selecione `web`, `databases` ou um grupo de manutenção sem codificar endereços dentro das tarefas.

## Configuração do Ansible

Mantenha a configuração explícita e pequena:

```ini
[defaults]
inventory = inventories/dev/hosts.yml
host_key_checking = true
interpreter_python = auto_silent
stdout_callback = default
retry_files_enabled = false
```

Uma opção definida pela linha de comando pode alterar o inventário para uma execução controlada:

```bash
ansible-playbook -i inventories/prod/hosts.yml playbooks/site.yml --limit web-01
```

Não coloque senhas em `ansible.cfg`. Use chave SSH, agente, integração com secret manager ou prompt seguro conforme o ambiente.

## Primeiro playbook

Um playbook lista plays, cada play seleciona hosts e cada tarefa chama um módulo. Use o Fully Qualified Collection Name para deixar a origem do módulo explícita:

```yaml
- name: Configure web hosts
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Enable nginx
      ansible.builtin.service:
        name: nginx
        enabled: true
        state: started
```

Playbooks são processados de cima para baixo e tarefas são executadas na ordem declarada. A ordem deve refletir dependências reais, e não ser usada para esconder uma condição que deveria estar expressa em `when` ou em um handler.

## Idempotência

Uma tarefa idempotente descreve o estado desejado. A execução seguinte deve retornar `ok` quando nada precisar mudar. Prefira um módulo que conheça o estado ao uso de `shell` ou `command`:

```yaml
- name: Create application directory
  ansible.builtin.file:
    path: /srv/application
    state: directory
    owner: deploy
    group: deploy
    mode: "0750"
```

Quando um comando for inevitável, declare como o Ansible identifica o estado já aplicado com `creates`, `removes` ou uma condição de mudança. Não marque sempre a tarefa como alterada, pois isso destrói a utilidade do relatório e aciona handlers sem necessidade.

## Roles

Uma role reúne uma responsabilidade reutilizável. Um playbook chama a role e fornece somente a configuração que varia:

```yaml
- name: Configure web hosts
  hosts: web
  become: true
  roles:
    - role: web
      web_listen_port: 8080
```

Em `roles/web/tasks/main.yml`, use tarefas pequenas e ordenadas. Coloque valores padrão substituíveis em `defaults/main.yml`, handlers que precisam ser notificados em `handlers/main.yml` e templates em `templates/`. `vars/main.yml` deve conter apenas valores que realmente tenham precedência alta e não sejam configuração comum de ambiente.

## Templates e handlers

Templates geram arquivos a partir de variáveis. O template deve ser uma representação completa e validável do arquivo, não uma sequência de comandos de edição:

```jinja
server {
  listen {{ web_listen_port }};
  server_name {{ web_server_name }};
}
```

Uma alteração no template pode notificar um handler para reiniciar ou recarregar o serviço:

```yaml
- name: Render nginx configuration
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/conf.d/application.conf
    owner: root
    group: root
    mode: "0644"
  notify: Reload nginx
```

```yaml
- name: Reload nginx
  ansible.builtin.service:
    name: nginx
    state: reloaded
```

Handlers rodam quando notificados e normalmente ao final do play. Isso reduz reinicializações repetidas e mantém o serviço estável durante a execução.

## Variáveis e precedência

Ansible combina defaults de role, variáveis de grupo, variáveis de host, variáveis de play e valores fornecidos na execução. Use nomes específicos e evite sobrescrever o mesmo valor em muitos lugares.

Uma variável de configuração de ambiente costuma pertencer a `group_vars`:

```yaml
web_listen_port: 8080
  web_server_name: web.example.test
```

`--extra-vars` tem precedência alta e deve ser reservado para uma substituição intencional. Não use essa opção para esconder uma configuração que deveria ser versionada. Quando um valor estiver surpreendente, execute com verbosidade e procure a fonte mais específica que o definiu.

## Condições, loops e falhas

Use `when` para condições de estado e loops para dados repetidos. A expressão de `when` não precisa de delimitadores Jinja:

```yaml
- name: Install monitoring package on Debian hosts
  ansible.builtin.package:
    name: monitoring-agent
    state: present
  when: ansible_facts.os_family == "Debian"
```

Se tarefas de uma sequência dependem de um resultado comum, agrupe-as em um bloco e trate falhas com responsabilidade. Não transforme toda falha em `ignore_errors`, pois isso cria um relatório verde para um host parcialmente configurado.

## Collections

Collections distribuem módulos, roles, plugins e documentação. Fixe versões em um arquivo de requisitos:

```yaml
collections:
  - name: community.general
    version: ">=9.0.0,<10.0.0"
```

Instale exatamente os requisitos no ambiente de execução:

```bash
ansible-galaxy collection install -r collections/requirements.yml
ansible-galaxy collection list
```

O uso de FQCN reduz ambiguidades e ajuda o linter a detectar módulos errados ou obsoletos.

## Segredos

Ansible Vault cifra arquivos ou valores que serão consumidos durante a execução:

```bash
ansible-vault create inventories/prod/group_vars/secret.yml
ansible-vault edit inventories/prod/group_vars/secret.yml
ansible-playbook playbooks/site.yml --ask-vault-pass
```

O Vault protege o arquivo no Git, mas a senha ainda precisa ser entregue com segurança ao processo. Em ambientes maiores, integre com um secret manager e limite a exposição em variáveis, fatos e logs. Nunca exiba segredos em `debug`.

## Execução segura

Antes de tocar um ambiente real, valide o inventário e o alvo:

```bash
ansible-inventory -i inventories/prod/hosts.yml --graph
ansible -i inventories/prod/hosts.yml web --module-name ansible.builtin.ping
ansible-playbook -i inventories/prod/hosts.yml playbooks/site.yml --check --diff
```

`--check` simula mudanças, mas não pode prever tudo quando uma tarefa depende de um arquivo ou fato que seria criado durante a própria execução. `--diff` mostra diferenças de arquivos e não deve ser usado onde o conteúdo possa conter segredo.

Use `--limit` para um subconjunto e `serial` para atualizar hosts em lotes:

```yaml
- name: Roll out web configuration
  hosts: web
  serial: 1
  become: true
  roles:
    - web
```

Em mudanças de alto risco, faça primeiro uma execução em um host representativo, confirme saúde e logs, e só depois amplie o lote.

## Push e pull

No modo push, um operador ou pipeline executa `ansible-playbook` contra o inventário. Esse modelo facilita aprovação explícita e limita o momento da mudança.

No modo pull, `ansible-pull` executa periodicamente no host e busca o playbook de um repositório. Ele pode ser útil em ambientes que não aceitam conexões inbound, mas transfere para o host a responsabilidade por agenda, credenciais, versão e falhas de atualização. O modo escolhido deve aparecer na arquitetura operacional e nos procedimentos de recuperação.

## Qualidade e testes

Execute o linter antes da aplicação:

```bash
ansible-lint playbooks roles
```

Molecule pode criar um ambiente descartável, aplicar uma role e verificar o resultado. Os cenários devem testar pelo menos convergência e idempotência:

```bash
molecule test
```

Em uma infraestrutura que opera um único host real, a verificação pode ser complementada por `--check --diff`, validações específicas do sistema e uma janela de mudança. O teste descartável e a verificação do ambiente real respondem a riscos diferentes.

## Diagnóstico

Comece distinguindo falha de conexão, falha de coleta de fatos, falha de módulo e falha de serviço:

```bash
ansible-inventory -i inventories/prod/hosts.yml --host web-01
ansible -i inventories/prod/hosts.yml web-01 -m ansible.builtin.setup
ansible-playbook -i inventories/prod/hosts.yml playbooks/site.yml --limit web-01 -vv
```

Verifique usuário, chave, `become`, Python remoto, permissões, espaço em disco e o gerenciador de pacotes da distribuição. Depois de uma falha parcial, não assuma que reexecutar é seguro sem ler quais tarefas mudaram e quais handlers foram notificados.

## Relações

- [Configuração de frotas](entregar-configuracao-a-uma-frota-de-hosts.md) relaciona automação de hosts a um procedimento operacional.
- [SSH](ssh.md) explica o canal de conexão normalmente usado pelo modo push.
- [Variáveis da infraestrutura](../arquitetura/variaveis.md) mostra uma decisão específica do repositório.
- [Primeiro bootstrap](../operacional/primeiro-bootstrap.md) é um runbook do ambiente, não um tutorial genérico de Ansible.

## Fontes primárias

- [Introduction to playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html)
- [Validating tasks: check mode and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- [Using collections in playbooks](https://docs.ansible.com/projects/ansible/latest/collections_guide/collections_using_playbooks.html)
- [Ansible Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html)
