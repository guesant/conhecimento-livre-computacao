# OpenTofu

OpenTofu é uma ferramenta de infraestrutura declarativa compatível com a
linguagem e o modelo de providers de Terraform. Ela calcula planos comparando
configuração, state e recursos observados.

O [tutorial completo de OpenTofu](opentofu-tutorial.md) cobre estrutura de
projeto, backend, state, módulos, importação, CI, drift e recuperação.

## Operação

`tofu init` instala providers e configura o backend. `tofu plan` mostra
mudanças. `tofu apply` executa um plano aprovado. O backend deve proteger
state e lock. `tofu import` associa recurso existente à configuração.

Fixe versões de providers e preserve o arquivo de lock. A execução precisa
receber credenciais pelo ambiente ou secret manager, não por valores
versionados.

## Escolha

OpenTofu faz sentido quando governança comunitária, licença e compatibilidade
com módulos HCL importam. Compatibilidade não elimina a necessidade de
validar providers, módulos e comportamento antes de trocar a implementação.

## Relações

- [HCL](hcl.md) é a linguagem.
- [State](state.md) e [State locking](state-locking.md) protegem a execução.
- [Terraform](terraform.md) é a alternativa compatível de outra governança.

## Fonte primária

- [OpenTofu documentation](https://opentofu.org/docs/)
