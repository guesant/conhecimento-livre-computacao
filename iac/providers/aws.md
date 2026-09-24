# Provider AWS

O provider AWS expõe uma grande parte das APIs da Amazon Web Services como resources e data sources. Ele é uma escolha comum para redes, identidades, computação, armazenamento e serviços gerenciados.

## Cuidados

Use roles e credenciais temporárias, separe contas e estados por ambiente e restrinja a política IAM àquilo que o módulo precisa. O catálogo amplo aumenta o risco de mudanças destrutivas e de state contendo dados sensíveis.

## Operação

Fixe a versão do provider, use lockfile e backend remoto com lock. Faça `plan` em identidade de leitura controlada antes de promover para a identidade que pode aplicar mudanças.

## Fonte primária

- [AWS provider](https://registry.opentofu.org/providers/hashicorp/aws/latest)
