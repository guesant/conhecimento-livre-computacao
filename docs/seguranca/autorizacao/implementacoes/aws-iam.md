# AWS IAM

AWS IAM controla identidades, credenciais e permissões para recursos AWS. O
modelo combina políticas, principais, ações, recursos e condições.

## Modelo

Uma policy pode permitir ou negar ações e pode ser aplicada a identidade,
recurso, sessão ou organização. A decisão efetiva resulta da combinação de
políticas aplicáveis, negações explícitas e limites de permissão.

## Boas práticas

Use roles temporárias, menor privilégio, MFA para operações humanas, separação
de contas e revisão de políticas. Evite chaves permanentes quando uma identidade
de workload puder assumir uma role.

## Fonte

- [Introdução ao AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
