# Conftest

Conftest testa dados estruturados usando políticas escritas em Rego sobre OPA. Em vez de perguntar apenas se a estrutura é válida, permite expressar regras organizacionais sobre o conteúdo.

## Casos de uso

Políticas sobre Kubernetes, Terraform/OpenTofu, JSON, YAML e outros formatos estruturados podem ser verificadas antes da aplicação.

## Boa prática

Escreva políticas pequenas, testáveis e acompanhadas de mensagens que expliquem a violação.

## Má prática

Transformar toda preferência estilística em política bloqueante cria um sistema difícil de evoluir e incentiva bypass.

## Fontes

- Conftest: <https://www.conftest.dev/>
