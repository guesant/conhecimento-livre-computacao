# Job

Job representa trabalho finito no Kubernetes. Seu objetivo é alcançar conclusão bem-sucedida, ao contrário de controllers voltados a manter serviços continuamente disponíveis.

## Controles

[Restart policy](restart-policy.md), [backoff limit](backoff-limit.md) e [active deadline](active-deadline.md) controlam tentativas e duração. Esses mecanismos são independentes e possuem páginas próprias.

## Casos de uso

Migrações, processamento batch e tarefas administrativas finitas são encaixes naturais. Um servidor HTTP permanente normalmente pertence a outro controller.

## Boa prática

Defina o que significa sucesso, limite retries e torne operações repetíveis quando reexecução for possível.

## Má prática

Usar Job para daemon permanente ou permitir retry infinito de uma falha determinística.
