# Segurança de infraestrutura como código

IaC scanning e policy as code analisam definições antes da aplicação. O alvo pode ser Terraform/OpenTofu, Kubernetes, Dockerfiles, CloudFormation ou artefatos renderizados.

## Abordagens

Schema validation pergunta se a estrutura é válida. Configuration scanning procura configurações conhecidas como inseguras. Policy as code avalia regras declaradas pela organização. Posture/compliance scanning relaciona estado ou manifestos a frameworks de controles.

Essas abordagens podem usar o mesmo YAML como entrada e ainda responder perguntas diferentes.

## Ferramentas

[Checkov](checkov.md) cobre múltiplos formatos de IaC. [KubeLinter](kubelinter.md) é especializado em Kubernetes. Conftest aplica políticas OPA/Rego a dados estruturados. Kubescape cobre posture e frameworks Kubernetes.

## Boa prática

Analise o artefato mais próximo do que será aplicado. Se Helm ou Kustomize transforma o source, validar apenas o template pode perder problemas introduzidos na renderização.

## Má prática

Somar ferramentas que implementam as mesmas regras sem entender sobreposição aumenta ruído, não cobertura.
