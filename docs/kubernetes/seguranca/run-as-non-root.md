# Run as non-root

Executar como usuário não-root reduz privilégios disponíveis ao processo no container.

Isso não transforma o workload em seguro por si só. Capabilities, mounts, kernel e outras permissões continuam relevantes.

Imagens precisam ser construídas para funcionar com UID/GID apropriados e permissões de filesystem compatíveis.
