# Tutorial de OpenTofu

OpenTofu descreve a infraestrutura como configuração declarativa, calcula a diferença entre essa configuração, o state e os recursos reais, e executa um plano aprovado por meio de providers. O comando não é apenas um script de criação: o state e o grafo de dependências fazem parte do modelo operacional.

Este tutorial parte de um projeto pequeno, mas as decisões apresentadas se aplicam a equipes e pipelines maiores.

## O modelo mental

Um projeto OpenTofu tem três referências diferentes:

| Referência | Papel |
| --- | --- |
| Configuração | O estado desejado descrito em HCL |
| State | A associação entre endereços OpenTofu e objetos gerenciados |
| Provider | A implementação que lê e altera a plataforma real |

O plano compara as três referências. Um recurso pode existir no provedor e ainda não estar no state. Também pode estar no state e ter sido removido manualmente da plataforma. Esses casos exigem importação ou correção de drift, não simplesmente um novo `apply` sem inspeção.

## Pré-requisitos

Instale uma versão de OpenTofu compatível com o repositório e confirme:

```bash
tofu version
tofu -help
```

Prepare credenciais fora do código, preferencialmente por secret manager ou variáveis de ambiente aceitas pelo provider. O usuário da execução deve ter somente os privilégios necessários para o escopo daquele projeto.

Uma estrutura inicial pode ser:

```text
infra/
  versions.tf
  providers.tf
  variables.tf
  main.tf
  outputs.tf
  environments/
    dev.tfvars
    prod.tfvars
  modules/
    network/
      main.tf
      variables.tf
      outputs.tf
```

Use módulos quando houver uma unidade de responsabilidade reutilizável. Não transforme cada recurso pequeno em um módulo apenas para criar indireção.

## Versões e providers

Declare a versão do OpenTofu e os providers necessários no módulo raiz:

```hcl
terraform {
  required_version = ">= 1.8.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}
```

Configure o provider no módulo raiz. Módulos filhos declaram suas exigências, mas normalmente recebem a configuração do provider do chamador:

```hcl
provider "docker" {
  host = var.docker_host
}
```

Depois de alterar requisitos, execute `tofu init` e revise o lockfile. O arquivo de lock deve ser versionado para que operadores e CI selecionem os mesmos checksums e versões resolvidas.

## Variáveis e outputs

Variáveis são a interface de entrada do módulo. Dê nomes que representem a responsabilidade e valide valores no limite do sistema:

```hcl
variable "environment" {
  type        = string
  description = "Nome do ambiente gerenciado."

  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "environment deve ser dev ou prod."
  }
}
```

Outputs são a interface de saída. Exponha somente valores necessários a outros módulos ou ao operador:

```hcl
output "container_id" {
  value       = docker_container.app.id
  description = "Identificador do container da aplicação."
}
```

Valores secretos não devem ser impressos em outputs sem uma razão operacional. Quando inevitável, marque o output como `sensitive = true` e ainda proteja o state, pois o valor continua existindo nele.

## Recursos, data sources e módulos

Um `resource` cria ou gerencia algo. Um `data` consulta algo que o provider já conhece. Um módulo compõe recursos e expõe uma interface menor:

```hcl
data "docker_network" "default" {
  name = "bridge"
}

resource "docker_image" "app" {
  name = "nginx:1.27"
}

module "network" {
  source      = "./modules/network"
  environment = var.environment
}
```

Não use `data` para esconder dependências ou substituir um recurso que o projeto deveria gerenciar. A distinção é importante para que a destruição e a recriação tenham uma semântica previsível.

## Inicialização e validação

Inicialize o diretório e execute as verificações baratas antes de gerar um plano:

```bash
tofu init
tofu fmt -check -recursive
tofu validate
```

`tofu init` configura o backend e instala providers e módulos. `fmt` verifica a forma canônica do HCL. `validate` verifica a configuração e os tipos locais, mas não confirma que a credencial funciona nem que o ambiente real pode ser alterado.

## Planejar e aplicar

Gere um plano nomeado e revise-o antes de aplicar:

```bash
tofu plan -var-file=environments/dev.tfvars -out=dev.tfplan
tofu show dev.tfplan
tofu apply dev.tfplan
```

Aplicar o arquivo de plano, em vez de gerar uma nova decisão durante o apply, evita que o ambiente mude entre a aprovação e a execução. Em produção, o pipeline deve guardar o plano com controles de acesso e expiração adequados.

O resultado esperado é que um segundo `plan` não proponha mudanças quando o ambiente estiver convergente. Se houver mudanças contínuas, investigue valores calculados, defaults do provider, normalização do recurso ou uma mutação externa antes de adicionar `ignore_changes`.

## Importar recursos existentes

Quando um recurso já existe, escreva a configuração que deve representá-lo, importe-o para o endereço correto e compare o plano:

```bash
tofu import docker_container.app existing-container-id
tofu plan -var-file=environments/dev.tfvars
```

Importar apenas atualiza o state. Não gera automaticamente uma configuração completa e não garante que o plano ficará vazio. Ajuste a configuração até que as diferenças sejam explicadas e intencionais.

## State, backend e locking

State local é adequado para experimentos isolados. Em uma equipe, use backend remoto com controle de acesso, versionamento e locking. O backend precisa resistir a interrupções durante escrita e oferecer restauração testável.

```hcl
terraform {
  backend "http" {
    address        = "https://state.example.test/tofu/project"
    lock_address   = "https://state.example.test/tofu/project/lock"
    unlock_address = "https://state.example.test/tofu/project/lock"
  }
}
```

O state não deve ser editado manualmente. `tofu state list`, `tofu state show` e operações de movimentação documentadas são preferíveis a alterações diretas no arquivo. `tofu state push` pode sobrescrever o state remoto e deve ser tratado como recuperação excepcional, com backup e revisão explícitos.

Após configurar ou alterar o backend, execute `tofu init -reconfigure` somente quando a intenção for realmente reconfigurar o backend. Não use isso para ocultar uma divergência entre ambientes.

## Workspaces e ambientes

Workspaces separam states que usam a mesma configuração. Eles são úteis para ambientes realmente equivalentes, mas podem esconder diferenças importantes quando cada ambiente tem permissões, regiões ou ciclos de vida distintos.

```bash
tofu workspace new dev
tofu workspace select dev
tofu workspace list
```

Quando os ambientes têm políticas e estruturas diferentes, diretórios raiz separados com módulos compartilhados costumam ser mais claros. O critério é evitar que uma seleção implícita de workspace direcione uma operação para o ambiente errado.

## Meta-argumentos e evolução

`for_each` cria instâncias identificadas por chaves estáveis. `count` é simples para conjuntos posicionais, mas uma remoção no meio pode deslocar índices. Prefira `for_each` quando cada instância tiver identidade própria.

```hcl
resource "docker_container" "worker" {
  for_each = toset(var.worker_names)
  name     = each.value
  image    = docker_image.app.image_id
}
```

`depends_on` deve expressar uma dependência real que o grafo não consegue inferir. `lifecycle` pode proteger ou substituir recursos, mas `prevent_destroy` não substitui backup e revisão.

Ao renomear um endereço sem recriar o recurso, use um bloco `moved` e confirme o plano:

```hcl
moved {
  from = docker_container.app
  to   = docker_container.web
}
```

Remova o bloco depois de todos os estados suportados terem passado pela migração e a política do projeto permitir essa limpeza.

## Fluxo local, revisão e CI

Um fluxo seguro separa formatação, validação, planejamento e aplicação:

1. `tofu fmt -check -recursive` verifica a forma.
2. `tofu validate` verifica a configuração.
3. Um linter verifica convenções, segurança e providers.
4. A CI executa `tofu plan` com credenciais de leitura e publica o resultado.
5. Uma aprovação explícita libera `tofu apply` de um plano controlado.
6. O resultado é registrado junto da revisão que produziu o plano.

Não coloque credenciais em `*.tfvars` versionados. Proteja logs para evitar que um provider imprima tokens. Restrinja o backend e os artefatos de plano, pois ambos podem conter valores sensíveis.

## Drift e diagnóstico

Drift é uma diferença entre o state, a configuração e o recurso real. Comece com um plano somente leitura e determine qual referência divergiu:

```bash
tofu plan -refresh-only
tofu state list
tofu state show docker_container.app
tofu providers
```

Se uma mudança manual for legítima, codifique-a e aplique pela revisão normal. Se for indesejada, o plano regular pode corrigi-la. Se o provider não conseguir ler o recurso, trate a falha de autenticação ou conectividade antes de aceitar qualquer plano destrutivo.

Falhas comuns incluem backend bloqueado, provider incompatível, recurso importado com endereço incorreto, dependência cíclica, credencial sem escopo e alteração externa não modelada. O diagnóstico deve preservar o state e não começar removendo recursos dele.

## Destruição e recuperação

`tofu destroy` é uma operação de alto impacto. Antes dela, gere um plano, confirme o workspace e o backend, valide a retenção de dados e faça o backup exigido pela plataforma. Em produção, a destruição deve exigir uma aprovação separada.

Quando um apply falhar, preserve o output, o plano e o state. Corrija a causa, verifique o estado real e gere um novo plano. Não repita cegamente uma operação parcial, especialmente quando ela criou um recurso fora do state esperado.

## Relações

- [Estado desejado](desired-state.md) explica a declaração do objetivo.
- [State](state.md) explica a associação entre configuração e recurso.
- [State locking](state-locking.md) explica a exclusão concorrente.
- [Drift](drift.md) explica divergências entre referências.
- [HCL](hcl.md) explica a linguagem da configuração.
- [Terraform](terraform.md) é uma alternativa compatível de outra governança.

## Fontes primárias

- [OpenTofu CLI init](https://opentofu.org/docs/cli/init/)
- [Provider requirements](https://opentofu.org/docs/language/providers/requirements/)
- [Provider configuration](https://opentofu.org/docs/language/providers/configuration/)
- [Modules](https://opentofu.org/docs/language/modules/)
- [State backends](https://opentofu.org/docs/language/state/backends/)
