# Validação de schema

Schema validation verifica se um documento respeita a estrutura formal esperada: campos permitidos, tipos, obrigatoriedade e outras restrições expressáveis pelo schema.

## Casos de uso

Validar manifests Kubernetes e CRDs antes de aplicar reduz erros estruturais e feedback tardio.

## Boa prática

Use o schema correspondente à versão real do recurso e inclua schemas de CRDs usados pelo projeto.

## Má prática

Confundir schema válido com configuração segura. Um manifesto pode ser perfeitamente válido e ainda executar como root, expor privilégios ou violar política.